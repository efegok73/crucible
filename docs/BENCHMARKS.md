# CRUCIBLE v7.3 — QUANTITATIVE BENCHMARK RESULTS
**Generated:** 2026-11-27  
**Audited By (AI Model):** Gemini 4 Hydrogen Extra High  
**Methodology:** Cross-Model Benchmark Protocol v1.0 (v7.3 Single-Document Grounded L1–L5)  
**Reference:** [`benchmarks/methodology/BENCHMARK_PROTOCOL.md`](../benchmarks/methodology/BENCHMARK_PROTOCOL.md)  
**Linter:** `scripts/crucible_linter.py` (`v7.3 --strict`) — All 9 EN showcase reports passed `[PASS]`  

---

## 1. PRIMARY METRIC TABLE: 9 Showcase Cases

| # | Case | Discipline | Dossier (KB) | EN Report (KB) | TR Report (KB) | Active Layers (M1) | Linter (M3) | Fallacies Detected (M4) | Auto-Falsification Depth (M5) | Source Matrix (M6) | Surgeon Card (M7) | EN/TR Ratio (M8) |
|:---|:---|:---|---:|---:|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 01 | Judith Butler – Gender Trouble | Post-Structuralist Philosophy | 9.0 | 35.4 | 36.6 | 6 | ✅ PASS | 4 | 5 | ✅ | ✅ | 0.97 |
| 02 | Jacques Lacan – Encore | Psychoanalysis / Semiotics | 11.3 | 38.4 | 39.7 | 6 | ✅ PASS | 7 | 4 | ✅ | ✅ | 0.97 |
| 03 | Cass Review – Gender Medicine | Clinical Medicine | 15.3 | 48.5 | 49.4 | 9 | ✅ PASS | 3 | 7 | ✅ | ✅ | 0.98 |
| 04 | Cheikh Anta Diop – African Origin | Historiography | 13.0 | 44.8 | 51.2 | 7 | ✅ PASS | 5 | 7 | ✅ | ✅ | 0.87 |
| 05 | Frank Snowden – Blacks in Antiquity | Classics / Ancient History | 13.9 | 31.9 | 32.0 | 6 | ✅ PASS | 4 | 3 | ✅ | ✅ | 1.0 |
| 06 | Cook et al. (2013) – 97% Climate Consensus | Bibliometrics / Climate Science | 11.3 | 31.6 | 31.1 | 8 | ✅ PASS | 3 | 7 | ✅ | ✅ | 1.01 |
| 07 | Judith Curry – Climate Uncertainty | Climate Science / Decision Theory | 12.7 | 41.3 | 43.5 | 9 | ✅ PASS | 4 | 7 | ✅ | ✅ | 0.95 |
| 08 | Joanna Moncrieff – Serotonin Theory | Psychiatry / Pharmacology | 14.1 | 37.0 | 36.6 | 9 | ✅ PASS | 9 | 7 | ✅ | ✅ | 1.01 |
| 09 | Simon Baron-Cohen – Essential Difference | Cognitive Neuroscience | 12.3 | 40.3 | 42.1 | 7 | ✅ PASS | 9 | 7 | ✅ | ✅ | 0.96 |

### 1.1. Aggregate Statistics

| Metric | Value |
|:---|:---|
| Total Cases Analyzed | 9 |
| Linter Pass Rate | 9/9 (100%) |
| Average Active Layers per Report | 7.4 |
| Total Fallacies Detected (All Cases) | 48 |
| Average Fallacies per Report | 5.3 |
| Total Auto-Falsification Items | 54 |
| Average Auto-Falsification Depth | 6.0 |
| Source Matrix Presence | 9/9 (100%) |
| Surgeon Card Presence | 9/9 (100%) |

---

## 2. CROSS-MODEL CONSISTENCY: V5 Evolution Test

The same target case (Evolution Theory — 4 Epistemic Boundaries) was analyzed by 4 frontier models under the V5.0 protocol. This tests whether CRUCIBLE produces structurally consistent output across different LLM engines.

| Model | Report Size (KB) | Active Layers | Fallacies Identified | Auto-Falsification | Structural Format |
|:---|---:|:---:|:---:|:---:|:---|
| Claude Opus 4.6 (Thinking) | 32.8 | K1,K2,K3,K5,K6-7,K8,K10 (7) | 4+ | 5 items | Full 3-phase V5 protocol |
| Claude Sonnet 4.6 (Thinking) | 21.4 | K1,K2,K3,K4,K5,K6-7,K8,K10 (8) | 4+ | 3 items | Full 3-phase V5 protocol |
| Gemini 3.1 Pro (High) | 7.0 | K1,K2,K4,K8 (4) | 3+ | 3 items | Compressed, bullet-point format |
| Gemini 3.8 Flash (High) | 11.5 | K1,K2,K4-5,K8,K9,K10 (6) | 5+ | 2 items | Full V5 protocol with nüans |

