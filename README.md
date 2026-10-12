# ⚖️ CRUCIBLE — Epistemic Auditing Framework for AI-Assisted Research

**Force AI to critique research like a senior scientific referee, not a diplomat.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-6.0-emerald.svg)](CHANGELOG.md)
[![Whitepaper](https://img.shields.io/badge/Whitepaper-Technical_Report-blueviolet.svg)](docs/CRUCIBLE_v6_Whitepaper.md)
[![Benchmarks](https://img.shields.io/badge/Benchmarks-9_Cases_Validated-success.svg)](docs/BENCHMARKS.md)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-informational.svg)](https://www.python.org/)

> *Originally conceived as* ***Mayın Tarlası*** *(Epistemic Minefield Model) — the testing ground where unstated axioms are either detonated or survive.*

---

## What Is CRUCIBLE?

CRUCIBLE is an **open-source prompt framework** that transforms commercial AI models (ChatGPT, Claude, Gemini) into rigorous, adversarial scientific auditors.

When you ask a standard AI to "review this paper," it produces polite, non-committal summaries that agree with the author and avoid confrontation. This is a well-documented failure mode called **sycophancy** — and it makes AI useless for serious research evaluation.

CRUCIBLE solves this by injecting a structured analytical constitution into the AI at inference time. No fine-tuning. No API keys. No model retraining. The same AI model, constrained by CRUCIBLE's 10-layer normative protocol, produces forensic-grade analysis instead of diplomatic handwaving.

**Who is this for?**
- Researchers who want a brutally honest second opinion on a paper, thesis, or book — including their own work.
- Students preparing thesis defenses who want to discover their weak points before their committee does.
- Science journalists and policy analysts who need to distinguish robust evidence from rhetorical confidence.
- Anyone who is tired of AI telling them what they want to hear.

---

## The Problem — and What CRUCIBLE Does About It

### What a normal AI produces when asked to "analyze this book":

> *"Butler's Gender Trouble is a groundbreaking and thought-provoking work that has profoundly influenced feminist theory. While some scholars have raised methodological questions, the text presents a compelling and nuanced argument for the performative nature of gender..."*

This tells you **nothing**. It's a book-jacket blurb, not an analysis.

### What CRUCIBLE produces from the same source material:

> **[Layer 3 — Hermeneutic Audit]:** The term "performativity" is deployed with three semantically distinct definitions across Chapters 1–3 — (a) involuntary citation of norms under duress, (b) Nietzschean metalepsis of cause/effect, (c) Austinian speech-act derivation — without explicit disambiguation. This creates a motte-and-bailey structure: when the strong ontological claim is challenged, the author retreats to the weaker epistemological reading.
>
> **[Layer 8 — Source Criticism Matrix]:**
>
> | Claim | Primary Source | Source Type | Verdict |
> |:---|:---|:---|:---|
> | Biological sex is discursively constructed | Foucault, *History of Sexuality* Vol. 1 | Post-structuralist discourse analysis | **Proxy Leap:** Unsubstantiated jump from "language mediates our description of anatomy" to "anatomy itself is a cultural artifact" |
>
> **[Layer 10 — Auto-Falsification]:** This audit's own analysis relies heavily on Anglo-American analytic philosophy of science as its evaluative benchmark, which may systematically underweight the Continental tradition's distinct epistemological commitments...

*— Condensed from [Case 01: Judith Butler – Gender Trouble](showcase/en/01_Judith_Butler_Report.html) (Full report: 25 KB, 192 lines, 5 active layers, 8 fallacies detected)*

---

## Quick Start

### ⚡ 10-Second Preview (Inspect a Real Report)
Want to see what CRUCIBLE actually produces without installing anything?  
👉 [**Open the Judith Butler – Gender Trouble Sealed Report (HTML)**](showcase/en/01_Judith_Butler_Report.html) or browse all [9 Verified Benchmark Cases](#9-verified-benchmark-cases).

---

### 🌐 Path A: Web & Cloud Users (No Coding Required)

Run audits in **Claude.ai**, **ChatGPT Plus**, or **Gemini Advanced** in 3 simple steps:

> 📌 **Why Two Stages?** Feeding a 400-page book directly into an AI with a single *"analyze this"* prompt triggers *smoothing error* — the AI collapses into a diplomatic 18 KB summary. To prevent this, we extract raw evidence first, then execute the audit.

1. **Step 1 — Extract the Evidence (Target Dossier):**
   - Open [`templates/CRUCIBLE_EXTRACTION_DIRECTIVE.md`](templates/CRUCIBLE_EXTRACTION_DIRECTIVE.md) and copy the text.
   - Paste it into your AI chat along with your source PDF or text.
   - The AI extracts verbatim claims, empirical data, and citations into a clean **Target Dossier** *(a raw claim list with zero editorial commentary)*.

2. **Step 2 — Execute the Auditing Constitution:**
   - Open [`templates/CRUCIBLE_WEB_PROMPT_EN.md`](templates/CRUCIBLE_WEB_PROMPT_EN.md) and copy the prompt.
   - In the same chat, instruct the model:  
     *"Now subject the Target Dossier from Step 1 to the CRUCIBLE 10-layer forensic audit using these rules:"* (paste prompt).

3. **Step 3 — Receive the Forensic Monograph:**
   - The AI stops diplomatic handwaving. It conducts epistemic triage, reconstructs the thesis at its strongest (steelmanning), runs source criticism, and generates a self-auditing **Auto-Falsification & Surgeon Card**.

> 💡 **Permanent Workspace Tip:** If using Claude.ai Projects or Gemini Gems, upload `docs/` and `templates/` directly to your project knowledge base once. Any paper you upload afterward is automatically audited under CRUCIBLE rules.

---

### 💻 Path B: IDE & Agentic Users (Antigravity, Cursor, Claude Code)

Fully automated pipeline for developers and agentic workflows:

1. **Clone and open the repository:**
   ```bash
   git clone https://github.com/efegok73/crucible.git
   cd crucible
   ```
   *(Constitutions `.cursorrules`, `AGENTS.md`, and `CLAUDE.md` load automatically).*

2. **Issue a single command to your agent:**
   > *"Extract the target dossier from @paper.pdf following @templates/CRUCIBLE_EXTRACTION_DIRECTIVE.md, audit it using CRUCIBLE methodology, and verify output with scripts/crucible_linter.py."*

3. **Receive your sealed report:**  
   The agent conducts the audit, executes the deterministic Python linter in the background, achieves `[PASS]`, and compiles a publication-ready `[Report_Name].html` file. Simply open it in your browser.

> 🛠️ **Manual / CI Verification (Optional):** If running without an AI agent or inside a CI pipeline, validate any report manually:
> ```bash
> pip install markdown
> python scripts/crucible_linter.py showcase/en/01_Judith_Butler_Report.md
> ```

---

## 🧠 Model Competence Threshold (Architectural Requirements)

CRUCIBLE is strictly model-agnostic and does not depend on any specific proprietary provider or transient model version. However, enforcing a 10-layer normative gauntlet, hermeneutic hygiene, and tabular source-criticism requires an underlying engine that satisfies **four structural competence criteria**:

1. **Anti-Smoothing Architecture:** High resistance to conversational politeness and diplomatic compression; capable of unyielding methodological friction rather than superficial summaries.
2. **Strict Tabular and Matrix Discipline:** Absolute fidelity in generating structured output, specifically the mandatory Layer 8 Claim-Source Matrix and Surgeon Cards, without syntactic deformation.
3. **Multi-Constraint Instruction Adherence:** Premier reasoning capacity capable of navigating complex epistemic triage without instruction decay or context degradation over long horizons.
4. **Substantial Context Capacity:** Sufficient context bandwidth to ingest primary source dossiers, extraction directives, and analytical constitutions simultaneously.

> ⚠️ **Lightweight Models Warning:** Distilled, lightweight, or conversational mini-models suffer rapid instruction decay under multi-layered normative constraints, invariably collapsing into journalistic summarization (*smoothing errors*).

---

## ⚠️ Three Rules You Must Follow

1. **Always use two stages.** Feeding a 400-page book directly into an AI with a single "analyze this" prompt triggers *smoothing error* — the AI compresses your audit into an 18 KB journalistic summary. Separate extraction from analysis.

2. **Match the language to the source.** If your source material is in English, run the audit in English. Forcing analysis of English scientific literature into a morphologically complex language (e.g., Turkish, Hungarian) costs ~50% of analytical depth due to tokenization overhead. Translate the sealed report afterward if needed. ([Evidence](docs/en/03_SUBSTRATE_PARITY_AND_LINGUISTIC_ASYMMETRY.md))

3. **Cross-validate across models.** AI providers silently update model weights. A model that executes all 10 layers flawlessly today may degrade next week. Run critical audits on at least 2 different frontier models.

---

## How It Works: The 10-Layer Normative Gauntlet

CRUCIBLE does not activate all 10 layers on every text. A dynamic **Epistemic Triage Matrix** selects relevant layers based on the discipline of the source material:

| Layer | Function | Example Activation |
|:---:|:---|:---|
| **L1** | **Epistemic Virtue & Demarcation** — Eliminates emotional rhetoric, enforces intellectual humility | Always active |
| **L2** | **Steelmanning** — Rebuilds the thesis in its strongest possible academic form before any critique | Always active |
| **L3** | **Hermeneutics & Lexical Hygiene** — Detects semantic shifts, double meanings, concept creep | Philosophy, social science |
| **L4** | **Statistics & Bayesian Audit** — Audits sample sizes, effect sizes, p-hacking, prior distributions | Empirical sciences, medicine |
| **L5** | **Experimental Design & Causality** — Tests for confounders, reverse causation, collider bias via DAGs | Clinical trials, epidemiology |
| **L6** | **Evidence Hierarchies** — Applies AMSTAR-2, GRADE protocols; filters single-case anecdotes | Systematic reviews, meta-analyses |
| **L7** | **Decision Science & Risk (DMDU)** — Evaluates risk tradeoffs, fat-tail exposures, antifragility | Policy analysis, climate science |
| **L8** | **Historical Source Criticism** — Enforces primary source triangulation; requires Claim-Source Matrix | Historiography, archival research |
| **L9** | **Computational Model Audit** — Checks for overfitting, validation leakage, parameter tuning | Simulations, ML, agent-based models |
| **L10** | **Auto-Falsification & Surgeon Card** — AI confesses its own blind spots; provides 3-minute human verification checklist | Always active |

After analysis, the output is validated by a **deterministic Python linter** ([`crucible_linter.py`](scripts/crucible_linter.py)) that checks structural completeness, triage integrity, and rhetorical hygiene. Reports that fail are rejected and cannot be sealed.

---

## Showcase: 9 Validated Benchmark Cases

Every report below passed the deterministic linter and is available in both English and Turkish:

| # | Discipline | Audited Work | Key Vulnerability Found | Verdict |
|:---:|:---|:---|:---|:---:|
| 01 | Philosophy & Gender | **Judith Butler** — *Gender Trouble* (1990) | Semantic equivocation on "performativity"; proxy leap from epistemology to ontology | Major Revision |
| 02 | Psychoanalysis | **Jacques Lacan** — *Seminaire XX* (1975) | Pseudo-mathematical topology (mathemes) without formal validation | Major Revision |
| 03 | Clinical Epidemiology | **Hilary Cass** — *The Cass Review* (NHS, 2024) | Excessive RCT threshold applied to observational pediatric cohort data | Minor Revision |
| 04 | Historiography | **Cheikh Anta Diop** — *The African Origin* (1974) | Anachronistic racial categories; false linguistic cognates | Rejected |
| 05 | Classical Philology | **Frank M. Snowden Jr.** — *Blacks in Antiquity* (1970) | Minimization of Greco-Roman physiognomic prejudice | Minor Revision |
| 06 | Bibliometrics | **Cook et al. vs. Tol** — *97% Climate Consensus* (2013) | Denominator manipulation (66.4% neutral abstracts excluded) | Major Revision |
| 07 | Climate Science | **Judith Curry** — *Climate Uncertainty* (2023) | Internal ocean oscillation claims vs. observed net energy imbalance | Major Revision |
| 08 | Psychiatry & EBM | **Joanna Moncrieff et al.** — *Serotonin Theory* (2022) | Aspirin Fallacy: conflating etiological irrelevance with clinical inefficacy | Major Revision |
| 09 | Evolutionary Psychology | **Simon Baron-Cohen** — *The Essential Difference* (2003) | Failed neonate replication (Connellan 2000); 80% sex overlap ignored | Major Revision |

📂 Full reports: [`showcase/en/`](showcase/en/) (English) | [`showcase/tr/`](showcase/tr/) (Turkish)  
📊 Quantitative metrics: [`docs/BENCHMARKS.md`](docs/BENCHMARKS.md)

---

## Documentation Map

| Document | What It Contains |
|:---|:---|
| [**Whitepaper**](docs/CRUCIBLE_v6_Whitepaper.md) | Full technical specification, SOTA comparison, architecture details |
| [**Benchmarks**](docs/BENCHMARKS.md) | Quantitative metrics (M1–M8) for all 9 cases, cross-model consistency data |
| [**Limitations**](docs/LIMITATIONS.md) | Failure modes, hard boundaries, and what CRUCIBLE cannot do |
| [**Benchmark Protocol**](benchmarks/methodology/BENCHMARK_PROTOCOL.md) | How benchmarks were designed, executed, and measured |
| [**Blind Test Protocol**](benchmarks/methodology/BLIND_TEST_PROTOCOL.md) | Protocol for testing CRUCIBLE on literature it has never seen |
| [**Contributing Guide**](CONTRIBUTING.md) | How to contribute reports, critique methodology, or improve the linter |
| [**Changelog**](CHANGELOG.md) | Version history |

---

## Known Limitations

CRUCIBLE is transparent about what it **cannot** do:

- **Not a theorem prover.** Pure symbolic mathematics (topology, number theory) requires formal proof checkers (Lean, Coq), not LLMs.
- **Not autonomous.** Human-in-the-loop is mandatory. The 3-phase interactive pause system prevents black-box output dumps.
- **Input volume ceiling.** Target dossiers exceeding ~20 pages / ~15 KB risk context dilution. Segment longer works.
- **Model drift.** AI provider weight updates can silently alter CRUCIBLE performance. The deterministic linter catches structural degradation, but not semantic regression.

Full autopsy: [`docs/LIMITATIONS.md`](docs/LIMITATIONS.md)

---

## Contributing

CRUCIBLE must withstand its own audit. **Methodological critiques are the most valuable contributions.** See [`CONTRIBUTING.md`](CONTRIBUTING.md) for details.

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
