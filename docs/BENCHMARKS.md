# CRUCIBLE — QUANTITATIVE BENCHMARK RESULTS (v7.2 Grounded Architecture)
**Document ID:** `BENCHMARKS.md`  
**Version:** 7.2  
**Last Updated:** 2026-11-20  
**Methodology:** Cross-Model Benchmark Protocol v7.2 (Universal Substrate Parity & Full-Text Grounding)  
**Reference:** [`benchmarks/methodology/BENCHMARK_PROTOCOL.md`](../benchmarks/methodology/BENCHMARK_PROTOCOL.md)  
**Linter:** `scripts/crucible_linter.py` — All 9 showcase cases (18 reports: 9 EN, 9 TR) verified `[PASS]`  

> [!NOTE]
> **Provenance & Grounding Notice:** All 9 showcase evaluations listed below are fully grounded against unabridged primary monographs via `scripts/index_source.py`, enforcing deterministic paragraph verification (`[P:xxxx]`) and the Universal Substrate Parity Law ($L_{source} \equiv L_{audit} \rightarrow L_{target}$). Every report has passed AST structure, source grounding, and rhetoric linting.

---

## 1. PRIMARY METRIC TABLE: 9 Grounded Showcase Cases (v7.2 Production)

| # | Case | Discipline | Source Index | EN Report (KB) | TR Report (KB) | Active Layers | Linter (M3) | Methodological Fractures | Auto-Falsification Items | Source Matrix (K8) | Surgeon Card | Substrate Parity |
|:---|:---|:---|:---|---:|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 01 | Judith Butler – Gender Trouble | Post-Structuralist Philosophy | 252 paras | 18.2 | 17.9 | 5 | ✅ PASS | 3 | 3 | ✅ | ✅ | EN ➔ TR |
| 02 | Jacques Lacan – Encore | Psychoanalysis / Semiotics | 156 paras | 17.7 | 16.4 | 5 | ✅ PASS | 3 | 3 | ✅ | ✅ | EN ➔ TR |
| 03 | Hilary Cass – The Cass Review | Clinical Medicine / Epidemiology | 549 paras | 18.7 | 18.7 | 6 | ✅ PASS | 3 | 3 | ✅ | ✅ | EN ➔ TR |
| 04 | Cheikh Anta Diop – African Origin | Historiography / Anthropology | 18 sections | 16.9 | 17.2 | 6 | ✅ PASS | 3 | 3 | ✅ | ✅ | EN ➔ TR |
| 05 | Frank Snowden – Blacks in Antiquity | Classics / Ancient History | 388 paras | 17.4 | 17.1 | 5 | ✅ PASS | 3 | 3 | ✅ | ✅ | EN ➔ TR |
| 06 | Cook et al. vs Tol – Climate Consensus | Bibliometrics / Climatology | 9 paras | 17.8 | 20.5 | 6 | ✅ PASS | 3 | 3 | ✅ | ✅ | EN ➔ TR |
| 07 | Judith Curry – Climate Uncertainty | Atmospheric Physics / DMDU | 534 paras | 16.7 | 17.7 | 7 | ✅ PASS | 3 | 3 | ✅ | ✅ | EN ➔ TR |
| 08 | Joanna Moncrieff – Serotonin Theory | Psychiatry / Pharmacology | 14 paras | 16.8 | 20.9 | 6 | ✅ PASS | 3 | 3 | ✅ | ✅ | EN ➔ TR |
| 09 | Simon Baron-Cohen – Essential Difference | Cognitive Neuroscience | 279 paras | 16.8 | 17.0 | 7 | ✅ PASS | 3 | 3 | ✅ | ✅ | EN ➔ TR |

### 1.1. Aggregate Statistics

| Metric | Value |
|:---|:---|
| Total Cases Analyzed | 9 (18 Reports: 9 EN + 9 TR) |
| Linter Pass Rate | 18/18 (100% `[PASS]`) |
| Average Active Layers per Report | 6.0 |
| Total Methodological Fractures Dissected | 27 (3 per case) |
| Total Auto-Falsification Items | 27 (3 per case) |
| Source Matrix Presence (K8) | 18/18 (100%) |
| Surgeon Audit Card Presence | 18/18 (100%) |
| Universal Substrate Parity Compliance | 18/18 (100%) |

---

## 2. CROSS-MODEL CONSISTENCY: Evolution Test

The same target case (Evolution Theory — 4 Epistemic Boundaries) was analyzed by 4 frontier models. This tests whether CRUCIBLE produces structurally consistent output across different LLM engines.

