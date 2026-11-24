---
name: skill-writing-guide
description: "Meta-skill for authoring and refactoring agent skills for frontier models. Separates the bare minimum (Goal, Mental Model, Contracts) from secondary guidance (Principles & Taste) and optional low-level patterns."
---

# Skill Writing Guide (`skill-writing-guide`)

## Meta: Design Philosophy of This Skill

This section is for skill authors and maintainers only. Do not leak it to end users.

- **Target**: Frontier models for years to come.
- **Why over-specified skills fail**: When a skill floods a frontier model with low-level procedures, rigid prohibitions, fill-in-the-blank templates, or long few-shot outputs, the model drops out of **reasoning mode** into **instruction-following (slot-filling) mode** and stops thinking.
- **Core rule — Do Not Repeat What You Know**:
  Treat everything that comes into your own mind critically. **Whatever a frontier model can work out on its own does not belong in a skill.** Every line in `SKILL.md` must earn its token cost under a strict value hierarchy:
  1. **User's Raw Intention** *(Highest Value)*: What is unique to the human owner—specific goal, scale target (e.g., `100 PRs/day`, `60-second scan`), non-standard framing, architectural taste, or personal voice.
  2. **Insights Emerged from Real Data / External Corpus**: Patterns distilled empirically from primary artifacts (accepted/rejected outputs, research logs, batch failure traces, or foundational literature)—never rules imagined in a vacuum.
  3. **Hard-Won Multi-Turn Conclusions**: Non-obvious root causes, design trade-offs, or footguns that took many turns of trial and error to uncover, recorded so future sessions conserve tokens.
- **Systems rule — Do Not Repeat Yourself (DRY)**:
  1. If information already lives in the project or skills system, introduce and reference it rather than copying it.
  2. Guard against de-sync rot: copy-pasted text drifts over time. When referencing another document or skill, state its durable role accurately and tell the reader when to open it.

---

## Goal

Write or refactor a skill that transfers the user's unique intent, domain mental model, and high-level contracts to a frontier model with minimal reading and token overhead—preserving autonomous thinking and openness where 100% compliance is unnecessary.

---

## Mental Model

1. **Give the `What`, `Why`, and `High-Level How` — Leave Execution to the Model**:
   - Trust the frontier model's coding, tool-use, and reasoning ability.
   - Instead of micromanaging mechanical steps, align the model on **What** to achieve (`Goal`), **Why** the problem is framed this way (`Mental Model`, `Principles`, and `Taste Preferences`), and **High-Level How** the pieces fit together (`Contracts`).

2. **Separate the Bare Minimum from Optional Additions**:
   - Not every skill needs every section. Keep the core spine minimal (`Goal`, `Mental Model`, `Contracts`), add `Principles & Taste Preferences` only where important boundaries or tie-breaking leans must be drawn, and pull in low-level structural patterns only when the task warrants them.

3. **Encourage Openness Where 100% Compliance Is Unnecessary**:
   - Separate true protocol invariants (where a parser, CLI, or safety boundary requires exact compliance) from structural guidance.
   - Frame outlines, field lists, and examples as **recommendations and demonstrations, not rigid templates**, explicitly allowing the agent to adapt, combine, or omit sections when it improves clarity or efficiency.

4. **Don't Tell the Model What It Already Knows (The Generalization–Specialization Model)**:
   - **High-Dimensional Generalization vs. Ad-Hoc Specialization**: Keep mental models and principles high-dimensional and abstract so frontier models can specialize them to the job ad-hoc. Never overreach into specialization, make narrow statements that fail to generalize, or impose prescriptive rules that blunt creativity.
   - **Contracts Exist Only from Outside Necessity**: Introduce structural contracts *only* when an external counterparty requires uniformity (for example, a verifier or parser expects a fixed schema, a CLI requires specific flags, or spawned workspaces expect a uniform directory layout). Pure cognitive-lens or principle-guiding skills need no output contract or `Structural Recommendation` section at all.
   - **No Speculative Prescriptive Patches**: Add detailed, prescriptive rules *only* when agents actually fail at that detail level in real runs—never invent them speculatively when authoring a skill.

5. **Positive Prompting — Avoid the "Pink Elephant" & Scar Tissue**:
   - State what good looks like rather than reciting mistakes to avoid; listing forbidden habits primes the model on them and accumulates brittle scar tissue across sessions.
   - Reserve explicit prohibitions or negative contrasts strictly for high-level conceptual, protocol, or safety boundaries where positive framing alone fails.

---

## 1. The Bare Minimum (`What`, `Why`, and Externally Necessary `High-Level How`)

Build every skill on up to three foundational elements (written as explicit sections, or woven into a single 25-line page for a pure cognitive lens):

1. **`Goal` (`What`)**:
   - State what the skill accomplishes, for what audience, and under what efficiency or scale target (e.g., earn reviewer trust with minimal reading at **100 PRs/day per engineer**; divide work cleanly between a frontier architect and a fast worker; keep open-ended research coherent across sessions via **belief updates**).

2. **`Mental Model` (`Why`)**:
   - Define the high-dimensional conceptual framing, order of operations, or responsibility split that governs decisions in this domain so the model can specialize it to any concrete task. Examples:
     - A 5-step simplification algorithm applied in strict sequence (question requirements -> delete -> simplify -> accelerate -> automate).
     - *Research = Belief Update* vs. *Engineering = State Transition*.
     - A *Decision Ladder* for delegation: `User Intent -> High-Level Design -> Module Contracts [Split Point] -> Implementation`.
     - *Theory of Mind for the Reader* + Swales' *CARS* moves + a *Single-Root, Single-End DAG* for structured writing.

