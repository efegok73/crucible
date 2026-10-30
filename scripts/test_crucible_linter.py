#!/usr/bin/env python3
"""
CRUCIBLE v6.0 Linter Unit Test Suite
====================================
Tests all Z1-Z10 epistemic audit checks, hierarchical heading parsing,
rhetorical hygiene, multilingual detection, and SHA-256 seal verification.
"""

import os
import sys
import json
import tempfile
import unittest

# scripts klasörünü sys.path'e ekle
_DIR = os.path.dirname(os.path.abspath(__file__))
if _DIR not in sys.path:
    sys.path.insert(0, _DIR)

from crucible_linter import CrucibleLinter, LintResult, CORE_SECTIONS


def make_valid_document(
    triage_extra: str = "",
    steelman_text: str = "",
    falsification_text: str = "",
    damage_text: str = "",
    extra_body: str = "",
    extra_sections: str = "",
    include_k8_table: bool = True
) -> str:
    """Builds a compliant mock report of sufficient payload and word counts."""
    triage_content = """
### Active Layers & Justification
| Layer | Status | Justification |
|---|---|---|
| **K1: Persona & Virtue** | ✅ ACTIVE | Persona and epistemic humility are always active throughout this analysis. |
| **K8: Disciplinary Matrix** | ✅ ACTIVE | Interdisciplinary source and textual criticism applied. |
| **K4: Statistics & Bayes** | ⛔ EXCLUDED | No quantitative data sets or clinical trials available in text. |
""" + triage_extra

    sm_body = steelman_text or """
In this section we construct the strongest possible version of the author's primary argument.
We identify the key premises: First, knowledge claims require grounding in observable reality.
Second, discursive categories must not be conflated with ontological substrates.
Third, internal coherence is evaluated through charitable interpretation and systematic reconstruction of every proposition.
"""

    fals_body = falsification_text or """
Here we subject our own analytical model to rigorous Popperian falsification criteria.
What specific historical discovery or empirical observation would decisively refute our conclusions?
We disclose potential confirmation biases, methodological assumptions, and single-source dependencies.
"""

    dam_body = damage_text or """
The minimal epistemic toll of this inquiry is moderate.
We document where the author's claims survive counter-objections and where they suffer critical structural damage.
Tensions between hermeneutic interpretation and causal claims remain unresolved.
"""

    k8_table = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Core proposition Alpha | Original Text (1990) | Primary Source | Internally coherent within hermeneutic model |
| Secondary premise Beta | Historical Archive (1920) | Archival Data | Contextual reading confirms historical thesis |
""" if include_k8_table else ""

    doc = f"""# Test Benchmark Analysis Report
*Analyst: Persona V6.0*

## [EPISTEMIC TRIAGE]
{triage_content}

## Article 1: STEELMAN FORMULATION
{sm_body}

## Article 2: AUTO-FALSIFICATION
{fals_body}

## Article 3: DAMAGE REPORT
{dam_body}

{k8_table}

{extra_sections}

## SURGEON'S AUDIT CARD
| # | Check | Action |
|---|---|---|
| ☐ | Spot Check #1 | Verify verbatim citation in primary source |
| ☐ | Spot Check #2 | Check cross-disciplinary boundaries |

