# CRUCIBLE v6.0 METODOLOJİK ÖZEL RAPOR: İKİ KADEMELİ BORU HATTI VE SUBSTRAT DİNAMİKLERİ
**Rapor Kodu:** CRUCIBLE-PIPE-2026-02  
**Başlık:** Büyük Dil Modellerinde (LLM) Veri Çıkarımı (Extraction) ile Analitik İşletim (Execution) Arasındaki Epistemik Asimetri, Model Mimarisi Davranışı ve Fiyasko Önleme Protokolü  
**Tarih:** 2026-10-04  
**Analitik Motor:** CRUCIBLE v6.0 Epistemolojik Cerrahi Protokolü  
**Statü:** Mühürlendi & Arşivlendi (GitHub Açık Kaynak Çerçeve Belgesi)  

---

## 1. YÖNETİCİ ÖZETİ VE PROBLEM TANIMI

Büyük Dil Modellerini (LLM) akademik, bilimsel ve felsefi tezlerin epistemolojik denetiminde kullanan araştırmacıların düştüğü en ölümcül yanılgı, **"Tek Tuşla Sihir" (One-Shot Hallucination)** varsayımıdır. Bu varsayıma göre araştırmacı, yüzlerce sayfalık ham birincil kaynağı (monografi, klinik rapor, ekonometrik makale) modele tek bir prompt ile verir ve derinlemesine bir epistemolojik otopsi üretmesini bekler.

Bu yaklaşım ampirik olarak kanıtlanmıştır ki istisnasız her seferinde **epistemik bir fiyaskoyla** sonuçlanır:
1. Model devasa metin girdisi altında ezilerek doğrudan **"Özetleyici Pürüzsüzleştirme" (Smoothing Error)** refleksine sığınır.
2. Tezin dayandığı kırılgan mantıksal sütunlar, veri hileleri ve metodolojik boşluklar genel geçer şemsiye ifadelere indirgenir.
3. Rapor, 11 normatif katmandan oluşan bir diseksiyon yerine, 15–20 KB'lik yüzeysel bir gazete köşe yazısı seviyesine çöker.

CRUCIBLE v6.0 mimarisi, bu çöküşü önlemek için süreci **iki bağımsız, birbirini denetleyen kademeye (Two-Stage Pipeline)** ayırır:
* **Kademe 1:** Kaynak Veriyi Çekme (Extraction / Target Dossier İnşası)
* **Kademe 2:** Veriyi Modele Sürme ve Raporlama (Crucible Execution / 01_MT Raporu)

Bu rapor; söz konusu iki kademenin model mimarisi ($M$) ve dil substratı ($L$) ile girdiği çapraz etkileşimi, ortaya çıkan 4 temel operasyonel senaryoyu ve araştırmacı için bağlayıcı güvenlik protokolünü modellerden bağımsız (model-agnostic) olarak kurallaştırmaktadır.

---

## 2. İKİ KADEMELİ EPİSTEMİK BORU HATTI ŞEMASI

```
                      [ BİRİNCİL HAM METİN ]
                   (Kitap / Makale / Klinik Rapor)
                                 │
                                 ▼
   ┌───────────────────────────────────────────────────────────┐
   │ KADEME 1: KAYNAK VERİYİ ÇEKME (EXTRACTION / DOSSIER)      │
   ├───────────────────────────────────────────────────────────┤
   │ • Rol: Araçsal Veri Çıkarıcı (Instrumental Data Extractor)│
   │ • Görev: Yorum yapmadan saf iddia, alıntı ve veri fişi    │
   │ • Kritik Değişkenler: Alıntı sadakati, Çelik Adam inşası, │
   │   ve Substrat Paritesi (Orijinal lisanda cımbızlama).     │
   └─────────────────────────────┬─────────────────────────────┘
                                 │
                                 ▼
                    [ HEDEF TAHTASI (DOSSIER) ]
              (Standardize Edilmiş 6 Bölümlük Kanıt Fişi)
                                 │
                                 ▼
   ┌───────────────────────────────────────────────────────────┐
   │ KADEME 2: VERİYİ MODELE SÜRME (CRUCIBLE EXECUTION)        │
   ├───────────────────────────────────────────────────────────┤
   │ • Rol: Acımasız Analitik Otorite (Sycophancy-Free Auditor) │
   │ • Görev: 11 Normatif Katman, Matrisler, Safsata Avı,      │
   │   Oto-Falsifikasyon ve Cerrah Denetim Kartı üretimi.      │
   │ • Kritik Değişkenler: Matris taşıma direnci, donanımsal   │
   │   token bütçesi (Attention bütçesi tahsisi).              │
   └─────────────────────────────┬─────────────────────────────┘
                                 │
                                 ▼
   ┌───────────────────────────────────────────────────────────┐
   │ NİHAİ ÇIKTI: 4K AKADEMİK OTOPSİ (35–50 KB)                │
   │ Deterministik Python Linter [PASS] Mühürlü Rapor          │
   └───────────────────────────────────────────────────────────┘
```