3. **`Contracts` (`High-Level How` — Only When Outside Necessity Requires It)**:
   - Include a contract **only** when an external system, verifier, workspace layout, or human workflow gate requires a predictable deliverable or procedural boundary. **If no external contract exists, do not invent a `Contracts` or `Structural Recommendation` section.**
   - When an external contract does exist, separate **hard protocol contracts** (exact file naming, sync directories, CLI flags, or human-approval status ceilings) from **adaptable structural recommendations** (e.g., *"Consider this a recommendation. Break this format whenever doing so improves clarity or efficiency."*).

---

## 2. Secondary Recommendations (`Principles` & `Taste Preferences`)

Add `Principles` and `Taste Preferences` when important boundaries or tie-breaking leans must be drawn—to prevent predictable LLM failure modes, protect reader experience, or capture the owner's analytical and aesthetic judgment:

1. **Drawing Boundaries with `Principles` (*What Is Valid vs. Invalid*)**:
   - **Theory of Mind & Zero Context Leakage**: Remember the reader was not in the room when the work was done. Write for a Token-Zero reader; use project-defined names and portable project-relative paths; define symbols on first use; never leak drafting scaffolding (*"in the supplied file"*, *"as discussed earlier"*).
   - **Attack the Premise & The Escape Hatch**: Authorize the agent to question whether the task framing, draft, or underlying code/data is actually valid before polishing or complying—and to halt or decline the deliverable when the premise fails.
   - **Principles Over Instructions**: State explicitly that rules serve the mental model and can be broken when justified by the audience or context.

2. **Pinning Judgment with `Taste Preferences` (*When Two Directions Are Both Valid, Which One to Lean On*)**:
   - **Honest Limitations & Scope Cuts**: Require upfront disclosure of deliberate simplifications, unhandled edge cases, and out-of-scope boundaries.
   - **Concrete Heuristic Budgets with Explainable Exceptions**: Give crisp numeric heuristics while allowing reasoned exceptions (e.g., in UI review: *"`< 5` theme colors, `< 5` font sizes, and `< 10` spacing sizes—every exception needs a source-code comment explaining why it looks better than the standard"*).
   - **Deterministic Ordering over Subjective Taste (When Stability Matters)**: In extraction or ledger tasks, prefer an ordering any agent will reproduce across runs (*"When in doubt, prefer stable ordering between runs over logical taste"*).
   - **Author's Voice (`Expression DNA`)**: When a skill speaks in the user's voice, distill structural rhythm (e.g., 2-space outline trees, milestones over intermediate steps, headline verdicts + compact tables, formatting and language habits) rather than fill-in-the-blank sentence templates.

---

## 3. Low-Level Recommendations (Optional Patterns)

Select from these concrete mechanisms only when they fit the skill's need:

1. **Optional `Meta: Design Philosophy` Section (For Skill Authors Only)**:
   - Place a brief `## Meta` block in `SKILL.md` declaring *"This section is for skill authors and maintainers only. Do not leak it to end users"* to record why the skill is shaped that way, its scale target, and whether `references/` should be skipped at runtime.

2. **Externalizing Assets into `resources/` (or `templates/`), `references/`, and `archive/`**:
   - Keep `SKILL.md` lean by pushing supporting files into dedicated subdirectories:
     - **`resources/` or `templates/` *(Used on demand at runtime)***: Self-contained directory templates where each subfolder carries its own local `README.md` contract so agents load rules only at point of use, or bundled lookup sheets (such as a terminology glossary).
     - **`references/` *(For skill authors only — not read at runtime)***: Raw corpus samples, evidence tables, and long counterexamples used while distilling the skill (prevents few-shot length bias from bloating runtime output).
     - **`archive/` *(Historical versions)***: Superseded editions of `SKILL.md`.

3. **Locked Loops vs. Open-Ended Menus**:
   - Lock only the schema that prevents reward-hacking or parser breakage, and explicitly leave adjacent work open-ended (e.g., lock paired experiment contract/result files while leaving synthesis, diagnostics, and roadmaps open-ended; or lock one mandatory core field and list optional ones in a `| Recommended field | When useful |` table).

4. **Non-Limiting Micro-Contrasts (Instead of Full-Document Examples)**:
   - When an example is needed to pin taste, use a compact side-by-side contrast table or a 3-line `Before / After` labeled *"treat these as examples of the principle, not sentence templates to copy"*.

5. **Composable Sibling Skills (`Related Skills`)**:
   - Delegate orthogonal concerns (such as sentence-level prose cleanup, structured claim extraction, or pre-execution scoping) to sibling skills by reference rather than duplicating their rules.

6. **Adversarial Second Pass / Isolated Verification**:
   - Close with a lightweight, high-leverage verification mechanism tailored to the domain:
     - **Isolated Token-Zero Subagent Blind Review**: A fresh subagent with zero drafting context evaluates whether the deliverable is trustworthy and readable.
     - **Adversarial Walk / Second-Pass Diagnostic**: A sentence-by-sentence *"Why am I looking at this?"* walk for writing, or a diagnostic checklist gated on a real rendered screenshot for UI work.

7. **Deterministic Helper Scripts to Remove Mechanical Friction (Without Killing Intelligence)**:
   - When an agent repeatedly burns tokens or hits race conditions on mechanical plumbing—such as file-locked state updates, multipart API uploads, zero-token process waiting, stripping noisy heartbeat lines from logs, or raw terminal capture—package that logic into a deterministic CLI or `scripts/` helper.
   - **Hard Boundary — Feed Intelligence, Never Replace It**: Script the **deterministic plumbing** (atomic I/O, locking, schema gates, noise filtering, raw capture), **never heuristic judgment**. If a helper script pre-classifies ambiguous state into JSON buckets, a frontier model will lazily format the script's JSON instead of inspecting the raw evidence with its own eyes.
