# ⚖️ CRUCIBLE (Mayın Tarlası Modeli v6.0) — TÜRKÇE KILAVUZ

**Yapay zekâyı diplomatik bir özetçiden acımasız bir bilimsel hakeme dönüştüren açık kaynak çerçeve.**

[![Lisans: MIT](https://img.shields.io/badge/Lisans-MIT-blue.svg)](LICENSE)
[![Versiyon](https://img.shields.io/badge/Versiyon-6.0-emerald.svg)](CHANGELOG.md)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-informational.svg)](https://www.python.org/)

> *Uluslararası Açık Kaynak Adı:* ***CRUCIBLE*** *| Özgün Kurucu Mimari:* ***Mayın Tarlası*** *(Gizli varsayımların ya sınandığı ya da havaya uçtuğu diyalektik stres testi arazisi)*

🌐 **English version:** [`README.md`](README.md)

---

## CRUCIBLE Nedir?

CRUCIBLE, ticari yapay zekâ modellerini (ChatGPT, Claude, Gemini) **sistematik ve acımasız bilimsel denetçilere** dönüştüren açık kaynaklı bir istem (prompt) çerçevesidir.

Normal bir yapay zekâya *"Bu makaleyi incele"* dediğinizde size nazik, tarafsız görünümlü bir özet verir: her iki tarafı da haklı bulur, yazara pohpohlayıcı ifadeler kullanır, eleştirileri "*bazı sınırlılıklar mevcuttur*" gibi boş cümlelerle kapatır. Buna akademik literatürde **sycophancy** (dalkavukluk önyargısı) denir ve yapay zekâyı ciddi araştırma değerlendirmesi için kullanılmaz hale getirir.

CRUCIBLE bu sorunu çözer: Aynı modeli, çalışma zamanında (inference time) 10 katmanlı analitik bir anayasa ile kuşatır. Model ağırlıkları değiştirilmez, API anahtarı gerekmez, fine-tuning yapılmaz. Sadece doğru talimatlarla doğru sırada çalıştırılır.

**Bu kimin için?**
- Bir makaleyi, tezi veya kitabı — **kendi eseri dahil** — acımasızca denetletmek isteyen araştırmacılar.
- Tez savunmasından önce zayıf noktalarını bulmak isteyen öğrenciler.
- Bilim gazetecileri ve politika analistleri.
- Yapay zekânın kendisine hep hak vermesinden bıkmış herkes.

---

## Sorun Nedir? CRUCIBLE Ne Fark Yaratır?

### Standart bir yapay zekâya "bu kitabı analiz et" dediğinizde:

> *"Butler'ın Gender Trouble eseri feminist teoriyi derinden etkileyen çığır açıcı bir çalışmadır. Bazı metodolojik sorular gündeme gelse de, yazar toplumsal cinsiyetin performatif doğasına ilişkin ikna edici bir argüman ortaya koymaktadır..."*

Bu bir **kitap tanıtım yazısı**, analiz değil. Hiçbir somut kusuru göstermiyor.

### Aynı kaynak materyale CRUCIBLE uygulandığında:

> **[Katman 3 — Hermenötik Denetim]:** "Performativite" kavramı, Bölüm 1–3 arasında birbiriyle çelişen üç farklı anlamda kullanılıyor: (a) baskı altında zorunlu norm tekrarı, (b) Nietzsche'ci neden-sonuç ters çevirimi (metalepsis), (c) Austin'ci söz-edim türevi. Bu belirsizlik, yazarın güçlü ontolojik iddiası sorgulandığında zayıf epistemolojik okumaya çekilmesini sağlayan bir *motte-and-bailey* yapısı oluşturuyor.
>
> **[Katman 8 — Kaynak Tenkiti Matrisi]:**
>
> | İddia | Birincil Kaynak | Kaynak Türü | Hüküm |
> |:---|:---|:---|:---|
> | Biyolojik cinsiyet söylemsel olarak inşa edilmiştir | Foucault, *Cinselliğin Tarihi* Cilt 1 | Post-yapısalcı söylem analizi | **Vekil Sıçraması:** "Dil, anatomiyi tanımlar" iddiasından "anatominin kendisi kültürel bir yapıdır" sonucuna dayanaksız geçiş |
>
> **[Katman 10 — Oto-Falsifikasyon]:** Bu denetimin kendi analizi, değerlendirme ölçütü olarak ağırlıklı olarak Anglo-Amerikan analitik bilim felsefesine dayanıyor; bu durum, Kıta felsefesi geleneğinin kendine özgü epistemolojik taahhütlerini sistematik olarak hafife alma riski taşıyor...

*— [Vaka 01: Judith Butler – Gender Trouble](showcase/tr/01_Judith_Butler_Report.html) raporundan yoğunlaştırılmış alıntı*

---

## Hızlı Başlangıç

### ⚡ 10 Saniyelik Önizleme (Hazır Rapor İncelemesi)
Hiçbir şey kurmadan CRUCIBLE'ın nasıl bir çıktı ürettiğini hemen görmek için:  
👉 [**Judith Butler – Gender Trouble Mühürlü Raporunu Açın (HTML)**](showcase/tr/01_Judith_Butler_Report.html) veya tüm [9 Doğrulanmış Benchmark Vakasını](#9-doğrulanmış-benchmark-vakası) inceleyin.

---

### 🌐 Yol A: Web ve Tarayıcı Kullanıcıları (Kodlama Bilgisi Gerekmez)

**Claude.ai**, **ChatGPT Plus** veya **Gemini Advanced** arayüzünde 3 basit adımda kendi makalenizi denetleyin:

> 📌 **Neden 2 Aşama?** 400 sayfalık bir kitabı modele tek bir *"bunu özetle"* komutuyla verirseniz, model diplomatik ve yüzeysel bir özete sıkışır (*smoothing error*). Bu yüzden önce ham kanıtları çıkarır, ardından denetimi başlatırız.

1. **Adım 1 — Kanıtları Çıkarın (Hedef Tahtası):**
   - [`templates/CRUCIBLE_EXTRACTION_DIRECTIVE_TR.md`](templates/CRUCIBLE_EXTRACTION_DIRECTIVE_TR.md) şablonunu açıp metnini kopyalayın.
   - Claude veya ChatGPT sohbetine yapıştırın ve denetlemek istediğiniz PDF veya metni ekleyin.
   - Model; yazarın iddia, veri ve alıntılarını yorum katmadan ham bir **Hedef Tahtası (Target Dossier)** listesi *(editoryal yorumdan arındırılmış saf iddia dökümü)* olarak çıkarır.

2. **Adım 2 — Denetim Anayasasını Çalıştırın:**
   - [`templates/CRUCIBLE_WEB_PROMPT_TR.md`](templates/CRUCIBLE_WEB_PROMPT_TR.md) şablonunu açıp anayasa metnini kopyalayın.
   - Aynı sohbette modele şunu yazıp şablonu yapıştırın:  
     *"1. Aşamada çıkardığın Hedef Tahtasını şimdi bu CRUCIBLE kurallarıyla acımasızca denetle."*

3. **Adım 3 — Adli Raporunuzu Alın:**
   - Model pohpohlamayı bırakır; epistemolojik triyaj yapar, iddiaları çelik adam (steelman) olarak yeniden kurar, kaynak tenkiti tablosunu döker ve kendi analitik sınırlarını itiraf eden bir **Oto-Falsifikasyon & Cerrah Kartı** üretir.

> 💡 **Kalıcı Çalışma Odası İpucu:** Claude.ai Projects veya Gemini Gems kullanıyorsanız, `docs/` ve `templates/` klasöründeki dosyaları proje hafızasına (Knowledge Base) tek seferde yükleyin; her yeni makale eklediğinizde sistem otomatik denetçiye dönüşür.

---

### 💻 Yol B: IDE ve Ajan Kullanıcıları (Antigravity, Cursor, Claude Code)

Geliştiriciler ve terminal kullanıcıları için tam otomatik boru hattı:

1. **Depoyu klonlayın ve açın:**
   ```bash
   git clone https://github.com/efegok73/crucible.git
   cd crucible
   ```
   *(Proje anayasaları `.cursorrules`, `AGENTS.md` ve `CLAUDE.md` ajanınız tarafından otomatik tanınır).*

2. **Ajanınıza tek komut verin:**
   > *"@templates/CRUCIBLE_EXTRACTION_DIRECTIVE_TR.md kurallarıyla @makale.pdf dosyasının hedef tahtasını çıkar, ardından CRUCIBLE metodolojisiyle analiz edip scripts/crucible_linter.py ile doğrula."*

3. **Mühürlü Raporunuzu Alın:**  
   Ajan analizi tamamlar, arka planda Python linter'ını çalıştırıp `[PASS]` alır ve yayına hazır `[Rapor_Adi].html` dosyasını üretir. Size sadece tarayıcınızda açıp incelemek kalır.

> 🛠️ **Manuel / CI Doğrulaması (İsteğe Bağlı):** Ajan kullanmıyorsanız veya raporu kendiniz elle denetlemek isterseniz:
> ```bash
> pip install markdown
> python scripts/crucible_linter.py showcase/tr/01_Judith_Butler_Report.md
> ```

---

## 🧠 Model Yetkinlik Eşiği (Hangi Modeller Gerekir?)

CRUCIBLE sıradan bir sohbet botu değil, adli bir bilimsel hakemlik protokolüdür. 10 normatif katmanı, hermenötik ayrıştırmayı ve kaynak tenkiti tablolarını işletebilmek yüksek akıl yürütme (reasoning) ve geniş bağlam penceresi gerektirir:

| Seviye | Modeller | Durum & Öneri |
|:---|:---|:---|
| 🟢 **Doğrulanmış & Önerilen (Frontier)** | **Claude 3.5 Sonnet / Opus**, **GPT-4o / o1**, **Gemini 1.5 Pro** | **Tam uyum.** 10 katmanı ve linter standartlarını eksiksiz işletir. |
| 🟡 **Ücretsiz Yüksek Kapasite** | **Google AI Studio (Gemini 1.5 Pro)** | **Sıfır abonelik ücreti.** 2M token bağlamında, uzun makale ve kitaplar için en güçlü ücretsiz çıkış kapısı. |
| 🔴 **Yetersiz / Desteklenmeyen (Küçük Modeller)** | **GPT-4o-mini**, **Claude Haiku**, **Llama-3-8B** | **Önerilmez.** Talimatları unutur, özetleme refleksine (*smoothing error*) çöker. |

---

## ⚠️ Uymanız Gereken 3 Kural

1. **Her zaman iki aşama kullanın.** Yüzlerce sayfalık bir kitabı tek bir "bunu incele" komutuyla modele boca etmek, analizi 18 KB'lik yüzeysel bir özete sıkıştırır (*smoothing error*). Veri çıkarımını analizden ayırın.

2. **Dili kaynağa uydurun.** İngilizce bir bilimsel makaleyi inceletiyorsanız, analizi İngilizce yaptırın. Türkçe gibi morfolojik olarak karmaşık dillerde analiz yaptırmak, tokenizasyon darboğazı nedeniyle analitik derinliğin ~%50'sini kaybettirir. Gerekiyorsa mühürlü raporu sonradan Türkçeye çevirin. ([Kanıt](docs/tr/03_DILSEL_SUBSTRAT_ASIMETRISI_VE_LLM_ANALIZ_DERINLIGI.md))

3. **Çapraz model doğrulaması yapın.** Yapay zekâ sağlayıcıları model ağırlıklarını sessizce günceller. Bugün 10 katmanı kusursuz işleten bir model gelecek hafta çökebilir. Kritik analizleri en az 2 farklı modelde çalıştırın.

---

## Nasıl Çalışır? 10 Normatif Katman

CRUCIBLE her metinde 10 katmanın hepsini çalıştırmaz. Dinamik bir **Epistemolojik Triyaj Matrisi**, kaynak materyalin disiplinine göre ilgili katmanları aktive eder:

| Katman | İşlev | Ne Zaman Aktif? |
|:---:|:---|:---|
| **K1** | **Epistemik Erdem** — Duygusal retoriği filtreler, entelektüel alçakgönüllülüğü zorlar | Her zaman |
| **K2** | **Çelik Adam (Steelmanning)** — Tezi eleştirmeden önce en güçlü akademik formda yeniden kurar | Her zaman |
| **K3** | **Hermenötik Hijyen** — Anlamsal kaymalar, çift anlamlılıklar, kavram enflasyonu | Felsefe, sosyal bilim |
| **K4** | **İstatistik ve Bayes** — Örneklem büyüklükleri, etki büyüklükleri, p-hacking, öncül dağılımlar | Ampirik bilimler, tıp |
| **K5** | **Deneysel Tasarım ve Nedensellik** — Karıştırıcılar, ters nedensellik, çarpıştırıcı sapması (DAG) | Klinik çalışmalar, epidemiyoloji |
| **K6** | **Kanıt Hiyerarşisi** — AMSTAR-2, GRADE standartları; tekil anekdotları eler | Sistematik derlemeler |
| **K7** | **Karar Bilimi ve Risk (DMDU)** — Kalın kuyruk riskleri, ters risk tradeoff'ları | Politika analizi, iklim bilimi |
| **K8** | **Tarihsel Kaynak Tenkiti** — Birincil kaynak üçgenlemesi; İddia-Kaynak Matrisi zorunlu | Tarih yazımı, arşiv araştırması |
| **K9** | **Hesaplamalı Model Denetimi** — Aşırı öğrenme, doğrulama sızıntısı, parametre ayarı | Simülasyonlar, makine öğrenmesi |
| **K10** | **Oto-Falsifikasyon ve Cerrah Kartı** — Model kendi kör noktalarını itiraf eder; 3 dakikalık insan doğrulama listesi sunar | Her zaman |

Analiz tamamlandıktan sonra çıktı, **deterministik bir Python linter** ([`crucible_linter.py`](scripts/crucible_linter.py)) tarafından doğrulanır. Yapısal bütünlük, triyaj tutarlılığı ve retorik hijyen kontrol edilir. Testi geçemeyen raporlar reddedilir.

---

## 9 Doğrulanmış Benchmark Vakası

Her rapor deterministik linter'dan geçmiş ve hem İngilizce hem Türkçe olarak mevcuttur:

| # | Disiplin | İncelenen Eser | Bulunan Temel Zafiyet | Hüküm |
|:---:|:---|:---|:---|:---:|
| 01 | Felsefe ve Cinsiyet | **Judith Butler** — *Gender Trouble* (1990) | "Performativite"de anlamsal kaçak; epistemolojiden ontolojiye dayanaksız sıçrama | Ağır Revizyon |
| 02 | Psikanaliz | **Jacques Lacan** — *Seminaire XX* (1975) | Formel doğrulaması olmayan sahte-matematiksel topoloji (mathemeler) | Ağır Revizyon |
| 03 | Klinik Epidemiyoloji | **Hilary Cass** — *The Cass Review* (2024) | Gözlemsel pediatrik kohort verisine orantısız RCT eşiği | Kısmi Revizyon |
| 04 | Tarih Yazımı | **Cheikh Anta Diop** — *The African Origin* (1974) | Anakronik ırk kategorileri; sahte dilsel eşseslilikler | Reddedildi |
| 05 | Klasik Filoloji | **Frank M. Snowden Jr.** — *Blacks in Antiquity* (1970) | Greko-Romen fizyognomik önyargının hafife alınması | Kısmi Revizyon |
| 06 | Bibliyometri | **Cook et al. vs. Tol** — *%97 İklim Konsensüsü* (2013) | Payda manipülasyonu (%66.4 nötr makale dışlanmış) | Ağır Revizyon |
| 07 | İklim Bilimi | **Judith Curry** — *Climate Uncertainty* (2023) | Okyanus iç salınım iddiaları vs. gözlenen net enerji dengesizliği | Ağır Revizyon |
| 08 | Psikiyatri ve KTT | **Joanna Moncrieff et al.** — *Serotonin Theory* (2022) | Aspirin Safsatası: etiyolojik ilgisizlikten klinik etkinsizlik türetme | Ağır Revizyon |
| 09 | Evrimsel Psikoloji | **Simon Baron-Cohen** — *The Essential Difference* (2003) | Replikasyonu çöken yenidoğan deneyi; %80 cinsiyet örtüşmesinin göz ardı edilmesi | Ağır Revizyon |

📂 Raporlar: [`showcase/tr/`](showcase/tr/) (Türkçe) | [`showcase/en/`](showcase/en/) (İngilizce)  
📊 Sayısal metrikler: [`docs/BENCHMARKS.md`](docs/BENCHMARKS.md)

---

## Belge Haritası

| Belge | İçerik |
|:---|:---|
| [**Whitepaper**](docs/CRUCIBLE_v6_Whitepaper.md) | Teknik şartname, SOTA karşılaştırması, mimari detaylar |
| [**Benchmarks**](docs/BENCHMARKS.md) | 9 vakanın sayısal metrikleri (M1–M8), çapraz model tutarlılık verisi |
| [**Limitations**](docs/LIMITATIONS.md) | Başarısızlık modları, kesin sınırlar, CRUCIBLE'ın yapamadığı şeyler |
| [**Benchmark Protokolü**](benchmarks/methodology/BENCHMARK_PROTOCOL.md) | Benchmarkların nasıl tasarlandığı, yürütüldüğü ve ölçüldüğü |
| [**Kör Test Protokolü**](benchmarks/methodology/BLIND_TEST_PROTOCOL.md) | Daha önce görülmemiş metinlerde test protokolü |
| [**Katkı Kılavuzu**](CONTRIBUTING.md) | Rapor ekleme, metodoloji eleştirisi, linter geliştirme rehberi |
| [**Değişiklik Günlüğü**](CHANGELOG.md) | Sürüm geçmişi |

---

## Bilinen Sınırlamalar

CRUCIBLE yapamadığı şeyleri gizlemez:

- **Teorem ispatlayıcı değildir.** Saf sembolik matematik (topoloji, sayılar teorisi) formel ispat denetleyicilerine (Lean, Coq) gerektirir, LLM'lere değil.
- **Otonom değildir.** İnsan denetimi zorunludur. 3 fazlı interaktif duraklama sistemi, kontrolsüz çıktı dökmeyi engeller.
- **Girdi hacmi tavanı.** ~20 sayfa / ~15 KB üzeri hedef dosyaları bağlam seyrelmesi riski taşır. Uzun eserleri parçalayın.
- **Model kayması.** Yapay zekâ sağlayıcılarının ağırlık güncellemeleri CRUCIBLE performansını sessizce değiştirebilir. Linter yapısal bozulmayı yakalar, semantik gerilemeyi yakalamaz.

Detaylı analiz: [`docs/LIMITATIONS.md`](docs/LIMITATIONS.md)

---

## Katkıda Bulunma

CRUCIBLE kendi denetiminden geçebilmelidir. **Metodolojik eleştiriler en değerli katkılardır.** Detaylar: [`CONTRIBUTING.md`](CONTRIBUTING.md)

---

## Lisans ve Atıf

[**MIT Lisansı**](LICENSE) altında açık kaynak olarak dağıtılmaktadır.

```bibtex
@software{crucible2026,
  author  = {CRUCIBLE Open-Source Contributors},
  title   = {CRUCIBLE: An Open-Source Framework for Epistemic Auditing and Dialectical Stress-Testing},
  year    = {2026},
  url     = {https://github.com/efegok73/crucible},
  note    = {Originally conceived as May{\i}n Tarlas{\i} (Epistemic Minefield) Protocol}
}
```