---

## 3. KADEME 1 DİSEKSİYONU: KAYNAK VERİYİ ÇEKME (EXTRACTION)

Kademe 1, ham metindeki gürültüyü ayıklayıp tezin iskeletini ortaya çıkarma ameliyatıdır. Bu aşamada yapılan bir hata, sonraki tüm analizleri sakatlar ("Garbage In, Garbage Out").

### 3.1. Model Mimarisinin Veri Çekimine Etkisi:
* **Özetleme Refleksine Sahip Modeller:** Zayıf veya agresif hizalanmış (RLHF) modeller, yönerge ne kadar katı olursa olsun metni okurken "kendi kelimeleriyle özetleme" eğilimine girer. Örneğin tez ile antitez arasındaki diyalektik çatışmayı iki ayrı izole kuyu olarak görür; zıt metinleri birbirine bağlayan yapısal nedensellik damarlarını (örn. etiyolojik neden yokluğundan farmakolojik etkinsizlik türetme safsatası) tek potada eritemez. Doğrudan alıntı yapmak yerine parafraz yapar; bu da kanıtın mahkemeye sunulmadan önce bozulması demektir.
* **Yüksek Bağlamsal Sadakate Sahip Frontier Modeller:** Yazarın tezini karikatürize etmeden, yazarın bizzat kurabileceği en güçlü biçimde (Çelik Adam / Steelmanning) yeniden inşa eder. Metnin altındaki zayıf sütunları (kaba vekil veriler, confounding değişkenler) cerrahi bir isabetle işaretler.

### 3.2. Dil Substratının Veri Çekimine Etkisi (Substrat Paritesi Kuralı):
* **İngilizce Kaynakların Çevrilerek Çekilmesi Hatası:** İncelenen külliyat İngilizce iken veri Türkçe olarak çekilmeye zorlanırsa; tıp, biyometri veya analitik felsefe literatürüne çakılı hassas kavramlar (*Diagnostic Overshadowing*, *Attrition Bias*, *Preferential Looking Chambers*, *Inter-Rater Reliability*) daha ilk adımda sentaktik bir çorbaya dönüşür.
* **Anayasal Çözüm:** Kaynak metin hangi dildeyse, **veriler sıfır çeviriyle, tırnak içinde ve orijinal lisanında cımbızlanmalıdır**. Kanıt cımbızlanırken araya dilsel bir filtre sokulamaz.

---

## 4. KADEME 2 DİSEKSİYONU: VERİYİ MODELE SÜRME (CRUCIBLE EXECUTION)

Kademe 1'de üretilen Hedef Tahtası, CRUCIBLE protokolünün 11 normatif katmanına sürülür. Gerçek analitik yarılma bu safhada gerçekleşir.

### 4.1. Model Mimarisinin Format Taşıma Gücü:
* **Düşük Taşıma Kapasitesi:** Bazı modeller, CRUCIBLE'ın devasa tablo ve matris mimarisini uzun metin boyunca sürdüremez. Raporun ortalarında yorularak matrisleri çökerdir ve basit madde imlerine (bullet points) döner. Çürütme aşamasında mantıksal safsataları adlandırmak yerine genel geçer şikâyetler sıralar.
* **Yüksek Mimari Disiplin:** 11 maddelik mimariyi tavizsiz işletir. Tablo hücre hizalamalarını, nedensellik şemalarını ve oto-falsifikasyon katmanını eksiksiz korur.

### 4.2. Dil Substratının Donanımsal Tavanı (Attention Bütçesi ve Token Darboğazı):
CRUCIBLE benchmark monografilerinin ortaya koyduğu en temel donanımsal gerçek:
1. **Yerel Dil (Türkçe) Çıkış Darboğazı (~18–21 KB Platosu):**  
   Modelden analiz çıktısını Türkçe üretmesi istendiğinde, sondan eklemeli morfoloji nedeniyle token tüketimi kelime başına 2.5–3.5 tokene fırlar. Modelin *Self-Attention* mekanizmasının hesaplama bütçesinin yaklaşık %50'si dilbilgisini, ekleri ve sentaksı ayakta tutmaya harcanır. Model ~175. satıra ulaştığında dikkat bütçesi tükenir; analizi derinleştiremez ve erken doygunluk platosuna oturarak raporu kapatır.
