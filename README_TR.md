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

### 🏛️ CRUCIBLE'ın Dört Epistemik İlkesi

CRUCIBLE sıradan bir "özetleyici" değil; akademik bir tezi dört aşamalı bir adli otopsiden geçiren kurumsal bir hakemdir:

1. **En Yüksek Metodolojik Standartların İşletilmesi:**  
   Metni genelgeçer kanaatlerle değil; çağdaş bilim felsefesinin en katı filtreleriyle (Popperiyen yanlışlanabilirlik, Bradford Hill nedensellik matrisi, GRADE kanıt piramidi) sınar.
2. **Veri ve Kaynak Cerrahisi:**  
   Tezin dayandığı birincil kaynakları, örneklem büyüklüklerini ve payda seçimlerini inceler; veriyle iddia arasındaki gizli sıçramaları (vekil veri manipülasyonu) açığa çıkarır.
3. **Kavramsal Çelişki ve Örtük Aksiyom Avı:**  
   Akademik jargona sarılarak gizlenmiş çift anlamlılıkları (motte-and-bailey), döngüsel mantıkları ve sorgulanmadan doğru kabul edilmiş örtük dogmaları patlatır.
4. **Mutlak Tarafsızlık Yerine Oto-Falsifikasyon:**  
   Hiçbir yapay zekânın mutlak bir hakikat yargıcı olamayacağını (Gödel-Tarski sınırı) baştan kabul eder. Kendi ürettiği analizin de zayıf noktalarını, tek-kaynak risklerini ve felsefi eğilimlerini dürüstçe itiraf eder; son kararı daima araştırmacının elindeki Cerrah Kartı'na bırakır.

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

## Hızlı Başlangıç: Adım Adım Uygulama Kılavuzu

### ⚡ 10 Saniyelik Önizleme (Hazır Rapor İncelemesi)
Hiçbir şey kurmadan CRUCIBLE'ın nasıl bir çıktı ürettiğini hemen görmek için:  
👉 [**Judith Butler – Gender Trouble Mühürlü Raporunu Açın (HTML)**](showcase/tr/01_Judith_Butler_Report.html) veya tüm [9 Doğrulanmış Benchmark Vakasını](#9-doğrulanmış-benchmark-vakası) inceleyin.

---

### 0. Ön Hazırlık: Dosyaları Bilgisayarınıza İndirin (Herkes İçin)
1. GitHub sayfasında **Code** sekmesindeyken, sağ üstteki yeşil **`<> Code`** butonuna tıklayın ve **`Download ZIP`** seçeneğini seçin.
2. İndirilen `.zip` dosyasına sağ tıklayıp **"Klasöre Çıkart"** (*Extract All*) deyin. Artık tüm şablonlar, yönergeler ve doğrulama betikleri yerel diskinizdedir.  
*(Geliştiriciler için terminal alternatifi: `git clone https://github.com/efegok73/crucible.git`)*

---

### 💻 Seçenek A (Tavsiye Edilen): Ajanik IDE ile Otonom Denetim
*(Antigravity, Cursor, VS Code + Roo/Cline veya Claude Code kullananlar için)*

Bu modda hiçbir metni kopyalayıp yapıştırmazsınız; klasördeki anayasa dosyalarını (`.cursorrules`, `AGENTS.md`) devralan aracı ajan tüm süreci ve doğrulamayı otonom yürütür.

1. **Klasörü Güvenle Açın (Workspace Trust):**  
   IDE'nizi açın, `Dosya > Klasörü Aç` diyerek ayıkladığınız `crucible-main` klasörünü seçin. Karşınıza çıkarsa *"Trust Authors / Yazarlara Güven"* seçeneğini onaylayın *(Onaylanmazsa ajan araçları ve arka plan linter'ı kısıtlanır)*.
2. **Kendi Çalışma Klasörünüzü Açın:**  
   Proje anayasasını temiz tutmak için sol dosya ağacında yeni bir klasör oluşturun (örneğin: `calismalarim/`).
