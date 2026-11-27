#!/usr/bin/env python3
"""
CRUCIBLE v7.2 Linter Unit Test Suite
====================================
Tests all Z1-Z10 epistemic audit checks, hierarchical heading parsing,
rhetorical hygiene, multilingual detection, substrate parity, paragraph bounds,
and SHA-256 seal verification.
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

from crucible_linter import CrucibleLinter, LintResult, CORE_SECTIONS, detect_text_language


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

        linter = CrucibleLinter(report_path, source_path=source_path, allow_localized=True)
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

        linter = CrucibleLinter(report_path, source_path=source_path, allow_localized=True)
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

        linter = CrucibleLinter(report_path, source_path=source_path, allow_localized=True)
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

        linter = CrucibleLinter(report_path, source_path=source_path, allow_localized=True)
        result = linter.validate()
        self.assertFalse(result.passed)
        self.assertTrue(any("UNVERIFIED QUOTE" in err for err in result.errors),
                        f"Expected unverified quote error, got: {result.errors}")

    def test_v7_multi_token_phantom_artifact_fails(self):
        """v7.1: Multi-token hallucinated artifact fails even if one token exists in source (AND logic)."""
        source_text = "Metinde sadece Selme köyünden bahsedilmektedir."
        source_path = self._create_report(source_text)

        matrix = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Core proposition Alpha | Tamamen Hayali Selme Kodeksi | Primary Source | Hallucinated artifact! |
"""
        md = make_valid_document(include_k8_table=False, extra_sections=matrix)
        report_path = self._create_report(md)

        linter = CrucibleLinter(report_path, source_path=source_path, allow_localized=True)
        result = linter.validate()
        self.assertFalse(result.passed)
        self.assertTrue(any("UNGROUNDED ARTIFACT" in err and "Tamamen Hayali Selme Kodeksi" in err for err in result.errors),
                        f"Expected ungrounded artifact error, got: {result.errors}")

    def test_v7_isolated_matrix_prevents_damage_report_table_leak(self):
        """v7.1: A second table in Damage Report does NOT leak into K8 matrix."""
        source_text = "Metinde Selme Yazıtı bulunmaktadır."
        source_path = self._create_report(source_text)

        matrix = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Core proposition Alpha | Selme Yazıtı | Primary Source | Verified in text |

## DAMAGE REPORT
Hasar raporu detayları aşağıdadır ve en az on beş kelimelik içerik barındırmaktadır.

| Hasar Türü | Etki Düzeyi | Not |
|---|---|---|
| Epistemik Bozulma | Düşük | Bu satır matris sanılmamalıdır |
"""
        md = make_valid_document(include_k8_table=False, extra_sections=matrix)
        report_path = self._create_report(md)

        linter = CrucibleLinter(report_path, source_path=source_path, allow_localized=True)
        result = linter.validate()
        self.assertTrue(result.passed, f"Expected pass, got errors: {result.errors}")
        self.assertTrue(result.grounded)

    def test_v7_turkish_case_folding_grounding(self):
        """v7.1: Turkish dotted/dotless I case folding works correctly in grounding."""
        source_text = "İSLAM ve IRAK coğrafyasındaki bulgular incelenmiştir."
        source_path = self._create_report(source_text)

        matrix = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Tarihsel tez | İslam ve Irak metinleri | Primary Source | Verified |
"""
        md = make_valid_document(include_k8_table=False, extra_sections=matrix)
        report_path = self._create_report(md)

        linter = CrucibleLinter(report_path, source_path=source_path, allow_localized=True)
        result = linter.validate()
        self.assertTrue(result.passed, f"Expected pass with Turkish case folding, got errors: {result.errors}")
        self.assertTrue(result.grounded)

    def test_v7_quote_with_apostrophe_and_after_anchor(self):
        """v7.1: Quotes with apostrophes and quotes preceding [P:xxxx] anchors are verified."""
        source_text = "Bu çalışmada Zuhayr'ın meşhur şiiri ve author's argument ele alınmaktadır."
        source_path = self._create_report(source_text)

        matrix = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Core proposition Alpha | Zuhayr şiiri | Primary Source | Verified in text |
