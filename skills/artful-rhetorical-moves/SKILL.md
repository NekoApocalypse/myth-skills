---
name: "Artful Rhetorical Moves"
description: Design and verify coherent, persuasive writing through deliberate rhetorical moves, high-contrast scene setting, and seamless conceptual transitions.
version: 20261022
---

# Artful Rhetorical Moves

Structure writing so every section, paragraph, and piece of evidence advances a single narrative arc. Apply this skill when drafting or reviewing essays, RFCs, product narratives, analytical reports, memos, or landing pages.

## Related Skills

- **`extract-claims-map` (Academic Counterpart):** The analytical reverse-engineering sibling of this skill. Where `extract-claims-map` deconstructs a research paper's rhetorical structure into a directed graph of scientific claims and experiments, `artful-rhetorical-moves` constructs forward-moving narrative flow for human readers.
- **`pstack/unslop` & `pstack/technical-writing` (Sentence-Level Execution):** Use alongside this skill. Once the macro rhetorical moves and transitions are in place, apply `pstack/unslop` to strip AI vocabulary, filler, crutch colons, em-dash abuse, and mannered prose.

---

## 1. Mental Model: Rhetorical Structure & Moves

Adapted from John Swales' **CARS (Create a Research Space)** model (1990) and `extract-claims-map`:

1. **Theory of Mind for the Reader (The Ultimate Verifier):**
   The reader was not in the room when the piece was drafted. Frontier models default to defensive, author-centric fact-dumping; this skill optimizes for the reader's live mental state. Every rhetorical move, conceptual transition, and self-contained explanation serves one test: what a cold reader knows, feels, and wonders at that exact sentence.
2. **Rhetorical Structure:** A document is not a container of paragraphs or a grid of cards. It is a directed narrative flow that moves a reader from their initial state of attention to a specific realization, decision, or action.
3. **Rhetorical Moves:** The argument unfolds through discrete functional moves. Every move must have three properties:
   - **Central Idea (`Assertion`):** What this specific part claims, verdicts, or establishes.
   - **Purpose (`Role`):** How this assertion advances the overarching argument at this exact moment.
   - **Connection (`Edge`):** How its concept grows out of the preceding move and hands off to the next move.
4. **Generalizing CARS Beyond Academia:**
   In academic introductions, Swales' CARS model moves through _Establishing a territory → Establishing a niche → Occupying the niche_. Across general, technical, and product writing, this generalizes into:
   - **Establish the Scene:** Anchor why the reader cares right now and surface a sharp tension.
   - **Expose the Gap:** Show why naive intuition, the status quo, or surface appearances fail.
   - **Occupy the Space:** Deliver the governing mechanism, evidence, and resolution.
   _(Treat this as a lens for how moves create space for the next thought, not a rigid section template.)_
5. **Single-Root, Single-End Topology (DAG):**
   - A coherent piece of writing forms a directed acyclic graph with **one root node** (the opening hook/scene) and **one end node** (the final conclusion or takeaway).
   - Every paragraph, example, or figure must lie on a path from the root to the end.
   - **No Dangling Nodes:** If a paragraph or chart merely reports a fact without advancing a claim on that path, either give it an assertion and role or cut it.

---

## 2. Core Principles

### Principle 1: Establish the Scene (The Hook)

Unless you are writing pure lookup reference documentation (where a dry definition comes first per `pstack/technical-writing`), do not open with a textbook definition or self-referential throat-clearing (_"In this document we describe..."_). Before a reader will care about your thesis, the opening must establish the scene through three checks:

1. **Immediate Relevance (Why Pay Attention Now):** Remind the reader of their own context, dilemma, or stakes in the first breath. The reader should immediately recognize why this matters to them, never wonder _"What is this, and why am I looking at it?"_
2. **The Magnet (Contrast, Emotion, Incentive, Hot Topic, or Significance):** Pair that relevance with a strong contrast, emotion, incentive, hot topic, or striking significance that draws their attention in.
3. **Attack the Premise:** Is the scene actually what you thought it is, or what the user or draft claims it is? Always reconsider the premise of the article when you start writing or reviewing it. For instance, a draft written like an introductory overview of an index might actually be an urgent decision brief on whether to buy a dip; a doc framed around a surface metric might actually be about a deeper structural shift. Fix the premise before polishing the sentences.

**Illustrative Examples (Non-Limiting):** There is no single formula for a hook. For example, when opening with unfamiliar metrics, anchoring the reader on a recognizable milestone before citing raw numbers is one effective way to give the numbers scale. The table below illustrates how establishing the scene differs from a cold textbook opening across domains—treat these as examples of the principle, not sentence templates to copy:

| Domain | Cold Textbook Opening (When Used by Mistake in a Narrative/Decision Doc) | Scene-Setting Opening (Relevance + Tension) |
| :--- | :--- | :--- |
| **Engineering RFC** | "Our CI pipeline consists of 42 container build stages managed by..." | "Every one-line CSS fix currently takes 47 minutes to reach staging, and 80% of that time is spent rebuilding containers that did not change." |
| **Product / Consumer** | "Personal wealth management tools help retail investors allocate assets..." | "Households hold 170T in deposits and 380T in property, yet under 5% in equities. Existing tools flood them with raw tickers instead of answers." |
| **Analytical Report** | "The index tracks 30 large technology and e-commerce companies..." | "The index is back to its 2024 rally starting line. Is buying here bottom-fishing or catching a falling knife? While the multiple looks cheap, institutional exposure has been cut in half." |

---

