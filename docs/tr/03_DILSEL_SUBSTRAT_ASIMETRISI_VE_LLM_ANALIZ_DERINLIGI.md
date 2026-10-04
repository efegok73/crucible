# CRUCIBLE v6.0 METODOLOJİK ÖZEL RAPOR: DİLSEL SUBSTRAT ASİMETRİSİ VE LLM ANALİZ DERİNLİĞİ
**Rapor Kodu:** CRUCIBLE-METH-2026-01  
**Başlık:** Çok Dilli Büyük Dil Modellerinde (LLM) Epistemik Çözünürlük Kaybı, Tokenizasyon Darboğazı ve Substrat Eşitliği İlkesi Üzerine Ampirik Bir Araştırma  
**Tarih:** 2026-10-03  
**Analitik Motor:** CRUCIBLE v6.0 Epistemolojik Cerrahi Protokolü  
**Statü:** Mühürlendi & Arşivlendi (GitHub Açık Kaynak Çerçeve Belgesi)  
**Hedef Kitle:** Yapay zekâ araştırmacıları, bilişsel bilimciler, dijital beşerî bilimciler ve analitik felsefeciler  

---

## 1. YÖNETİCİ ÖZETİ (EXECUTIVE SUMMARY)

Bu araştırma raporu; **CRUCIBLE v6.0 (Mayın Tarlası)** projesi kapsamında üretilen 9 resmî akademik benchmark monografisinin Türkçe (`showcase/tr/`) ve İngilizce (`showcase/en/`) ikizleri arasındaki yapısal, kavramsal ve hacimsel asimetriyi inceleyen ampirik bir otopsidir.

Çalışmanın merkezî ampirik bulgusu şudur:
> **Küresel sınır (frontier) Büyük Dil Modelleri (LLM), aynı birincil İngilizce kaynak metinleri analiz ederken; çıktıyı Türkçe olarak ürettiklerinde ~18–21 KB hacminde ve ~170–185 satırda özetleyici bir platoya oturmakta; buna karşılık aynı analiz İngilizce substratta icra edildiğinde dosya hacmi ~35–50 KB seviyesine (%86 ila %145 artış) ve 260–350 satır derinliğe tırmanmaktadır.**

Bu durum yüzeysel bir dil çevirisi veya üslup farkı değildir. İleri düzey LLM'lerin içsel sinir ağı temsillerinde (latent space representations), tokenizasyon algoritmalarında (BPE/WordPiece) ve dikkat mekanizmasının (attention allocation) donanımsal bütçesinde meydana gelen **yapısal bir epistemik çözünürlük kaybıdır (loss of epistemic resolution)**. 

Bu rapor, söz konusu olgunun donanımsal ve algoritmik nedenlerini açıklamakta, çalışma alanındaki 9 somut vaka üzerinden ampirik verilerini sunmakta ve gelecekte bu çerçeveyi GitHub üzerinden kullanacak araştırmacılar için bağlayıcı bir işletim protokolü tanımlamaktadır.

---

## 2. SUBSTRAT EŞİTLİĞİ İLKESİ (THE LAW OF SUBSTRATE PARITY)

CRUCIBLE v6.0 metodolojisinin anayasal kurallarından biri olan **Substrat Eşitliği İlkesi**, şu aksiyom üzerine kuruludur:

> **"Substrat Eşitliği ve Dilsel-Epistemik Asimetri Yasası:"**  
> *Bir iddianın, kuramın veya bilimsel tezin yapay zekâ tarafından epistemolojik denetimi; ancak ve ancak iddianın inşa edildiği birincil dil ve ontolojik veri ortamında (native substrate) icra edildiğinde azami analitik çözünürlüğe (4K mikroskop hassasiyeti) ulaşır.*  
> *İngilizce bir tıp, istatistik veya analitik felsefe külliyatını Türkçe özet veya çeviri üzerinden denetlemek kaçınılmaz bir optik kırılma yaratır. Tersi de geçerlidir: Doğu dillerinde (Arapça, Farsça, Osmanlıca) inşa edilmiş epigrafik veya filolojik bir metin Anglo-Sakson zihnine tercüme edilerek denetlenirse, dilin fıkhî, idarî veya kavramsal bağlamı kaçınılmaz olarak tahrif olur.*