"""

        body_with_quotes = """
In this section we construct the strongest possible version of the author's primary argument.
We identify the key premises: First, knowledge claims require grounding in observable reality.
As stated: "Zuhayr'ın meşhur şiiri ve author's argument" [P:1], the dialectical friction is analyzed.
This section contains detailed substantive text meeting all minimum word count thresholds.
"""
        md = make_valid_document(steelman_text=body_with_quotes, include_k8_table=False, extra_sections=matrix)
        report_path = self._create_report(md)

        linter = CrucibleLinter(report_path, source_path=source_path, allow_localized=True)
        result = linter.validate()
        self.assertTrue(result.passed, f"Expected quote with apostrophe to pass, got errors: {result.errors}")

    def test_v7_universal_language_detection(self):
        """v7.2: Multi-lingual script and stop-word language detector handles non-Latin & Latin scripts."""
        # Chinese
        self.assertEqual(detect_text_language("这是一段关于科学方法论与认识论批判的中文学术文本，包含足够的字符进行语言识别。"), 'zh')
        # Arabic
        self.assertEqual(detect_text_language("هذا نص أكاديمي باللغة العربية يتعلق بالمنهجية الفلسفية ونقد المصادر التاريخية للتحقق من صحة النص الأصلي."), 'ar')
        # Russian
        self.assertEqual(detect_text_language("Это академический текст на русском языке, посвященный методологии научного исследования и эпистемологии."), 'ru')
        # Turkish
        self.assertEqual(detect_text_language("Bu makale bilim felsefesi ve epistemolojik triyaj ilkeleri üzerine odaklanmaktadır."), 'tr')
        # English
        self.assertEqual(detect_text_language("This paper focuses on the philosophy of science and the empirical falsification of historical claims."), 'en')

    def test_v7_substrate_parity_violation_fails(self):
        """v7.2: English source audited directly in Turkish without two-stage declaration fails Substrate Parity."""
        source_text = "The quick brown fox jumps over the lazy dog. Scientific methodology demands empirical falsification."
        source_path = self._create_report(source_text)

        # Turkish report with Turkish headings and stop words
        tr_body = """
Bu bölümde yazarın öne sürdüğü temel savın en güçlü ve tutarlı halini yeniden kuruyoruz.
Yazarın birinci temel öncülü şudur: Bilimsel bilgi iddiaları gözlemlenebilir gerçekliğe dayanmak zorundadır.
İkinci olarak, söylemsel kategoriler ile ontolojik zemin birbirine karıştırılmamalıdır.
Üçüncü olarak, iç tutarlılık titiz bir metodolojik çözümlemeyle sınanmalıdır.
"""
        matrix = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Core proposition Alpha | Scientific methodology | Primary Source | Verified in text |
"""
        # A Turkish document
        triage_tr = """
### Aktif Katmanlar
| Katman | Durum | Gerekçe |
|---|---|---|
| **K1: Persona** | ✅ AKTİF | Epistemik alçakgönüllülük ve analitik tutum zorunludur. |
| **K8: Disipliner Matris** | ✅ AKTİF | Kaynak tenkiti işletilmektedir. |
"""
        md = f"""# Test Raporu
## [EPİSTEMOLOJİK TRİYAJ]
{triage_tr}
## 2. ÇELİK ADAM
{tr_body}
## 3. OTO-FALSİFİKASYON
Kendi analizimizdeki metodolojik kısıtları, model eğilimlerini ve tek kaynak risklerini burada dürüstçe sorguluyoruz. Hangi ampirik bulgunun veya karşıt arşiv belgesinin bu analizimizin temel çıkarımlarını yanlışlayacağını açıkça ifşa ediyoruz.
## 4. HASAR RAPORU
Tezin aldığı asgari epistemik hasar ve geriye kalan sağlam iddia çekirdeği burada özetlenmektedir. Metodolojik zafiyetler tezin genellenebilirlik sınırlarını daraltmıştır.
{matrix}
## 5. CERRAH DENETİM KARTI
- [ ] Birincil kaynakta doğrudan alıntı kontrolü yap.
""" + ("\n<!-- padding dolgusu -->" * 25)

        report_path = self._create_report(md)
        linter = CrucibleLinter(report_path, source_path=source_path, allow_localized=False)
        result = linter.validate()
        self.assertFalse(result.passed)
        self.assertFalse(result.substrate_parity)
        self.assertTrue(any("SUBSTRATE PARITY VIOLATION" in e for e in result.errors))

    def test_v7_substrate_parity_pass_with_allow_localized_or_parent_audit(self):
        """v7.2: Localized report passes when --allow-localized or **Primary Audit:** metadata is present."""
        source_text = "The quick brown fox jumps over the lazy dog. Scientific methodology demands empirical falsification."
        source_path = self._create_report(source_text)

        tr_body = """
Bu bölümde yazarın öne sürdüğü temel savın en güçlü ve tutarlı halini yeniden kuruyoruz.
Yazarın birinci temel öncülü şudur: Bilimsel bilgi iddiaları gözlemlenebilir gerçekliğe dayanmak zorundadır.
İkinci olarak, söylemsel kategoriler ile ontolojik zemin birbirine karıştırılmamalıdır.
Üçüncü olarak, iç tutarlılık titiz bir metodolojik çözümlemeyle sınanmalıdır.
"""
        matrix = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Core proposition Alpha | Scientific methodology | Primary Source | Verified in text |