| Model | Report Size (KB) | Active Layers | Fallacies Identified | Auto-Falsification | Structural Format |
|:---|---:|:---:|:---:|:---:|:---|
| Claude Opus 4.6 (Thinking) | 32.8 | K1,K2,K3,K5,K6-7,K8,K10 (7) | 4+ | 5 items | Full protocol |
| Claude Sonnet 4.6 (Thinking) | 21.4 | K1,K2,K3,K4,K5,K6-7,K8,K10 (8) | 4+ | 3 items | Full protocol |
| Gemini 3.1 Pro (High) | 7.0 | K1,K2,K4,K8 (4) | 3+ | 3 items | Compressed, bullet-point format |
| Gemini 3.8 Flash (High) | 11.5 | K1,K2,K4-5,K8,K9,K10 (6) | 5+ | 2 items | Full protocol with nuance |

### 2.1. Cross-Model Observations

| Observation | Detail |
|:---|:---|
| **Structural Consistency** | All models produced the required core structure (Triage → Analysis → Auto-Falsification). The protocol is model-invariant at the structural level. |
| **Depth Variance** | Opus (32.8 KB) produced 4.7× more analytical depth than Gemini Pro (7.0 KB) on the same input. Model capability significantly affects analytical granularity. |
| **Triage Convergence** | All models activated K1 (Epistemic Virtues), K2 (Steelmanning), and K8 (Disciplinary Matrix) for this case. Triage decisions show strong convergence. |
| **Auto-Falsification Variance** | Opus produced the deepest self-critique (5 items). Gemini Pro produced the shallowest (3 items). Self-critical depth correlates with model reasoning capacity. |
| **Format Collapse Risk** | Gemini Pro compressed the format into bullet points, losing tabular and matrix structures. This failure led to strict deterministic linter enforcement (`crucible_linter.py`). |

---

## 3. LINGUISTIC ASYMMETRY DATA

Dedicated studies on EN vs TR analytical output quality:

| Study | Key Finding | Source |
|:---|:---|:---|
| 3-Case Comparative Linguistic Audit | EN reports average 1.5–1.9× larger than TR counterparts on identical inputs | [`docs/en/04_THREE_CASE_LINGUISTIC_AUDIT.md`](en/04_THREE_CASE_LINGUISTIC_AUDIT.md) |
| Linguistic Substrate Asymmetry Report | English-native training corpus creates measurable analytical depth advantage in EN | [`docs/en/03_SUBSTRATE_PARITY_AND_LINGUISTIC_ASYMMETRY.md`](en/03_SUBSTRATE_PARITY_AND_LINGUISTIC_ASYMMETRY.md) |
| Model + Language Interaction Study | Substrate Parity Law dictates primary audits must occur in source text's native tongue | [`docs/en/05_TWO_STAGE_PIPELINE_AND_SUBSTRATE_DYNAMICS.md`](en/05_TWO_STAGE_PIPELINE_AND_SUBSTRATE_DYNAMICS.md) |

---

## 4. CROSS-MODEL CONVERGENCE ANALYSIS

Two frontier models (Opus and Gemini Pro) independently proposed methodological improvements. Their proposals were cross-validated for convergence and divergence:

| Convergence Point | Opus Proposal | Gemini Proposal | Strength |
|:---|:---|:---|:---:|
| Scalable Output Format | Enforced 5-section constitutional structure | Multi-layer = full format; single thesis = minimal | ★★★★★ |
| Performative Bayesianism Shield | Directional scale (↑↑/↑/→/↓/↓↓) + mandatory caveat | Directional symbols + numerical estimate ban | ★★★★★ |
| Linguistic Substrate Parity | Operate in source text's original language | Agreed | ★★★★☆ |

> **Significance:** When two independent AI models converge on the same diagnosis and solution, the finding gains substantial inter-rater reliability.

---

## 5. BENCHMARK LIMITATIONS

1. **Controlled Vanilla Baseline (Resolved - N=3):** Factorial comparison across Claude Opus 4.6 and Gemini 3.8 Flash demonstrated +100% to +164% payload expansion and enforcement of formal causal DAGs/source matrices absent in unconstrained outputs. See [`benchmarks/vanilla_baselines/`](../benchmarks/vanilla_baselines/).
2. **Single annotator.** Programmatic metrics (M1–M7) are objective; human-dependent metrics (M9–M12) await multi-annotator crowdsourcing.
3. **Non-API environment.** Historical benchmark models were evaluated in web environments.
4. **Single run per case.** No variance statistics across repeated runs.
5. **EN/TR ratio conflates language efficiency with analytical depth.**
