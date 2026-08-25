"""The in-page extraction script.

One `evaluate` round-trip returns every raw signal we need: interactive nodes
with computed role/name/geometry, explicit and inferred forms, landmarks, and
currently-open overlays. Doing this in one shot rather than per-element keeps a
200-element page to a single IPC hop.

Note on the accessibility signal: we compute role and accessible name in-page
rather than calling ``page.accessibility.snapshot()``. The snapshot returns a
tree with no stable mapping back to DOM nodes, and we need role/name *attached
to an element we can then build a selector for*. The ladder below mirrors the
ARIA accname algorithm closely enough for QA purposes (aria-labelledby ->
aria-label -> associated label -> text -> title -> placeholder -> alt/value).
"""

from __future__ import annotations

EXTRACT_JS = r"""
(opts) => {
  // Site-supplied markers for "this is clickable". Analytics instrumentation is
  // the best such signal there is: a team that tracks button clicks has already
  // labelled every button, and those labels survive re-skinning because the
  // reporting depends on them.
  //
  // It is also the only signal for controls the platform cannot see. Samsung
  // VXT's profile avatar -- the sole route to Settings and its eleven pages --
  // has no role, no tabindex, and `cursor: auto`, so it is invisible to every
  // generic rule. It does carry ga_text_key and ga-button-action-class.
  const EXTRA_CLICKABLE = ((opts || {}).extraClickable || []).filter(Boolean);
  const INTERACTIVE = [
    'a[href]', 'button', 'input', 'select', 'textarea',
    '[role]', '[onclick]', '[tabindex]:not([tabindex="-1"])',
    '[contenteditable]:not([contenteditable="false"])',
    'summary', 'label[for]',
    'div', 'span', 'li', 'td', 'article', 'section', 'img'  // filtered by looksClickable
  ].join(',');

  // `[role]` in the selector above also matches structural roles -- region,
  // status, search landmarks, banner. Those are not things a tester clicks, and
  // letting them into the inventory both inflates it and destabilises the
  // fingerprint. Only these roles count as interactive.
  const INTERACTIVE_ROLES = new Set([
    'button', 'link', 'checkbox', 'radio', 'switch', 'tab', 'menuitem',
    'menuitemcheckbox', 'menuitemradio', 'option', 'combobox', 'listbox',
    'textbox', 'searchbox', 'slider', 'spinbutton', 'treeitem', 'gridcell',
  ]);
  const NATIVE_TAGS = new Set(['A', 'BUTTON', 'INPUT', 'SELECT', 'TEXTAREA', 'SUMMARY']);

  // Content inside a transient overlay must not reach the signature: a toast
  // that auto-dismisses after 4s would otherwise make every visit to the same
  // page a brand new state.
  const TRANSIENT_SEL = '[role=alert],[role=status],[role=tooltip]';

  // A layout container is not a control, whatever role it claims.
  //
  // Samsung VXT ships `<div id="container" role="button">` around the entire
  // page grid. Taken at face value that is one "button" whose accessible name
  // is every word on the screen ("ContentBuy Nowsouresh Anand...SettingsManual
  // Sign Out..."), which is useless as a test target, destabilises the
  // fingerprint, and hides the real controls nested inside it. The pointer-
  // cursor path already guards against this; anything qualifying by role or
  // tabindex bypassed those guards entirely.
  //
  // Native controls are exempt: a <button> wrapping a lot of markup is still a
  // button, and cannot contain other interactive elements legally anyway.
  function isContainer(el) {
    if (NATIVE_TAGS.has(el.tagName)) return false;
    if ((el.innerText || '').trim().length > 200) return true;
    return el.querySelectorAll(
      'a[href],button,input,select,textarea,[role=button],[role=link],[role=menuitem]'
    ).length >= 5;
  }

  function matchesExtra(el) {
    for (const sel of EXTRA_CLICKABLE) {
      try { if (el.matches(sel)) return true; } catch (e) { /* bad selector */ }
    }
    return false;
  }

  function isInteractive(el) {
    if (NATIVE_TAGS.has(el.tagName)) return true;
    if (matchesExtra(el)) return true;
    const r = (el.getAttribute('role') || '').split(/\s+/)[0];
    if (r && INTERACTIVE_ROLES.has(r)) return true;
    if (el.hasAttribute('onclick')) return true;
    if (el.hasAttribute('contenteditable')) return true;
    const ti = el.getAttribute('tabindex');
    if (ti !== null && ti !== '-1') return true;
    return false;
  }

  // React attaches listeners at the root, so a <div onClick={...}> has NO
  // onclick attribute in the DOM -- attribute sniffing cannot see it at all.
  // `cursor: pointer` is the one framework-agnostic signal left: it is what
  // makes the element look clickable to the user, so it is what makes it
  // clickable to a tester.
  //
  // Nesting is the hard part, and it cannot be decided one element at a time.
  // A dashboard card is itself clickable *and* carries its own action buttons
  // (a "+", a kebab menu); both are real, separate test targets. So this is a
  // two-phase resolution: collect every candidate, then decide which survive
  // by looking at the candidate set as a whole (see resolveClickables).
  function pointerCandidate(el) {
    if (getComputedStyle(el).cursor !== 'pointer') return false;
    const r = el.getBoundingClientRect();
    if (r.width < 8 || r.height < 8) return false;
    if (r.width * r.height > window.innerWidth * window.innerHeight * 0.5) return false;
    // Skip if it contains its own native control; that control is the target.
    if (el.querySelector('a[href],button,input,select,textarea')) return false;
    // Skip if it *sits inside* a real control. `cursor` is an inherited
    // property, so every span inside a styled <a> computes to pointer;
    // reporting them duplicates the link under a worse selector.
    //
    // "Real" is load-bearing. Samsung VXT puts role="button" on the page grid
    // (`<div id="container" role="button">`), and a naive closest() match
    // therefore rejected every pointer-cursor element in the entire
    // application -- the header, the profile menu, the left nav, all of it.
    // So walk up, and let a container-sized ancestor pass by.
    const CONTROL_SEL = 'a[href],button,input,select,textarea,summary,' +
        '[role=button],[role=link],[role=menuitem],[role=tab],[role=option]';
    let host = el.parentElement ? el.parentElement.closest(CONTROL_SEL) : null;
    while (host) {
      if (!isContainer(host)) return false;      // a genuine control owns us
      host = host.parentElement ? host.parentElement.closest(CONTROL_SEL) : null;
    }
    // Skip page-level containers that merely inherit `cursor: pointer`. Their
    // accessible name is the entire page text ("ContentBuy Nowsouresh Anand..."),
    // which is useless as a test target and pollutes every state.
    if ((el.innerText || '').trim().length > 120) return false;
    if (el.querySelectorAll('*').length > 60) return false;
    return true;
  }

  // Two rejection rules, both needing the whole candidate set:
  //
  //  - **pass-through wrapper**: a candidate that contains another candidate
  //    of nearly its own size is just a shell around it -- keep the inner one.
  //  - **container**: a row or grid holds several candidates that each take a
  //    large share of its own area. Measuring share rather than raw count is
  //    what separates it from a card, whose "+" and kebab menu are tiny next to
  //    the card itself -- so the card survives as a click target and its
  //    buttons survive alongside it.
  //  - **echo of an ancestor**: `cursor` is inherited, so the title span inside
  //    a clickable card is itself a candidate carrying the card's own text.
  //    Same text as an enclosing candidate means it adds nothing -- drop it and
  //    keep the ancestor, which owns the handler and the better selector.
  //
  // Anything else survives, so a clickable card and the "+" inside it are BOTH
  // reported. The previous rule rejected any element with a pointer-cursor
  // ancestor, which silently discarded every control inside every clickable
  // card -- on a real dashboard that was 62 of 78 candidates.
  // Does this element carry an identifier a test can rely on? Used to settle
  // pass-through ties: between a card with data-testid and the bare <img>
  // filling it, the card is the target worth reporting.
  function hasStableId(el) {
    if (el.getAttribute('data-testid') || el.getAttribute('data-test') ||
        el.getAttribute('data-cy') || el.getAttribute('data-qa')) return true;
    return !!(el.id && !GENERATED_ID.test(el.id));
  }

  function resolveClickables() {
    const raw = [];
    for (const el of document.querySelectorAll(INTERACTIVE)) {
      if (!isVisible(el)) continue;
      if (isInteractive(el)) continue;      // handled by the native/role path
      if (!pointerCandidate(el)) continue;
      raw.push(el);
      if (raw.length >= 300) break;
    }
    const keep = new Set();
    const text = new Map(raw.map((el) => [el, norm(el.innerText || el.textContent)]));
    for (const el of raw) {
      const rect = el.getBoundingClientRect();
      const area = Math.max(rect.width * rect.height, 1);
      let inner = 0;
      let large = 0;
      let passthrough = false;
      let echo = false;
      for (const other of raw) {
        if (other === el) continue;
        if (el.contains(other)) {
          inner += 1;
          const o = other.getBoundingClientRect();
          const share = (o.width * o.height) / area;
          if (share >= 0.8) {
            // A tie on size is broken by identifier: keep whichever of the two
            // a generated test can actually locate again.
            if (!(hasStableId(el) && !hasStableId(other))) { passthrough = true; break; }
          } else if (share >= 0.25) {
            large += 1;
          }
        } else if (other.contains(el) && !hasStableId(el) && hasStableId(other) &&
                   area >= other.getBoundingClientRect().width *
                           other.getBoundingClientRect().height * 0.8) {
          // The other side of that tie: we fill an identifiable ancestor, so it
          // is the target and we are its filler.
          echo = true;
          break;
        } else if (other.contains(el) && text.get(other) === text.get(el)) {
          // Only when the ancestor is genuinely bigger. If it is the same size
          // it is a pass-through wrapper, and the rule above already drops it
          // in favour of this element -- dropping both would lose the control.
          const o = other.getBoundingClientRect();
          if (area < o.width * o.height * 0.8) { echo = true; break; }
        }
      }
      // `inner >= 8` is the backstop for a dense list whose rows are each too
      // small to trip the share test.
      if (passthrough || echo || large >= 2 || inner >= 8) continue;
      keep.add(el);
    }
    return keep;
  }

  const IMPLICIT_ROLE = {
    A: 'link', BUTTON: 'button', SELECT: 'combobox', TEXTAREA: 'textbox',
    SUMMARY: 'button', NAV: 'navigation', MAIN: 'main', ASIDE: 'complementary',
    HEADER: 'banner', FOOTER: 'contentinfo', FORM: 'form', DIALOG: 'dialog',
    TABLE: 'table', UL: 'list', OL: 'list', LI: 'listitem', IMG: 'img',
  };
  const INPUT_ROLE = {
    button: 'button', submit: 'button', reset: 'button', image: 'button',
    checkbox: 'checkbox', radio: 'radio', range: 'slider', search: 'searchbox',
    email: 'textbox', tel: 'textbox', url: 'textbox', text: 'textbox',
    number: 'spinbutton', password: 'textbox', file: 'button',
  };

  const norm = (s) => (s || '').replace(/\s+/g, ' ').trim().slice(0, 160);

  function isVisible(el) {
    if (!el || !el.isConnected) return false;
    if (el.closest('[aria-hidden="true"]')) return false;
    if (el.closest('[inert]')) return false;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') return false;
    if (parseFloat(cs.opacity || '1') === 0) return false;
    const r = el.getBoundingClientRect();
    if (r.width <= 0 || r.height <= 0) return false;
    return true;
  }

  function role(el) {
    const explicit = el.getAttribute('role');
    if (explicit) return explicit.split(/\s+/)[0];
    if (el.tagName === 'INPUT') {
      return INPUT_ROLE[(el.type || 'text').toLowerCase()] || 'textbox';
    }
    return IMPLICIT_ROLE[el.tagName] || '';
  }

  function labelText(el) {
    // <label for=id>
    if (el.id) {
      try {
        const lab = document.querySelector('label[for="' + CSS.escape(el.id) + '"]');
        if (lab) return { text: norm(lab.textContent), source: 'label[for]' };
      } catch (e) {}
    }
    // wrapping <label>
    const wrap = el.closest('label');
    if (wrap) return { text: norm(wrap.textContent), source: 'wrapping-label' };
    return null;
  }

  function accName(el) {
    const byIds = el.getAttribute('aria-labelledby');
    if (byIds) {
      const txt = byIds.split(/\s+/)
        .map((id) => { const n = document.getElementById(id); return n ? n.textContent : ''; })
        .join(' ');
      if (norm(txt)) return { name: norm(txt), source: 'aria-labelledby' };
    }
    const aria = el.getAttribute('aria-label');
    if (norm(aria)) return { name: norm(aria), source: 'aria-label' };

    const lab = labelText(el);
    if (lab && lab.text) return { name: lab.text, source: lab.source };

    if (!['INPUT', 'TEXTAREA', 'SELECT'].includes(el.tagName)) {
      const txt = norm(el.textContent);
      if (txt) return { name: txt, source: 'text' };
    }
    const title = el.getAttribute('title');
    if (norm(title)) return { name: norm(title), source: 'title' };

    const ph = el.getAttribute('placeholder');
    if (norm(ph)) return { name: norm(ph), source: 'placeholder' };

    if (el.tagName === 'INPUT' && ['submit', 'button', 'reset'].includes(el.type)) {
      if (norm(el.value)) return { name: norm(el.value), source: 'value' };
    }
    const img = el.querySelector('img[alt]');
    if (img && norm(img.alt)) return { name: norm(img.alt), source: 'img-alt' };

    return { name: '', source: 'none' };
  }

  // -- selector synthesis ladder -----------------------------------------
  const GENERATED_ID = /^(:[a-z0-9]+:|ember\d+|react-|radix-|mui-|headlessui-|[0-9a-f]{8,})/i;
  const OBFUSCATED_CLASS = /^(css-|sc-|jsx-|_[a-z0-9]{5,}|[a-z]{1,3}[0-9]{4,})/i;

  function q(s) { return String(s).replace(/(["\\])/g, '\\$1'); }

  function stableClasses(el) {
    return Array.from(el.classList)
      .filter((c) => c && !OBFUSCATED_CLASS.test(c) && c.length < 40)
      .slice(0, 2);
  }

  function cssPath(el) {
    const parts = [];
    let node = el;
    let depth = 0;
    while (node && node.nodeType === 1 && depth < 6) {
      if (node.id && !GENERATED_ID.test(node.id)) {
        parts.unshift('#' + CSS.escape(node.id));
        return parts.join(' > ');
      }
      let seg = node.tagName.toLowerCase();
      const cls = stableClasses(node);
      if (cls.length) seg += '.' + cls.map((c) => CSS.escape(c)).join('.');
      const parent = node.parentElement;
      if (parent) {
        const sameTag = Array.from(parent.children)
          .filter((c) => c.tagName === node.tagName);
        if (sameTag.length > 1) seg += ':nth-of-type(' + (sameTag.indexOf(node) + 1) + ')';
      }
      parts.unshift(seg);
      node = parent;
      depth += 1;
    }
    return parts.join(' > ');
  }

  function synthesize(el, r, name) {
    for (const attr of ['data-testid', 'data-test', 'data-cy', 'data-qa']) {
      const v = el.getAttribute(attr);
      if (v) return { selector: '[' + attr + '="' + q(v) + '"]', strategy: attr, confidence: 'certain' };
    }
    if (el.id && !GENERATED_ID.test(el.id)) {
      return { selector: '#' + CSS.escape(el.id), strategy: 'id', confidence: 'certain' };
    }
    if (r && name) {
      return {
        selector: 'role=' + r + '[name="' + q(name) + '"]',
        strategy: 'role+name',
        confidence: 'high',
      };
    }
    const aria = el.getAttribute('aria-label');
    if (aria) return { selector: '[aria-label="' + q(aria) + '"]', strategy: 'aria-label', confidence: 'high' };

    const ph = el.getAttribute('placeholder');
    if (ph) return { selector: '[placeholder="' + q(ph) + '"]', strategy: 'placeholder', confidence: 'medium' };

    const nm = el.getAttribute('name');
    if (nm) {
      return {
        selector: el.tagName.toLowerCase() + '[name="' + q(nm) + '"]',
        strategy: 'name-attr',
        confidence: 'medium',
      };
    }
    return { selector: cssPath(el), strategy: 'css-path', confidence: 'low' };
  }

  // -- overlays -----------------------------------------------------------
  const OVERLAY_ROLES = ['dialog', 'alertdialog', 'menu', 'listbox', 'tooltip', 'alert', 'status'];

  function zIndexBaseline() {
    const zs = Array.from(document.querySelectorAll('body *'))
      .slice(0, 800)
      .map((e) => parseInt(getComputedStyle(e).zIndex, 10))
      .filter((n) => !isNaN(n))
      .sort((a, b) => a - b);
    if (!zs.length) return 0;
    return zs[Math.floor(zs.length * 0.9)];
  }

  function detectOverlays() {
    const out = [];
    const seen = new Set();
    const baseline = zIndexBaseline();
    const vw = window.innerWidth, vh = window.innerHeight;

    const push = (el, type) => {
      if (seen.has(el)) return;
      seen.add(el);
      const nm = accName(el).name || norm(el.getAttribute('aria-label'));
      out.push({
        overlay_type: type,
        role: role(el),
        label: nm,
        selector: synthesize(el, role(el), nm).selector,
        element_count: el.querySelectorAll(INTERACTIVE).length,
      });
    };

    for (const el of document.querySelectorAll('[role],[aria-modal="true"],dialog[open]')) {
      if (!isVisible(el)) continue;
      const r = role(el);
      if (!OVERLAY_ROLES.includes(r) && el.getAttribute('aria-modal') !== 'true') continue;
      let type = 'modal';
      if (r === 'tooltip') type = 'tooltip';
      else if (r === 'alert' || r === 'status') type = 'toast';
      else if (r === 'menu' || r === 'listbox') type = 'dropdown';
      push(el, type);
    }

    // Portal / z-index heuristic: a large fixed panel appended near <body>.
    for (const el of document.body.children) {
      if (!isVisible(el)) continue;
      if (seen.has(el)) continue;
      const cs = getComputedStyle(el);
      if (cs.position !== 'fixed' && cs.position !== 'absolute') continue;
      const z = parseInt(cs.zIndex, 10);
      if (isNaN(z) || z <= baseline) continue;
      const r = el.getBoundingClientRect();
      const coverage = (r.width * r.height) / (vw * vh);
      if (coverage < 0.15) continue;
      const anchored = r.width / vw > 0.9 || r.height / vh > 0.9;
      push(el, anchored && coverage < 0.6 ? 'drawer' : 'modal');
    }
    return out;
  }

  // -- forms --------------------------------------------------------------
  const FIELD_SEL = 'input:not([type=hidden]),select,textarea';
  const SUBMITISH = /save|submit|continue|next|send|create|update|sign\s?in|log\s?in|register|apply|confirm|search/i;

  function fieldRecord(el) {
    const lab = accName(el);
    const opts = el.tagName === 'SELECT'
      ? Array.from(el.options).slice(0, 40).map((o) => norm(o.textContent))
      : null;
    const describedBy = el.getAttribute('aria-describedby') || el.getAttribute('aria-errormessage');
    let validationMsg = null;
    if (describedBy) {
      const n = document.getElementById(describedBy.split(/\s+/)[0]);
      if (n) validationMsg = norm(n.textContent) || null;
    }
    const r = role(el);
    return {
      name: el.getAttribute('name') || el.id || el.getAttribute('data-testid') || null,
      label: lab.name || null,
      label_source: lab.source,
      input_type: el.tagName === 'SELECT' ? 'select'
        : el.tagName === 'TEXTAREA' ? 'textarea'
        : (el.getAttribute('type') || 'text').toLowerCase(),
      semantic_hint: el.getAttribute('autocomplete') || null,
      required: el.hasAttribute('required') || el.getAttribute('aria-required') === 'true',
      pattern: el.getAttribute('pattern'),
      min: el.getAttribute('min'),
      max: el.getAttribute('max'),
      minlength: el.getAttribute('minlength') ? parseInt(el.getAttribute('minlength'), 10) : null,
      maxlength: el.getAttribute('maxlength') ? parseInt(el.getAttribute('maxlength'), 10) : null,
      step: el.getAttribute('step'),
      options: opts,
      default_value: el.getAttribute('value') || null,
      readonly: el.hasAttribute('readonly'),
      disabled: el.disabled === true,
      validation_message: validationMsg,
      selector: synthesize(el, r, lab.name).selector,
      confidence: lab.source === 'placeholder' ? 'low' : 'high',
    };
  }

  function findSubmit(scope) {
    const cands = Array.from(scope.querySelectorAll('button,input[type=submit],[role=button]'));
    for (const c of cands) {
      if (!isVisible(c)) continue;
      if (c.type === 'submit') return c;
      if (SUBMITISH.test(accName(c).name)) return c;
    }
    return null;
  }

  function collectForms() {
    const forms = [];
    let n = 0;
    const claimed = new Set();

    // Pass 1 -- explicit <form>
    for (const f of document.querySelectorAll('form')) {
      if (!isVisible(f)) continue;
      const fields = Array.from(f.querySelectorAll(FIELD_SEL)).filter(isVisible);
      fields.forEach((x) => claimed.add(x));
      const sub = findSubmit(f);
      forms.push({
        form_id: 'F' + String(++n).padStart(3, '0'),
        origin: 'explicit',
        selector: synthesize(f, 'form', accName(f).name).selector,
        action: f.getAttribute('action'),
        method: (f.getAttribute('method') || 'GET').toUpperCase(),
        submit_selector: sub ? synthesize(sub, role(sub), accName(sub).name).selector : null,
        submit_label: sub ? accName(sub).name : null,
        fields: fields.map(fieldRecord),
        confidence: 'certain',
      });
    }

    // Pass 2 -- inferred clusters. React usually omits <form> entirely, so
    // without this most real forms are invisible to us.
    const orphans = Array.from(document.querySelectorAll(FIELD_SEL))
      .filter((el) => isVisible(el) && !claimed.has(el) && !el.closest('form'));

    const groups = new Map();
    for (const el of orphans) {
      let anc = el.parentElement;
      let hops = 0;
      while (anc && hops < 5 && anc !== document.body) {
        const count = Array.from(anc.querySelectorAll(FIELD_SEL)).filter(isVisible).length;
        if (count >= 2 || findSubmit(anc)) break;
        anc = anc.parentElement;
        hops += 1;
      }
      if (!anc || anc === document.body || anc === document.documentElement) continue;
      if (!groups.has(anc)) groups.set(anc, []);
      groups.get(anc).push(el);
    }

    for (const [anc, fields] of groups) {
      const sub = findSubmit(anc);
      const committing = fields.some((f) =>
        ['password', 'email', 'file'].includes((f.getAttribute('type') || '').toLowerCase()));
      if (!(fields.length >= 2 || committing)) continue;
      if (!sub) continue;
      forms.push({
        form_id: 'F' + String(++n).padStart(3, '0'),
        origin: 'inferred',
        selector: synthesize(anc, role(anc), accName(anc).name).selector,
        action: null,
        method: null,
        submit_selector: synthesize(sub, role(sub), accName(sub).name).selector,
        submit_label: accName(sub).name,
        fields: fields.map(fieldRecord),
        confidence: fields.length >= 2 ? 'high' : 'medium',
      });
    }
    return forms;
  }

  // -- main collection ----------------------------------------------------
  const elements = [];
  const clickable = resolveClickables();
  let idx = 0;

  // Cross-path de-duplication.
  //
  // resolveClickables() settles nesting *within* the pointer-cursor set, but an
  // element can now also qualify natively, by role, or by an analytics marker.
  // A dashboard card matches two of those at once and arrives twice --
  // `#dashboard_screenCard` and `[data-testid="dashboard_screen"]` are one
  // control, and reporting both doubles the click budget and the fingerprint.
  //
  // Nesting plus near-identical area is what identifies a duplicate; a card and
  // the small "+" inside it overlap barely at all and both survive.
  const kept = [];
  function duplicateOf(el, box) {
    const area = Math.max(box.width * box.height, 1);
    for (const other of kept) {
      if (!el.contains(other.el) && !other.el.contains(el)) continue;
      const ratio = (other.box.width * other.box.height) / area;
      // Two ways to be the same control. Either the boxes are near-identical in
      // area, or they share a corner and a width -- a wrapper and the block
      // inside it, which is how `#dashboard_screenCard` and
      // `[data-testid="dashboard_screen"]` both arrived. The "+" on the same
      // card sits 200px to the right, so neither test can ever merge them.
      const sameCorner =
        Math.abs(other.box.left - box.left) <= 4 &&
        Math.abs(other.box.top - box.top) <= 4 &&
        Math.abs(other.box.width - box.width) <= 8;
      if (!sameCorner && (ratio < 0.8 || ratio > 1.25)) continue;
      // Same control. Keep whichever a generated test can locate more reliably.
      if (hasStableId(el) && !hasStableId(other.el)) {
        other.replaced = true;
        return null;            // caller replaces the older entry
      }
      return other;
    }
    return null;
  }
  for (const el of document.querySelectorAll(INTERACTIVE)) {
    if (!isVisible(el)) continue;
    const interactive = isInteractive(el);
    if (!interactive && !clickable.has(el)) continue;
    if (interactive && isContainer(el)) continue;

    const box0 = el.getBoundingClientRect();
    const dup = duplicateOf(el, box0);
    if (dup) continue;                       // an equivalent entry already exists
    if (el.tagName === 'LABEL' && el.getAttribute('for')) continue;  // label proxies its control
    const r = role(el);
    const a = accName(el);
    const sel = synthesize(el, r, a.name);
    const owningForm = el.closest('form');
    // Page-absolute geometry, so the crawler can walk a state the way a person
    // reads it: top to bottom, left to right. Scroll offsets are added because
    // an element below the fold has a negative viewport top and would otherwise
    // sort above the header.
    const box = box0;
    kept.push({el: el, box: box});
    elements.push({
      ref: 'E' + String(++idx).padStart(3, '0'),
      landmark: (function () {
        // Which structural region owns this control. Used to say "in the
        // header" rather than "at x=1128,y=25" in a generated test step.
        if (el.closest('[role=dialog],[role=alertdialog],dialog')) return 'dialog';
        if (el.closest('header,[role=banner]')) return 'header';
        if (el.closest('footer,[role=contentinfo]')) return 'footer';
        if (el.closest('nav,[role=navigation]')) return 'nav';
        if (el.closest('aside,[role=complementary]')) return 'aside';
        return null;
      })(),
      x: Math.round(box.left + window.scrollX),
      y: Math.round(box.top + window.scrollY),
      w: Math.round(box.width),
      h: Math.round(box.height),
      tag: el.tagName.toLowerCase(),
      role: r,
      name: a.name,
      name_source: a.source,
      selector: sel.selector,
      selector_strategy: sel.strategy,
      selector_confidence: sel.confidence,
      enabled: !(el.disabled === true || el.getAttribute('aria-disabled') === 'true'),
      visible: true,
      href: el.getAttribute('href'),
      target: el.getAttribute('target'),
      input_type: el.tagName === 'INPUT' ? (el.getAttribute('type') || 'text').toLowerCase() : null,
      aria_haspopup: el.getAttribute('aria-haspopup'),
      aria_expanded: el.getAttribute('aria-expanded'),
      in_search_landmark: !!el.closest('[role=search]'),
      transient: !!el.closest(TRANSIENT_SEL),
      pointer_cursor: !interactive,
      autocomplete: el.getAttribute('autocomplete'),
      form_ref: owningForm ? (owningForm.id || 'form') : null,
    });
    if (idx >= 400) break;   // hard cap: pathological pages must not blow up the payload
  }

  const landmarks = [];
  for (const el of document.querySelectorAll(
    'nav,main,aside,header,footer,[role=navigation],[role=main],[role=search],' +
    '[role=complementary],[role=banner],[role=contentinfo]')) {
    if (!isVisible(el)) continue;
    landmarks.push({ role: role(el) || el.tagName.toLowerCase(), label: accName(el).name || null });
  }

  return {
    url: location.href,
    title: document.title || '',
    elements: elements,
    forms: collectForms(),
    landmarks: landmarks,
    overlays: detectOverlays(),
    opened: (window.__qagen && window.__qagen.opened) || [],
    js_errors: (window.__qagen && window.__qagen.errors) || [],
    body_scroll_locked: getComputedStyle(document.body).overflow === 'hidden',
    dom_nodes: document.querySelectorAll('*').length,
    viewport_width: window.innerWidth,
    viewport_height: window.innerHeight,
    document_height: Math.max(
      document.documentElement.scrollHeight, window.innerHeight),
  };
}
"""