"""
        triage_tr = """
### Aktif Katmanlar
| Katman | Durum | Gerekçe |
|---|---|---|
| **K1: Persona** | ✅ AKTİF | Epistemik alçakgönüllülük ve analitik tutum zorunludur. |
| **K8: Disipliner Matris** | ✅ AKTİF | Kaynak tenkiti işletilmektedir. |
"""
        # With **Primary Audit:** header
        md_with_meta = f"""# Test Raporu
**Primary Audit:** `audits/primary_source_audit_en.md`

## [EPİSTEMOLOJİK TRİYAJ]
{triage_tr}
## 2. ÇELİK ADAM
{tr_body}
## 3. OTO-FALSİFİKASYON
Kendi analizimizdeki metodolojik kısıtları, model eğilimlerini ve tek kaynak risklerini burada dürüstçe sorguluyoruz. Hangi ampirik bulgunun veya karşıt arşiv belgesinin bu analizimizin temel çıkarımlarını yanlışlayacağını açıkça ifşa ediyoruz.
## 4. HASAR RAPORU
Tezin aldığı asgari epistemik hasar ve geriye kalan sağlam iddia çekirdeği burada özetlenmektedir. Metodolojik zafiyetler tezin genellenebilirlik sınırlarını daraltmıştır.
{matrix}
## 5. CERRAH DENETİM KARTI
- [ ] Birincil kaynakta doğrudan alıntı kontrolü yap.
""" + ("\n<!-- padding dolgusu -->" * 25)

        report_path = self._create_report(md_with_meta)
        linter = CrucibleLinter(report_path, source_path=source_path, allow_localized=True)
        result = linter.validate()
        self.assertTrue(result.passed, f"Expected pass with metadata, got errors: {result.errors}")
        self.assertTrue(result.substrate_parity)

        # Also test with allow_localized=True without metadata
        md_bare = md_with_meta.replace("**Primary Audit:** `audits/primary_source_audit_en.md`", "")
        report_path_bare = self._create_report(md_bare)
        linter_allowed = CrucibleLinter(report_path_bare, source_path=source_path, allow_localized=True)
        res_allowed = linter_allowed.validate()
        self.assertTrue(res_allowed.passed, f"Expected pass with allow_localized, got errors: {res_allowed.errors}")
        self.assertTrue(res_allowed.substrate_parity)

    def test_v7_invalid_paragraph_index_fails(self):
        """v7.2 Hardening: Out-of-bounds paragraph index produces compile ERROR instead of warning."""
        source_text = "Birinci paragraf metni burada yer almaktadır.\n\nİkinci paragraf metni de buradadır."
        source_path = self._create_report(source_text)

        md = f"""# Test Raporu
