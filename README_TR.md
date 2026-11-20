# ⚖️ CRUCIBLE (Mayın Tarlası Modeli v7.2) — KULLANICI VE METODOLOJİ KILAVUZU

**Yapay zekâyı diplomatik bir metin özetleyicisinden, birincil kaynak metne dayalı, acımasız ve berrak bir bilimsel hakeme dönüştüren açık kaynak denetim çerçevesi.**

[![Lisans: MIT](https://img.shields.io/badge/Lisans-MIT-blue.svg)](LICENSE)
[![Versiyon](https://img.shields.io/badge/Versiyon-7.2-emerald.svg)](CHANGELOG.md)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-informational.svg)](https://www.python.org/)

> *Uluslararası Açık Kaynak Adı:* ***CRUCIBLE*** *| Özgün Kurucu Mimari:* ***Mayın Tarlası*** *(Gizli varsayımların ya sınandığı ya da havaya uçtuğu diyalektik stres testi arazisi)*

🌐 **English version:** [`README.md`](README.md)

---

## CRUCIBLE Nedir?

CRUCIBLE, ticari büyük dil modellerini (Claude, ChatGPT, Gemini) **metodolojik açıdan tavizsiz, birincil kaynak metne dayalı ve analitik derinliğe sahip bilimsel hakemlere** dönüştüren iki bileşenli bir açık kaynak araştırma çerçevesidir:

1. **10 Katmanlı Normatif Anayasa:** Modeli çıkarım anında (inference time) Karl Popper'ın yanlışlanabilirlik ilkesi, nedensel yönlü grafikler (DAG), Bayesçi olasılık güncellemeleri, Alıntısız Eleştiri Yasağı ve Şeytanın Savunmanı filtresiyle bağlayan epistemik yönerge protokolü.
2. **Kaynak Metin Dayanaklı Deterministik Linter (`scripts/crucible_linter.py`):** Modelin kurallara uyup uymadığını dışarıdan denetleyen bağımsız bir Python derleyicisidir. İncelenen rapordaki her alıntıyı ve iddiayı orijinal kaynak dosya (`--source`) ile karşılaştırır; uydurma kaynaklarda (*hayalet referans*) veya dil uyuşmazlığında (*Substrate Parity Gate*) derlemeyi durdurur; yalnızca tüm şartları sağlayan raporlara doğrulanmış yeşil mühür basar.

### Sıradan Yapay Zekâ Neden Bilimsel Hakemlik Yapamaz?

Herhangi bir yapay zekâya *"Bu makaleyi veya tezi incele"* dediğinizde, karşınıza neredeyse her zaman nazik, suya sabuna dokunmayan ve yazarı pohpohlayan bir özet çıkar. Model her iki tarafı da haklı bulur, temel kavramsal yarılmaları *"farklı bakış açıları mevcuttur"* diyerek geçiştirir ve zayıflıkları *"bazı metodolojik sınırlılıklar bulunabilir"* gibi içi boş diplomatik kalıplarla örter.

Yapay zekâ araştırmalarında bu zaafa **dalkavukluk önyargısı (sycophancy)** adı verilir. LLM'ler kullanıcıyı memnun etmek ve çatışmadan kaçınmak üzere eğitildikleri için, zorlu bir akademik tezin zayıf noktalarını kendi başlarına asla cerrahi bir titizlikle ortaya koyamazlar.

CRUCIBLE bu sorunu salt bir "istem mühendisliği" (prompt engineering) ile çözmeye çalışmaz. Çünkü uzun metinlerde modeller istemleri sessizce unutabilir ya da kuralları esnetebilir. CRUCIBLE, istem anayasasını **harici bir deterministik Python linter'ı** ile denetleyerek yapay zekâ muhakemesine derleme-zamanı (compile-time) tip kontrolü getirir. Modelin ağırlıkları değiştirilmez, pahalı eğitim süreçlerine gerek duyulmaz.

**Bu Çerçeve Kimler İçin Tasarlandı?**
- Makalesini, doktora tezini veya kitabını — **kendi çalışması dahil** — hakem heyetinden önce en katı metodolojik stres testine sokmak isteyen araştırmacılar.
- Tez savunması öncesinde metodolojisindeki karıştırıcı değişkenleri ve veri sıçramalarını keşfetmek isteyen akademisyen ve öğrenciler.
- Bilimsel iddialar ile retorik gösterişi birbirinden ayırmak isteyen bilim gazetecileri ve politika analistleri.
- Yapay zekânın kendisine sürekli hak vermesinden ve boş özetler üretmesinden yorulan herkes.

---

## 🏛️ Dört Epistemik İlke

CRUCIBLE bir "özetleyici" değil; akademik metinlere adli otopsi uygulayan kurumsal bir bilim hakemidir:

1. **Katı Metodolojik Filtreler:**  
   İncelenen metni genel geçer kanaatlerle değil; çağdaş bilim felsefesinin en sert standartlarıyla (Popperiyen yanlışlanabilirlik, Bradford Hill nedensellik kriterleri, GRADE kanıt hiyerarşisi) sorgular.
2. **Veri ve Payda Cerrahisi:**  
   Tezin dayandığı birincil verileri, örneklem büyüklüklerini ve payda seçimlerini inceler. Örneğin verideki bir korelasyondan ontolojik bir gerçeklik türetilip türetilmediğini (vekil veri sıçraması) adli bir titizlikle açığa çıkarır.
3. **Kavramsal Belirsizlik ve Örtük Dogma Avı:**  
   Akademik jargona sığınılarak gizlenmiş çift anlamlılıkları (*motte-and-bailey*), döngüsel mantık yürütmeleri ve kanıtlanmadan doğru kabul edilmiş örtük aksiyomları tek tek deşer.
4. **Oto-Falsifikasyon (Modelin Kendi Kör Noktalarını İtirafları):**  
   Hiçbir yapay zekânın mutlak bir hakikat yargıcı olamayacağını baştan kabul eder (Gödel-Tarski sınırı). Kendi hazırladığı analizin de zayıf noktalarını, tek kaynağa bağımlılık risklerini ve felsefi eğilimlerini dürüstçe itiraf eder. Nihai hükmü daima araştırmacının elindeki Cerrah Denetim Kartı'na bırakır.

---

## 🌐 Evrensel Dil Substrat Paritesi Kanunu ($L_{source} \equiv L_{audit} \rightarrow L_{target}$)

CRUCIBLE, dünyanın her yerindeki araştırmacılar için tasarlanmış evrensel bir mimaridir. İster Çinli bir araştırmacı Çince bir felsefe metnini Arapça olarak incelemek istesin, ister Türk bir araştırmacı İngilizce bir tıp makalesini Türkçe analiz etmek istesin; dilsel asimetri aynı doğa kanununa tabidir.

### 1. Temel Sorun: Neden Doğrudan Başka Bir Dilde Analiz Yapılamaz?
Büyük dil modelleri, kaynak metin ile analiz dili birbirinden farklı olduğunda **iki katmanlı bir bilişsel erozyon** yaşar:
- **Tokenizasyon Darboğazı ve Anlamsal Kayıp:** İngilizce yazılmış bir makaleyi doğrudan Türkçe, Çince veya Arapça analiz etmeye zorladığınızda, model bir yandan kaynak metnin kavramsal örgüsünü çözmeye çalışırken diğer yandan anlık çeviri yükü altına girer. Bu durum, analitik muhakeme derinliğinde %40 ile %50 arasında kayba yol açar (*smoothing loss*).
- **Yapay Çeviri Yanılsaması (Translationese):** Yazarın orijinal dilde özenle koyduğu ihtiyat şerhleri ve emniyet supapları, çeviri sırasında buharlaşır; model yazara haksız yere "saman adam" eleştirileri yöneltir.

### 2. Evrensel Çözüm: İki Kademeli Protokol
Bu nedenle CRUCIBLE mimarisinde şu evrensel kural tavizsiz bir yasa olarak uygulanır:

$$\mathbf{L_{audit} \equiv L_{source}} \quad \longrightarrow \quad \mathbf{L_{target}}$$

1. **Kademe 1 (Kaynak Dilde Birincil Denetim):**  
   İncelenen eser hangi dilde kaleme alınmışsa ($L_{source}$ — İngilizce, Çince, Arapça, Rusça, Türkçe vb.), birinci kademe analitik denetim ($L_{audit}$) **istisnasız o kaynak dilde** gerçekleştirilir ve mühürlenir (`audit_en.md`, `audit_zh.md` vb.).
2. **Kademe 2 (Hedef Dile İki Kademeli Yerelleştirme):**  
   Kullanıcı hedef dilde ($L_{target}$ — örneğin Türkçe veya Arapça) bir rapor istiyorsa, mühürlü birincil rapor hedef dile aktarılır. Raporda `**Primary Audit:** <birincil_rapor_yolu>` üstverisi açıkça belirtilir ve kaynak metindeki deterministik `[P:xxxx]` paragraf çıpaları ile orijinal alıntılar çift çıpa olarak muhafaza edilir.

### 3. Programatik Güvence: Substrate Parity Gate
Bu kural artık kullanıcı veya model inisiyatifine bırakılmış bir temenni değildir. `CRUCIBLE/scripts/crucible_linter.py` motoru, hem kaynak metnin hem de üretilen raporun dilini (Latin, Arap, Kiril ve CJK alfabeleri dahil) mekanik olarak tespit eder.
- Eğer İngilizce bir kaynak dosya doğrudan Türkçe bir raporla linter'a verilirse, linter işlemi derhal durdurur ve **`[FAIL: SUBSTRATE PARITY VIOLATION]`** hatası verir.
- Rapor ancak geçerli bir birincil denetim üstverisi taşıdığında veya `--allow-localized` parametresi sağlandığında onaylanır.

---

## 🎯 Pedagojik Berraklık ve Doğal Dil İlkesi

CRUCIBLE analizlerinin temel varlık sebebi; araştırmacının, incelenen eserdeki metodolojik kusurun **tam olarak ne olduğunu** hiçbir şüpheye yer bırakmayacak biçimde anlamasını sağlamaktır.

Bu hedef iki somut ilkeyle garanti altına alınmıştır:

### A. Mekanik Çeviri ve Bürokrasi Yasağı (Anti-Translationese)
Rapor dili; robotik tercümelerin, peş peşe yığılmış edilgen çatıların (`gerçekleştirilmektedir`, `mütalaa edilmektedir`, `tarafından icra edilen`) ve soğuk bürokratik kalıpların kurbanı olamaz. Gerek İngilizce gerekse yerelleştirilmiş Türkçe raporlar; akıcı, zengin, anlaşılır ve doğrudan etken bir dille yazılır. Linter motoru, rapordaki mekanik bürokratik kalıpların yoğunluğunu otomatik olarak denetler.

### B. "Bir Kavram, Bir Somut Örnek" Standardı
Yazara salt akademik jargon fırlatıp kenara çekilmek yasaktır. Raporda kullanılan her teknik kavram ve yöneltilen her metodolojik eleştiri, konuya yabancı olmayan her okuyucunun zihninde anında somutlaşacak berrak bir örnekle veya analojiyle açılmak zorundadır:
- **Kötü / Kapalı Örnek:** *"Yazar burada bir motte-and-bailey safsatası işletmektedir."* (Okuyucu ne kastedildiğini tam olarak kavrayamaz).
- **CRUCIBLE Standardı:** *"Yazar burada bir 'kale-ve-avlu' (motte-and-bailey) taktiği işletmektedir: Tıpkı düşman saldırdığında savunması kolay taştan bir kaleye (motte) sığınıp, tehlike geçince verimli ama savunmasız ovaya (bailey) geri dönen bir ordu gibi; yazar da radikal iddiası ('biyolojik cinsiyet tamamen dilsel bir yanılsamadır') sorgulandığında hemen savunması kolay ılımlı teze ('cinsiyete dair algılarımız kültüreldir') geri çekilmekte, eleştiri savuşturulunca yeniden radikal iddiasına dönmektedir."*

---

## Sorun Nedir? CRUCIBLE Ne Fark Yaratır?

### Standart bir yapay zekâya "bu kitabı analiz et" dediğinizde:
> *"Butler'ın Gender Trouble eseri feminist teoriyi derinden etkileyen çığır açıcı bir çalışmadır. Bazı metodolojik sorular gündeme gelse de, yazar toplumsal cinsiyetin performatif doğasına ilişkin ikna edici ve incelikli bir argüman ortaya koymaktadır..."*

Bu bir **kitap arka kapağı tanıtımıdır**; bilimsel bir analiz değildir. Hiçbir somut çelişkiyi göstermez.

### Aynı kaynak materyale CRUCIBLE uygulandığında:
> **[Katman 3 — Hermenötik Denetim]:** "Performativite" kavramı, Bölüm 1–3 arasında birbiriyle çelişen üç farklı anlamda kullanılıyor: (a) toplumsal baskı altında normların zorunlu tekrarı, (b) Nietzsche'ci neden-sonuç tersyüz edimi, (c) dilbilimsel söz-edim türevi. Bu belirsizlik, yazarın ontolojik iddiası sıkıştığında daha zayıf olan epistemolojik yoruma kaçmasına imkân tanıyan bir *motte-and-bailey* yapısı üretmektedir.
>
> **[Katman 8 — Kaynak Tenkiti Matrisi]:**
>
> | İddia | Birincil Kaynak | Kaynak Durumu | Metodolojik Hüküm |
> |:---|:---|:---|:---|
> | Biyolojik cinsiyet söylemsel olarak inşa edilmiştir | Foucault, *Cinselliğin Tarihi* Cilt 1 | Post-yapısalcı söylem analizi | **Vekil Sıçraması:** "Dil, anatomiyi tarif eder" öncülünden "anatomik yapının kendisi kültürel bir kurgudur" sonucuna dayanaksız geçiş. |
>
> **[Katman 10 — Oto-Falsifikasyon]:** Bu denetimin kendi analitik modeli, değerlendirme ölçütü olarak ağırlıklı biçimde analitik bilim felsefesine dayanmaktadır. Bu durum, Kıta Avrupası felsefesinin kendine özgü kavramsal taahhütlerini sistematik biçimde hafife alma riski barındırabilir...

---

## Hızlı Başlangıç: Adım Adım Uygulama Kılavuzu

### 💻 Seçenek A (Tavsiye Edilen): Ajanik IDE ile Otonom Denetim
*(Antigravity, Cursor, VS Code veya Claude Code kullananlar için)*

Bu modda dosyaları tek tek kopyalayıp yapıştırmazsınız; klasördeki anayasa dosyalarını devralan ajan tüm süreci ve doğrulamayı otonom yürütür:

1. **Çalışma Klasörünü Açın:**  
   IDE'nizi açarak `crucible` reposunu çalışma alanı olarak yükleyin.
2. **Belgenizi Yerleştirin:**  
   İncelenecek eseri (PDF, Word veya Markdown) çalışma klasörünüze (örneğin `data/` veya `kaynaklar/`) ekleyin.
3. **Kaynak Metin Dokunulmazlığı (v7.2 Kuralı):**  
   - Eseri asla 20-25 sayfalık parçalara bölmeyin veya özetlemeyin.
   - İsterseniz önce `python scripts/index_source.py data/eser.pdf -o data/eser_indeksli.txt` komutuyla deterministik `[P:xxxx]` kütüğünü oluşturun.
4. **Komut Verin:**  
   > *"Klasördeki `@data/eser.pdf` eserini CRUCIBLE v7.2 kurallarıyla analiz et. Kaynak dilde birincil denetimi mühürle, ardından hedef dilde akıcı ve berrak yerelleştirilmiş raporu üretip linter'ı çalıştır."*
5. **Mühürlü Çıktıyı Alın:**  
   Ajan analizi tamamlar, `scripts/crucible_linter.py` çalıştırıp `[PASS]` alır ve yayına hazır `.html` raporunu üretir.

---

### 🌐 Seçenek B: Web Arayüzü ile Doğrudan Denetim
*(Claude.ai, ChatGPT Plus, Google AI Studio kullananlar için — Sıfır Kurulum)*

1. [`templates/CRUCIBLE_WEB_PROMPT_TR.md`](templates/CRUCIBLE_WEB_PROMPT_TR.md) (veya İngilizce kaynaklar için [`CRUCIBLE_WEB_PROMPT_EN.md`](templates/CRUCIBLE_WEB_PROMPT_EN.md)) dosyasındaki metni kopyalayın.
2. Web sohbetine yapıştırın ve yanına tam metin dosyanızı ekleyin.
3. Üretilen analitik metni kaydedin (`rapor.md`).
4. Terminalden deterministik linter denetimini çalıştırın:  
   ```bash
   pip install markdown pypdf
   python scripts/crucible_linter.py rapor.md --source eser.pdf
   ```  
   Linter; zorunlu 5 bölümü, Katman 8 tablosunu, alıntıların doğruluğunu ve dil paritesini denetler. Onaylanan rapora resmi yeşil **`[PASS]`** mührü basılır ve `rapor.html` derlenir.

---

## Nasıl Çalışır? 10 Normatif Katman

Dinamik **Epistemolojik Triyaj Matrisi**, incelenen eserin disiplinine göre ilgili katmanları devreye alır:

| Katman | İşlev | Ne Zaman Aktif? |
|:---:|:---|:---|
| **K1** | **Epistemik Erdem** — Retorik gösterişi filtreler, entelektüel alçakgönüllülüğü zorunlu kılar | Her zaman |
| **K2** | **Çelik Adam (Steelmanning)** — Tezi eleştirmeden önce en güçlü akademik formülasyonuyla yeniden kurar | Her zaman |
| **K3** | **Hermenötik Hijyen** — Anlamsal kaymalar, kavram enflasyonu, örtük aksiyomlar | Felsefe, sosyal bilimler |
| **K4** | **İstatistik ve Bayes** — Örneklem boyutları, p-hacking, öncül olasılık güncellemeleri | Ampirik bilimler, tıp |
| **K5** | **Deneysel Tasarım ve Nedensellik** — Karıştırıcılar, ters nedensellik, DAG şemaları | Klinik çalışmalar, biyoloji |
| **K6** | **Kanıt Hiyerarşisi** — AMSTAR-2, GRADE standartları; tekil vaka anlatılarını ayıklar | Sistematik derlemeler |
| **K7** | **Karar Bilimi ve Risk (DMDU)** — Derin belirsizlik, kalın kuyruk riskleri, açık bilim | Politika analizi, iklim bilimi |
| **K8** | **Tarihsel Metin Tenkiti** — Birincil kaynak çapraz doğrulaması; İddia-Kaynak Matrisi zorunludur | Tarih yazımı, arşiv araştırması |
| **K9** | **Hesaplamalı Model Denetimi** — Aşırı öğrenme, doğrulama sızıntısı, algoritma önyargısı | Yapay zekâ, simülasyonlar |
| **K10** | **Oto-Falsifikasyon ve Cerrah Kartı** — Model kendi kör noktalarını itiraf eder; 3 dakikalık denetim listesi sunar | Her zaman |

---

## 9 Doğrulanmış Benchmark Vakası

Tüm raporlar deterministik linter tarafından doğrulanmış ve mühürlenmiştir:

| # | Disiplin | İncelenen Eser | Temel Metodolojik Zafiyet | Hüküm |
|:---:|:---|:---|:---|:---:|
| 01 | Felsefe & Toplumsal Cinsiyet | **Judith Butler** — *Gender Trouble* (1990) | "Performativite"de anlamsal kaçak; epistemolojiden ontolojiye dayanaksız vekil sıçraması | Ağır Revizyon |
| 02 | Psikanaliz | **Jacques Lacan** — *Seminaire XX* (1975) | Formel matematiksel temeli olmayan sahte-topoloji (mathemeler) | Ağır Revizyon |
| 03 | Klinik Epidemiyoloji | **Hilary Cass** — *The Cass Review* (2024) | Gözlemsel pediatrik kohort verisine orantısız RCT katılığı uygulanması | Kısmi Revizyon |
| 04 | Tarih Yazımı | **Cheikh Anta Diop** — *The African Origin* (1974) | Anakronik ırk kategorileri; fonetik benzerlikten sahte köken türetme | Reddedildi |
| 05 | Klasik Filoloji | **Frank M. Snowden Jr.** — *Blacks in Antiquity* (1970) | Greko-Romen fizyognomik önyargının ve dilsel ayrımcılığın hafife alınması | Kısmi Revizyon |
| 06 | Bibliyometri & İklim | **Cook et al. vs. Tol** — *%97 İklim Konsensüsü* (2013) | Payda manipülasyonu (%66.4 nötr makale analiz dışı bırakılarak yüzde şişirilmiş) | Ağır Revizyon |
| 07 | İklim Modellemesi | **Judith Curry** — *Climate Uncertainty* (2023) | Okyanus içi salınım savları vs. uydulardan gözlenen net gezegensel enerji dengesizliği | Ağır Revizyon |
| 08 | Psikiyatri & Kanıta Dayalı Tıp | **Joanna Moncrieff et al.** — *Serotonin Theory* (2022) | **V7 Zemin Düzeltmesi:** Yazarın etiyoloji şerhleri doğrulanarak V6'nın haksız "Aspirin Safsatası" ithamı düşürüldü; asıl sorun biyokimyasal belirteç ile klinik seyir arasındaki vekil sıçraması olarak tespit edildi. | Ağır Revizyon |
| 09 | Evrimsel Psikoloji | **Simon Baron-Cohen** — *The Essential Difference* (2003) | Replikasyonu çöken yenidoğan deneyi; %80 cinsiyet örtüşmesinin yok sayılması | Ağır Revizyon |

📂 Mühürlü Raporlar: [`showcase/tr/`](showcase/tr/) (Türkçe) | [`showcase/en/`](showcase/en/) (İngilizce)  
📊 Sayısal Metrikler: [`docs/BENCHMARKS.md`](docs/BENCHMARKS.md)

---

## Bilinen Sınırlamalar

CRUCIBLE yapamadığı şeyleri dürüstçe ortaya koyar:

- **Matematiksel Teorem İspatlayıcısı Değildir:** Saf sembolik matematik (sayılar teorisi, cebirsel topoloji) LLM'leri değil, formel ispat asistanlarını (Lean, Coq) gerektirir.
- **Tamamen Otonom Bir Hakikat Yargıcı Değildir:** İnsan denetimi şarttır. 3 fazlı interaktif yürütme ve Cerrah Denetim Kartı, kontrolün araştırmacıda kalmasını sağlar.
- **Model Kayması (Model Drift):** Model sağlayıcılarının ağırlık güncellemeleri performansı etkileyebilir. Linter yapısal bozulmaları yakalar; bu nedenle kritik analizlerde en az iki farklı modelle çapraz doğrulama önerilir.

---

## Lisans ve Atıf

CRUCIBLE, [**MIT Lisansı**](LICENSE) altında açık kaynak olarak dağıtılmaktadır.

```bibtex
@software{crucible2026,
  author  = {CRUCIBLE Open-Source Contributors},
  title   = {CRUCIBLE: An Open-Source Framework for Epistemic Auditing and Dialectical Stress-Testing},
  year    = {2026},
  url     = {https://github.com/efegok73/crucible},
  note    = {Originally conceived as May{\i}n Tarlas{\i} (Epistemic Minefield) Protocol}
}
```