#: Cheap signature used by the settle poll and by restore() -- must stay far
#: cheaper than a full extraction, since it runs every 150ms.
#:
#: Transient overlays are excluded here for the same reason they are excluded
#: from the real fingerprint: otherwise a toast makes restore() believe the
#: page never came back to its previous state.
SIGNATURE_JS = r"""
() => {
  // Deliberately narrower than the full extraction: native controls and
  // explicit roles only. Pointer-cursor elements are excluded here for the
  // same reason they are excluded from the real fingerprint -- they drift
  // between renders, and restore() would never see the page come back.
  const sel = 'a[href],button,input,select,textarea,[role],[tabindex]:not([tabindex="-1"])';
  const out = [];
  const seen = new Set();
  for (const el of document.querySelectorAll(sel)) {
    if (el.closest('[role=alert],[role=status],[role=tooltip]')) continue;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const r = el.getBoundingClientRect();
    if (r.width <= 0 || r.height <= 0) continue;
    seen.add(el);
    out.push((el.getAttribute('role') || el.tagName) + ':' +
             (el.textContent || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 40));
    if (out.length > 400) break;
  }

  // React menus are made of plain divs, so the selector above cannot see them:
  // a "+" that opened "Add Screen" / "New Screen Wall" left this signature
  // completely unchanged, and the crawler's fast path recorded the click as
  // inert without ever running a real extraction. Identifier-bearing
  // pointer-cursor elements close that gap -- and only those, since a div found
  // by position is exactly the set that churns between renders. The identifier
  // alone is recorded, never the text, so a counter cannot move the signature.
  const IDENTIFIED = '[data-testid],[data-test],[data-cy],[data-qa],[id]';
  for (const el of document.querySelectorAll(IDENTIFIED)) {
    if (seen.has(el)) continue;
    if (el.closest('[role=alert],[role=status],[role=tooltip]')) continue;
    const cs = getComputedStyle(el);
    if (cs.cursor !== 'pointer') continue;
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const r = el.getBoundingClientRect();
    if (r.width <= 0 || r.height <= 0) continue;
    out.push('@' + (el.getAttribute('data-testid') || el.getAttribute('data-test') ||
                    el.getAttribute('data-cy') || el.getAttribute('data-qa') || el.id));
    if (out.length > 600) break;
  }
  return out.sort().join('|');
}
"""

