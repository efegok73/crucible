# CRUCIBLE v6.0: A Multi-Layer Normative Gauntlet and Deterministic Protocol for Forensic Epistemic Auditing of Academic Literature

**Whitepaper & Technical Specification**  
**Document ID:** `CRUCIBLE-WP-2026-v6.0`  
**Classification:** Open Source Framework Specification / Preprint Draft (`cs.AI`, `cs.CL`)  
**Date:** October 2026  
**License:** MIT License  
**Repository:** [github.com/curious/CRUCIBLE](https://github.com/curious/CRUCIBLE)  

---

## ABSTRACT

Large Language Models (LLMs) deployed as academic and scientific evaluators suffer from three systemic pathology modes: **sycophancy** (systematic confirmation bias toward user prompts and cited authorities), **smoothing errors** (loss of microscopic methodological granularity in favor of generic, diplomatic summaries), and **hallucinatory consensus** (premature dialectical resolution without empirical justification). While training-time alignments (e.g., Constitutional AI, RLHF) mitigate crude toxicities, they fail to enforce rigorous disciplinary demarcation or methodological friction during post-hoc inference. 

In this paper, we introduce **CRUCIBLE v6.0**, an open-source, model-agnostic normative framework and deterministic audit gauntlet designed to transform commercial frontier LLMs into adversarial, unyielding epistemic auditors. CRUCIBLE deploys a 10-layer disciplinary gauntlet encompassing epistemic virtues, Popperian steelmanning, hermeneutic hygiene, Bayesian likelihood calibration, Directed Acyclic Graph (DAG) causality, systematic review hierarchies (AMSTAR-2/GRADE), decision-making under deep uncertainty (DMDU), historical source criticism, and Gödel-Tarski auto-falsification. 

To prevent context collapse and tokenisation bottlenecks, CRUCIBLE mandates a **Two-Stage Extraction Pipeline** governed by the **Law of Substrate Parity**. Crucially, analytical integrity is deterministically enforced by an external Python linter (`crucible_linter.py`) that halts execution and forbids report sealing unless all triage mandates, tabular matrices, and auto-falsification confessions are verified. 

We evaluate CRUCIBLE across 9 highly contested academic benchmark dossiers spanning clinical epidemiology, climatology, psychiatry, historiography, and psychoanalysis. Across all 9 cases (100% deterministic linter pass rate), CRUCIBLE identified 56 discrete formal fallacies (mean: 6.2 per case), activated an average of 6.4 normative layers, and produced 28 formal self-falsification confessions. Cross-model experiments across four frontier engines (Claude Opus 4.6, Claude Sonnet 4.6, Gemini 3.1 Pro, Gemini 3.8 Flash) demonstrate structural protocol invariance. We openly document the framework's failure modes—including monolithic context limits (>400 pages) and formal mathematical deduction boundaries—establishing CRUCIBLE as a calibrated whetstone for human-in-the-loop scientific inquiry.

**Keywords:** Epistemic Auditing, Sycophancy Mitigation, Large Language Models, Steelmanning, Deterministic Linting, Causality, Scientific Criticism.

---

## 1. INTRODUCTION: THE CALIBRATION CRISIS IN LLM-ASSISTED INQUIRY

### 1.1. The Three Failure Modes of Generative Peer Review
As generative AI models assume larger roles in scientific synthesis, peer review assistance, and automated literature auditing, an alarming epistemic failure mode has become entrenched: **generative sycophancy** (Sharma et al., 2023; Perez et al., 2022). Frontier models trained via Reinforcement Learning from Human Feedback (RLHF) systematically optimize for agreeable, polite, and superficially helpful prose. When presented with published literature containing methodological confounders, statistical fragility, or rhetorical pseudo-mathematics, standard LLMs default to:

1. **Confirmation Bias and Authority Sycophancy:** The model validates the author's conclusions simply because they are expressed in formal academic syntax, avoiding confrontational methodological inquiry.
2. **Smoothing Errors (Resolution Attrition):** When handling intricate disputes (e.g., selection bias in pediatric observational cohorts or denominator manipulation in bibliometrics), standard prompts collapse granular metrics ($d$-values, sample attrition, unmeasured colliders) into colloquial summaries (*"some methodological limitations exist"*).
3. **The Deliverable Reflex:** Models rush to produce an uncontroversial, homogenized consensus rather than exposing deep epistemological fault lines.

### 1.2. The Inference-Time Gap
While substantial research has focused on *training-time alignment* (Bai et al., 2022) or domain-specific fine-tuning (OpenReviewer; Huang et al., 2025), these interventions alter model weights at massive capital cost and remain locked to specific architectures. Furthermore, safety-aligned models often display hyper-caution, avoiding decisive critiques of contentious literature.

**CRUCIBLE v6.0** addresses this crisis at *inference time*. It operates as an uncompromising, external normative constitution. Rather than treating the LLM as an autonomous arbiter, CRUCIBLE treats the LLM as a high-powered scalpel that must be constrained by an unyielding mechanical harness.

---

## 2. RELATED WORK & SOTA POSITIONING

CRUCIBLE intersects several emerging paradigms in AI alignment, dialectical reasoning, and automated peer review. Table 1 delineates CRUCIBLE’s operational taxonomy relative to state-of-the-art frameworks.

### Table 1: State-of-the-Art Comparative Positioning Matrix

| Framework / System | Architectural Layer | Primary Scope | Quantitative / Statistical Gauntlet? | Deterministic Verification? | Disciplinary Breadth | Epistemic Auto-Falsification? |
|:---|:---|:---|:---:|:---:|:---|:---:|
| **Constitutional AI** *(Bai et al., 2022)* | Training-Time (RLHF/RLAIF) | Harmlessness & General Alignment | ❌ No | ❌ Stochastic | General Domain | ❌ No |
| **CriticGPT** *(OpenAI, 2024)* | Fine-Tuned Model (RLHF) | Code Bug & Syntax Auditing | ❌ No | ⚠️ Partial (Compiler) | Software Code Only | ❌ No |
| **OpenReviewer** *(Huang et al., 2025)* | Fine-Tuned Model (Llama-8B) | Academic Peer Review | ❌ No | ❌ Stochastic | ML / AI Papers Only | ❌ No |
| **GoldBerry** *(2026)* | Inference-Time Prompt Framework | Critical Thinking & Lenses | ❌ No | ❌ No | Cultural & Media Studies | ⚠️ Qualitative Only |
| **MAVEN** *(2025)* | Multi-Agent Reasoning | In-Step Epistemic Verification | ⚠️ Minimal | ❌ Stochastic | Formal Logic Chains | ❌ No |
| **SycEval / CAP** *(2025–2026)* | Evaluation Benchmark | Sycophancy Measurement | ❌ No | ⚠️ Metric Output | Benchmark Testing | ❌ No |
| **CRUCIBLE v6.0** *(Ours)* | **Inference-Time Normative Protocol** | **Forensic Academic & Epistemic Audit** | **✅ Yes (Bayes, DAGs, GRADE)** | **✅ Deterministic (Python Linter)** | **Universal Multi-Disciplinary (10 Layers)** | **✅ Yes (Layer 10 + Surgeon Card)** |

### 2.1. Distinction from Model-Specific Tuning
Unlike OpenReviewer, CRUCIBLE requires zero weight fine-tuning. It functions across arbitrary frontier reasoning models (Anthropic Claude, Google Gemini, OpenAI GPT). When the underlying foundation model improves, CRUCIBLE's analytical resolution scales without retraining.

### 2.2. Distinction from Qualitative Frameworks
Unlike qualitative lens systems (e.g., GoldBerry), CRUCIBLE enforces quantitative rigor: Layer 4 mandates Bayesian prior updates and effect-size auditing ($d$, $\eta^2$); Layer 5 formalizes causal Directed Acyclic Graphs (DAGs) to identify collider and unmeasured confounding biases; and Layer 6 enforces PRISMA/AMSTAR-2 systematic review standards.

---

## 3. THE CRUCIBLE v6.0 ARCHITECTURE

CRUCIBLE v6.0 is structured around four interlocking components: (1) The 10-Layer Normative Gauntlet, (2) The Epistemic Triage Matrix, (3) The Two-Stage Extraction Pipeline, and (4) The Deterministic Verification Harness.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        RAW MONOGRAPH / THESIS                          │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Stage 1: Extraction Directive
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│               TARGET DOSSIER (Source-Fidelity Quotes)                  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Stage 2: Epistemic Gauntlet
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                     EPISTEMIC TRIAGE MATRIX                            │
│           (Active Layer Selection & Exclusion Justification)           │
├───────────────────────────────────┬────────────────────────────────────┤
│ Phase 1: Steelmanning & Virtues   │ Phase 2: Dissection & Causal Audit │
│ [L1] Demarcation & Humility       │ [L4] Bayesian / Statistical Audit  │
│ [L2] Popperian Steelmanning       │ [L5] DAGs & Confounder Forensics   │
│ [L3] Hermeneutic Hygiene          │ [L6] Systematic Evidence Grading   │
│                                   │ [L7] DMDU & Tail-Risk Science      │
│                                   │ [L8] Historical Source Criticism   │
│                                   │ [L9] Computational Parameter Audit │
├───────────────────────────────────┴────────────────────────────────────┤
│ Phase 3: Post-Mortem & Auto-Falsification                              │
│ [L10] Gödel-Tarski Self-Critique & 3-Minute Human Surgeon Card         │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Markdown Monography Output
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│               DETERMINISTIC PYTHON LINTER (crucible_linter.py)         │
│         Regex Checks • Structural Validation • Forbidden Lexicon       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ [PASS] Verified
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│              SEALED MONOGRAPHY (Machine MD + Formatted HTML)           │
└────────────────────────────────────────────────────────────────────────┘
```

### 3.1. The 10-Layer Normative Gauntlet

1. **Layer 1: Epistemic Virtue & Demarcation:** Enforces epistemic humility, purges emotive/tribal rhetoric, and delineates empirical claims from metaphysical assertions.
2. **Layer 2: Steelmanning & Philosophy of Science:** Imposes the principle of charity at maximum academic fidelity. The auditor must reconstruct the target thesis in its most formidable, coherent formulation before any critique is permitted.
3. **Layer 3: Hermeneutics & Lexical Hygiene:** Dissects rhetorical equivocation, concept creep, reification fallacies, and terminological shifts.
4. **Layer 4: Statistics, Probability & Bayesian Mechanics:** Audits statistical power, $p$-hacking, sample attrition, prior probability distributions, and effect-size realities.
5. **Layer 5: Experimental Design & Causal Inference:** Formalizes Directed Acyclic Graphs (DAGs) to identify collider conditioning, selection bias, reverse causality, and unobserved confounders ($Z$).
6. **Layer 6: Evidence Hierarchies & Systematic Review:** Evaluates clinical and empirical evidence against AMSTAR-2, RoB-2, and GRADE hierarchies. Anecdotal or single-center studies cannot substantiate macro claims.
7. **Layer 7: Decision Science & Risk (DMDU):** Analyzes Decision Making Under Deep Uncertainty, Fat-Tail risks, and fragility tradeoffs.
8. **Layer 8: Historical & Archival Source Criticism:** Enforces classical primary source triangulation (internal/external criticism). When Layer 8 is active, the model is strictly forbidden from abstract preaching; it must output a structured `Source-Claim Matrix`.
9. **Layer 9: Computational Simulation & Agent-Based Modeling:** Audits parameter overfitting, synthetic data circularity, and validation leakage.
10. **Layer 10: Auto-Falsification & Epistemic Damage Report:** Mandates that the model expose the fatal vulnerabilities of its *own* critique. Concludes with a 3-minute structured `Surgeon Checklist` for external human verification.

### 3.2. Epistemic Triage & Disciplinary Demarcation
To avoid superficial checkbox compliance, CRUCIBLE forbids activating all layers indiscriminately. The model must perform an explicit **Epistemic Triage**:
* It must declare which layers are **Active** (with operational justification).
* It must declare which layers are **Excluded** (e.g., excluding Layer 8 historical criticism when evaluating a pure mathematical proof, or excluding Layer 4 statistics when analyzing an epigraphic fragment).

### 3.3. Two-Stage Pipeline & The Law of Substrate Parity
Empirical stress tests revealed that passing raw 300-page monographs directly into the audit gauntlet triggered severe context dilution. CRUCIBLE establishes a strict **Two-Stage Pipeline**:
1. **Extraction Stage (`CRUCIBLE_EXTRACTION_DIRECTIVE.md`):** The model ingests the primary text and extracts a structured, neutral **Target Dossier** consisting solely of verified citations, formal definitions, and empirical data tables.
2. **Audit Stage (`CRUCIBLE_WEB_PROMPT_EN.md`):** The audit gauntlet is executed exclusively against the Target Dossier.

Furthermore, CRUCIBLE codifies the **Law of Substrate Parity**: An epistemic audit achieves maximum resolution only when executed in the conceptual and linguistic substrate in which the literature was produced. Auditing English biomedical or analytic philosophy through translated prompts causes sub-word tokenisation penalties and early synthesis plateaus (see Section 4.5).

### 3.4. Deterministic Verification Harness (`crucible_linter.py`)
To prevent the LLM from declaring completion while silently omitting required analytical sections, CRUCIBLE integrates an automated, non-LLM Python validator:
* **Structural Regex Validation:** Confirms the presence of all 11 mandatory sections, triage matrices, Layer 8 tables, Layer 10 auto-falsification confessions, and Surgeon cards.
* **Lexical Sanitation Filter:** Scans the text for forbidden polemical, emotional, or dogmatic jargon (e.g., *"unquestionable"*, *"absurd"*, *"obviously false"*).
* **Deterministic Sealing:** If any violation occurs, the script exits with code 1 (`[FAIL]`) and blocks HTML generation. Only zero-defect reports are compiled into sealed human-readable HTML documents.

### 3.5. The Gödel-Tarski Boundary & Scalpel-and-Surgeon Protocol
Recognizing Tarski’s undefinability theorem as an epistemological constraint, CRUCIBLE acknowledges that *no computational system can fully validate the truth-value of its own meta-language*. Layer 10 enforces the **Gödel-Tarski Boundary**: the model does not declare an absolute truth verdict. Instead, it provides a 3-minute structured checklist for the **External Will** (the human investigator), who alone holds the mandate to physically inspect primary archives and raw experimental data.

---

## 4. QUANTITATIVE BENCHMARK EVALUATION

CRUCIBLE v6.0 was quantitatively benchmarked against 9 highly contested academic debates across 5 disparate faculties. The evaluation data was extracted programmatically via `scripts/benchmark_extractor.py` and validated under the formal [`BENCHMARK_PROTOCOL.md`](../benchmarks/methodology/BENCHMARK_PROTOCOL.md).

### Table 2: Primary Quantitative Benchmark Results (9 Showcase Cases)

| # | Benchmark Case | Academic Faculty / Discipline | Dossier Size (KB) | EN Monography (KB) | Active Layers (M1) | Linter Status (M3) | Fallacies Detected (M4) | Auto-Falsification Items (M5) | Source Matrix (M6) | Surgeon Card (M7) |
|:---|:---|:---|---:|---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **01** | Judith Butler – *Gender Trouble* | Post-Structuralist Philosophy | 9.0 | 25.0 | 5 | ✅ PASS | 8 | 4 | ✅ | ✅ |
| **02** | Jacques Lacan – *Seminar XX: Encore* | Psychoanalysis / Semiotics | 11.3 | 35.1 | 6 | ✅ PASS | 5 | 3 | ✅ | ✅ |
| **03** | Hilary Cass – *The Cass Review* | Clinical Medicine / Epidemiology | 15.3 | 37.7 | 8 | ✅ PASS | 6 | 3 | ✅ | ✅ |
| **04** | Cheikh Anta Diop – *African Origin* | Historiography / Epigraphy | 13.0 | 36.1 | 6 | ✅ PASS | 6 | 3 | ✅ | ✅ |
| **05** | Frank Snowden – *Blacks in Antiquity* | Classics / Ancient History | 13.9 | 34.8 | 5 | ✅ PASS | 2 | 3 | ✅ | ✅ |
| **06** | Cook et al. vs Tol – *Climate Consensus* | Bibliometrics / Climatology | 11.3 | 45.5 | 7 | ✅ PASS | 9 | 3 | ✅ | ✅ |
| **07** | Judith Curry – *Climate Uncertainty* | Climate Science / DMDU | 12.7 | 42.5 | 7 | ✅ PASS | 6 | 3 | ✅ | ✅ |
| **08** | Joanna Moncrieff – *Serotonin Theory* | Psychiatry / Evidence-Based Medicine | 14.1 | 41.8 | 8 | ✅ PASS | 7 | 3 | ✅ | ✅ |
| **09** | Simon Baron-Cohen – *Essential Difference*| Cognitive Neuroscience | 12.3 | 49.0 | 6 | ✅ PASS | 7 | 3 | ✅ | ✅ |

### 4.1. Aggregate Statistical Indicators
* **Deterministic Pass Rate (M3):** 9/9 (100.0%) of reports met every structural and rhetorical constraint enforced by `crucible_linter.py`.
* **Layer Engagement Density (M1):** Across the suite, an average of **6.4 distinct normative layers** were actively engaged per audit.
* **Fallacy Detection Yield (M4):** A total of **56 discrete logical, statistical, or methodological fallacies** were formally isolated and labeled (mean: 6.2 per audit).
* **Auto-Falsification Rigor (M5):** The framework generated **28 formal self-critique items** (mean: 3.1 vulnerabilities admitted per audit).
* **Structural Compliance (M6 & M7):** 100% of applicable reports contained the mandatory tabular Source-Claim Matrix and the 3-minute Surgeon Verification Card.

### 4.2. Cross-Model Structural Invariance
To test whether CRUCIBLE is model-invariant or reliant on idiosyncratic features of a single proprietary engine, the identical target case (*Evolutionary Biology & Epistemic Boundaries*) was evaluated under CRUCIBLE across four frontier LLMs.

### Table 3: Cross-Model Execution Comparison (Identical Target Input)

| Evaluated Engine | Report Payload (KB) | Active Layers | Fallacies Detected | Auto-Falsification Items | Structural Compliance |
|:---|---:|:---:|:---:|:---:|:---|
| **Claude Opus 4.6 (Thinking)** | 32.8 | 7 layers | 4+ | 5 items | Full 11-section protocol; exhaustive forensic depth |
| **Claude Sonnet 4.6 (Thinking)** | 21.4 | 8 layers | 4+ | 3 items | Full 11-section protocol; sharp demarcation |
| **Gemini 3.1 Pro (High)** | 7.0 | 4 layers | 3+ | 3 items | **Format Collapse:** compressed into bullet points |
| **Gemini 3.8 Flash (High)** | 11.5 | 6 layers | 5+ | 2 items | Full protocol; rigorous adherence to constraints |

**Key Finding:** All models successfully produced the 3-phase macro-structure (Steelmanning → Dissection → Auto-Falsification). However, model capacity dictates analytical granularity: Opus generated 4.7× more analytical payload than Gemini Pro on identical data. Crucially, the failure of Gemini Pro (format collapse into bullet lists) led directly to the development of CRUCIBLE’s deterministic linter, which rejects collapsed formats automatically.

### 4.3. Multi-Model Consensus on Architecture
During the transition from v5.0 to v6.0, independent proposals for framework optimization were solicited from Claude Opus 4.6 and Gemini 3.1 Pro. Both independent models converged on three core architectural principles:
1. **Scalable Output Tiers:** Formally bifurcating monolithic outputs into Tier A (multi-disciplinary) and Tier B (focused single-thesis) protocols.
2. **Performative Bayesianism Shield:** Banning arbitrary subjective numerical probabilities (e.g., *"73.4% likely"*) in favor of directional ordinal bounds ($\Uparrow\Uparrow, \Uparrow, \rightarrow, \Downarrow, \Downarrow\Downarrow$) with explicit caveats.
3. **Substrate Parity:** Operating in the target text's original language to eliminate translation artifacts.

### 4.4. Empirical Substrate Asymmetry
Across all 9 showcase cases, parallel Turkish (`showcase/tr/`) and English (`showcase/en/`) monographs were generated from identical underlying dossiers. As detailed in Figure 2 and [`03_SUBSTRATE_PARITY_AND_LINGUISTIC_ASYMMETRY.md`](en/03_SUBSTRATE_PARITY_AND_LINGUISTIC_ASYMMETRY.md), non-native agglutinative prompting exhibits a rigid physical ceiling at ~18–21 KB (~175 lines). Conversely, conducting the audit in native English unlocked an average payload expansion of **+99.2%** (reaching up to +144.8% in Case 09), introducing granular biostatistical calculations, LaTeX matrices, and replication forensics that were completely erased under non-native prompting.

---

## 5. SYSTEM BOUNDARIES & FAILURE MODES

In accordance with Section 10 of our framework, CRUCIBLE documents its own boundary conditions:

1. **Context Dilution on Monolithic Documents (>400 Pages):** Direct ingestion of whole books causes the self-attention mechanism to disregard technical appendices and methodological footnotes ("lost in the middle"). CRUCIBLE requires human-curated Target Dossiers for massive texts.
2. **Pure Axiomatic Mathematics:** CRUCIBLE is an empirical, rhetorical, and epistemic gauntlet, not an Automated Theorem Prover (ATP). It excels at exposing rhetorical math abuse (e.g., Lacan’s topology) but cannot verify 50-step formal lemmas without an external symbolic engine (e.g., Lean or Isabelle).
3. **Model Weight Drift:** Commercial API weight updates can silently soften critique hardness. This is mitigated by enforcing deterministic CI/CD linter gates on every commit.
4. **Single-Run Benchmark Statistics:** The current benchmark suite documents reference execution cases rather than stochastic Monte Carlo distributions ($N=30$).

---

## 6. REPRODUCIBILITY & ARTIFACT AVAILABILITY

All target dossiers, audit monographs, Python verification scripts, and raw extraction templates are released under the permissive MIT License in the official repository:

* **Repository:** `github.com/curious/CRUCIBLE`
* **Benchmarks:** `benchmarks/en/` and `benchmarks/tr/` (18 dossiers)
* **Showcase Monographs:** `showcase/en/` and `showcase/tr/` (18 sealed reports)
* **Linter & Metric Extractor:** `scripts/crucible_linter.py` & `scripts/benchmark_extractor.py`
* **Methodology Specifications:** `docs/en/` (5 foundational treatises)

To reproduce the benchmark extraction table:
```bash
python scripts/benchmark_extractor.py
```
To validate any audited report against the normative specification:
```bash
python scripts/crucible_linter.py showcase/en/03_Cass_Review_Report.md
```

---

## 7. CONCLUSION

Generative AI cannot achieve genuine utility in scientific inquiry so long as it remains tethered to sycophantic alignment and smoothing abstractions. **CRUCIBLE v6.0** demonstrates that inference-time normative architectures—grounded in classical epistemology, causal DAGs, Popperian steelmanning, and deterministic linting—can force commercial frontier LLMs to operate as rigorous, unsparing analytical surgical instruments. By enforcing the Gödel-Tarski boundary and returning ultimate epistemic verification to the human surgeon, CRUCIBLE offers a robust, reproducible foundation for the future of automated scientific criticism.

---

## REFERENCES

1. **Bai, Y., et al. (2022).** *Constitutional AI: Harmlessness from AI Feedback.* Anthropic Preprint, arXiv:2212.08073.
2. **Bradford Hill, A. (1965).** *The Environment and Disease: Association or Causation?* Proceedings of the Royal Society of Medicine, 58(5), 295–300.
3. **Dhuliawala, S., et al. (2023).** *Chain-of-Verification Reduces Hallucination in Large Language Models.* arXiv:2309.11495.
4. **Huang, Y., et al. (2025).** *OpenReviewer: Automating Academic Paper Reviewing with Large Language Models.* arXiv:2501.xxxxx.
5. **Irving, G., Christiano, P., & Amodei, D. (2018).** *AI Safety via Debate.* arXiv:1805.00899.
6. **Madaan, A., et al. (2023).** *Self-Refine: Iterative Refinement with Self-Feedback.* NeurIPS 2023.
7. **OpenAI. (2024).** *CriticGPT: Training LLMs to Criticize Code.* OpenAI Research Technical Report.
8. **Pearl, J. (2009).** *Causality: Models, Reasoning, and Inference.* Cambridge University Press.
9. **Perez, E., et al. (2022).** *Discovering Language Model Behaviors with Model-Written Evaluations.* arXiv:2212.09251.
10. **Popper, K. R. (1959).** *The Logic of Scientific Discovery.* Hutchinson & Co.
11. **Sharma, M., et al. (2023).** *Towards Understanding Sycophancy in Large Language Models.* arXiv:2310.13548.
12. **Tarski, A. (1936).** *Der Wahrheitsbegriff in den formalisierten Sprachen.* Studia Philosophica, 1, 261–405.
