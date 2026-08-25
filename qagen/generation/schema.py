"""The LLM-facing schema.

Deliberately narrower than ``TestCase``: the model produces the QA content, and
we assign the provenance fields (``test_id``, ``source_url``, ``needs_review``)
ourselves. Asking the model for fields we already know invites it to guess at
them.

``harden_schema`` adapts Pydantic's JSON Schema output to the structured-output
requirements: every object needs ``additionalProperties: false`` and an explicit
``required`` list.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from ..models import Category, Step, TestCase


class GeneratedStep(BaseModel):
    step_number: int = Field(description="1-based, contiguous within this test case")
    action: str = Field(description="One concrete action a tester performs")
    expected_result: str = Field(description="Observable outcome of this step alone")


class GeneratedCase(BaseModel):
    category: Category = Field(description="Exactly one of the five categories")
    title: str = Field(description="Short imperative summary of what is being tested")
    preconditions: list[str] = Field(description="What must be true before step 1")
    steps: list[GeneratedStep] = Field(description="Ordered steps, at least one")
    overall_expected_result: str = Field(description="End condition of the whole case")
    source_selectors: list[str] = Field(
        description="Selectors copied verbatim from the supplied inventory"
    )


class GeneratedBatch(BaseModel):
    cases: list[GeneratedCase]


def harden_schema(model: type[BaseModel]) -> dict[str, Any]:
    """Pydantic JSON Schema -> structured-output-compatible JSON Schema."""
    schema = model.model_json_schema()

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            if node.get("type") == "object" or "properties" in node:
                node["additionalProperties"] = False
                props = node.get("properties")
                if isinstance(props, dict) and props:
                    node["required"] = list(props.keys())
            # Constraints the structured-output validator does not accept.
            for unsupported in ("minLength", "maxLength", "minimum", "maximum",
                                "multipleOf", "minItems", "maxItems", "format"):
                node.pop(unsupported, None)
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(schema)
    return schema


def to_test_case(generated: GeneratedCase, source_url: str) -> TestCase:
    return TestCase(
        test_id="TC_000",  # assigned by the validator
        category=generated.category,
        preconditions=list(generated.preconditions),
        steps=[
            Step(
                step_number=s.step_number,
                action=s.action,
                expected_result=s.expected_result,
            )
            for s in generated.steps
        ],
        overall_expected_result=generated.overall_expected_result,
        source_url=source_url,
        source_selectors=list(generated.source_selectors),
        review_notes=[f"title: {generated.title}"] if generated.title else [],
    )