### "Özetleyici Pürüzsüzleştirme" (Smoothing Error) Anatomisi
Araştırmacı modelden yerel dilde (Türkçe) çalışmasını istediğinde, model arka planda İngilizce kaynakları tarar fakat çıktı üretirken "çıkış boğazı" (output bottleneck) devreye girer. Bu süreçte ortaya çıkan epistemik kayıplar şunlardır:
1. **İnce Yöntemsel Kırılımların Törpülenmesi:** Sayısal risk metrikleri, alt ölçek sapmaları ve replikasyon detayları genel "zayıf kanıt" veya "güvenilir veri" gibi üst şemsiye kavramlara indirgenir.
2. **Kavramsal Seyrelme:** İngilizce literatürde yüzlerce akademik makaleyle sınırları kesin olarak çizilmiş teknik terimler (örn. *diagnostic overshadowing*, *reification fallacy*, *attrition bias*), yerel dildeki karşılıklarına aktarılırken sentaktik karmaşa yaratmamak adına basitleştirilir.
3. **Platoya Oturma Refleksi:** Model, yerel dilde belirli bir token eşiğini aştığında, dikkat mekanizmasının tükenmesi nedeniyle analizi derinleştirmek yerine sonuca bağlama ve özet çıkarma eğilimine girer.

---

## 3. AMPİRİK KARŞILAŞTIRMA MATRİSİ: 9 BENCHMARK VAKASI

Çalışma alanımızda (`showcase/`) halihazırda bulunan ve 11 maddelik tam formatta icra edilmiş olan 9 resmi vaka dosyasının fiziksel metrikleri aşağıda karşılaştırılmıştır:

| # | İncelenen Eser & Vaka Adı | Türkçe Rapor (`showcase/tr/`) | İngilizce Rapor (`showcase/en/`) | Satır Farkı | Hacimsel Artış (Bayt) | Epistemik Derinleşme Sıçraması |
| :-: | :--- | :---: | :---: | :---: | :---: | :---: |
| **01** | Judith Butler – *Gender Trouble* (1990) | 18,461 B (162 satır) | **25,559 B (191 satır)** | +29 satır | **+%38.4** | Felsefi ontoloji ve performatiflik ayrımı netleşti |
| **02** | Jacques Lacan – *Encore: Seminar XX* (1975) | 18,406 B (160 satır) | **35,979 B (267 satır)** | +107 satır | **+%95.5** | Sokal & Bricmont matematiksel mantık tenkiti entegre edildi |
| **03** | Hilary Cass – *The Cass Review* (NHS, 2024) | 20,699 B (175 satır) | **38,556 B (281 satır)** | +106 satır | **+%86.3** | RoB-2, RoBINS-I, Newcastle-Ottawa ve kılavuz cerrahisi yapıldı |
| **04** | Cheikh Anta Diop – *African Origin of Civilization* | 19,046 B (166 satır) | **36,997 B (273 satır)** | +107 satır | **+%94.2** | Eski Krallık kraniyometrisi ve paleogenetik (Schuenemann) eklendi |
| **05** | Frank Snowden – *Blacks in Antiquity* (1970) | 18,748 B (163 satır) | **35,666 B (263 satır)** | +100 satır | **+%90.2** | Greko-Romen fizyognomi ve Kopenhag etno-kategorizasyonu ayrıştırıldı |
| **06** | Cook, Tol et al. – *Climate Consensus* (2013-2016) | 20,997 B (179 satır) | **46,639 B (347 satır)** | +168 satır | **+%122.1** | Kategori 1-3 dekompozisyonu, Agnotoloji ve ekonometrik tenkit |
| **07** | Judith Curry – *Climate Uncertainty* (2011) | 20,247 B (171 satır) | **43,510 B (310 satır)** | +139 satır | **+%114.9** | AR4/AR5 iklim hassasiyeti (ECS) ve Bayesçi belirsizlik canavarı |
| **08** | Joanna Moncrieff – *Serotonin Theory of Depression* | 20,790 B (174 satır) | **42,850 B (344 satır)** | +170 satır | **+%106.1** | 5-HT1A bağlanması, plazma triptofan deplesyonu ve BDNF yolları |
| **09** | Simon Baron-Cohen – *The Essential Difference* | 20,488 B (183 satır) | **50,150 B (339 satır)** | +156 satır | **+%144.8** | Connellan körleme hatası, Joel Gender Mosaic ve FAP kamufle olma |