## [EPİSTEMOLOJİK TRİYAJ]
* K1 (Persona): AKTİF
* K8 (Kaynak Tenkit): AKTİF
## 2. ÇELİK ADAM
Burada yazarın savı en güçlü haliyle ele alınmaktadır. İddia edilen sav incelenmektedir.
[P:9999] "Birinci paragraf metni burada yer almaktadır."
## 3. OTO-FALSİFİKASYON
Analizin sınırlarını dürüstçe açıklıyoruz. Model kısıtlarını açıkça belirtiyoruz.
## 4. HASAR RAPORU
Tezin aldığı hasar ve asgari epistemik bedel özetlenmektedir.
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Sav Alpha | Birinci paragraf | Primary Source | Verified |
## 5. CERRAH DENETİM KARTI
- [ ] Kontrol et.
""" + ("\n<!-- padding dolgusu -->" * 25)

        report_path = self._create_report(md)
        linter = CrucibleLinter(report_path, source_path=source_path)
        result = linter.validate()
        self.assertFalse(result.passed)
        self.assertTrue(any("INVALID PARAGRAPH INDEX" in e for e in result.errors))

    def test_v7_page_reference_stripping_in_matrix(self):
        """v7.2 Hardening: Academic page references [Sayfa 116] or [p. 45] are stripped from matrix artifacts."""
        source_text = "Önerme 9 Açıklama metni burada açıkça yer almaktadır ve incelenmiştir."
        source_path = self._create_report(source_text)

        matrix = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Önerme Savı | Önerme 9 Açıklama [Sayfa 116] | Primary Source | Metodolojik Hüküm |
"""
        steelman = (
            "Bu bölümde yazarın savı en güçlü akademik biçimde yeniden kurulmaktadır. "
            "Metodolojik öncüller ayrıntılı bir biçimde incelenmiş ve yazarın temel çıkarımları "
            "zemin metin çıpasıyla doğrulanmıştır. [P:1] \"Önerme 9 Açıklama metni burada açıkça yer almaktadır ve incelenmiştir.\""
        )
        md = make_valid_document(steelman_text=steelman, extra_sections=matrix, include_k8_table=False)

        report_path = self._create_report(md)
        linter = CrucibleLinter(report_path, source_path=source_path, allow_localized=True)
        result = linter.validate()
        self.assertTrue(result.passed, f"Expected pass with stripped page ref, got errors: {result.errors}")

    def test_v7_expanded_quote_and_blockquote_range(self):
        """v7.2 Hardening: Long quotes (>250 chars) and markdown blockquotes (> [P:1] ...) are verified."""
        long_quote = (
            "Bilimsel tefekkürün temel gayesi olguları önceden varsayılmış dogmatik şablonlara uydurmak değil, "
            "tam aksine ampirik gözlemin sunduğu çelişkileri cesaretle göğüsleyerek mevcut kuramsal çerçeveyi "
            "tavizsiz bir metodolojik teste tabi tutmaktır; zira hakikatin aranması ancak yanılgının ifşasıyla mümkündür."
        )
        self.assertGreater(len(long_quote), 250)
        source_text = f"Giriş paragrafı.\n\n{long_quote}\n\nSonuç paragrafı."
        source_path = self._create_report(source_text)

        matrix = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Bilimsel Sav | Giriş paragrafı | Primary Source | Doğrulandı |
"""
        steelman_valid = f'Yazarın temel yaklaşımı şu blok alıntıda açıkça görülmektedir:\n\n> [P:2] "{long_quote}"'
        md_valid = make_valid_document(steelman_text=steelman_valid, extra_sections=matrix, include_k8_table=False)

        report_path_valid = self._create_report(md_valid)
        linter_valid = CrucibleLinter(report_path_valid, source_path=source_path, allow_localized=True)
        res_valid = linter_valid.validate()
        self.assertTrue(res_valid.passed, f"Expected long quote to pass, got: {res_valid.errors}")

        # Fabricated long quote fails
        fabricated_quote = long_quote.replace("tavizsiz bir metodolojik teste", "tamamen hayali bir kurguya")
        steelman_invalid = f'Yazarın temel yaklaşımı şu blok alıntıda açıkça görülmektedir:\n\n> [P:2] "{fabricated_quote}"'
        md_invalid = make_valid_document(steelman_text=steelman_invalid, extra_sections=matrix, include_k8_table=False)
        report_path_invalid = self._create_report(md_invalid)
        linter_invalid = CrucibleLinter(report_path_invalid, source_path=source_path, allow_localized=True)
        res_invalid = linter_invalid.validate()
        self.assertFalse(res_invalid.passed)
        self.assertTrue(any("UNVERIFIED QUOTE" in e for e in res_invalid.errors))

    def test_v7_passive_block_collision_prevented(self):
        """v7.2 Hardening: Generic words (e.g. 'tarihsel') in passive layer descriptions do not remove other active layers."""
        triage_text = """