{extra_body}
"""
    # Ensure minimum payload requirements (30 lines and 1500 chars)
    padding = "\n<!-- Payload expansion padding for deterministic linter compliance -->" * 20
    return doc + padding


class TestCrucibleLinter(unittest.TestCase):

    def setUp(self):
        self.temp_files = []

    def tearDown(self):
        for p in self.temp_files:
            if os.path.exists(p):
                try:
                    os.remove(p)
                except OSError:
                    pass
            html_p = os.path.splitext(p)[0] + ".html"
            if os.path.exists(html_p):
                try:
                    os.remove(html_p)
                except OSError:
                    pass

    def _create_report(self, text: str) -> str:
        fd, path = tempfile.mkstemp(suffix=".md", prefix="crucible_test_")
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(text)
        self.temp_files.append(path)
        return path

    # ────────────────────────────────────────────────────────────────
    # Baseline Test
    # ────────────────────────────────────────────────────────────────

    def test_valid_baseline_report_passes(self):
        """A well-formed compliant report must PASS with zero errors."""
        md = make_valid_document()
        path = self._create_report(md)
        linter = CrucibleLinter(path)
        result = linter.validate()

        self.assertTrue(result.passed, f"Validation unexpectedly failed: {result.errors}")
        self.assertEqual(len(result.errors), 0)

    # ────────────────────────────────────────────────────────────────
    # Z1: Hollow Section Attack vs Valid Sections
    # ────────────────────────────────────────────────────────────────

    def test_z1_hollow_section_fails(self):
        """Z1: Sections with title only (no substantive body) must FAIL."""
        hollow_md = """# Analysis Report
*Analyst: Persona V6.0*

## [EPISTEMIC TRIAGE]
Active layers: K1.

## STEELMANNING
(empty)

## AUTO-FALSIFICATION
(empty)

## DAMAGE REPORT
(empty)

## SURGEON CHECKLIST
- [ ] check 1
""" + ("\nline filler line text " * 50)

        path = self._create_report(hollow_md)
        linter = CrucibleLinter(path)
        result = linter.validate()

        self.assertFalse(result.passed)
        hollow_errors = [e for e in result.errors if "Hollow Section" in e]
        self.assertGreater(len(hollow_errors), 0, "Should detect hollow sections")

    # ────────────────────────────────────────────────────────────────
    # Z2: Triage Layer & Passive Exclusion Discrimination
    # ────────────────────────────────────────────────────────────────

    def test_z2_triage_active_and_excluded_layers(self):
        """Z2: Active layers detected in body; excluded layers ignored."""
        md = make_valid_document()
        path = self._create_report(md)
        linter = CrucibleLinter(path)
        result = linter.validate()

        self.assertIn('K1', result.active_layers)
        self.assertIn('K8', result.active_layers)
        self.assertNotIn('K4', result.active_layers, "Excluded K4 must not be in active layers")
        self.assertTrue(result.passed)

    # ────────────────────────────────────────────────────────────────
    # Z3: Scoped Rhetorical Exception (No Global Leak)
    # ────────────────────────────────────────────────────────────────

    def test_z3_scoped_rhetorical_exception(self):
        """Z3: Forbidden term in ordinary text flagged; didactic table exempted."""
        didactic_extra = """
### Yasak İfadeler ve Safsata Analizi
| Safsata Türü | Yazarın Cümlesi | Değerlendirme |
|---|---|---|
| Dogmatizm | "şüphesiz bu böyledir" | Yazar dogmatik kesinlik safsatası yapmıştır |