3. **Belgenizi Taşıyın:**  
   İncelenecek eseri (PDF, Word veya Markdown) bu klasörün içine sürükleyip bırakın.
4. **Metin Boyutuna Göre Komut Verin:**
   - **Kısa Metinler (< 20 Sayfa / < 10.000 Kelime — Tekil Makale veya Deneme):**  
     Ajan paneline doğrudan komut verin:  
     > *"Klasördeki `@calismalarim/makale.pdf` dosyasını CRUCIBLE v6.0 protokolüyle analiz et ve raporu mühürle."*
   - **Uzun Metinler (> 20 Sayfa — Kitap, Doktora Tezi, Monografi):**  
     Ajanla iki kademeli boru hattını işletin:
     - **1. Aşama:** *"Bu kitaba `templates/CRUCIBLE_EXTRACTION_DIRECTIVE_TR.md` direktifini uygula ve bir Hedef Tahtası (`hedef_tahtasi.md`) dökümü çıkar."*
     - **2. Aşama:** *"Şimdi `hedef_tahtasi.md` dosyasını CRUCIBLE anayasasıyla analiz et ve raporu mühürle."*
5. **Mühürlü Çıktıyı Alın:**  
   Ajan analizi tamamlar, raporu diske kaydeder, arka planda terminalden `crucible_linter.py` çalıştırıp `[PASS]` alır ve yayına hazır `.html` raporunu üretir. Size sadece üretilen HTML dosyasına çift tıklayıp okumak kalır.

---

### 🌐 Seçenek B: Web Arayüzü ile Doğrudan Denetim
*(Claude.ai, ChatGPT Plus, Google AI Studio web arayüzlerini kullananlar için — Sıfır Kurulum)*

1. **Metin Boyutuna Göre Süreci Başlatın:**
   - **Kısa Metinler (< 20 Sayfa / < 10.000 Kelime):**  
     İndirdiğiniz klasördeki [`templates/CRUCIBLE_WEB_PROMPT_TR.md`](templates/CRUCIBLE_WEB_PROMPT_TR.md) dosyasını Not Defteri ile açıp metnini kopyalayın. Web sohbetine yapıştırın, yanına inceleyeceğiniz makaleyi ekleyip gönderin.
   - **Uzun Metinler (> 20 Sayfa — Kitap, Doktora Tezi):**  
     - **1. Aşama (Hedef Tahtası Çıkarımı):** [`templates/CRUCIBLE_EXTRACTION_DIRECTIVE_TR.md`](templates/CRUCIBLE_EXTRACTION_DIRECTIVE_TR.md) metnini kopyalayıp web sohbetine yapıştırın, kitabı ekleyin. Model size bir `Hedef Tahtası` dökümü üretir.
     - **Temiz Sohbet Açın (Zorunlu):** Çıkan hedef tahtası metnini kopyalayın. **Yeni ve temiz bir sohbet penceresi açın** *(Bu adım bağlam gürültüsünü temizlemek ve özetleme refleksini önlemek için zorunludur)*.
     - **2. Aşama (Analiz):** Temiz sohbete [`templates/CRUCIBLE_WEB_PROMPT_TR.md`](templates/CRUCIBLE_WEB_PROMPT_TR.md) şablonunu ve kopyaladığınız Hedef Tahtasını yapıştırıp analizi çalıştırın.
2. **Raporunuzu Kaydedin:**  
   Modelin ürettiği analitik metni kopyalayıp Not Defteri'ne yapıştırın ve `calismalarim/rapor.md` olarak kaydedin.