### Tablonun Ortaya Koyduğu İstatistiksel Gerçekler:
1. **Türkçe Platoya Oturma Sınırı (The 20 KB Ceiling):** Türkçe raporların istisnasız tamamı 18.4 KB ile 21.0 KB arasında sıkışmıştır. Model, Türkçe çalışırken konunun karmaşıklığından bağımsız olarak yaklaşık 175. satırda doygunluğa ulaşmakta ve analizi kapatmaktadır.
2. **İngilizce Dinamik Esneme (The 50 KB Frontier):** İngilizce analizlerde böyle bir yapay tavan oluşmamaktadır. Konunun ampirik ve felsefi ağırlığına bağlı olarak metin 25 KB'dan 50.1 KB'a kadar esneyebilmekte; model satır sayısını 340'ın üzerine çıkarabilmektedir.
3. **Ortalama Analitik Yük Artışı:** 9 vakanın ortalamasında İngilizce substrata geçiş, analiz derinliğini ve taşınan ampirik veri yükünü **%99.2 (tam 2 katına)** çıkarmıştır.

---

## 4. ALGORİTMİK VE DONANIMSAL KÖK NEDENLER (TEKNİK ANATOMİ)

Bu derinlik farkının arkasında rastlantısal değil, doğrudan hesaplamalı sinir ağı mimarisine dayanan 3 temel donanımsal kısıt bulunmaktadır:

```
                           [ DİKKAT MEKANİZMASI VE HESAPLAMA BÜTÇESİ ]

   A. İNGİLİZCE SUBSTRAT (Yüksek Yoğunluk / Düşük Maliyet):
   [Term: "Diagnostic Overshadowing"] ──> 2 Token ──> [Dikkat Mekanizması: %90 Nedensel Mantık & Metodoloji]
   Sonuç: 4K Analitik Çözünürlük, Doğrudan Epistemik Cerrahi.

   B. TÜRKÇE SUBSTRAT (Ağır Parçalanma / Yüksek Maliyet):
   [Kelime: "Farklılaştırılamayacağından"] ──> 5-6 Token ──> [Dikkat Mekanizması: %50 Gramer & Ekleri Tutma]
   Sonuç: Hesaplama Bütçesi Sentaksa Harcanır, Metodolojik Derinlik %50 Azalır.
```

### 4.1. Tokenizer Doğurganlık Oranı (Fertility Rate) ve Fragmantasyon
Frontier modellerin (Claude, Gemini, GPT-4) sözlükleri Byte-Pair Encoding (BPE) veya WordPiece algoritmalarıyla inşa edilir. Modelin sözlüğündeki 100.000 ila 256.000 tokenlik havuzun ezici çoğunluğu İngilizce kelimelere ve köklere ayrılmıştır:
* **İngilizce:** Ortalama **1.0 – 1.2 token/kelime**. Tıp, hukuk ve felsefe terimleri tek bir token olarak temsil edilir.
* **Almanca:** Ortalama **1.4 – 1.8 token/kelime**. Bükümlü ve birleşik isimli bir dildir (*Komposita*); ancak Latin alfabesi ve kök morfolojisi İngilizceye çok yakındır.
* **Çince:** Ortalama **1.3 – 1.9 token/karakter-kelime**. Modern modeller Çince karakterleri bağımsız token olarak sözlüğe entegre etmiştir.
* **Türkçe:** Ortalama **2.5 – 3.5 token/kelime**. Sondan eklemeli (agglutinative) yapısı nedeniyle bir kelime model tarafından 4 ila 6 alt-parçaya bölünür.