* **Aktif Katmanlar:**
  * **K1 (Persona):** AKTİF
  * **K8 (Tarihsel Kaynak Tenkiti):** AKTİF
* **Pasif Katmanlar:**
  * **K5 (Deneysel Nedensellik):** DIŞLANDI. Kültürel makro-tarihsel süreçler laboratuvara sokulamaz.
"""
        md = make_valid_document(triage_extra=triage_text)
        report_path = self._create_report(md)
        linter = CrucibleLinter(report_path)
        result = linter.validate()
        self.assertIn("K8", result.active_layers, "K8 should remain active despite 'tarihsel' appearing in K5 passive explanation!")
        self.assertNotIn("K5", result.active_layers)

    def test_v7_all_layer_artifacts_coverage(self):
        """v7.2 Hardening: All 10 normative layers are covered in LAYER_ARTIFACTS."""
        from crucible_linter import LAYER_ARTIFACTS
        expected_layers = {'K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10'}
        self.assertEqual(expected_layers, set(LAYER_ARTIFACTS.keys()))

    # ────────────────────────────────────────────────────────────────
    # v7.3 Hardening Tests (L1-L4)
    # ────────────────────────────────────────────────────────────────

    def test_v73_l1_backtick_and_markdown_quote_wrappers(self):
        """v7.3 L1: Fabricated quotes with backticked `[P:x]` and italics cannot bypass quote verification."""
        source_text = "Randomized controlled trials demonstrated no convincing effects of the depletion intervention."
        source_path = self._create_report(source_text)

        matrix = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Depletion result | Randomized controlled trials | Primary Data | Verified |
"""
        # 1. Valid backticked verbatim quote passes
        valid_steelman = (
            'The authors construct their primary empirical claim in this section through rigorous comparison '
            'and summarize the core experimental result cleanly without distortion across all included clinical samples:\n\n'
            '* *Verbatim Citation:* *"no convincing effects of the depletion intervention"* `[P:0001]`.\n'
            'Further dialectical premises remain internally coherent across every proposition examined in this review.'
        )
        res_valid = CrucibleLinter(
            self._create_report(make_valid_document(steelman_text=valid_steelman, extra_sections=matrix, include_k8_table=False)),
            source_path=source_path,
            allow_localized=True,
        ).validate()
        self.assertTrue(res_valid.passed, f"Valid backticked quote failed unexpectedly: {res_valid.errors}")

        # 2. Inverted / fabricated quote with backticks and blockquote must FAIL
        bad_steelman = (
            'The authors supposedly summarize their experimental trial findings while constructing an argument '
            'and report an inverted empirical claim that reverses the original source wording across clinical subjects:\n\n'
            '> *"Randomized controlled trials demonstrated mood reducing effects of the depletion intervention"* `[P:0001]`.\n'
            'Further dialectical premises remain internally coherent across every proposition examined in this review.'
        )
        res_bad = CrucibleLinter(
            self._create_report(make_valid_document(steelman_text=bad_steelman, extra_sections=matrix, include_k8_table=False)),
            source_path=source_path,
            allow_localized=True,
        ).validate()
        self.assertFalse(res_bad.passed)
        self.assertTrue(any("UNVERIFIED QUOTE" in e for e in res_bad.errors), f"Expected UNVERIFIED QUOTE, got: {res_bad.errors}")

    def test_v73_l2_triage_data_row_does_not_trigger_k8_matrix(self):
        """v7.3 L2: Triage row containing 'Claim' and 'Source' must not hijack in_matrix state."""
        source_text = "Original Text presents clear historical evidence in the primary corpus."
        source_path = self._create_report(source_text)

        triage_with_claim_and_source = """
### Layer Matrix
| Layer | Status | Justification |
|---|---|---|
| **K1: Persona & Virtue** | ✅ ACTIVE | Baseline philosophical honesty enforced. |
| **K8: Disciplinary Matrix & Source Criticism** | ✅ ACTIVE | Audit claim-to-source fidelity in the corpus. |
| **K10: Complexity & Epistemic Post-Mortem** | ✅ ACTIVE | Damage report and checklist active. |
"""
        matrix = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Historical proposition | Original Text | Primary Source | Grounded |
