"""Core data models.

Three families live here:

* Extraction  -- Element, FormField, FormSpec, SearchControl, PageModel
* Graph       -- NavNode, NavEdge, NavGraph
* Output      -- Step, TestCase, TestSuite

The test-case family mirrors the required QA format exactly (Test ID, Category,
Preconditions, numbered Steps with per-step expected results, Overall Expected
Result). ``source_url`` and ``source_selectors`` are additions that make the
validator's anti-hallucination check possible.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, Field

try:  # 3.11+
    from enum import StrEnum
except ImportError:  # 3.10 compat -- same semantics for our purposes
    from enum import Enum

    class StrEnum(str, Enum):  # type: ignore[no-redef]
        def __str__(self) -> str:
            return str(self.value)

# --------------------------------------------------------------------------
# Enums
# --------------------------------------------------------------------------


class Confidence(StrEnum):
    CERTAIN = "certain"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class ElementKind(StrEnum):
    """Output of the classification cascade (CRAWLING_AND_EXTRACTION.md §1.2)."""

    SEARCH = "search"
    TEXT_INPUT = "text_input"
    EMAIL_INPUT = "email_input"
    PASSWORD_INPUT = "password_input"
    NUMBER_INPUT = "number_input"
    DATE_INPUT = "date_input"
    TEL_INPUT = "tel_input"
    URL_INPUT = "url_input"
    FILE_INPUT = "file_input"
    CHECKBOX = "checkbox"
    RADIO = "radio"
    RANGE = "range"
    COLOR = "color"
    TEXTAREA = "textarea"
    SELECT = "select"
    NAV_LINK = "nav_link"
    EXTERNAL_LINK = "external_link"
    SUBMIT = "submit"
    OVERLAY_TRIGGER = "overlay_trigger"
    DISCLOSURE = "disclosure"
    TAB = "tab"
    MENUITEM = "menuitem"
    OPTION = "option"
    SWITCH = "switch"
    DESTRUCTIVE = "destructive"
    GENERIC_BUTTON = "generic_button"
    INFERRED_CLICKABLE = "inferred_clickable"
    UNKNOWN = "unknown"


#: Kinds worth attempting an in-page interaction with.
#:
#: NAV_LINK is deliberately absent: links are enqueued onto the crawl frontier
#: instead. Clicking them here as well would burn the click budget on
#: navigations we already have queued -- on a 50-item list page that starves
#: every interesting button on the page.
CLICKABLE_KINDS: frozenset[ElementKind] = frozenset(
    {
        ElementKind.OVERLAY_TRIGGER,
        ElementKind.DISCLOSURE,
        ElementKind.TAB,
        ElementKind.MENUITEM,
        ElementKind.OPTION,
        ElementKind.SWITCH,
        ElementKind.CHECKBOX,
        ElementKind.RADIO,
        ElementKind.GENERIC_BUTTON,
        ElementKind.INFERRED_CLICKABLE,
    }
)

#: Kinds a tester can actually do something with. Wider than CLICKABLE_KINDS,
#: which is only what the *crawler* attempts: a submit button and a destructive
#: control are prime test targets even though the crawler refuses to press them.
ACTIONABLE_KINDS: frozenset[ElementKind] = CLICKABLE_KINDS | frozenset(
    {
        ElementKind.SEARCH,
        ElementKind.SELECT,
        ElementKind.TEXTAREA,
        ElementKind.SUBMIT,
        ElementKind.DESTRUCTIVE,
        ElementKind.FILE_INPUT,
        ElementKind.NAV_LINK,
        ElementKind.EXTERNAL_LINK,
        ElementKind.TEXT_INPUT,
        ElementKind.EMAIL_INPUT,
        ElementKind.PASSWORD_INPUT,
        ElementKind.NUMBER_INPUT,
        ElementKind.DATE_INPUT,
        ElementKind.TEL_INPUT,
        ElementKind.URL_INPUT,
        ElementKind.RANGE,
        ElementKind.COLOR,
    }
)


def is_actionable(element: "Element") -> bool:
    """Can a tester do something with this element?

    Disabled controls count: "Save stays disabled until the form is valid" is a
    real test case. Only UNKNOWN and invisible elements are excluded.
    """
    return element.visible and element.kind in ACTIONABLE_KINDS


#: Ranking used by the action planner (crawl sub-phase 4F). Lower sorts first,
#: so a tight click budget drops the least valuable actions rather than an
#: arbitrary tail.
ACTION_PRIORITY: dict[ElementKind, int] = {
    ElementKind.OVERLAY_TRIGGER: 2,
    ElementKind.DISCLOSURE: 2,
    ElementKind.TAB: 3,
    ElementKind.MENUITEM: 3,
    ElementKind.SWITCH: 3,
    ElementKind.CHECKBOX: 4,
    ElementKind.RADIO: 4,
    ElementKind.OPTION: 4,
    ElementKind.GENERIC_BUTTON: 5,
    ElementKind.INFERRED_CLICKABLE: 6,
}


class OverlayType(StrEnum):
    MODAL = "modal"
    DRAWER = "drawer"
    DROPDOWN = "dropdown"
    TOOLTIP = "tooltip"
    TOAST = "toast"
    CONSENT = "consent"


#: Overlays that appear and vanish on their own. Excluded from the fingerprint,
#: otherwise a 4-second toast makes every visit to a page a brand new state.
TRANSIENT_OVERLAYS: frozenset[OverlayType] = frozenset(
    {OverlayType.TOOLTIP, OverlayType.TOAST}
)


class Outcome(StrEnum):
    """The nine things an action can actually do (CRAWLING §4H)."""

    NO_CHANGE = "no_change"
    IN_PAGE_STATE = "in_page_state"
    NAVIGATION = "navigation"
    NEW_TAB = "new_tab"
    NATIVE_DIALOG = "native_dialog"
    FILE_CHOOSER = "file_chooser"
    DOWNLOAD = "download"
    BLOCKED_MUTATION = "blocked_mutation"
    ERROR = "error"


class Category(StrEnum):
    HAPPY_PATH = "Happy Path"
    NEGATIVE = "Negative"
    EDGE_CASE = "Edge Case"
    UI_UX = "UI/UX"
    FORM_FILLING = "Form Filling"


# --------------------------------------------------------------------------
# Extraction models
# --------------------------------------------------------------------------

_DIGITS = re.compile(r"\d+")


def _normalise_name(name: str) -> str:
    """Collapse data out of an accessible name so identity tracks structure.

    ``Used 0.00KB`` and ``Used 12.4KB`` are the same control showing different
    data; they must not be different states.
    """
    return _DIGITS.sub("#", (name or "").strip().lower())[:48]


class Element(BaseModel):
    ref: str
    kind: ElementKind
    role: str
    name: str
    tag: str
    selector: str
    selector_strategy: str
    confidence: Confidence = Confidence.MEDIUM
    enabled: bool = True
    visible: bool = True
    href: str | None = None
    target: str | None = None
    input_type: str | None = None
    aria_haspopup: str | None = None
    aria_expanded: str | None = None
    form_ref: str | None = None
    classification_rule: int = 0
    #: Inside a transient overlay (toast/tooltip). Excluded from the
    #: fingerprint -- see interactive_signature().
    transient: bool = False
    #: Detected only by `cursor: pointer` -- a React div whose onClick lives in
    #: the framework, not the DOM. Kept in the inventory because it is
    #: genuinely testable, but excluded from the fingerprint: the
    #: pointer-cursor set shifts between renders, and including it turned one
    #: Settings page into a dozen states on a real app.
    pointer_cursor: bool = False
    #: Page-absolute position and size, used to walk a state in reading order
    #: (top to bottom, left to right) rather than in an order that only makes
    #: sense to the tool.
    x: int = 0
    y: int = 0
    w: int = 0
    h: int = 0
    #: Structural region reported by the DOM (header/footer/nav/dialog), when
    #: the app uses landmarks at all.
    landmark: str | None = None
    #: Where a person would look for this control, in words: "header,
    #: top-right", "main area, middle-centre". Computed once at extraction from
    #: the geometry above, and the thing a test step should say instead of a
    #: pixel coordinate or a CSS selector.
    location: str = ""
    #: Which part of the app this control lives in. "shell" is the persistent
    #: frame -- header, left menu, floating assistant -- and "main" is the
    #: content area the shell swaps around. Advisory: it reorders the action
    #: plan and labels the report, and never removes anything.
    region: Literal["shell", "main"] = "main"
    #: The name came from a tooltip revealed by hovering, not from the DOM. An
    #: icon-only control with no accessible name is also a real accessibility
    #: finding, so the provenance is worth keeping rather than erasing.
    name_from_hover: bool = False

    @property
    def stable_selector(self) -> bool:
        """Located by something the app named on purpose, not by position.

        A ``data-testid`` or a real ``id`` survives a re-render; a css-path does
        not. This is what decides whether a pointer-cursor element is trusted
        enough to participate in state identity.
        """
        return self.selector_strategy.split("+")[0] in {
            "data-testid", "data-test", "data-cy", "data-qa", "id",
        }

    def describe_location(
        self, viewport_width: int, document_height: int, sidebar_fraction: float = 0.25
    ) -> str:
        """Say where this control is the way a person would.

        A test step reading "click Add Screen (main area, top-left)" can be
        followed by someone looking at the screen; "click [data-testid=
        dashboard_screen_addbtn]" cannot, and neither can a raw pixel pair.
        The selector still travels with the step for automation -- this is the
        human half.

        Vertical position is measured against the whole document, because
        "bottom of the page" means the end of the content, not the bottom of the
        window. Horizontal is measured against the viewport, since pages
        essentially never scroll sideways.
        """
        width = max(viewport_width, 1)
        height = max(document_height, 1)

        if self.landmark == "dialog":
            region = "dialog"
        elif self.landmark == "header":
            region = "header"
        elif self.landmark == "footer":
            region = "footer"
        elif self.landmark in {"nav", "aside"} or (
            self.x + self.w <= width * sidebar_fraction
        ):
            # Apps routinely build a sidebar out of plain divs, so position has
            # to stand in for the landmark the markup never declared.
            region = "left sidebar"
        else:
            region = "main area"

        centre_y = self.y + self.h / 2
        centre_x = self.x + self.w / 2
        vertical = (
            "top" if centre_y < height / 3
            else "middle" if centre_y < height * 2 / 3
            else "bottom"
        )
        horizontal = (
            "left" if centre_x < width / 3
            else "centre" if centre_x < width * 2 / 3
            else "right"
        )
        return f"{region}, {vertical}-{horizontal}"

    def reading_key(self, band: int = 20) -> tuple[int, int]:
        """Sort key for "top to bottom, left to right".

        The vertical position is bucketed into ``band``-pixel rows before the
        horizontal one is considered, because controls a person reads as one row
        are rarely pixel-aligned: a 32px button next to a 24px icon differ by a
        few pixels vertically, and sorting on raw ``y`` would interleave two
        rows into a staircase.
        """
        return (self.y // band, self.x)

    def stable_identity(self) -> str:
        """Identity that survives the page being redrawn.

        ``identity()`` includes the selector, and on this app a quarter of
        selectors are positional -- ``li:nth-of-type(3)``. When the list redraws
        and the same control lands at position 2, its identity changes and it
        looks like a control we have never seen. Measured consequence: one
        "Export" button was queued as four separate popups, and 21 unnamed
        ``div`` triggers produced 21 states.

        So: prefer the label the app gave the control, fall back to its role and
        name with digits normalised, and only use the raw selector when there is
        nothing better -- which at least keeps behaviour no worse than before.
        """
        if self.stable_selector:
            return f"{self.role}{self.selector}"
        name = _normalise_name(self.name)
        if name:
            return f"{self.role}{name}"
        return f"{self.role}{self.selector}"

    def identity(self) -> str:
        """Cross-state identity, used to exercise global chrome only once.

        A floating help button or a header nav item appears on every state.
        Clicking it once per state wastes the entire click budget on the same
        control; this key is what lets the crawler recognise it as already
        exercised.

        A hover-derived name is left out for the same reason it is left out of
        the signature: it depends on whether the tooltip appeared for us this
        time, so including it would make one control look like two.
        """
        label = "" if self.name_from_hover else self.name.strip().lower()
        return f"{self.role}\x1f{label}\x1f{self.selector}"

    def signature(self) -> tuple[str, str, bool, str]:
        """The tuple that participates in the state fingerprint.

        The name is normalised before it counts toward identity: digits become
        ``#`` and it is truncated. On a real dashboard the accessible name of a
        card container is its entire text content -- ``StorageUsed0.00KB``,
        ``AppsApp NameApp Name...`` -- so a counter ticking or a list gaining a
        row would otherwise make the same page a brand new state. Identity
        should track *structure*, not the data rendered into it.

        A hover-derived name is deliberately excluded: whether the tooltip won
        the race in a given run is a property of our probe, not of the page, so
        letting it in would make the same state fingerprint two different ways.
        """
        return (
            self.role,
            "" if self.name_from_hover else _normalise_name(self.name),
            self.enabled,
            str(self.kind),
        )


class FormField(BaseModel):
    name: str | None = None
    label: str | None = None
    label_source: str | None = None
    input_type: str = "text"
    semantic_hint: str | None = None
    required: bool = False
    pattern: str | None = None
    min: str | None = None
    max: str | None = None
    minlength: int | None = None
    maxlength: int | None = None
    step: str | None = None
    options: list[str] | None = None
    default_value: str | None = None
    readonly: bool = False
    disabled: bool = False
    validation_message: str | None = None
    selector: str = ""
    confidence: Confidence = Confidence.MEDIUM

    def constraint_summary(self) -> str:
        bits: list[str] = []
        if self.required:
            bits.append("required")
        if self.pattern:
            bits.append(f"pattern={self.pattern}")
        if self.minlength is not None:
            bits.append(f"minlength={self.minlength}")
        if self.maxlength is not None:
            bits.append(f"maxlength={self.maxlength}")
        if self.min is not None:
            bits.append(f"min={self.min}")
        if self.max is not None:
            bits.append(f"max={self.max}")
        if self.step is not None:
            bits.append(f"step={self.step}")
        if self.semantic_hint:
            bits.append(f"autocomplete={self.semantic_hint}")
        if self.options:
            bits.append(f"options={len(self.options)}")
        return " ".join(bits)


class FormSpec(BaseModel):
    form_id: str
    origin: Literal["explicit", "inferred"]
    selector: str
    action: str | None = None
    method: str | None = None
    submit_selector: str | None = None
    submit_label: str | None = None
    fields: list[FormField] = Field(default_factory=list)
    confidence: Confidence = Confidence.HIGH


class SearchControl(BaseModel):
    input_selector: str
    label: str | None = None
    submit_selector: str | None = None
    live_suggestions: bool = False
    result_container: str | None = None
    submits_via: Literal["GET", "POST", "client_only", "unknown"] = "unknown"


class OverlaySpec(BaseModel):
    overlay_type: OverlayType
    role: str | None = None
    label: str | None = None
    selector: str | None = None
    element_count: int = 0

    @property
    def transient(self) -> bool:
        return self.overlay_type in TRANSIENT_OVERLAYS


class Landmark(BaseModel):
    role: str
    label: str | None = None


class EndpointObservation(BaseModel):
    method: str
    url: str
    status: int | None = None
    blocked: bool = False


class Boundary(BaseModel):
    origin: str
    url: str
    reason: str
    triggered_by: str | None = None


class Observation(BaseModel):
    """Anything noteworthy that is not itself a state: dialogs, uploads,
    downloads, blocked writes. All of it is useful QA material."""

    kind: str
    detail: str
    triggered_by: str | None = None


class PageModel(BaseModel):
    url: str
    normalized_url: str
    title: str
    fingerprint: str = ""
    depth: int = 0
    arrival_action: str = "initial navigation"
    landmarks: list[Landmark] = Field(default_factory=list)
    elements: list[Element] = Field(default_factory=list)
    forms: list[FormSpec] = Field(default_factory=list)
    searches: list[SearchControl] = Field(default_factory=list)
    overlays: list[OverlaySpec] = Field(default_factory=list)
    network: list[EndpointObservation] = Field(default_factory=list)
    console_errors: list[str] = Field(default_factory=list)
    blocked_mutations: list[str] = Field(default_factory=list)
    observations: list[Observation] = Field(default_factory=list)
    screenshot_path: str | None = None
    html_path: str | None = None
    #: Viewport and full document size at capture time. Kept so a position can
    #: be re-derived, and so a reviewer knows which screen size the locations
    #: in the test cases describe.
    viewport_width: int = 0
    viewport_height: int = 0
    document_height: int = 0
    #: Total DOM nodes on the page. Context for the interactive counts: 13
    #: actionable controls inside 2,400 DOM nodes is a very different page from
    #: 13 inside 60.
    dom_nodes: int = 0
    capture_status: Literal["complete", "partial_timeout", "partial_error"] = "complete"

    @property
    def actionable_count(self) -> int:
        """Elements a tester can act on, as opposed to everything extracted."""
        return sum(1 for e in self.elements if is_actionable(e))

    @property
    def main_actionable_count(self) -> int:
        """Actionable elements in the content area, ignoring the app frame.

        The number that actually says how much of this state is worth testing:
        a Settings page with 38 actionable elements of which 27 are the header
        and the left menu is an 11-element page wearing a big number.
        """
        return sum(1 for e in self.elements if is_actionable(e) and e.region == "main")

    def selector_set(self) -> set[str]:
        """Every selector this page can vouch for -- the validator's grounding set."""
        found = {e.selector for e in self.elements if e.selector}
        for form in self.forms:
            found.add(form.selector)
            if form.submit_selector:
                found.add(form.submit_selector)
            found.update(f.selector for f in form.fields if f.selector)
        for search in self.searches:
            found.add(search.input_selector)
            if search.submit_selector:
                found.add(search.submit_selector)
        return {s for s in found if s}