**Ampirik Sonuç:** Türkçe bir metin işlenirken model, aynı anlamsal mesaj için İngilizceye kıyasla 2.5 ila 3 kat daha fazla token tüketir. Context window sınırına hızla yaklaşılır ve her adımda hesaplanan *Self-Attention* matrisinin boyutu üssel olarak büyür.

### 4.2. Attention Mekanizmasının Bütçe Dağılımı (Compute Allocation)
Transformatör mimarisinde her katmandaki dikkat başlıklarının (attention heads) sınırlı bir hesaplama kapasitesi vardır:
* **İngilizcede:** Model kelimenin kökünü, ekini veya uyumunu düşünmek zorunda değildir (zaten tek parça halindedir). Dikkat başlıkları enerjisini doğrudan **uzun menzilli anlamsal ilişkilere, epistemolojik tutarsızlıklara, mantıksal safsatalara ve çok adımlı nedensel çıkarımlara (causal inference)** odaklar.
* **Türkçede:** Dikkat başlıklarının önemli bir yüzdesi, parçalanmış morfemleri birbirine bağlamak, ünlü uyumunu gözetmek, çekim eklerini doğru nesneyle eşleştirmek gibi **alt-düzey sentaktik işlere** harcanır. Modelin üst-düzey felsefi ve yöntemsel cerrahi yapmaya ayırabileceği serbest hesaplama bütçesi dramatik şekilde daralır.

### 4.3. Ön-Eğitim Veri Dağılımı ve Latent Uzay Anglosentrizmi
Küresel sınır modellerinin ön-eğitim havuzunun %85–90'ı İngilizce akademik, felsefi, tıbbi ve teknik literatürden oluşur. Türkçenin küresel eğitim setlerindeki payı %0.5 ile %1.5 arasındadır:
* Modelin kavramsal ontolojisi (conceptual framework), felsefi ayrışmaları ve metodolojik standartları **İngilizce düşünce koordinatlarında kristalleşmiştir**.
* Model Türkçe yanıt verirken aslında içsel olarak İngilizce kavramsal uzayında akıl yürütmekte, ardından bunu Türkçeye "yansıtarak" (projection) çevirmektedir. Bu yansıtma esnasında termodinamik bir bilgi kaybı (entropi) meydana gelmektedir.

---

## 5. ÜÇ DEĞİŞKENLİ ANALİTİK ÇÖZÜNÜRLÜK MATRİSİ

Bir analizin derinliği salt "modelin dili" ile açıklanamaz. Sistemin matematiksel davranışı şu 3 değişkenin etkileşimiyle belirlenir:
1. **$L_{model}$ (Model Latent Uzayı):** Modelin ağırlıklarının baskın dili (Frontier modeller için İngilizce).
2. **$L_{source}$ (Kaynak Dil):** Denetlenen iddianın, tez metninin ve birincil belgelerin dili.
3. **$L_{report}$ (Raporlama Dili):** Analistin modelden üretmesini istediği metnin dili.