3. **Zorunlu Linter Doğrulaması ve Mühürleme (Deterministik Denetim):**  
   CRUCIBLE protokolünde linter **isteğe bağlı bir tavsiye değildir; dışsal anayasal mahkemedir.** Modelin "ben tüm kurallara uydum" iddiasına güvenilmez. Raporun 5 zorunlu bölümü, Katman 8 İddia-Kaynak tablosu ve retorik hijyeni deterministik kodla denetlenmelidir:  
   ```bash
   pip install markdown
   python scripts/crucible_linter.py calismalarim/rapor.md
   ```  
   Linter raporu satır satır denetler. Şartlar sağlanmışsa **`[PASS]`** mührünü basar ve eşzamanlı olarak okunmaya hazır `rapor.html` dosyasını üretir. Hata varsa hangi katmanın eksik kaldığını açıkça raporlar. *(Linter'dan geçmeyen raporlar CRUCIBLE literatüründe mühürsüz taslak sayılır).*

---

### 📌 Önemli İlkesel Not: Seçenek A ile Seçenek B Arasındaki Eşitlik
> Talimatlara uygun işletildiğinde **Seçenek A ile Seçenek B epistemolojik derinlik, felsefi cerrahi ve analitik kalite açısından %100 özdeştir.** Her iki seçenek de aynı anayasal kuralları yürütür ve aynı deterministik linter denetiminden geçer.  
> 
> Tek fark iş akışının otomasyonundadır: **Seçenek A'da** iki aşamalı boru hattını, pencereler arası metin aktarımını, dosya kayıtlarını ve linter sağlama adımlarını sizin yerinize IDE ajanınız (Antigravity, Cursor, VS Code) otonom olarak yapar. **Seçenek B'de** ise aynı profesyonel boru hattını tarayıcı sekmeleri arasında siz manuel olarak yönetirsiniz.

---

## 🧠 Model Yetkinlik Eşiği (Mimari Gereksinimler)

CRUCIBLE belirli bir yapay zekâ sağlayıcısına veya geçici model sürümüne bağlı değildir; modelden bağımsız (model-agnostic) çalışır. Ancak 10 normatif katmanı, hermenötik ayrıştırmayı ve kaynak tenkiti matrislerini işletebilmek için kullanılan motorun şu **4 yapısal yetkinlik kriterini** karşılaması şarttır:

1. **Düşük Özetleme Refleksi (Anti-Smoothing):** Diplomatik özetleme ve pohpohlama eğilimine girmeyen, metindeki metodolojik çelişkilere doğrudan cerrahi müdahale yapabilen amiral gemisi akıl yürütme mimarileri.
2. **Katı Tablo ve Matris Disiplini:** Katman 8 İddia-Kaynak matrisini ve cerrah kartını sözdizimi bozulmadan, eksiksiz tablo formatında üretebilen biçimsel çıktı sadakati.
3. **Çok Katmanlı Yönerge Takibi:** Uzun analiz boyunca epistemolojik triyaj kurallarını unutmayan, bağlam erozyonuna uğramayan derin akıl yürütme kapasitesi.
4. **Geniş Bağlam Penceresi:** Birincil metinleri, kanıt dökümlerini ve metodolojik anayasayı aynı anda işleyebilecek bağlam hacmi.

> ⚠️ **Hafif Modeller Uyarısı:** Damıtılmış, hafif veya özetleme odaklı küçük modeller (distilled/mini/haiku sınıfları); yönerge kaybı (*instruction decay*) yaşar ve 10 katmanlı analitik yükün altında ezilerek yüzeysel özetlere çöker.

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
🔬 Kontrollü Vanilla Karşılaştırma Çalışması: [`benchmarks/vanilla_baselines/`](benchmarks/vanilla_baselines/) (N=3 Faktöriyel Benchmark)

---

## Belge Haritası

| Belge | İçerik |
|:---|:---|
| [**Whitepaper**](docs/CRUCIBLE_v6_Whitepaper.md) | Teknik şartname, SOTA karşılaştırması, mimari detaylar |
| [**Benchmarks**](docs/BENCHMARKS.md) | 9 vakanın sayısal metrikleri (M1–M8), çapraz model tutarlılık verisi |
| [**Vanilla Karşılaştırmaları**](benchmarks/vanilla_baselines/COMPARATIVE_FACTORIAL_ANALYSIS.md) | Aynı gün icra edilen N=3 faktöriyel deney: Doktora düzeyinde serbest talimat vs CRUCIBLE |
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