# --------------------------------------------------------------------------
# Navigation graph
# --------------------------------------------------------------------------


class NavNode(BaseModel):
    id: str
    fingerprint: str
    url: str
    normalized_url: str
    title: str
    depth: int
    node_type: Literal[
        "page", "modal", "drawer", "dropdown", "panel", "boundary", "external"
    ] = "page"
    element_count: int = 0
    #: Subset of element_count that a tester can act on.
    actionable_count: int = 0
    #: Subset of actionable_count that is NOT the persistent header/left menu.
    main_actionable_count: int = 0
    #: Total DOM nodes, for context.
    dom_nodes: int = 0
    form_ids: list[str] = Field(default_factory=list)
    is_entry: bool = False
    visit_count: int = 1
    screenshot: str | None = None
    html: str | None = None
    #: What a tester can actually do here: one line per actionable element.
    actions: list[str] = Field(default_factory=list)
    #: Actionable elements this crawl did not exercise, and why.
    not_exercised: list[str] = Field(default_factory=list)
    #: For a state that is the *same page* with something opened on top of it:
    #: the node it opened from, and the control that opened it. Without these a
    #: menu shows up as a second mysterious node with the same title as the
    #: page, and a generated precondition cannot say how to get back to it.
    parent_state: str | None = None
    opened_by: str | None = None