"""
        extra = "\n## EXTRA PROTOCOL\nDamage report checklist verified with clinical boundaries.\n"
        # Build custom report overriding default triage
        md = make_valid_document(include_k8_table=False, extra_sections=matrix + extra)
        md = md.replace(
            "| **K8: Disciplinary Matrix** | ✅ ACTIVE | Interdisciplinary source and textual criticism applied. |",
            "| **K8: Disciplinary Matrix & Source Criticism** | ✅ ACTIVE | Audit claim-to-source fidelity across cited works. |\n| **K10: Complexity** | ✅ ACTIVE | Damage report and ethical boundary assessment applied. |",
        )
        res = CrucibleLinter(self._create_report(md), source_path=source_path, allow_localized=True).validate()
        self.assertTrue(res.passed, f"Triage K8 data row leaked into matrix parser: {res.errors}")
        self.assertTrue(res.grounded)

    def test_v73_l3_triage_conflict_and_range_bounds(self):
        """v7.3 L3: Contradictory 'Layer 10' keeps K10 active with warning; invalid [P:x-y] ranges fail."""
        source_text = "First paragraph evidence.\n\nSecond paragraph evidence."
        source_path = self._create_report(source_text)

        triage_conflict = """
### 1.1. Active Normative Layers
* **Layer 10 (Damage Report & Epistemic Autopsy):** ✅ ACTIVE. Mandatory closing audit.

