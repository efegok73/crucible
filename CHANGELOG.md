# Changelog

All notable changes to the CRUCIBLE framework will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [7.2.0] - 2026-11-21

### Fixed & Hardened (Adli Reçete Uygulaması)
- **Paragraf Sınır Aşımı Sertleştirmesi (`[P:xxxx]`)** — Metinde olmayan veya toplam paragraf sayısını aşan indeksler (`p_idx > max_para` veya `p_idx <= 0`) uyarıdan derlemeyi durduran kesin hataya (`[FAIL: INVALID PARAGRAPH INDEX]`) dönüştürüldü.
- **Akademik Sayfa Referansı Temizliği** — K8 İddia-Kaynak matrisinde yer alan `[Sayfa 116]`, `[p. 45]`, `[pp. 12-14]` gibi editoryal referanslar otomatik temizlenerek yapay hayalet referans (`[FAIL: UNGROUNDED ARTIFACT]`) hataları önlendi.
- **Alıntı Doğrulama ve Blok Pasaj Genişletmesi** — Alıntı doğrulama aralığı `15-600` karaktere genişletildi; markdown blok alıntıları (`> [P:xxxx] "..."`) için tam tırnak ve paragraf doğrulama desteği getirildi.
- **PyMuPDF (`fitz`) Öncelikli Yükleyici** — `load_source` ve `index_source.py` içine PyMuPDF entegre edilerek AES şifreli ve karmaşık dizgili PDF'lerin hasarsız ve bağımlılık hatası üretmeden okunması sağlandı (pypdf/PyPDF2 fallback olarak korundu).
- **Çok Dilli Akademik Stop-Words Kümesi** — Latince, Almanca ve Fransızca yaygın akademik bağlaç ve edatlar (`et`, `in`, `de`, `ad`, `und`, `der`, `die`, `das`, `le`, `la`, `les` vb.) eklenerek yabancı dildeki kaynak denetimlerinde sahte hayalet referans alarmları engellendi.
- **Triyaj Pasif Blok Kapsam İzolasyonu** — Dışlanan bir katmanın açıklamasında geçen genel terimlerin (ör. K5 pasif satırında geçen `tarihsel` kelimesi) aktif K8 katmanını sessizce silmesi engellendi; satır bazlı hedef katman tespiti getirildi.
- **Tüm Katmanlar İçin Kanıt İmzası (`LAYER_ARTIFACTS`)** — K2, K3, K6, K7, K9, K10 katmanları için tanımlayıcı belirteçler eklenerek 10 katmanın tamamı linter denetim ağına alındı.
- **Tek Doğruluk Kaynağı (`benchmark_extractor.py`)** — Heuristik 200 karakterlik katman sayacı kaldırılarak doğrudan `CrucibleLinter` sınıfına bağlandı; M1 katman sayımı deterministik hale getirildi.
- **Yekpare Sürüm ve Yol Senkronizasyonu** — `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, `LIMITATIONS.md` ve şablonlar tek bir `v7.2` standardında eşitlendi; hayalet yerel yollar bağımsız repo yapısına uyarlandı.
- **Genişletilmiş Birim Testleri** — `test_crucible_linter.py` süitine 5 yeni adli güvenlik testi eklendi (toplam 24 test, %100 PASS).

## [7.1.0] - 2026-11-20

### Fixed & Hardened
- **Hayalet Referans AND Mantığı (Linter Güvenliği)** — K8 matrisinde tek kelimelik gevşek `OR` eşleşmesi kaldırılarak, uydurma kaynakların (`Tamamen Hayali Selme Kodeksi`) tek bir kelime üzerinden linter'ı delmesi engellendi; çoklu token `AND` eşiği getirildi.
- **Tablo Durum Sızıntısı İzolasyonu (`in_matrix` Bug'ı)** — Markdown tabloları satır satır izole edilerek, K8 matrisinden sonraki bölümlerde (Hasar Raporu, Cerrah Kartı vb.) yer alan tabloların K8 zannedilmesi ve meşru raporların haksız yere `[FAIL: UNGROUNDED ARTIFACT]` alması önlendi.
- **Doğrudan PDF Desteği** — `crucible_linter.py` motoruna `pypdf`/`PyPDF2` entegre edilerek `.pdf` kaynak metinlerinin ikili akış olarak çökmesi engellendi; yerel PDF'ler doğrudan zemin metin olarak desteklendi.
- **Türkçe Karakter Desteği (`tr_lower`)** — Standart Python `.lower()` dönüşümünün ürettiği `İ/I` harf anomalisi giderildi; Türkçe kaynaklardaki terimlerin sessizce eşleşme hatası vermesi önlendi.
- **Alıntı Doğrulamasında Paragraf Yakınlığı ve Kesme İşareti Tamiri** — Tırnak içi alıntıların kesme işaretleriyle (`Zuhayr'ın`, `author's`) kırılması önlendi, alıntının beyan edilen `[P:xxxx]` paragrafında (±1 komşu aralığında) bulunması denetlendi; paragraf kayması uyarıları eklendi.
- **Koşulsuz Mühür Düzeltmesi** — Kaynak verilip doğrulanmadığında veya kısmi kaldığında mühre otomatik "Sıfır Hayalet Referans" yazılması engellendi; sadece 100% zemin doğrulamasından geçen raporlara tam onay damgası verildi.

### Added
- **Deterministik Paragraf İndeksleyici (`scripts/index_source.py`)** — `.pdf`, `.docx`, `.txt`, `.md` birincil metinlerini `crucible_linter.py` ile birebir aynı kurallarla `[P:0001]...` formatında indeksleyen CLI aracı eklendi.
- **Dinamik Benchmark Denetimi** — `scripts/benchmark_extractor.py` dosyasındaki sabitlenmiş `✅ PASS` kaldırılarak gerçek linter motoru entegre edildi; safsata sayımına olumsuzlama/kaçınma filtresi getirildi.
- **Genişletilmiş Birim Testleri** — `scripts/test_crucible_linter.py` süitine 4 yeni güvenlik testi eklendi (toplam 16 test, %100 PASS).
- **CI/CD Birim Test Entegrasyonu** — GitHub Actions (`ci.yml`) iş akışına `test_crucible_linter.py` testi ve `requirements.txt` bağımlılık kurulumu eklendi.

### Deprecated & Cleaned
- **20-25 Sayfa Atomizasyon Fiyaskosu İptali** — 1M+ bağlam pencereli modellerde bağlam bütünlüğünü imha eden iki aşamalı Target Dossier boru hattı (`05_TWO_STAGE...`) metodolojik olarak feshedildi ve otopsi şerhiyle arşivlendi.
- **Zombi Dosya Temizliği** — `config/` altındaki 2 Ekim tarihli kopyalanmış eski `.cursorrules`, `AGENTS.md` ve `CLAUDE.md` dosyaları kaldırıldı.

## [7.0.0] - 2026-10-30

### Added
- **Grounded Source Cross-Checking Engine (`--source`)** — Deterministik linter artık birincil kaynak belgesini (`.docx`, `.txt`, `.md`) doğrudan okuyarak rapordaki iddiaları zemin metinle doğrular.
- **Sıfır Hayalet Referans Kalkanı (Zero-Hallucination Guard)** — K8 İddia-Kaynak matrisinde yer alan birincil nesnelerin kaynak belgede fiilen var olup olmadığını denetler. Metinde bulunmayan ve `[DIŞ KAYNAK]` etiketi taşımayan hayalet referanslarda derleme anında `[FAIL: UNGROUNDED ARTIFACT]` ile durdurulur.
- **Paragraf Çıpası ve Tırnak İçi Alıntı Doğrulaması (`[P:xxxx]`)** — Raporda tırnak içinde verilen doğrudan alıntıların birincil kaynak metinde kelimesi kelimesine var olduğunu deterministik olarak doğrular. Uydurma alıntılar `[FAIL: UNVERIFIED QUOTE]` ile engellenir.
- **Epistemik İndeks ve Yapı Haritası Protokolü (Registry Protocol)** — v6.0'ın metnin %97'sini silerek bağlam atomizasyonuna ve saman adam üretimine yol açan kayıplı "Hedef Tahtası" özeti kaldırıldı; yerine metni yok etmeden paragraf kütüğü çıkaran v7 İndeks formatı getirildi.
- **Şeytanın Savunmanı Filtresi (Adversarial Defense / Anti-Strawman)** — Yazarın kendi metninde zaten tartıştığı veya şerh düştüğü hususların modele "yeni kusur" gibi atfedilmesini engelleyen zorunlu karşı-denetim kuralı.
- **v7.0 Zemin Çıpalı Mühür** — Derlenen HTML raporlarına birincil kaynak adı, paragraf sayısı ve sıfır hayalet referans tescilini içeren yeşil mühür damgası.
- **Yeni Birim Testleri** — `scripts/test_crucible_linter.py` dosyasına kaynak zemin doğrulamasını, hayalet referans yakalamayı, dış kaynak istisnalarını ve alıntı kontrolünü test eden 4 yeni birim test eklendi (toplam 12 test).

## [6.0.0] - 2026-10-04

### Added

- **10-Layer Normative Architecture (v6)** — Complete epistemic auditing gauntlet with dynamic triage matrix for multi-disciplinary academic analysis.
  - L1: Epistemic Virtue & Sycophancy Filter
  - L2: Steelmanning & Dialectical Reconstruction
  - L3: Hermeneutics & Lexical Hygiene
  - L4: Bayesian Probabilities & Statistical Triaging
  - L5: Experimental Design, Counterfactuals & Confounders
  - L6: Systematic Review & Evidence Hierarchies
  - L7: Game Theory & DMDU Decision Science
  - L8: Historical & Archival Source Criticism
  - L9: Computational Simulation & Agent-Based Models
  - L10: Auto-Falsification & Epistemic Damage Report
- **Deterministic Python Linter** (`scripts/crucible_linter.py`) — Validates report structural compliance, rhetorical hygiene, and dynamic triage integrity before sealing.
- **9 Showcase Monographies** — Stress-tested across 5 academic disciplines (Philosophy, Psychoanalysis, Clinical Epidemiology, Historiography, Climatology). Available in English and Turkish (`showcase/en/`, `showcase/tr/`).
- **9 Benchmark Target Dossiers** (`benchmarks/en/`) — Structured evidence packages for reproducible auditing.
- **Two-Stage Extraction Protocol** — Decoupled pipeline: Stage 1 (Target Dossier Extraction) → Stage 2 (Crucible Forensic Audit). Prevents smoothing error and pipeline collapse.
- **Linguistic Asymmetry Documentation** (`docs/en/03_…`, `04_…`, `05_…`) — Empirical analysis of transformer tokenization bottlenecks in agglutinative languages.
- **Dual Operating Pathways** — Path A (Web/Cloud: Gemini, Claude, ChatGPT) and Path B (Agentic IDE: Antigravity, Cursor, Claude Code).
- **Template Files** — `CRUCIBLE_EXTRACTION_DIRECTIVE.md` and `CRUCIBLE_WEB_PROMPT_EN.md` for immediate deployment.
- **GitHub Actions CI** (`.github/workflows/ci.yml`) — Automated linter validation on push and PR.
- **Multi-agent constitution files** — `.cursorrules`, `AGENTS.md`, `CLAUDE.md` for IDE-native deployment.
- **MIT License** for open-source distribution.
- **README** in English and Turkish (`README.md`, `README_TR.md`).

### Changed

- N/A (initial open-source release).

### Fixed

- N/A (initial open-source release).

### Known Limitations

- Dense mathematical formalism (pure theorem proofs) may exceed analytical capacity.
- Single-session processing of 400+ page manuscripts risks pipeline collapse; two-stage decoupling is mandatory.
- Agglutinative language tokenization (e.g., Turkish) degrades analytical resolution by ~50% compared to English-native execution.
- Model weight updates by AI providers can silently alter CRUCIBLE performance; cross-model validation is recommended.

[6.0.0]: https://github.com/efegok73/crucible/releases/tag/v6.0.0