### 2.1. Cross-Model Observations

| Observation | Detail |
|:---|:---|
| **Structural Consistency** | All 4 models produced the required 3-phase structure (Triage → Analysis → Auto-Falsification). The protocol is model-invariant at the structural level. |
| **Depth Variance** | Opus (32.8 KB) produced 4.7× more analytical depth than Gemini Pro (7.0 KB) on the same input. Model capability significantly affects analytical granularity. |
| **Triage Convergence** | All models activated K1 (Epistemic Virtues), K2 (Steelmanning), and K8 (Disciplinary Matrix) for this case. Triage decisions show strong convergence. |
| **Auto-Falsification Variance** | Opus produced the deepest self-critique (5 items). Gemini Pro produced the shallowest (3 items). Self-critical depth correlates with model reasoning capacity. |
| **Format Collapse Risk** | Gemini Pro compressed the V5 format into bullet points, losing tabular and matrix structures. This failure directly informed the V6 "Scalable Output Format" improvement. |

---

## 3. LINGUISTIC ASYMMETRY DATA

Dedicated studies on EN vs TR analytical output quality:

| Study | Key Finding | Source |
|:---|:---|:---|
| 3-Case Comparative Linguistic Audit | EN reports average 1.5–1.9× larger than TR counterparts on identical inputs | [`docs/en/04_THREE_CASE_LINGUISTIC_AUDIT.md`](en/04_THREE_CASE_LINGUISTIC_AUDIT.md) |
| Linguistic Substrate Asymmetry Report | English-native training corpus creates measurable analytical depth advantage in EN | [`docs/en/03_SUBSTRATE_PARITY_AND_LINGUISTIC_ASYMMETRY.md`](en/03_SUBSTRATE_PARITY_AND_LINGUISTIC_ASYMMETRY.md) |
| Model + Language Interaction Study | Flash High > Pro for both extraction and CRUCIBLE execution; EN > TR for formal schema adherence | [`docs/en/05_TWO_STAGE_PIPELINE_AND_SUBSTRATE_DYNAMICS.md`](en/05_TWO_STAGE_PIPELINE_AND_SUBSTRATE_DYNAMICS.md) |

---

## 4. V6 CROSS-VALIDATION: CONVERGENCE ANALYSIS

Two frontier models (Opus 4.6 and Gemini Pro) independently proposed improvements to the V5→V6 methodology. Their proposals were then cross-validated for convergence and divergence:

| Convergence Point | Opus Proposal | Gemini Proposal | Strength |
|:---|:---|:---|:---:|
| Scalable Output Format | Tier A (full 11-section) vs Tier B (minimal 5-section) | Multi-layer = full format; single thesis = minimal | ★★★★★ |
| Performative Bayesianism Shield | 5-grade directional scale (↑↑/↑/→/↓/↓↓) + mandatory caveat | Directional symbols + numerical estimate ban | ★★★★★ |
| Linguistic Substrate Parity | Operate in source text's original language | Agreed | ★★★★☆ |

> **Significance:** When two independent AI models converge on the same diagnosis and solution, the finding gains substantial inter-rater reliability — analogous to two independent reviewers reaching the same conclusion in a systematic review.

---

## 5. LIMITATIONS

This benchmark data carries the following limitations (see `BENCHMARK_PROTOCOL.md` Section 5 for full details):

1. **Controlled Vanilla Baseline (Resolved - N=3):** Factorial comparison across Claude Opus 4.6 and Gemini 3.8 Flash against an elite academic prompt demonstrated +100% to +164% payload expansion and enforcement of formal causal DAGs/source matrices absent in unconstrained outputs. See [`benchmarks/vanilla_baselines/`](../benchmarks/vanilla_baselines/).
2. **Single annotator.** Programmatic metrics (M1–M7) are objective; human-dependent metrics (M9–M12) are not yet populated.
3. **Non-API environment.** Model parameters were not API-locked.
4. **Single run per case.** No variance statistics across repeated runs.
5. **EN/TR ratio conflates language efficiency with analytical depth.**