class NavEdge(BaseModel):
    id: str
    source: str
    target: str
    action: Literal[
        "navigate", "click", "type", "select", "press_enter", "check", "hover"
    ]
    label: str
    selector: str = ""
    element_role: str = ""
    element_name: str = ""
    input_value: str | None = None
    outcome: Outcome
    annotations: list[str] = Field(default_factory=list)
    reversible_by: Literal["escape", "back", "goto", "none"] = "goto"


class NavGraph(BaseModel):
    target: str
    generated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    nodes: list[NavNode] = Field(default_factory=list)
    edges: list[NavEdge] = Field(default_factory=list)
    entry_node: str = ""
    boundaries: list[Boundary] = Field(default_factory=list)
    unexplored: list[str] = Field(default_factory=list)


# --------------------------------------------------------------------------
# Test cases
# --------------------------------------------------------------------------


class Step(BaseModel):
    step_number: int = Field(description="1-based, contiguous within the test case")
    action: str = Field(description="One concrete action a tester performs")
    expected_result: str = Field(description="Observable outcome of this step alone")


class TestCase(BaseModel):
    __test__ = False  # not a pytest class
    test_id: str = Field(description="Format TC_001")
    category: Category
    preconditions: list[str] = Field(default_factory=list)
    steps: list[Step] = Field(default_factory=list)
    overall_expected_result: str = ""
    source_url: str = ""
    source_selectors: list[str] = Field(default_factory=list)
    needs_review: bool = False
    review_notes: list[str] = Field(default_factory=list)


class TestCaseBatch(BaseModel):
    __test__ = False  # not a pytest class
    """What one LLM call returns -- the structured-output schema."""

    cases: list[TestCase] = Field(default_factory=list)


class TestSuite(BaseModel):
    __test__ = False  # not a pytest class
    target: str
    generated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    cases: list[TestCase] = Field(default_factory=list)