#: Is a loading indicator on screen right now?
#:
#: Waiting for the spinner to *go away* is a far better "page is ready" signal
#: than any timer, because the app itself is telling us when it is done. Extra
#: site-specific selectors can be supplied from config.
LOADER_JS = r"""
(extraSelectors) => {
  const BUILTIN = [
    '[aria-busy="true"]',
    '[role=progressbar]',
    '[class*="loader" i]', '[class*="loading" i]', '[class*="spinner" i]',
    '[class*="skeleton" i]', '[class*="shimmer" i]',
    '[id*="loader" i]', '[id*="loading" i]', '[id*="spinner" i]',
    '[data-loading="true"]',
  ];
  const selectors = BUILTIN.concat(extraSelectors || []);
  for (const sel of selectors) {
    let nodes;
    try { nodes = document.querySelectorAll(sel); } catch (e) { continue; }
    for (const el of nodes) {
      const cs = getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden') continue;
      if (parseFloat(cs.opacity || '1') === 0) continue;
      const r = el.getBoundingClientRect();
      if (r.width <= 0 || r.height <= 0) continue;
      // A wrapper that merely has "loading" in a utility class but fills the
      // page is not a spinner; ignore anything covering most of the viewport
      // unless it explicitly declares aria-busy.
      const covers = (r.width * r.height) > (window.innerWidth * window.innerHeight * 0.85);
      if (covers && el.getAttribute('aria-busy') !== 'true') continue;
      return sel;
    }
  }
  return null;
}
"""