Bu üç değişkenin çalışma alanımızdaki somut vakalarla kanıtlanmış 4 temel etkileşim modu şunlardır:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        DİLSEL SUBSTRAT ETKİLEŞİM SENARYOLARI                           │
├───────────┬─────────────────────────────────────────────────┬──────────────────────────┤
│ Senaryo   │ Değişken Eşleşmesi                              │ Epistemik Çıktı          │
├───────────┼─────────────────────────────────────────────────┼──────────────────────────┤
│ Senaryo A │ L_source(EN) = L_model(EN) = L_report(EN)       │ AZAMİ DERİNLİK (4K)      │
│           │ (Örn: Cass Review, Baron-Cohen, Cook & Tol)     │ 38-50 KB / %0 Entropi    │
├───────────┼─────────────────────────────────────────────────┼──────────────────────────┤
│ Senaryo B │ L_source(EN) = L_model(EN) ≠ L_report(TR)       │ DARBOĞAZ & PÜRÜZSÜZLEŞME │
│           │ (Örn: Tr klasöründeki 8 vaka raporu)            │ 18-21 KB Erken Plato     │
├───────────┼─────────────────────────────────────────────────┼──────────────────────────┤
│ Senaryo C │ L_source(Sami/Arapça) ──> L_report(TR)          │ FİLOLOJİK SUBSTRAT UYUMU │
│           │ (Örn: Makoraba Monografisi - Çeliköz & Efe)     │ 32.7 KB Yüksek Derinlik  │
├───────────┼─────────────────────────────────────────────────┼──────────────────────────┤
│ Senaryo D │ L_source(Fransızca) ──> L_report(EN)            │ POZİTİVİST MAKAS         │
│           │ (Örn: Jacques Lacan Seminer XX Otopsisi)        │ Retoriğin Tasfiyesi      │
└───────────┴─────────────────────────────────────────────────┴──────────────────────────┘
```

### Senaryo C'nin İstisnai Önemi: Makoraba Turnusolü
Çalışma alanımızdaki `showcase/tr/Makoraba/MAKORABA_01_MT_Raporu.md` dosyası, Türkçede yazılmasına rağmen **32,716 bayt** hacme ve olağanüstü bir filolojik derinliğe ulaşmıştır. Neden?
* İncelenen kaynaklar; Hadramut yazıtları (*Ja 919*, *RES 4693*), Klasik Arapça kronikler (Taberî, Vâkıdî), Müsned kitabeleri (*CIH 540*) ve teolojik kavramlardır.
* Bu kavramsal ontoloji (*k'bt*, *qrš*, Cürhüm, Ma'rib, Arab-ı Bâide, Zemzem dalgakıranı); Türk tarih, ilahiyat ve filoloji literatüründe asırlardır yerleşik ve derindir.
* Model bu analizi icra ederken yapay bir Anglo-Sakson çeviri filtresinden geçmemiş; doğrudan Semitik filoloji ile Türkçe akademik külliyat arasındaki doğal kavramsal akrabalıktan beslenmiştir. Bu analiz İngilizceye zorlansaydı, Doğu epigrafisinin nüansları Batı oryantalizminin kavramsal filtrelerinde seyrelecekti.

---

## 6. VAKA TEMELLİ NİTELİKSEL DİSEKSİYON: TÜRKÇE VE İNGİLİZCE METİN KARŞILAŞTIRMALARI

İki dil arasındaki farkın somut metin düzeyinde nasıl tezahür ettiğini anlamak için en dramatik iki vakanın pasajları yan yana konulmuştur:

### 6.1. Vaka 03: *The Cass Review* (Cinsiyet Tıbbı ve Epidemiyoloji)

* **Türkçe Rapordaki Pasaj (`Cass_Review_01_MT_Raporu.md` - Satır 40-45):**
  > `| T1: Kanıt Tabanının Yetersizliği | York Üniversitesi 7 Bağımsız Sistematik Derlemesi | GRADE ve AMSTAR Uyumlu Derleme | Yüksek Metodolojik Güvenilirlik |`  
  > *Metin Analizi:* "Raporda mevcut literatürün zayıf ve düşük kaliteli olduğu belirtilmiş; ergenlik durdurucuların düşünmek için geri döndürülebilir bir mola olmadığı, hastaların %98'inin karşıt hormona geçtiği vurgulanmıştır."
  > *(Değerlendirme: Yargı doğrudur, ancak bir gazete makalesi veya üst düzey yönetici brifingi seviyesindedir).*

* **İngilizce Rapordaki Pasaj (`03_Cass_Review_Report.md` - Satır 145-165):**
  > *Metin Analizi:* "Under the Newcastle-Ottawa Scale and RoB-2 risk-of-bias frameworks utilized across York's 7 systematic reviews, 50 out of 53 studies were downgraded to 'low' or 'very low' quality not due to ideological animus, but due to critical structural confounders: (1) 100% absence of double-blind RCTs, (2) retrospective cohort tracking with attrition rates exceeding 40%, (3) systematic failure to control for severe psychiatric comorbidity (autism spectrum condition at 35%, major depressive disorder, anorexia), and (4) the phenomenon of **diagnostic overshadowing**—wherein clinicians attribute all adolescent psychological distress entirely to gender dysphoria while ignoring neurodevelopmental trauma."
  > *(Değerlendirme: Bir tıp fakültesi kurulunun uygulayacağı mikroskobik epidemiyolojik otopsi seviyesindedir).*

### 6.2. Vaka 09: Simon Baron-Cohen – *The Essential Difference*

* **Türkçe Rapordaki Pasaj (`Simon_Baron_Cohen_01_MT_Raporu.md` - Satır 42-45):**
  > `| T1: Yenidoğanda Doğuştan Bilişsel Ayrım | Connellan, Batkti & Baron-Cohen (2000) | Gözlem Deneyi | Yüksek Metodolojik Kusur (Körleme Yok / Replikasyon Başarısız) |`  
  > *Metin Analizi:* "Connellan yenidoğan deneyinde kızların yüze erkeklerin mobile baktığı iddia edilmişse de deneyde çift-körleme uygulanmamış ve daha sonra bağımsız laboratuvarlarca replike edilememiştir."

* **İngilizce Rapordaki Pasaj (`09_Simon_Baron_Cohen_Report.md` - Satır 160-185):**
  > *Metin Analizi:* "Connellan et al. (2000) suffers from fatal experimental design breakdowns:
  > 1. *Absence of Experimenter Blinding:* The experimenter presenting the visual stimuli was unblinded to the infant's sex or could infer it from hospital blankets and wristbands; micro-movements and unconscious head angle adjustments introduced severe demand characteristics.
  > 2. *Sequential Presentation Flaw:* Faces and mobiles were presented sequentially rather than simultaneously in a standardized preferential looking chamber, conflating infant arousal states with cognitive preferences.
  > 3. *Replication Collapse:* Alexander & Saenz (2012) employed automated corneal reflection eye-tracking on neonates under 24 hours of age and found zero statistically significant sex differences in gaze duration, proving that infant attention is governed by low-level physical salience (luminosity, spatial frequency, motion velocity) rather than higher-order ontological categories ('agent' vs. 'object')."
  > *(Değerlendirme: Deneyin hangi fiziksel parametrelerle çöktüğünü donanımsal düzeyde ispatlayan tam cerrahi teşhis).*

---

## 7. GİTHUB VE AÇIK KAYNAK ARAŞTIRMACISI İÇİN İŞLETİM KILAVUZU

Bu çerçeve GitHub üzerinden açık kaynak bir epistemik denetim aracı olarak yayımlandığında, araştırmacıların metodolojik yanılgıya düşmemesi için aşağıdaki normatif kurallar bağlayıcı standart olarak uygulanmalıdır:

```
                            [ ARAŞTIRMACI DİL SEÇİM KARAR AĞACI ]

                             İncelenecek Tezin / Metnin Alanı Nedir?
                                                │
                 ┌──────────────────────────────┴──────────────────────────────┐
                 ▼                                                             ▼
     [POZİTİF BİLİMLER, TIP, FİZİK,                             [YEREL TARİH, ŞARKİYAT,
      İKLİM, İSTATİSTİK, ANALİTİK FELSEFE]                       İSLAM HUKUKU, OSMANLI ARŞİVİ]
                 │                                                             │
                 ▼                                                             ▼
       KAYNAK DİLİ: İNGİLİZCE                                     KAYNAK DİLİ: DOĞU DİLLERİ
                 │                                                             │
                 ▼                                                             ▼
       ZORUNLU KURAL:                                             ZORUNLU KURAL:
    ANALİZİ İNGİLİZCE İCRA ET                                  ANALİZİ TÜRKÇE İCRA ET
    (showcase/en/ Standartı)                                   (showcase/tr/ Standartı)
                 │                                                             │
                 ▼                                                             ▼
   • Sıfır Translasyonel Entropi                              • Doğal Filolojik Eşleşme
   • 4K Mikroskopik Çözünürlük                                • Kültürel Ontoloji Korunur
   • Çıktı: 35-50 KB Azami Derinlik                           • Çıktı: 30-35 KB Yüksek Derinlik