### Principle 2: Artful Transitions (Conceptual & Rhythmic Continuation)

Transitions should never rely on explicit hand-waving or mechanical glue (_"Furthermore"_, _"Moving on to section 2"_, _"Next, let's examine..."_). Instead, they should follow a natural logical, rhythmic, and slightly poetic flow where the **continuation of concept** is already present between the moves, giving the reader an effortless _"aha"_ feeling of connection.

1. **The "Aha" Concept Continuation:**
   - The link between Move $N$ and Move $N+1$ lives in the ideas and rhythm themselves, so the reader crosses the boundary before realizing a transition happened.
   - **Non-Limiting by Design:** There is no fixed formula for how a concept continues. Depending on the piece, continuation can take many shapes—for example (non-exhaustive):
     - _Resolving a live tension:_ Move $N$ leaves an unspoken question or paradox that Move $N+1$ immediately answers (e.g., showing valuation is at a record low, then immediately distinguishing _downside odds_ from _upward timing_).
     - _Causal or dimensional zoom:_ Stepping naturally from a symptom to its root mechanism, from macro structure to a concrete micro instance, or from diagnosis to resolution.
     - _Conceptual or rhythmic echo:_ Carrying a key image, constraint, or cadence from the closing line of one move into the opening line of the next so the thought pivots smoothly in place.
2. **Avoid Explicit Hand-Waving & Finger-Pointing:**
   - Strip meta-navigational commentary (_"As shown in the chart below"_, _"How to use the diagram below"_, _"The following sections answer different questions"_).
   - If a section requires a preamble explaining _how_ to read the next section, the narrative sequence is broken. Fix the sequence and delete the finger-pointing.
3. **Signposts Only Where Strictly Needed:**
   - Structural signposts (headings, eyebrows, numbered pillars, dividers) exist _only_ where the reader genuinely needs orientation across macro shifts.
   - Everywhere else, extra sub-labels, repetitive kickers, and inline `Label: explanation` crutch colons are visual clutter.

---

### Principle 3: Zero Context Leakage (Stand-Alone Integrity)

After a long working session, an author or agent is steeped in their own private context—the prompt history, intermediate files, internal theory docs, or raw datasets. Applying **Theory of Mind for the Reader**, remember that the actual audience (an executive, a customer, a colleague opening the document cold) was _not_ in the room when the piece was drafted. Write strictly for their mental state and vocabulary so the document stands completely on its own:

1. **Never Leak the Scaffolding:** Strip all references to the drafting process, internal rubrics, or workspace artifacts that the reader cannot see or does not care about (_"in the supplied file"_, _"per our theory doc"_, _"as discussed earlier"_, _"source unverified"_).
2. **Define on First Use:** Never drop magic symbols, internal shorthand, or domain jargon cold. Unless you are certain the target audience already knows a term, weave a concise definition into its first appearance.
3. **Quarantine Plumbing & Disclaimers:** Do not inject data-pipeline apologies, schema caveats, or compliance hedges into the main narrative flow where they undercut the argument. State verified claims directly in the body and push scope boundaries or methodology notes to footnotes.

---

### Principle 4: Assertion-Driven, Forward & Rhythmic Writing

1. **Forward Momentum & Varied Rhythm:** State claims directly without defensive hedging. Vary sentence lengths on purpose: short sentences land a verdict; longer sentences carry a causal chain or contrast. Run `pstack/unslop` to eliminate AI vocabulary, crutch colons, and em-dash abuse.
2. **Assertion supported by Data:** Never drop a raw statistic or figure and expect the reader to infer the point (_"Value dropped from 32.8% to 15.2%"_). Keep the claim close to the number, and include its consequences when relevant. For dramatic effects, you are allowed to switch the order around, but you should never produce dangling numbers.

---

### Principle 5: Principles Over Instructions

Every rule in this skill is breakable when justified by the narrative or audience need. A piece of writing that obeys every rule on paper while sounding mechanical, overcooked, or unnatural to a human reader has failed. Treat the specific patterns here as servants of the underlying mental model—shaping what the reader experiences sentence by sentence—not a rigid compliance rubric.

---

## 3. Final Adversarial Checklist

Run this pass at the end of a session to catch the specific failure modes agents drift into mid-work:

- [ ] **The Sentence-by-Sentence _"Why Am I Looking At This?"_ Walk:** Read the finished piece straight through from top to bottom (not just the block you last edited). Is there any sentence, card, or chart where a reader can stop and ask _"Why am I looking at this right now?"_ or where a data point sits without a clear verdict?
- [ ] **Signpost & Finger-Pointing Creep:** Did explicit hand-waving (_"see below"_, _"as shown in the next section"_, _"how to read the following"_) or redundant eyebrows/labels sneak in as visual clutter where the concept itself should carry the transition?
- [ ] **Session Context Leakage:** Stepping into the shoes of a cold reader who was _not_ in this conversation, did any internal vocabulary, prompt artifacts, file references (_"in the supplied CSV"_), or undefined shorthand leak into the text?
- [ ] **Overcooking vs. AI Slop (`pstack/unslop`):** Did the rewrite overcompensate into cheap drama/clickbait, or relapse into AI tells (`Label: explanation` crutch colons, em-dash chains, _"not just X, but Y"_, or main-flow disclaimers that undercut the claim)?
- [ ] **Extract Claims Map (`extract-claims-map`):** Does your writing follow a single DAG, where the claims are delivered with a series of artful rhetorical moves? Does everything else (e.g. data, explanations, evidence) support that rhetorical structure, instead of obscuring it?