#: Read whatever label is on screen right now, optionally for a hovered element.
#:
#: Icon-only controls -- the "+" on a dashboard card -- routinely carry no
#: aria-label, no title and no text, so the accname ladder returns "". Their one
#: and only label is the tooltip the app renders on hover, which does not exist
#: in the DOM until the pointer is over the element. Called twice per element:
#: once with null for a baseline, once after hovering.
TOOLTIP_JS = r"""
(sel) => {
  const TIP = '[role=tooltip],[class*="tooltip" i],[id*="tooltip" i],[data-tooltip],' +
              '[class*="popper" i],[class*="tippy" i]';
  const norm = (s) => (s || '').replace(/\s+/g, ' ').trim().slice(0, 60);

  if (sel) {
    let host = null;
    try { host = document.querySelector(sel); } catch (e) {}
    if (host) {
      // Static labels first: cheaper and unambiguous.
      const t = norm(host.getAttribute('title') || host.getAttribute('data-tooltip'));
      if (t) return t;
      const dsc = host.getAttribute('aria-describedby');
      if (dsc) {
        const n = document.getElementById(dsc.split(/\s+/)[0]);
        if (n && norm(n.textContent)) return norm(n.textContent);
      }
    }
  }

  // Otherwise: the shortest visible tooltip-ish text on the page. Shortest,
  // because a tooltip is a word or two and a mis-matched container is a
  // paragraph.
  const out = [];
  for (const el of document.querySelectorAll(TIP)) {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    if (parseFloat(cs.opacity || '1') === 0) continue;
    const r = el.getBoundingClientRect();
    if (r.width <= 0 || r.height <= 0) continue;
    const txt = norm(el.innerText || el.textContent);
    if (txt) out.push(txt);
  }
  out.sort((a, b) => a.length - b.length);
  return out[0] || '';
}
"""