2. **Native Substrat (İngilizce) Dinamik Esneme (35–50 KB 4K Çözünürlük):**  
   İngilizcede token yoğunluğu 1.0–1.2 token/kelimedir ve küresel modellerin latent uzayı %85–90 İngilizce ile eğitilmiştir. Model hesaplama bütçesinin %90'ını doğrudan felsefi, mantıksal ve istatistiksel cerrahiye ayırır. Analiz 50 KB'a kadar esneyebilir; en ince replikasyon çöküşleri ve matematiksel formüller eksiksiz dökülür.

---

## 5. DÖRT TEMEL OPERASYONEL SENARYO MATRİSİ

Boru hattındaki iki kademenin ve değişkenlerin çaprazlanması şu sonuçları doğurur:

| Senaryo | Kademe 1: Veri Çekimi | Kademe 2: Analiz İşletimi | Ortaya Çıkan Epistemik Çıktı | Hüküm |
| :---: | :--- | :--- | :--- | :--- |
| **Senaryo I** | Özetleyici Refleks / Türkçe | Düşük Sadakat / Türkçe Substrat | **Tam Epistemik Çöküş:** Gazete brifingi seviyesinde yüzeysel metin, kayıp matrisler, <20 KB erken doygunluk. | **KABUL EDİLEMEZ** |
| **Senaryo II** | Yüksek Sadakat / İngilizce | Düşük Sadakat / Türkçe Substrat | **Girdisi Zengin Ama Çıktısı Boğulmuş:** Kanıtlar doğru cımbızlansa da, model çıktıyı Türkçe dil darboğazına ve özet refleksine kurban eder (~20 KB). | **VERİMSİZ** |
| **Senaryo III** | Yüksek Sadakat / İngilizce | Yüksek Disiplin / Türkçe Substrat | **Felsefi Olarak Sert Ama Hacimce Sıkışık:** Güçlü bir retorik ton yakalanır; ancak token darboğazı nedeniyle derin teknik ve sayısal detaylar seyreler (~21–25 KB). | **SINIRLI GEÇERLİ** |
| **Senaryo IV** | **Yüksek Sadakat / Orijinal Dil (Native)** | **Yüksek Disiplin / İngilizce Substrat** | **4K HAKİKİ CRUCIBLE RAPORU:** 35–50 KB, sıfır pürüzsüzleştirme, 11 maddelik mimari kusursuz ayakta, tam donanımsal mikroskopik cerrahi. | **ALTIN STANDART** |

---

## 6. GİTHUB ARAŞTIRMACISI İÇİN BAĞLAYICI DOKTRİN

Açık kaynak CRUCIBLE motorunu kullanan araştırmacıların fiyasko yaşamasını önlemek için şu anayasal kurallar bağlayıcıdır:

1. **İki Kademeli Protokol Zorunludur:** Ham PDF asla doğrudan analiz motoruna verilmez. Önce `templates/CRUCIBLE_EXTRACTION_DIRECTIVE.md` ile **Hedef Tahtası** çıkarılır, ardından analiz motoruna sürülür.
2. **Substrat Paritesi:** İngilizce literatür incelenirken analiz dili zorla Türkçeye çevrilemez. Süreç İngilizce işletilir ve 4K rapor mühürlenir.
3. **İki Aşamalı Editoryal Çeviri:** Eğer araştırmacı veya kurum yerel dilde (Türkçe) rapor okumak istiyorsa; model doğrudan Türkçe düşünmeye zorlanmaz. Önce Senaryo IV ile İngilizce 4K rapor üretilir ve mühürlenir; ardından bu mühürlü rapor editoryal olarak Türkçeye aktarılır.
4. **Model Yetkinlik Eşiği:** Model isimleri değişken ve geçicidir. Araştırmacı; özetleme refleksi asgari düzeyde olan, katı tablo ve matris disiplinine riayet eden, yüksek bağlam pencereli Frontier LLM sınıflarını tercih etmelidir.

---
**Mühürleyen:** CRUCIBLE v6.0 Analitik Otorite  
**Belge Konumu:** `docs/tr/05_IKI_KADEMELI_BORU_HATTI_VE_SUBSTRAT_DINAMIKLERI.md`  