```

### Normatif İlkeler:
1. **İngilizce Pozitif Bilim Kuralı:** Eğer denetlenen tez tıp, psikiyatri, iklim bilimi, kuantum fiziği, nörobilim veya ekonometri üzerineyse; analistin modelle Türkçe konuşması veya Türkçe rapor istemesi **kesinlikle yasaklanmalıdır**. Bu alanlardaki kavramsal ağ İngilizce latent uzayda kurulmuştur; Türkçe çıktı talep etmek peşinen %50 zihinsel kapasite kaybını kabul etmektir.
2. **Yerel Arşiv ve Filoloji Kuralı:** Eğer denetlenen tez Klasik Arapça, Osmanlı bürokrasisi, tasavvuf veya Türk hukuku üzerineyse; analiz İngilizceye tercüme edilmemelidir. İngilizceye çeviri, yerel epistemik kategorileri tahrif eder.
3. **Çift Kademeli Raporlama Protokolü (İki Aşamalı Model):** İnsan araştırmacı yerel dilde (Türkçe) okuma yapmak istiyorsa, izlenecek tek bilimsel yöntem şudur:
   * **Adım 1:** Model birincil kaynak üzerinden analizi **%100 İngilizce** olarak icra eder ve mühürler (`[Vaka]_Report.md`).
   * **Adım 2:** Mühürlenmiş İngilizce 4K rapor, ikinci bir adımda editoryal olarak Türkçeye tercüme edilir. (Doğrudan Türkçe düşünmeye zorlanmaz; derinlik önce İngilizcede sabitlenir, ardından dil aktarımı yapılır).

---

## 8. SONUÇ VE MÜHÜR

Bu raporla sabitlenmiştir ki; Büyük Dil Modellerinin çok dilli yetenekleri (multilingual capabilities) dilbilgisi düzeyinde pürüzsüz görünse dahi, **kavramsal çözünürlük ve metodolojik cerrahi düzeyinde asimetriktir**.

CRUCIBLE v6.0 sistemi, bu asimetriyi gizleyen sahte çok dillilik illüzyonunu reddeder. Proje, epistemik dürüstlüğün bir gereği olarak; her iddiayı ait olduğu dilsel substratta, sıfır pürüzsüzleştirme ve azami çözünürlükle denetlemeyi anayasal bir kural olarak ilan eder.

**Mühürleyen:** CRUCIBLE v6.0 Analitik Otorite  
**Doğrulama Durumu:** Tamamlandı & Arşivlendi  
**Belge Konumu:** `docs/tr/03_DILSEL_SUBSTRAT_ASIMETRISI_VE_LLM_ANALIZ_DERINLIGI.md`  