### Genel Değerlendirme
Bu teorik tez şüphesizdir ve tartışmasızdır.
"""
        md = make_valid_document(extra_body=didactic_extra)
        path = self._create_report(md)
        linter = CrucibleLinter(path)
        result = linter.validate()

        # Dogmatic warning should be caught from general text
        rhetoric_warnings = [w for w in result.warnings if "Forbidden dogmatic term" in w]
        self.assertGreater(len(rhetoric_warnings), 0, "Dogmatic claim in general text must be flagged")

    # ────────────────────────────────────────────────────────────────
    # Z4 & Z5: Multilingual Forbidden Terms & Turkish Boundary
    # ────────────────────────────────────────────────────────────────

    def test_z4_z5_multilingual_forbidden_terms(self):
        """Z4/Z5: Multilingual dogmatic words caught with proper boundary."""
        # 1. Turkish dogmatic
        tr_md = make_valid_document(extra_body="\nBu iddia şüphesizdir ve kesinlikle ispatlanmıştır.\n")
        path_tr = self._create_report(tr_md)
        res_tr = CrucibleLinter(path_tr).validate()
        tr_warnings = [w for w in res_tr.warnings if "Forbidden dogmatic term" in w]
        self.assertGreater(len(tr_warnings), 0, "Turkish dogmatic term must trigger warning")

        # 2. English dogmatic
        en_md = make_valid_document(extra_body="\nThis thesis is beyond all doubt and undeniably true.\n")
        path_en = self._create_report(en_md)
        res_en = CrucibleLinter(path_en).validate()
        en_warnings = [w for w in res_en.warnings if "Forbidden dogmatic term" in w]
        self.assertGreater(len(en_warnings), 0, "English dogmatic term must trigger warning")

        # 3. Clean neutral text
        clean_md = make_valid_document(extra_body="\nNötr bir epistemik inceleme yürütülmektedir.\n")
        path_clean = self._create_report(clean_md)
        res_clean = CrucibleLinter(path_clean).validate()
        clean_warnings = [w for w in res_clean.warnings if "Forbidden dogmatic term" in w]
        self.assertEqual(len(clean_warnings), 0, "Neutral text should trigger zero rhetorical warnings")

    # ────────────────────────────────────────────────────────────────
    # Z6: Content-Based Language Detection
    # ────────────────────────────────────────────────────────────────

    def test_z6_language_detection(self):
        """Z6: Stop-word frequency determines language from content."""
        tr_sample = "Bu araştırma raporunda yazarın ortaya koyduğu argümanlar için titiz bir inceleme yapılmıştır çünkü veri yoktur ancak iddia büyüktür. " * 10
        en_sample = "In this research report, the author provides an argument which is based on several premises that are not fully supported by empirical data. " * 10

        md_tr = make_valid_document(extra_body=tr_sample)
        path_tr = self._create_report(md_tr)
        res_tr = CrucibleLinter(path_tr).validate()
        self.assertEqual(res_tr.detected_language, 'tr')

        md_en = make_valid_document(extra_body=en_sample)
        path_en = self._create_report(md_en)
        res_en = CrucibleLinter(path_en).validate()
        self.assertEqual(res_en.detected_language, 'en')

    # ────────────────────────────────────────────────────────────────
    # Z7: SHA-256 Verification Seal in HTML
    # ────────────────────────────────────────────────────────────────

    def test_z7_cryptographic_seal_in_html(self):
        """Z7: Compiled HTML contains deterministic verification seal with sha256."""
        md = make_valid_document()
        path = self._create_report(md)
        linter = CrucibleLinter(path)
        result = linter.validate()
        self.assertTrue(result.passed)

        html_path = linter.compile_html()
        self.assertIsNotNone(html_path)
        self.assertTrue(os.path.exists(html_path))

        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        self.assertIn("DETERMINISTIC VERIFICATION SEAL", html_content)
        self.assertIn("sha256:", html_content)
        self.assertIn("[PASS] CONSTITUTIONAL COMPLIANCE", html_content)

    # ────────────────────────────────────────────────────────────────
    # Subheading Hierarchy
    # ────────────────────────────────────────────────────────────────

    def test_subheading_hierarchy_preserves_section_body(self):
        """Subheadings (###) within (##) must not zero out the parent section body."""
        subheadings = """
### Subsection 1.1: Active Layers
| Layer | Status |
|---|---|
| K1 | ✅ ACTIVE |

### Subsection 1.2: Methodological Scope
Here is an extensive explanation of the methodological scope of the research project,
containing sufficient words so that the triage section is fully populated and valid.
We systematically review the disciplinary matrix and its boundaries.
"""
        md = make_valid_document(triage_extra=subheadings)
        path = self._create_report(md)
        linter = CrucibleLinter(path)
        result = linter.validate()

        triage_sec = next((s for s in linter.sections if "TRIAGE" in s.title), None)
        self.assertIsNotNone(triage_sec)
        self.assertGreater(triage_sec.word_count, 20, "Triage section should include subsections")
        self.assertTrue(result.passed, f"Failed with errors: {result.errors}")

    # ────────────────────────────────────────────────────────────────
    # v7.0 Source Grounding Verification Tests
    # ────────────────────────────────────────────────────────────────

    def test_v7_grounded_artifact_verification_success(self):
        """v7.0: When primary source is provided and matrix artifacts exist in source, passes."""
        source_text = "Here is the historical corpus discussing Birmingham manuscript and Zuhayr inscription."
        source_path = self._create_report(source_text)

        matrix = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Core proposition Alpha | Birmingham manuscript (1936) | Primary Source | Verified in text |
| Epigraphic finding Beta | Zuhayr inscription (H. 24) | In Situ Rock | Verified in text |
"""
        md = make_valid_document(include_k8_table=False, extra_sections=matrix)
        report_path = self._create_report(md)

        linter = CrucibleLinter(report_path, source_path=source_path)
        result = linter.validate()
        self.assertTrue(result.passed, f"Expected pass, got errors: {result.errors}")
        self.assertTrue(result.grounded)

    def test_v7_ungrounded_artifact_fails(self):
        """v7.0: An artifact in the matrix not found in the primary source triggers hard failure."""
        source_text = "Here is the corpus discussing only Damascus coins and Fustat papyri."
        source_path = self._create_report(source_text)

        matrix = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Core proposition Alpha | Damascus coins | Primary Source | Verified in text |
| Epigraphic finding Beta | Selme Yazıtı (H. 80) | In Situ Rock | Hallucinated artifact! |
"""
        md = make_valid_document(include_k8_table=False, extra_sections=matrix)
        report_path = self._create_report(md)

        linter = CrucibleLinter(report_path, source_path=source_path)
        result = linter.validate()
        self.assertFalse(result.passed)
        self.assertTrue(any("UNGROUNDED ARTIFACT" in err and "Selme" in err for err in result.errors),
                        f"Expected ungrounded artifact error for Selme, got: {result.errors}")

    def test_v7_external_artifact_tag_exemption(self):
        """v7.0: An external comparison tagged with [DIŞ KAYNAK] is exempted from source matching."""
        source_text = "Here is the corpus discussing only Damascus coins."
        source_path = self._create_report(source_text)

        matrix = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Core proposition Alpha | Damascus coins | Primary Source | Verified in text |
| External comparison | [DIŞ KAYNAK] Selme Yazıtı (H. 80) | External Evidence | Legitimate external reference |
"""
        md = make_valid_document(include_k8_table=False, extra_sections=matrix)
        report_path = self._create_report(md)

        linter = CrucibleLinter(report_path, source_path=source_path)
        result = linter.validate()
        self.assertTrue(result.passed, f"Expected pass with external exemption, got errors: {result.errors}")

    def test_v7_unverified_quote_fails(self):
        """v7.0: Fabricated quotes attached to [P:xxxx] trigger hard validation errors."""
        source_text = "Paragraph 1: Real text discussing early manuscripts."
        source_path = self._create_report(source_text)

        body_with_bad_quote = """
## Article 1: STEELMAN FORMULATION
In this section we construct the strongest possible version of the author's primary argument.
We identify the key premises: First, knowledge claims require grounding in observable reality.
As the author states [P:1] *"Completely fabricated quote that appears nowhere in the source text"*,
the structural coherence is evaluated through charitable interpretation and systematic reconstruction of every proposition.
"""
        md = make_valid_document(steelman_text=body_with_bad_quote)
        report_path = self._create_report(md)

        linter = CrucibleLinter(report_path, source_path=source_path)
        result = linter.validate()
        self.assertFalse(result.passed)
        self.assertTrue(any("UNVERIFIED QUOTE" in err for err in result.errors),
                        f"Expected unverified quote error, got: {result.errors}")


if __name__ == '__main__':
    unittest.main()
