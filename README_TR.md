# ⚖️ CRUCIBLE (Mayın Tarlası Modeli v6.0) — TÜRKÇE BAŞVURU KILAVUZU
### Epistemolojik Denetim ve Diyalektik Stres Testi Açık Kaynak Çerçevesi
*(Uluslararası Açık Kaynak Adı: **CRUCIBLE** | Özgün Kurucu Mimari: **Mayın Tarlası Modeli**)*

[![License: MIT](https://img.shields.io/badge/Lisans-MIT-blue.svg)](LICENSE)
[![Versiyon](https://img.shields.io/badge/Versiyon-6.0_Epistemolojik_Cerrahi-emerald.svg)](README_TR.md)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-informational.svg)](https://www.python.org/)

> **"Bir tez bu mayın tarlasından ya zayıf varsayımları infilak ederek elenir, ya metodolojik yaralarını fark edip revizyona çekilir, ya da şimdilik falsifikasyona direnerek daha dayanıklı bir biçimde çıkar. Nihai amaç mutlak hakikat ilan etmek değil; araştırmacının kendi kör noktalarını görmesini sağlayan tavizsiz bir diyalektik sürtünme yaratmaktır."**  
> *(Mayın Tarlası: Gizli varsayımların ve yöntemsel kırılganlıkların sınandığı çetin diyalektik stres testi arazisi; Crucible: Bir tezin retorik cürufundan arındırılması için maruz bırakıldığı analitik pota.)*

---

## 🧭 CRUCIBLE ASLINDA NEDİR? (SIFIR JARGONLA)

> **"Bir araştırmanın ilk veri kırıntısından nihai tez savunmasına kadar; araştırmacının kendisinden bile gizlenen kör noktaları, yöntemsel çelişkileri ve bilinçdışı önyargıları ifşa eden açık kaynaklı bir denetim mimarisidir.**  
> **Yapay zekâyı 'harikasın' diyen bir dalkavuktan, duygularından arınmış keskin bir bilimsel hakeme dönüştürür: Bu hakem ne sizi pohpohlar, ne de pışpışlar!"**

Normalde yapay zekâya *"Bu makaleyi veya kitabı incele"* dediğinizde bir politikacı gibi konuşur: her iki tarafı da haklı bulur, suya sabuna dokunmayan özetler geçer ve kullanıcıyı memnun etmeye çalışır. 

CRUCIBLE ise yapay zekâyı **bir mahkeme savcısı ve kıdemli bir bilimsel hakem gibi** çalışmaya zorlar:
1. Önce tezi yazarın bizzat savunabileceğinden daha kusursuz bir akademik formda kurdurur (**Çelik Adam / Steelmanning**).
2. Ardından tezi 10 katmanlı bir metodolojik sınavdan geçirerek veri hilelerini, karıştırıcı değişkenlerini ve nedensellik deliklerini tek tek masaya yatırır.
3. Analiz bittiğinde kendi hatalarını itiraf ettirir (**Oto-Falsifikasyon**) ve deterministik bir Python linter'ı ile raporu mühürler.

---

## ⚡ İKİ FARKLI ÇALIŞMA YOLU (HIZLI BAŞLANGIÇ)

CRUCIBLE'ı çalışma ortamınıza ve teknik seviyenize göre iki yoldan biriyle hemen kullanabilirsiniz:

### 🌐 Yol A: Web ve Tarayıcı Kullanıcısıysanız (Gemini Advanced, Claude.ai, ChatGPT)
*Kodlama bilmenize veya bilgisayarınıza program kurmanıza gerek yoktur. Modelin özetleme tuzağına düşmesini engellemek için işlem **2 aşamada** yürütülür:*

1. **1. Aşama (Veriyi Çıkarın / Hedef Tahtası):**
   * [`templates/CRUCIBLE_EXTRACTION_DIRECTIVE_TR.md`](templates/CRUCIBLE_EXTRACTION_DIRECTIVE_TR.md) dosyasındaki talimatı kopyalayın.
   * Gemini/Claude sohbet kutusuna yapıştırın ve incelemek istediğiniz PDF'i veya metni ekleyin.
   * Model size editoryal yorum katmadan, yazarın iddia ve alıntılarının cımbızlandığı saf **"Hedef Tahtası"** fişini teslim edecektir.

2. **2. Aşama (Otopsiyi Başlatın):**
   * [`templates/CRUCIBLE_WEB_PROMPT_TR.md`](templates/CRUCIBLE_WEB_PROMPT_TR.md) dosyasındaki tek parça istemi kopyalayın.
   * Modele: *"1. Aşamada çıkardığın bu Hedef Tahtasını şimdi bu anayasal istemle otopsiye al"* deyin.
   * Model hiçbir özetleme yapmadan 10 katmanlı derin akademik raporu ve Cerrah Denetim Kartını dökecektir.

*(💡 İpucu: Claude.ai Projects veya Gemini Gems kullanıyorsanız; `docs/` altındaki anayasa dosyalarını proje hafızasına yükleyerek bu iki adımı kalıcı bir çalışma odasına dönüştürebilirsiniz.)*

---

### 💻 Yol B: Ajan ve IDE Kullanıcısıysanız (Antigravity, Cursor, Claude Code)
*Klasörü editörde açmanız yeterlidir; sistem kökteki `.cursorrules`, `AGENTS.md` ve `CLAUDE.md` anayasalarını otomatik olarak yükler:*

1. **Klasörü Açın:** İndirdiğiniz `crucible` klasörünü editörünüzde açın (`File -> Open Folder -> crucible`).
2. **Tek Komutla Çalıştırın:** Ajan sohbet kutusuna doğrudan şu komutu verin:
   > *"@templates/CRUCIBLE_EXTRACTION_DIRECTIVE_TR.md kurallarıyla @makale.pdf dosyasının hedef tahtasını çıkar, ardından CRUCIBLE metodolojisiyle analiz edip scripts/crucible_linter.py ile doğrula."*
3. **Mühürlü Raporu Alın:** Ajan analizi yazar, terminalden Python linter'ını çalıştırıp `[PASS]` alır ve mühürlü `.html` raporunu üretir.

---

## 🚨 KRİTİK İŞLETİM UYARISI: FİYASKO VE DİL ÇÖKÜŞÜNÜ ÖNLEME

> **⚠️ Model Performansı Fizik Sabiti Değildir:**  
> AI sağlayıcıları model ağırlıklarını sessizce günceller. Bugün 11 normatif katmanı kusursuz işleten bir model, gelecek hafta 5. katmanda çökebilir — tersi de doğrudur. Kritik analizleri mutlaka en az 2 farklı sınır modelle çapraz doğrulayın.

> **🚨 İki Kademeli Boru Hattı Zorunluluğu:**  
> CRUCIBLE tek adımlı bir özetleyici değildir! Yüzlerce sayfalık ham birincil metinleri tek bir komutla modele boca etmek doğrudan *Özetleyici Pürüzsüzleştirme (Smoothing Error)* hatasına yol açar ve analizi 18 KB'lik sığ bir gazete brifingine hapseder. Süreç kesinlikle önce **Veri Çıkarımı (Hedef Tahtası)**, ardından **Analiz İşletimi (Otopsi)** olarak ikiye ayrılmalıdır.

> **🌐 Substrat Eşitliği Yasası (Dil Kuralı):**  
> Pozitif tıp, bilişsel nörobilim veya istatistiki bir İngilizce makale inceleniyorsa; modelden Türkçe analiz talep etmek morfolojik token darboğazı nedeniyle analitik derinliğin **%50'sini peşinen çöpe atmaktır**. İngilizce kaynakların analizi **İngilizce icra edilmeli ve mühürlenmelidir**. Türkçe okuma isteniyorsa, mühürlü 4K İngilizce rapor sonradan editoryal olarak Türkçeye çevrilmelidir.  
> *(Donanımsal ve ampirik kanıtlar için bkz: `docs/tr/03_...`, `docs/tr/04_...` ve `docs/tr/05_...`)*

---

## 🏛️ METODOLOJİK MİMARİ: 10 NORMATİF KATMAN

CRUCIBLE dinamik bir **Epistemolojik Triyaj Matrisi** ile çalışır. İncelenen tezin disiplinine göre ilgili katmanlar aktif hale getirilir:

* **Katman 1 (Epistemik Erdem ve Persona):** Duygusal ve ideolojik retoriği filtreler; epistemik alçakgönüllülüğü zorunlu kılar.
* **Katman 2 (Çelik Adam ve Bilim Felsefesi):** Tezi eleştirmeden önce, onun en kusursuz ve en güçlü akademik halini yeniden inşa ettirir.
* **Katman 3 (Hermenötik ve Anlamsal Hijyen):** Çift anlamlılıkları ve dil oyunlarını eler.
* **Katman 4 (İstatistik, Olasılık ve Bayes):** Örneklem boyutlarını ($N$), etki büyüklüklerini (Cohen's $d$), $p$-değerlerini ve Bayesçi öncülleri denetler.
* **Katman 5 (Deneysel Tasarım ve Nedensellik):** Karıştırıcı değişkenleri ($Z$), ters nedenselliği ve karşıolgusal (*counterfactual*) senaryoları test eder.
* **Katman 6 (Kanıt Hiyerarşisi ve Sistematik Derleme):** AMSTAR-2 ve GRADE standartlarıyla tekil anekdotları eler.
* **Katman 7 (Karar Bilimi ve Risk - DMDU):** Derin belirsizlik altında karar alma, ters riskler (*risk-risk tradeoffs*) ve anti-kırılganlığı denetler.
* **Katman 8 (Tarihsel ve Metinsel Kaynak Tenkiti):** Birincil kaynaklara, epigrafik kayıtlara ve iç/dış tenkite dayanmayan iddiaları reddeder.
* **Katman 9 (Hesaplamalı Modeller ve AI):** Simülasyon ayar parametrelerini (*tuning*) ve aşırı öğrenmeyi (*overfitting*) denetler.
* **Katman 10 (Oto-Falsifikasyon ve Cerrah Kartı):** Model kendi analizindeki kör noktaları ifşa eder ve araştırmacı için 3 dakikalık somut **Cerrah Denetim Kartı** sunar.

---

## 🔬 9 KANITLANMIŞ BENCHMARK VAKASI

CRUCIBLE v6.0 motoru, 5 farklı akademik sahada en çetin 9 tartışma üzerinde test edilmiş ve raporların tamamı linter'dan `[PASS]` alarak mühürlenmiştir:

| # | Disiplin | İncelenen Eser & Yazar | Temel Zayıf Karın & Sürtünme | Hüküm | Monografi |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **01** | **Felsefe & Cinsiyet** | **Judith Butler** – *Gender Trouble* (1990) | Biyolojik dimorfizmin ontolojik inkarı | Ağır Revizyon | [HTML Raporu](showcase/tr/01_Judith_Butler_Report.html) |
| **02** | **Psikanaliz** | **Jacques Lacan** – *Seminaire XX: Encore* (1975) | Topolojik mathemelerin sahte-bilimselliği | Ağır Revizyon | [HTML Raporu](showcase/tr/02_Jacques_Lacan_Report.html) |
| **03** | **Klinik Epidemiyoloji** | **Dr. Hilary Cass** – *The Cass Review* (NHS, 2024) | Gözlemsel kohort verisine aşırı katı RCT eşiği | Kısmi Revizyon | [HTML Raporu](showcase/tr/03_Cass_Review_Report.html) |
| **04** | **Tarih Yazımı** | **Cheikh Anta Diop** – *The African Origin* (1974) | Anakronik ırk projeksiyonu ve sahte eşseslilik | Reddedildi | [HTML Raporu](showcase/tr/04_Cheikh_Anta_Diop_Report.html) |
| **05** | **Klasik Filoloji** | **Frank M. Snowden Jr.** – *Blacks in Antiquity* (1970) | Greko-Romen fizyognomi ve yabancı düşmanlığının aklanması | Kısmi Revizyon | [HTML Raporu](showcase/tr/05_Frank_Snowden_Report.html) |
| **06** | **Bibliyometri** | **Cook et al. vs. Tol** – *%97 İklim Konsensüsü* (2013) | Payda manipülasyonu (%66.4 nötr makalenin dışlanması) | Ağır Revizyon | [HTML Raporu](showcase/tr/06_Cook_Tol_Climate_Report.html) |
| **07** | **İklim Fiziği & Risk** | **Judith Curry** – *Climate Uncertainty* (2023) | Okyanus iç salınımları vs Net Enerji Dengesizliği | Ağır Revizyon | [HTML Raporu](showcase/tr/07_Judith_Curry_Report.html) |
| **08** | **Nöropsikiyatri & EBM**| **Joanna Moncrieff et al.** – *Serotonin Theory* (2022) | Etiyolojik nedensizlikten klinik etkinsizlik türetme (Aspirin Safsatası) | Ağır Revizyon | [HTML Raporu](showcase/tr/08_Joanna_Moncrieff_Report.html) |
| **09** | **Evrimsel Biyoloji** | **Simon Baron-Cohen** – *Essential Difference* (2003) | Replikasyonu çöken yenidoğan deneyi (Connellan 2000) | Ağır Revizyon | [HTML Raporu](showcase/tr/09_Simon_Baron_Cohen_Report.html) |

Tüm dosyalar `showcase/tr/` klasöründe hem `.md` hem interaktif `.html` olarak incelenebilir.

---

## 🛡️ TEMEL GÜVENLİK İLKELERİ

1. **Katı Salt-Okunur Güvenlik Duvarı:** Siz açıkça *"KAYDET"* veya *"YAZ"* demedikçe model dosyalarda değişiklik yapamaz.
2. **Zorunlu Fazlı Duraklama:** Geniş kapsamlı analizlerde model tek seferde kontrolsüzce metin dökemez; Faz 1 (Steelman), Faz 2 (Çürütme) ve Faz 3 (Oto-Falsifikasyon) sınırlarında durup sizden *"Devam"* onayı beklemek zorundadır.
3. **Epistemik Alçakgönüllülük:** Kanıtın olmadığı veya bilinmeyen yerlerde modelin kesin hüküm vermesi yasaktır; açıkça *"Bilinmiyor"* demek zorundadır.

---

## 📜 LİSANS

Bu proje **MIT Lisansı** altında açık kaynak olarak dağıtılmaktadır. Ayrıntılar için [`LICENSE`](LICENSE) dosyasına bakınız.