#: Cheap consent probe. A cookie banner reappears on every page load unless the
#: app persists the choice, and our own restore()-by-goto reloads constantly --
#: so this has to run per navigation, which means it cannot afford a full
#: extraction. Marks the button with an attribute and lets Python click it.
CONSENT_JS = r"""
(vocab) => {
  // Pass 1 -- a button whose own label says accept/agree/got it.
  const cands = document.querySelectorAll('button,[role=button],a[href="#"],input[type=button]');
  for (const el of cands) {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const r = el.getBoundingClientRect();
    if (r.width <= 0 || r.height <= 0) continue;
    const text = (el.textContent || el.getAttribute('aria-label') || el.value || '')
      .replace(/\s+/g, ' ').trim().toLowerCase();
    if (!text || text.length > 40) continue;
    if (vocab.some((v) => text.includes(v))) {
      el.setAttribute('data-qagen-consent', '1');
      return text;
    }
  }

  // Pass 2 -- a pinned banner that talks about cookies but whose only control
  // is an unlabelled X. Samsung VXT does exactly this, and pass 1 cannot see
  // it because the button has no consent vocabulary of its own.
  for (const box of document.querySelectorAll('div,section,aside,footer')) {
    const cs = getComputedStyle(box);
    if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
    const rect = box.getBoundingClientRect();
    if (rect.width <= 0 || rect.height <= 0) continue;
    const text = (box.innerText || '').toLowerCase();
    if (text.length > 600) continue;
    if (!/cookie|consent|privacy policy/.test(text)) continue;
    const closer = box.querySelector(
      'button,[role=button],[aria-label*="close" i],[aria-label*="dismiss" i],[class*="close" i]');
    if (closer) {
      closer.setAttribute('data-qagen-consent', '1');
      return 'cookie banner close';
    }
  }
  return null;
}
"""
