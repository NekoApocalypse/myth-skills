# The Hardened Protocol: Design Principles for Autonomous Agents

**Version:** 1.0
**Philosophy:** Determinism > Latent Surprise.
**Core Tenet:** Humans govern ad-hoc learning and latent intuition; Agents govern hardened, serialized execution.

## 1. Role Pinning (The Reliability Anchor)

* **Principle:** Agents do not "figure out" who they are; they are told.
* **Implementation:** Every prompt must begin with a high-priority "System Role" definition.
* **Why:** LLMs are probabilistic. "Pinning" the persona (e.g., "You are a Senior Systems Architect specialized in Go") collapses the probability distribution, making compliance with subsequent instructions significantly more reliable.

## 2. Imperative Orchestration (The Topology Fix)

* **Principle:** LLMs lack spatial awareness and graph topology intuition. Do not ask them to "plan"; ask them to "follow."
* **Implementation:**
* Use a **Simple Orchestrator**: A root control node that issues linear, imperative commands.
* **Progressive Disclosure:** Agents act on a "Need-to-Know" basis. The Orchestrator sees the map; the Worker sees only the next step.


* **Why:** Preventing the agent from seeing the full complexity prevents hallucinated shortcuts and "context bleeding."

## 3. Cognitive Separation: Thinkers vs. Executors

* **Principle:** Separating "Planning" from "Doing" prevents logic drift.
* **Implementation:**
* **The Thinker:** Generates the spec (PRD, Architecture, JSON Schema). High temperature, reasoning-heavy.
* **The Executor:** Implements the spec. Low temperature, strictly pinned to "follow instructions without deviation."


* **Why:** An agent tasked with both designing and building simultaneously will unconsciously simplify the design to make the build easier (lazy evaluation).

## 4. Prompting as Activation (The LoRA Theory)

* **Principle:** Prompts are for **alignment**, not **education**. You cannot teach an LLM a complex theory it hasn't seen during training within a prompt context.
* **Implementation:**
* Use standard industry terms to "activate" latent knowledge (like a LoRA adapter).
* If specific nuance is required, use **Few-Shot Examples** (3-5 input/output pairs) to bias the style.
* Avoid pedagogical explanations; state the constraints and principles upfront as immutable laws.



## 5. Structural Communication (The Handoff Protocol)

* **Principle:** Natural language is lossy. Agent-to-Agent communication must be structured.
* **Implementation:**
* Use **Meta-JSON Handoffs**: Intermediate outputs must follow a strict schema (e.g., `{"rationale": "...", "next_step": "...", "context_keys": [...]}`).
* No "chatty" handoffs. Data is passed as a structured payload.



## 6. Hybrid Determinism

* **Principle:** If a sub-task is computationally hard but logically deterministic, do not use an LLM.
* **Implementation:**
* **Programmatic Conversion:** Offload deterministic logic (math, complex sorting, strict formatting) to code (Python scripts/Tools).
* Use the LLM only for the fuzzy/semantic parts of the pipeline.



## 7. Stateless Deliverables

* **Principle:** A deliverable must stand alone, independent of the conversation history that created it.
* **Implementation:**
* Roadmaps, status logs, and reasoning chains belong in **Meta-Data**.
* The final output (Code, Doc, Report) must be **clean**, containing no artifacts of the agent's internal monologue.



## 8. Context Hygiene (The 100-Line Heuristic)

* **Principle:** "Long Context" is a marketing term, not an engineering reality. High-fidelity attention degrades rapidly.
* **Implementation:**
* **MECE Isolation:** Sub-tasks must be Mutually Exclusive and Collectively Exhaustive.
* **Context Cap:** Critical control instructions should fit within ~100 lines of high-density text.
* **Cyclic Guarding:** Any loop (e.g., Code -> Test -> Fix) must be guarded by a "Critical Auditor" with the authority to terminate the loop if it detects oscillation (auto-healing).