### 1.2. Excluded Normative Layers
* **Layer 10 (Macro Complex Systems):** ⛔ EXCLUDED. No formal dynamical equations used.
"""
        steelman_range_oob = (
            "The author argues with clear premises and cites out-of-bounds range [P:0001–0099] "
            "while examining first and second paragraphs thoroughly."
        )
        md = make_valid_document(triage_extra=triage_conflict, steelman_text=steelman_range_oob)
        res = CrucibleLinter(self._create_report(md), source_path=source_path, allow_localized=True).validate()
        self.assertIn("K10", res.active_layers, "Layer 10 must remain active when explicitly declared ACTIVE before partial exclusion")
        self.assertTrue(any("TRIAGE CONFLICT" in w and "K10" in w for w in res.warnings))
        self.assertFalse(res.passed)
        self.assertTrue(any("INVALID PARAGRAPH INDEX" in e for e in res.errors), f"Expected out-of-bounds range error, got: {res.errors}")

    def test_v73_l4_shallow_k4_quantitative_audit_warning(self):
        """v7.3 L4: Active K4 on a quantitative source without concrete extracted statistics emits SHALLOW K4 AUDIT."""
        source_text = (
            "Trial cohort enrolled N = 1,250 participants. Primary outcome showed OR = 1.02, p = 0.78, "
            "95% CI [0.89, 1.17] with 42.5% follow-up response across groups."
        )
        source_path = self._create_report(source_text)

        triage_k4 = "\n| **K4: Statistics & Bayes** | ✅ ACTIVE | Inspect posterior probabilities and sample sizes. |\n"
        # Prose-only body mentioning Bayes/prior without citing a single number from the quantitative source
        prose_only_fals = (
            "In this section we evaluate Bayesian prior and posterior beliefs conceptually. "
            "Sample size and confidence interval considerations are weighed qualitatively against confirmation biases."
        )
        matrix = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Trial claim | Trial cohort | Primary Data | Checked |
"""
        md_shallow = make_valid_document(
            triage_extra=triage_k4,
            falsification_text=prose_only_fals,
            include_k8_table=False,
            extra_sections=matrix,
        )
        res_shallow = CrucibleLinter(self._create_report(md_shallow), source_path=source_path, allow_localized=True).validate()
        self.assertTrue(any("SHALLOW K4 AUDIT" in w for w in res_shallow.warnings),
                        f"Expected SHALLOW K4 AUDIT warning, got: {res_shallow.warnings}")

        # Strict mode escalates SHALLOW K4 AUDIT to hard error
        res_strict = CrucibleLinter(self._create_report(md_shallow), source_path=source_path, strict=True, allow_localized=True).validate()
        self.assertFalse(res_strict.passed)
        self.assertTrue(any("SHALLOW K4 AUDIT" in e for e in res_strict.errors))

        # Quantitative body extracting real numbers passes with zero shallow-K4 warning
        quant_fals = prose_only_fals + " Specifically, cohort N = 1,250 yielded OR = 1.02 (95% CI [0.89, 1.17], p = 0.78)."
        md_quant = make_valid_document(
            triage_extra=triage_k4,
            falsification_text=quant_fals,
            include_k8_table=False,
            extra_sections=matrix,
        )
        res_quant = CrucibleLinter(self._create_report(md_quant), source_path=source_path, allow_localized=True).validate()
        self.assertFalse(any("SHALLOW K4 AUDIT" in w for w in res_quant.warnings),
                         f"Unexpected SHALLOW K4 AUDIT warning on quantitative report: {res_quant.warnings}")

    def test_v73_l5_anchored_audit_cockpit_before_triage_passes(self):
        """v7.3 L5: An anchored Audit Cockpit box above H2 Triage passes with zero triage/header leaks."""
        source_text = "Randomized trial enrolled N = 1,250 participants demonstrating no primary effect (OR = 1.00, p = 0.95)."
        source_path = self._create_report(source_text)

        cockpit_header = (
            "> **Audit Cockpit (Navigation Index — Not Independent Proof):**\n"
            "> - **Primary Verdict Anchor:** No effect found (`OR = 1.00, p = 0.95`, `N = 1,250`) `[P:0001]`.\n"
            "> - **Top Fracture Pointer:** Check quantitative metric extraction against K4 rules below.\n\n"
        )
        fals_quant = (
            "Here we evaluate Popperian falsification criteria, statistical power, and empirical disclosures. "
            "Trial reported N = 1,250 with OR = 1.00 (p = 0.95), confirming null primary findings reliably."
        )
        matrix = """
## CLAIMS-SOURCE AUDIT MATRIX
| Thesis / Claim | Primary Source | Source Status | Methodological Verdict |
|---|---|---|---|
| Trial claim | Randomized trial | Primary Data | Confirmed null |
"""
        md = make_valid_document(
            falsification_text=fals_quant,
            include_k8_table=False,
            extra_sections=matrix,
        ).replace(
            "| **K4: Statistics & Bayes** | ⛔ EXCLUDED | No quantitative data sets or clinical trials available in text. |",
            "| **K4: Statistics & Bayes** | ✅ ACTIVE | Inspect OR and p-value metrics. |"
        ).replace("*Analyst: Persona V6.0*", f"*Analyst: Persona V7.2*\n\n{cockpit_header}")

        res = CrucibleLinter(self._create_report(md), source_path=source_path, allow_localized=True).validate()
        self.assertTrue(res.passed, f"Audit Cockpit triggered unexpected linter errors: {res.errors}")
        self.assertEqual(len(res.warnings), 0, f"Audit Cockpit triggered unexpected warnings: {res.warnings}")

    def test_v73_empty_primary_source_fails(self):
        """v7.3 Hardening: An empty or 0-paragraph --source document must FAIL rather than skip grounding."""
        empty_source = self._create_report("   \n\n   ")
        md = make_valid_document()
        res = CrucibleLinter(self._create_report(md), source_path=empty_source, allow_localized=True).validate()
        self.assertFalse(res.passed)
        self.assertFalse(res.grounded)
        self.assertTrue(
            any("EMPTY PRIMARY SOURCE" in e for e in res.errors),
            f"Expected EMPTY PRIMARY SOURCE error, got: {res.errors}",
        )


if __name__ == '__main__':
    unittest.main()
