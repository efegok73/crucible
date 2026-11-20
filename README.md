# ⚖️ CRUCIBLE (Mayın Tarlası Model v7.2) — Grounded Epistemic Auditing Framework

**Transform frontier AI from a polite summarizer into an uncompromising, source-grounded scientific referee.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-7.2-emerald.svg)](CHANGELOG.md)
[![Whitepaper](https://img.shields.io/badge/Whitepaper-Technical_Report-blueviolet.svg)](docs/CRUCIBLE_v7.1_Whitepaper.md)
[![Benchmarks](https://img.shields.io/badge/Benchmarks-9_Cases_Validated-success.svg)](docs/BENCHMARKS.md)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-informational.svg)](https://www.python.org/)

> *Originally conceived as* ***Mayın Tarlası*** *(Epistemic Minefield Protocol) — the testing ground where unstated axioms are either detonated or survive.*

🌐 **Türkçe sürüm:** [`README_TR.md`](README_TR.md)

---

## What Is CRUCIBLE?

CRUCIBLE is an open-source epistemic auditing framework that transforms commercial frontier AI models (Claude, ChatGPT, Gemini) into adversarial, forensic-grade scientific referees through a **two-component architecture**:

1. **A 10-Layer Normative Prompt Constitution:** Enforces Popperian falsification, causal Directed Acyclic Graphs (DAGs), Bayesian ordinal updates, No-Citation No-Critique constraints, and Adversarial Defense filters at inference time.
2. **A Source-Grounded Deterministic Python Linter (`scripts/crucible_linter.py`):** Acts as an external constitutional court. It cross-checks cited claims and paragraph citations directly against the primary source document (`--source`), blocks hallucinated / ungrounded artifacts with a hard compile error, enforces the Substrate Parity Gate, penalizes dogmatic rhetoric, and cryptographically stamps reports with a verified `[PASS]` certificate.

### Why Standard AI Fails at Scientific Peer Review

When you ask a standard commercial AI to "review this paper," it produces polite, non-committal summaries that agree with the author and avoid confrontation. This is a well-documented failure mode called **sycophancy** — and it makes AI useless for serious research evaluation.

CRUCIBLE is fundamentally distinct from mere "prompt engineering." Prompting alone is stochastic and untrustworthy; models silently omit negative constraints as token context expands. CRUCIBLE couples normative reasoning directives with **compile-time AST & regex verification**. No fine-tuning. No API keys. No model retraining.

**Who is this for?**
- Researchers who want a brutally honest second opinion on a paper, thesis, or book — **including their own work**.
- Doctoral students preparing defenses who want to discover their weak points before their committee does.
- Science journalists and policy analysts who need to distinguish robust evidence from rhetorical confidence.
- Anyone who is tired of AI telling them what they want to hear.

---

## 🏛️ The Four Epistemic Pillars

CRUCIBLE is not a polite summarizer; it is an inference-time forensic harness operating on four non-negotiable principles of scientific inquiry:

1. **Enforcement of Frontier Methodological Standards:**  
   Audits claims against formal scientific demarcation (Popperian falsifiability, Bradford Hill causal criteria, GRADE evidentiary hierarchies) rather than consensus rhetoric.
2. **Forensic Evidence & Denominator Surgery:**  
   Dissects the empirical foundation of the thesis—hunting denominator inflation, sample attrition, and unsubstantiated leaps from proxy data to ontological reality.
3. **Detection of Semantic Equivocation & Unstated Axioms:**  
   Exposes motte-and-bailey defenses, circular definitions, and dogma masquerading as settled methodology behind academic prose.
4. **Radical Auto-Falsification (The Gödel-Tarski Boundary):**  
   Acknowledging that no AI can formally validate its own meta-language, it subjects its own critique to adversarial self-examination, explicitly cataloging its own blind spots, disciplinary biases, and single-source risks before handing the verdict to a human researcher.

---

## 🌐 The Universal Substrate Parity Law ($L_{source} \equiv L_{audit} \rightarrow L_{target}$)

CRUCIBLE is designed as a universal architecture for scholars worldwide. Whether a Chinese researcher audits a Chinese philosophical text for Arabic publication, or an English scholar reviews a German treatise in English, linguistic asymmetry obeys the same mathematical law.

### 1. The Core Problem: Why Direct Cross-Lingual Auditing Fails
When an LLM is asked to evaluate a text in a language different from the source document, it suffers a **two-fold cognitive collapse**:
- **Tokenization Bottleneck & Smoothing Loss:** Cross-lingual semantic transfer forces the model to simultaneously translate and critically reason, causing an estimated ~40% to ~50% degradation in analytical depth (*smoothing loss*).
- **Translationese & Strawman Hallucinations:** Delicate authorial hedges, regional caveats, and safety valves evaporate in translation, leading the AI to falsely accuse the author of unhedged fallacies.

### 2. The Two-Stage Universal Protocol
CRUCIBLE mathematically codifies the Substrate Parity Law:

$$\mathbf{L_{audit} \equiv L_{source}} \quad \longrightarrow \quad \mathbf{L_{target}}$$

1. **Stage 1 (Native Substrate Primary Audit):**  
   The primary forensic audit ($L_{audit}$) must **strictly execute in the native language of the source document** ($L_{source}$ — English, Chinese, Arabic, Russian, Turkish, etc.) and be verified by the linter (`audit_en.md`, `audit_zh.md`).
2. **Stage 2 (Localized Transfer with Dual Anchors):**  
   To generate a report in the researcher's target language ($L_{target}$), the verified primary audit is translated while maintaining dual paragraph coordinates `[P:xxxx]` and verbatim quotes, declaring metadata: `**Primary Audit:** <path_to_stage1_audit>`.

### 3. Programmatic Enforcement: Substrate Parity Gate
In `scripts/crucible_linter.py`, this rule is enforced at compile time. The linter automatically detects the script and language of both source and report. Auditing an English paper directly in Turkish or Arabic without passing `--allow-localized` or linking a primary audit halts execution with:
`[FAIL: SUBSTRATE PARITY VIOLATION]`

---

## 🎯 Pedagogical Clarity & Anti-Translationese Standard

An audit is worthless if the researcher cannot immediately grasp the exact methodological flaw. CRUCIBLE enforces two non-negotiable communicative standards:

1. **Anti-Translationese (Natural Academic Prose):**  
   Reports must reject mechanical bureaucratic calques, stacked passive verbs, and robotic translationese. Prose must be vivid, lucid, and direct.
2. **"One Concept, One Concrete Example" Standard:**  
   Hurling abstract jargon at an author is prohibited. Every technical critique (*motte-and-bailey*, *causal DAG collapse*, *proxy leap*) must be followed by an intuitive, concrete real-world analogy. For instance:
   > *"The author deploys a motte-and-bailey defense: like a medieval army retreating from an indefensible fertile valley (the bailey: 'biological sex is entirely a discursive illusion') to an unassailable stone fortress (the motte: 'our descriptions of anatomy are culturally conditioned') whenever attacked, only to reoccupy the radical claim once scrutiny subsides."*

---

## Quick Start Guide

### 💻 Option A (Recommended): Autonomous Agentic IDE
*(Antigravity, Cursor, VS Code + Roo/Cline, or Claude Code)*

1. **Open Workspace:** Open the `crucible` repository in your agentic IDE.
2. **Place Primary Document:** Put your PDF, Word, or Markdown document in your working directory (e.g., `CALISMALARIM/`).
3. **Ground-Truth Immutability (v7.2 Rule):** Do NOT chunk or summarize. Use `python scripts/index_source.py CALISMALARIM/paper.pdf -o CALISMALARIM/paper_indexed.txt` to generate deterministic paragraph coordinates.
4. **Issue Command:**
   > *"Audit `@CALISMALARIM/paper.pdf` using CRUCIBLE v7.2. Execute the primary audit in the native substrate language of the paper, then localize with dual anchors and run crucible_linter.py until verified."*
5. **Inspect Sealed Output:** The agent runs the linter and compiles the final verified HTML monograph with the green verification seal.

---

### 🌐 Option B: Direct Web Interface
*(Claude.ai, ChatGPT Plus, Google AI Studio — Zero Setup)*

1. Copy the system prompt from [`templates/CRUCIBLE_WEB_PROMPT_EN.md`](templates/CRUCIBLE_WEB_PROMPT_EN.md) (or [`_TR.md`](templates/CRUCIBLE_WEB_PROMPT_TR.md)).
2. Paste into the web model with your full document.
3. Save the resulting output to `report.md`.
4. Run the local deterministic linter:
   ```bash
   pip install markdown pypdf
   python scripts/crucible_linter.py report.md --source paper.pdf
   ```
   The linter validates structure, Claim-Source matrices, paragraph anchors, and language parity before producing `report.html` with the official green **`[PASS]`** seal.

---

## How It Works: The 10 Normative Layers

| Layer | Function | Trigger Condition |
|:---:|:---|:---|
| **L1** | **Epistemic Virtue** — Filters rhetorical theater, eliminates sycophancy | Always active |
| **L2** | **Steelmanning** — Reconstructs thesis in its strongest academic form | Always active |
| **L3** | **Hermeneutic Hygiene** — Semantic equivocation, concept inflation | Philosophy, humanities |
| **L4** | **Statistics & Bayes** — Sample sizes, p-hacking, Bayesian prior updating | Empirical science, medicine |
| **L5** | **Experimental Design** — Confounders, reverse causality, causal DAGs | Clinical trials, epidemiology |
| **L6** | **Evidence Hierarchy** — GRADE / AMSTAR-2 standards; filters single anecdotes | Systematic reviews |
| **L7** | **Decision Science (DMDU)** — Fat-tail risks under deep uncertainty | Policy analysis, climate science |
| **L8** | **Source Criticism** — Primary document cross-checking; Claim-Source matrix | Historiography, archival research |
| **L9** | **Computational Models** — Overfitting, validation leakage, algorithmic bias | AI, simulations |
| **L10** | **Auto-Falsification** — Model self-discloses blind spots; outputs Surgeon Card | Always active |

---

## 9 Validated Benchmark Cases

Every benchmark report has passed the deterministic linter:

| # | Discipline | Audited Work | Key Methodological Vulnerability Found | Verdict |
|:---:|:---|:---|:---|:---:|
| 01 | Philosophy & Gender | **Judith Butler** — *Gender Trouble* (1990) | Semantic equivocation on "performativity"; proxy leap from epistemology to ontology | Major Revision |
| 02 | Psychoanalysis | **Jacques Lacan** — *Seminaire XX* (1975) | Pseudo-mathematical topology (mathemes) without formal validation | Major Revision |
| 03 | Clinical Epidemiology | **Hilary Cass** — *The Cass Review* (NHS, 2024) | Excessive RCT threshold applied to observational pediatric cohort data | Minor Revision |
| 04 | Historiography | **Cheikh Anta Diop** — *The African Origin* (1974) | Anachronistic racial categories; false linguistic cognates | Rejected |
| 05 | Classical Philology | **Frank M. Snowden Jr.** — *Blacks in Antiquity* (1970) | Minimization of Greco-Roman physiognomic prejudice | Minor Revision |
| 06 | Bibliometrics | **Cook et al. vs. Tol** — *97% Climate Consensus* (2013) | Denominator manipulation (66.4% neutral abstracts excluded to inflate consensus) | Major Revision |
| 07 | Climate Science | **Judith Curry** — *Climate Uncertainty* (2023) | Internal ocean oscillation claims vs. satellite-observed net planetary energy imbalance | Major Revision |
| 08 | Psychiatry & EBM | **Joanna Moncrieff et al.** — *Serotonin Theory* (2022) | **V7 Grounded Correction:** Author hedges verified; V6 "Aspirin Fallacy" false accusation dismissed; core vulnerability identified as biochemical proxy leap to clinical prognosis. | Major Revision |
| 09 | Evolutionary Psychology | **Simon Baron-Cohen** — *The Essential Difference* (2003) | Failed neonate replication (Connellan 2000); 80% sex overlap ignored | Major Revision |

📂 Full reports: [`showcase/en/`](showcase/en/) | [`showcase/tr/`](showcase/tr/)  
📊 Quantitative metrics: [`docs/BENCHMARKS.md`](docs/BENCHMARKS.md)

---

## Known Limitations

CRUCIBLE is transparent about what it **cannot** do:

- **Not a theorem prover.** Pure symbolic mathematics requires formal proof assistants (Lean, Coq), not LLMs.
- **Not autonomous.** Human-in-the-loop verification is mandatory. The 3-phase interactive execution ensures researchers retain final judgment.
- **Model drift.** Model provider weight updates can alter performance. The deterministic linter detects structural degradation, but cross-model verification on 2+ frontier models is recommended for high-stakes audits.

---

## License & Citation

Distributed under the [**MIT License**](LICENSE).

```bibtex
@software{crucible2026,
  author  = {CRUCIBLE Open-Source Contributors},
  title   = {CRUCIBLE: An Open-Source Framework for Epistemic Auditing and Dialectical Stress-Testing},
  year    = {2026},
  url     = {https://github.com/efegok73/crucible},
  note    = {Originally conceived as May{\i}n Tarlas{\i} (Epistemic Minefield) Protocol}
}
```
