# CRUCIBLE v6.0 — BENCHMARK SUITE

Welcome to the **CRUCIBLE v6.0 Benchmark Suite**. This directory contains the structured target dossiers, methodology protocols, evaluation procedures, and reproducibility tooling used to quantitatively validate the CRUCIBLE epistemic gauntlet across 9 contentious academic and scientific battlefields.

---

## 📂 DIRECTORY STRUCTURE

```
benchmarks/
├── en/                                # 9 Primary English Target Dossiers
│   ├── 01_Judith_Butler_Gender_Trouble.md
│   ├── 02_Jacques_Lacan_Encore.md
│   ├── 03_Cass_Review_Gender_Medicine.md
│   ├── 04_Cheikh_Anta_Diop_African_Origin.md
│   ├── 05_Frank_Snowden_Blacks_in_Antiquity.md
│   ├── 06_Cook_Tol_Climate_Consensus.md
│   ├── 07_Judith_Curry_Climate_Uncertainty.md
│   ├── 08_Joanna_Moncrieff_Serotonin_Theory.md
│   └── 09_Simon_Baron_Cohen_Essential_Difference.md
├── tr/                                # 9 Parallel Turkish Target Dossiers
│   └── [01–09 Corresponding Turkish Dossiers]
├── methodology/                       # Formal Evaluation Protocols
│   ├── BENCHMARK_PROTOCOL.md          # Quantitative cross-model protocol (M1–M12 metrics)
│   └── BLIND_TEST_PROTOCOL.md         # Protocol for testing unseen academic works
└── README.md                          # This directory index
```

---

## 📊 SUITE OVERVIEW & CORE DELIVERABLES

| Component | Location | Description |
|:---|:---|:---|
| **Quantitative Results** | [`docs/BENCHMARKS.md`](../docs/BENCHMARKS.md) | Full 9-case metric table (M1–M8), aggregate statistics, V5 cross-model data, and V6 model consensus. |
| **Benchmark Protocol** | [`methodology/BENCHMARK_PROTOCOL.md`](methodology/BENCHMARK_PROTOCOL.md) | Formal experimental design, M1–M12 metric definitions, and cross-model validation rules. |
| **Blind Test Protocol** | [`methodology/BLIND_TEST_PROTOCOL.md`](methodology/BLIND_TEST_PROTOCOL.md) | Standardized procedure for independent researchers to audit unseen literature without bias. |
| **Limitations & Failure Modes** | [`docs/LIMITATIONS.md`](../docs/LIMITATIONS.md) | Transparent autopsy of computational boundaries (400+ page collapse, formal math limits, linguistic asymmetry). |
| **Automated Metric Extractor** | [`scripts/benchmark_extractor.py`](../scripts/benchmark_extractor.py) | Python script that programmatically regenerates `BENCHMARKS.md` from raw reports. |
| **Deterministic Linter** | [`scripts/crucible_linter.py`](../scripts/crucible_linter.py) | Structural and rhetorical validator enforcing 100% compliance before report sealing. |

---

## 🔬 THE 9 BENCHMARK DOMAINS

The benchmark suite spans 5 distinct faculties, testing the framework against diverse epistemological challenges:

1. **Post-Structuralist Philosophy:** Butler (Performative ontology vs. biological materiality)
2. **Psychoanalysis / Semiotics:** Lacan (Topological mathemes vs. pseudo-mathematics)
3. **Clinical Medicine / Epidemiology:** Cass Review (Pediatric cohort evidence grading under NICE standards)
4. **Historiography / Epigraphy:** Diop (Afrocentric diffusionism vs. Old Kingdom osteology)
5. **Classics / Ancient History:** Snowden (Greco-Roman somatic aesthetics vs. modern racial constructs)
6. **Bibliometrics / Climatology:** Cook vs. Tol (Consensus quantification & denominator exclusion)
7. **Climate Risk / Decision Science:** Curry (Deep uncertainty, ECS bounds vs. IPCC consensus)
8. **Psychiatry / Evidence-Based Medicine:** Moncrieff (Serotonin deficit hypothesis & the Aspirin Fallacy)
9. **Cognitive Neuroscience:** Baron-Cohen (Systemizing-Empathizing theory, neonate eye-tracking replication)

---

## ⚙️ REPRODUCIBILITY GUIDE

### 1. Re-extract Quantitative Metrics
To re-parse all showcase monographies and regenerate `docs/BENCHMARKS.md`:
```bash
python scripts/benchmark_extractor.py
```

### 2. Validate Any Monograph via Deterministic Linter
To verify structural compliance and rhetorical hygiene on any report:
```bash
python scripts/crucible_linter.py showcase/en/01_Judith_Butler_Report.md
```

### 3. Run Independent Blind Test
Follow the step-by-step scoring rubric and verification checklist in:
[`benchmarks/methodology/BLIND_TEST_PROTOCOL.md`](methodology/BLIND_TEST_PROTOCOL.md)
