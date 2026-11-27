# CRUCIBLE v7.3 — Kaynak Metin Dayanaklı Epistemik Denetim Raporu (Vaka 06)

**İncelenen Eser:** John Cook, Dana Nuccitelli, Sarah A. Green, Mark Richardson, Bärbel Winkler, Rob Painting, Robert Way, Peter Jacobs & Andrew Skuce (2013) — *"Quantifying the consensus on anthropogenic global warming in the scientific literature"*, *Environmental Research Letters* 8:024024 (`doi:10.1088/1748-9326/8/2/024024`) `[P:0003]`  
**Denetleyen Yapay Zekâ Modeli:** Gemini 4 Hydrogen Extra High  
**Primary Audit:** ../en/06_Cook_Tol_Report.md  
**Birincil Kaynak Metin:** `Cook_2013_Environ._Res._Lett._8_024024.pdf` (`Cook_Indexed_Source.txt`, 9 İndeksli Paragraf `[P:0001]`–`[P:0009]`)  
**Analitik Standart:** CRUCIBLE v7.3 Çift Kademeli Yerelleştirme Protokolü (`L1–L5`, $L_{source} \equiv L_{audit} \rightarrow L_{target}$)  
**Operasyonel Statü:** Kademe 2 Doğal Türkçe Denetim Raporu (Tek-Belge Zemini; Ek Çevrimiçi Veri Setleri ve 2013 Sonrası Dış Eleştiriler `L5` Uyarınca Hüküm Dışı Bırakılmıştır)

> **Denetim Kokpiti (`L5` Odak İndeksi — Çıpalı `[P:xxxx]` Adresleri):**
> - **Hüküm Özeti:** İncelenen hakemli külliyatta antropojenik küresel ısınma (AGW) reddinin yok denecek kadar az olduğu (`78 / 11.944 = %0.7`) çekirdeği **Sağlam Şekilde Ayakta** (`[P:0003]`, `[P:0006]`); manşet `%97.1` oranının `>%50` birincil insan nedenselliğine eşitlenmesi **Büyük Revizyon** gerektirir (`[P:0004]`–`[P:0007]`).
> - **Ana Nicel Çıpalar:** `11.944` özet (`1991–2011`); Onay `%32.6 (3.896)` / pozisyon bildirenlerde `%97.1`; Görüş Yok `%66.4 (7.930)`; Ret `%0.7 (78)`; Belirsiz `%0.3 (40)` `[P:0003]`, `[P:0006]`; Öz-değerlendirme `2.142` makale (`8.547` davette `%14` yanıt oranı) -> Onay `%62.7 (1.342)` / pozisyonlarda `%97.2` `[P:0006]`–`[P:0007]`.
> - **3 Yapısal Yarılma:** (1) `Düzey 3 Örtük Onay` kategorisinin ayrı sayı verilmeden `>%50` ana tanımıyla tek sepette birleştirilmesi (`[P:0004]`–`[P:0006]`); (2) `%27`/`%33` -> `%11`/`%16` kodlayıcı uyuşmazlığında $\kappa$/$\alpha$ eksikliği ve `%14` anket yanıtında Tablo 5 `12 -> 39` (`3.25×`) ret sıçramasının örtük geçilmesi (`[P:0005]`–`[P:0007]`); (3) Tarama çerçevesi duyarlılığı (`11.944` vs `43.548` vs `128.440`) ve Oreskes `%75`–`%28` kırılganlığı (`[P:0008]`).
> - **Tek-Belge Sınırı (`L5`):** Doğrulanmamış harici dağılımlar ve dış literatür (`[DIŞ DOĞRULAMA ADAYI]`) hüküm bölümlerinden çıkarılmış, yalnızca `## 5. CERRAH DENETİM KARTI`'na yönlendirilmiştir.

---

## 1. EPİSTEMOLOJİK TRİYAJ

Katman aktivasyonu bu 7 sayfalık birincil makalenin yürüttüğü ampirik işlemlere dayanır (bibliyometrik veri tabanı filtrelemesi, çok-kodlayıcılı sıralı içerik analizi, doğrusal eğilim regresyonu ve yazar öz-değerlendirme anketi):

| Katman | Durum | Dahil Etme / Dışlama Metodolojik Gerekçesi |
| :--- | :---: | :--- |
| **K1: Epistemik Erdem ve Dalkavukluk Filtresi** | ✅ AKTİF | Zorunlu taban. Hem iklim fiziğini reddetmek için ölçüm kusurlarını istismar eden yaklaşımlara hem de `"%97"` metriğini eleştirilemez dogma sayan aktivist retoriğe karşı *Skeptical Science* kökenli gönüllü tasarım bağlamında denetim yapar (`[P:0004]`, `[P:0008]`). |
| **K2: Felsefi Yöntem (Çelik Adam & Yanlışlama)** | ✅ AKTİF | Zorunlu taban. Görüş bildirmeyen özetleri paydadan çıkarmanın olgun bilim paradigmasının normal bir yansıması mı yoksa mutabakat sınırlarını genişleten bir payda daraltması mı olduğunu yargılar (`[P:0007]`, `[P:0008]`). |
| **K3: Hermenötik, Kavramsal Hijyen ve Yapısal Güvence** | ✅ AKTİF | Çekirdek katman. Tablo 2'deki Düzey 1 (`>%50` birincil insan nedeni), Düzey 3 (`sera gazı emisyonlarının ısınmaya yol açtığını varsayar`) ve konsolide `Endorse AGW` başlıkları arasındaki kavramsal kaymayı denetler (`[P:0004]`–`[P:0006]`). |
| **K4: Nicel Metodoloji ve Bayesçi İstatistik** | ✅ AKTİF | Payda seçimi (`11.944` vs `4.014`), regresyon eğimleri (`R²`, `p`-değerleri), `2.142` öz-değerlendirme dağılımı, `%14` anket yanıt kaybı ve makale başına yazar sayısı farkları (`[P:0005]`–`[P:0007]`) için zorunludur. |
| **K5: Deneysel Tasarım ve Nedensellik** | ❌ DIŞLANDI | Çalışma tamamen gözlemsel bir bibliyometrik tarama ve gönüllü yazar anketidir; randomize klinik veya fiziksel deney düzeneği içermez. |
| **K6: Kanıt Hiyerarşisi ve Sistematik Derleme** | ✅ AKTİF | Web of Science eleme protokolü (`12.465 -> 11.944`), çift-kodlayıcı hakemlik prosedürü ve Oreskes (2004) / Schulte (2008) karşılaştırmalarını (`[P:0004]`–`[P:0008]`) denetler. |
| **K7: Karar Bilimi ve Açık Bilim** | ✅ AKTİF | Çalışmanın açık kamu politikası destek gerekçesini (`Ding et al 2011`, `Lewandowsky et al 2012` `[P:0003]`, `[P:0008]`) ve yayımlanan tablolardan alt-düzey ham sayılarının dışarıda bırakılmasını (`[P:0006]`) inceler. |
| **K8: Disipliner Matris ve Kaynak Tenkiti** | ✅ AKTİF | Bibliyometri, içerik analizi güvenilirliği ve anket metodolojisi ilkelerini yalnızca `[P:0001]`–`[P:0009]` içindeki atıflar üzerinden denetler. |
| **K9: Hesaplamalı Modeller ve Simülasyon** | ❌ DIŞLANDI | Makine öğrenimi sınıflandırıcısı veya iklim simülasyon modeli kullanılmamıştır; puanlamalar web arayüzüyle manuel yapılmıştır (`[P:0004]`). |
| **K10: Karmaşıklık, Genişletilmiş Etik ve Epistemik Otopsi** | ✅ AKTİF | Zorunlu taban. Hasar bilançosunu, ayakta kalan asgari çekirdeği, bilim iletişimi etiğini ve Cerrah Denetim Kartını sentezler. |

---

## 2. ÇELİK ADAM

En güçlü akademik formülasyonuyla yeniden kurulduğunda Cook et al. (2013), temel bir **bilim sosyolojisi sorusunu** yanıtlamak üzere tasarlanmıştır: Kamuoyu yoklamalarının (`%57–%60` ABD'de bilimsel anlaşmazlık algısı `[P:0004]`, `[P:0008]`) ve karşı-yorumların (`Oddie 2012`, `Allègre et al 2012` `[P:0008]`) öne sürdüğünün aksine, hakemli iklim literatüründe antropojenik küresel ısınmayı (AGW) aktif olarak reddeden büyük veya büyüyen bir bilimsel karşı-akım var mıdır?

1. **Hakemli Literatürde Aktif Reddin Sıfıra Yakınlığının Gösterilmesi (`[P:0003]`, `[P:0006]`):**  
   `1991–2011` arasında `'global climate change'` veya `'global warming'` taramasıyla ulaşılan `11.944` hakemli makalede (`1.980` dergide `29.083` yazar), kimlikleri gizlenmiş çift kodlayıcılar yalnızca `78` özetin (tüm özetlerin `%0.7`'si; görüş bildirenlerin `%1.9`'u; yazar bazında `124` kişi = `%0.4`) AGW'yi açık veya örtük biçimde reddettiğini saptamıştır (`[P:0005]`, `[P:0006]`). Üstelik `21` yıllık zaman serisinde öz-değerlendirmeli ret oranı istatistiksel olarak anlamlı biçimde gerilemiştir (`−0.25% ± 0.18% yr⁻¹`, `R² = 0.28, p = 0.01` `[P:0007]`); bu da "sapkın bilim insanlarının arttığı" iddiasını çürütür (`[P:0008]`).

2. **Suskun Özetlerin Payda Dışı Bırakılmasının Bilim Sosyolojisi Gerekçesi (`[P:0007]`, `[P:0008]`):**  
   Özetlerin `%66.4`'ünün (`7.930`) AGW konusunda tutum belirtmemesi bilimsel kararsızlık anlamına gelmez; Oreskes (`2007`) ve Shwed & Bearman (`2010`) atıflarıyla kurulduğu üzere, olgunlaşmış bilim dallarında araştırmacılar her özetin içine temel fizik aksiyomlarını yeniden yazmaz (`[P:0007]`). Yazarlar bu sosyolojik varsayımı boşta bırakmayıp 2. Aşamada doğrudan test etmiştir: özeti "Görüş Yok" sayılan makalelerde kendi tam metnini puanlayan yazarların `"53.8% were self-rated as endorsing the consensus"` bildirmesi (`[P:0006]`), aynı `2.142` makale alt kümesinde `"No position"` oranını `%62.5`'ten `%35.5`'e indirmiş (`Tablo 5` `[P:0007]`) ve pozisyon bildirenlerdeki oranı neredeyse birebir doğrulamıştır (özetlerde `%97.1` vs öz-değerlendirmede `%97.2` `[P:0003]`).

3. **Yazarların Kendi İhtiyat ve Sınır Şerhleri (`Şeytanın Savunmanı Kaydı`):**  
   Metinde zaten açıkça kabul edilen sınırlılıklar hakkaniyet gereği kayda alınır:
   - **Örneklem Kapsam Sınırı:** Yazarlar `"11 944 papers is only a fraction of the climate literature"` diyerek `'climate change'` (`43.548`) ve `'climate'` (`128.440`) taramalarının çok daha geniş olduğunu açıklar (`[P:0007]`–`[P:0008]`).
   - **Özet Kısalığı ve Muğlaklık:** Kısa özetlerin tam makale anlamını yansıtamadığını ve dil belirsizliği doğurduğunu kabul ederler (`[P:0008]`).
   - **Gönüllü Kökeni ve Yanlılık İtirafı:** Projenin *Skeptical Science* gönüllülerince yürütüldüğünü (`[P:0004]`), süreç içinde `"clarifications and amendments were required as specific situations presented themselves"` gerektiğini ve iki karşıt yanlılık riskini açıkça yazarlar: `"Two sources of rating bias can be cited: ﬁrst, given that the raters themselves endorsed the scientiﬁc consensus on AGW, they may have been more likely to classify papers as sharing that endorsement."` (`[P:0008]`) *(kodlayıcıların bizzat konsensüsü benimsemesi lehine kodlama eğilimi)* ve bunun tersi olan aşırı ihtiyatlılık / ESLD (`mean difference 0.6 in units of endorsement level` `[P:0008]`).

   **En Güçlü Çelik Adam Çekirdeği:** Düzey 1–3 alt kırılımlarından bağımsız olarak, taranan `'global warming'` / `'global climate change'` özetlerinde (`%0.7`) ve yanıt veren yazarlar arasında (`%1.8`) AGW reddinin aşırı küçük bir azınlık kaldığı savı ampirik olarak sağlam biçimde gösterilmiştir (`[P:0006]`–`[P:0007]`).

---

## HAKİKİ METODOLOJİK CERRAHİ

Yazarların önceden şerh düştüğü tüm hususlar dışarıda bırakıldığında, `[P:0001]`–`[P:0009]` metni içinde çözümsüz kalan **üç gerçek yapısal yarılma** tespit edilir:

### Yarılma 1: Yedi Kademenin Üç Sepete Sıkıştırılması ve Ana Eşik Tanımının Gizlenmesi (`K3`, `K4`, `K7`)
Bölüm 1 ve Yöntem, araştırmanın hedeflediği bilimsel konsensüs tanımını insan etkisinin ısınmanın yarıdan fazlasını oluşturmasına bağlar: `"in order to determine the level of scientific consensus that human activity is very likely causing most of the current GW (anthropogenic global warming, or AGW)"` (`[P:0004]`, Yöntemde anılan `2007 IPCC` ölçütü: `"humans are contributing more than 50% of global warming"` `[P:0004]`).

Tablo 2 bu ayrımı yedi sıralı basamağa ayırır `[P:0005]`:
- **Düzey (1) Nicel açık onay:** `"Explicitly states that humans are the primary cause of recent global warming"` `[P:0005]`
- **Düzey (2) Nicel olmayan açık onay:** `"Explicitly states humans are causing global warming or refers to anthropogenic global warming/climate change as a known fact"` `[P:0005]`
- **Düzey (3) Örtük onay:** `"research assumes greenhouse gas emissions cause warming without explicitly stating humans are the cause"` (Örnek: `". . . carbon sequestration in soil is important for mitigating global climate change"`) `[P:0005]`

Ancak Bölüm 3 bu yedi basamağı tek hamlede eritir:
> `"To simplify the analysis, ratings were consolidated into three groups: endorsements (including implicit and explicit; categories 1–3 in table 2), no position (category 4) and rejections (including implicit and explicit; categories 5–7)."` `[P:0005]` *(Analizi basitleştirmek amacıyla puanlamalar üç grupta birleştirilmiştir: onaylar [Tablo 2'deki 1–3 kategorileri, örtük ve açık dahil], görüş yok [kategori 4] ve retler [5–7].)*

1. **Düzey 1–3 ve 5–7 Alt Sayılarının Makaleden Çıkarılması:** Yedi sayfalık ana metnin ne Tablo 3'ünde (`[P:0006]`) ne de metninde `3.896` onay makalesinin kaç tanesinin **Düzey 1 (`>%50` birincil neden)**, kaç tanesinin ise **Düzey 3 (`örtük varsayım`)** olduğu yayımlanmıştır! Ayrıca Tablo 4 Dipnot `a–c` incelendiğinde `"Self-rated papers that endorse AGW have an average endorsement rating less than 4 (1 = explicit endorsement with quantification, 7 = explicit rejection with quantification)."` görülmektedir (`[P:0007]`). Dolayısıyla sera gazı etkisini yalnızca arka plan kabul eden bir etki/azaltım özeti (`Düzey 3`) ya da `3.5` puanlı bir öz-değerlendirme, `%97.1` / `%97.2` manşet payında `>%50` insan nedenselliğini ölçen `Düzey 1` çalışmasıyla birebir aynı ağırlığı taşır.
2. **Ölçüm Eşdeğerliği Çöküşü (`K3`):** `[P:0008]` içinde yapılan Oreskes (2004) kıyaslaması örtük kuralların sonucu ne kadar oynattığını bizzat ifşa eder: `"Oreskes determined that 75% of papers endorsed the consensus, based on the assumption that mitigation and impact papers implicitly endorse the consensus."` (`[P:0008]`), buna karşılık Cook et al.'ın aynı kümedeki bulgusu (`%28` onay ve `%72` görüş yok `[P:0008]`). Oreskes'in `%75`'i ile kendilerinin `%28`'i arasındaki uçurumun doğrudan "örtük varsayım" kodlamasından doğduğunu görürler; buna karşın Düzey 3 örtük varsayımları kendi `%32.6` / `%97.1` toplamına katıp ayrı basamak sayısını paylaşmazlar.
- **Bir Kavram, Bir Somut Örnek (Klinik Şiddet Sepeti Birleştirmesi):** Bir hastanenin *"başvuran hastaların %97.1'i kalp müdahalesi gerektirdi"* başlığı atıp, Kategori 1 *(açık baypas ameliyatı)*, Kategori 2 *(kolesterol ilacı reçetesi)* ve Kategori 3 *(kalp tanısı koymadan rutin tansiyon ölçümü)* sayılarını ayrı vermeden tek kovada toplaması, kamuoyunda ameliyat sıklığına dair doğrulanmamış bir ağırlık algısı doğurur.

---

### Yarılma 2: Kodlayıcılar Arası Güvenirlik Boşluğu, Taraf Gönüllü Eğimi ve Tablo 5 Asimetrisi (`K1`, `K4`, `K6`)
Makale araştırmanın *Skeptical Science* gönüllülerince yürütüldüğünü (`"This letter was conceived as a ‘citizen science’ project by volunteers contributing to the Skeptical Science website (www.skepticalscience.com)."` `[P:0004]`), `12` çekirdek gönüllünün oyların `%97.4`'ünü (`23.061` değerlendirme, diğer `12` kişi `%2.6 = 607`) yaptığını açıklar `[P:0004]`–`[P:0005]`. Verilen anlaşmazlık ve anket verilerini izleyelim (`[P:0005]`–`[P:0007]`):

> `"Initially, 27% of category ratings and 33% of endorsement ratings disagreed."` `[P:0005]`
> `"Following this, 11% of category ratings and 16% of endorsement ratings disagreed; these were then resolved by a third party."` `[P:0005]`
> `"We emailed 8547 authors an invitation to rate their own papers and received 1200 responses (a 14% response rate)."` `[P:0006]`

1. **Şansa Göre Düzeltilmiş Güvenirlik ve Hakem Yönü Eksikliği:** İlk turda onay puanlamalarının tam üçte birinde (`%33`) yaşanan uyuşmazlık, tartışma sonrası dahi `%16` düzeyinde (~`1.911` makalede üçüncü hakem kararı gerektirerek) kalmıştır (`[P:0005]`). Yalnızca ham yüzde vermek; şansa bağlı uyumu arındıran `Cohen kappa` veya `Krippendorff alpha` istatistiğini, çiftler arası hata matrisini ve üçüncü hakemlerin uyuşmazlıkları hangi yönde çözdüğünü gizler. Ek olarak `"No Position"` özetlerinin tamamı değil yalnızca `"a random sample of 1000 ‘No Position’ category abstracts"` (`[P:0005]`, toplamın `%12.5`'i) taranarak `4b Belirsiz` çıkarılmıştır (`[P:0005]`–`[P:0006]`).
2. **Düzeltilmemiş `%14` Anket Kaybı ve Tablo 5'te Göz Ardı Edilen `3.25×` Ret Artışı:** Yazarlar özetlerde "Görüş Yok" çıkanların yarıdan fazlasının yazarlarınca onay sayılmasına odaklanır (`"53.8% were self-rated as endorsing the consensus"` `[P:0006]`, `[P:0007]`) ve bunu yalnızca bilimsel çekingenliğin (`ESLD`) onayları düşük saymasına yorar (`[P:0008]`). Oysa `Tablo 5` `[P:0007]` iki yönlü bir tablo sunar:
   - Özet `Onay`: `791 (%36.9)` -> Öz-değerlendirme `1.342 (%62.7)` (**1.70 kat** artış; üstelik `791/2.142 = %36.9`'un genel `%32.6` oranının üzerinde olması onaylı makale yazarlarının biraz daha yüksek katıldığına işaret eder).
   - Özet `Ret`: `12 (%0.6)` -> Öz-değerlendirme `39 (%1.8)` (**3.25 kat** oransal artış—ve Tablo 4'te pozisyon bildiren yazarlar içinde ret `%2.8` / yanıtlayan kişilerde `%3.6` iken Tablo 3'te `%1.9` / `%1.2` idi!).
   Özet kodlamasının yalnızca onayları değil reddeden pozisyonları da daha yüksek bir oranda görünmez kıldığı (`12 -> 39`) Tablo 5'te açıkça görülmesine rağmen, Bölüm 4.1 (`[P:0008]`) bunu tek yönlü bir ESLD kanıtı olarak okur ve yanıt vermeyen `%86`'lık kitle için ağırlıklandırma düzeltmesi sunmaz.
- **Bir Kavram, Bir Somut Örnek (Çift Yönlü Kısaltmayı Tek Yönlü Yorumlamak):** Telgraf özetlerini tam mektuplarla kıyaslayıp, tam metinlerde olumsuz/eleştirel görüşlerin `3.25 kat`, övgülerin `1.70 kat` arttığını görürken yalnızca övgü kaybından şikâyet etmek, iki taraflı bilgi kaybının bir kanadını görmezden gelmektir.

---

### Yarılma 3: Tarama Çerçevesi Kırılganlığı ve Kamu Politikası İletişimi Köprüsü (`K2`, `K3`, `K7`)
Bölüm 3 ve Bölüm 5 arasındaki kapsam geçişine bakalım:

1. **Külliyat Kesiti Duyarlılığı (`11.944` vs `43.548` vs `128.440` `[P:0008]`):** Yazarlar dürüstçe aynı dönemde `'climate change'` aramasının `43.548`, `'climate'` aramasının ise `128.440` makale getirdiğini belirtirler (`[P:0008]`). Seçilen `11.944` makalelik kümenin daha geniş külliyatı (`%27.4` ve `%9.3`) yanlılıksız temsil edip etmediği sınanmamıştır. Üstelik `Schulte (2008)` karşılaştırmasında (`529` vs `539` makale; `0` vs `6` açık ret `[P:0008]`) farklılığın nedeni açıklanamamaktadır (`"the reason for this discrepancy is unclear"` `[P:0008]`).
2. **Betimsel Ölçümden Politik İletişime Geçiş (`[P:0003]`, `[P:0008]`):** Giriş ve Sonuç bölümleri bilimsel mutabakat algısını doğrudan iklim politikası desteğinin zorunlu şartı olarak konumlandırır: `"is a necessary element in public support for climate policy (Ding et al 2011)."` (`[P:0008]`). Koşullu `%97.1` / `%97.2` oranını politika iletişiminin merkezine koymak, kamusal dolaşımda iki temel şartın düşürülmesini kolaylaştırır: (i) özetlerin `%66.4`'ünün (`7.930/11.944`) AGW tutumu bildirmediği (`[P:0006]`) ve (ii) Düzey 3 örtük varsayımların da `Onay` payına sayıldığı (`[P:0005]`).
- **Bir Kavram, Bir Somut Örnek (Etikette Şartların Silinmesi):** Kampanya afişine *"Makalelerin %97.1'i Mutabakatta"* yazıp, *"pozisyon bildiren %33.6'lık dilim içinde, ısınmayı yalnızca arka plan varsayan örtük çalışmalar dahil"* şerhini teknik metinde bırakmak, koşullu oranı koşulsuz toplum algısına dönüştürür.

---

## SAFSATA AVI

Birincil metin (`[P:0001]`–`[P:0009]`) içindeki yapısal akıl yürütme aksaklıkları:

1. **Ölçüm Eşdeğerliği Çöküşü (`K3` / Operasyonel Kayma):** `Düzey 3 Örtük Onay` tanımını (`"assumes greenhouse gas emissions cause warming without explicitly stating humans are the cause"` `[P:0005]`) ana başlıkta hedeflenen `>%50` birincil insan nedenselliği teziyle (`[P:0004]`) aynı onay havuzunda eritmek ve ayrı sayıları yayımlamamak (`[P:0006]`).
2. **Koşullu Payda Belirsizliği (`K4`):** Özette `%32.6` ve `%97.1`'i yan yana verse de (`[P:0003]`), Sonuç ve politika mesajında (`[P:0008]`) yalnızca pozisyon-bildiren koşullu oranı ön plana çıkarmak.
3. **Tablo 5 Farklılaşmasının Tek Yönlü Okunması (`K1`, `K4`):** Özet-tam metin sıçramasını (`791 -> 1.342`) yalnızca `ESLD` yönlü onay eksikliği kanıtı sayıp (`[P:0008]`), retlerdeki `3.25×` artışı (`12 -> 39`, `[P:0007]`) çözümlememek.
4. **Şansa Düzeltmesiz Kodlama Güvenirliği (`K1`, `K6`):** *Skeptical Science* gönüllülerinin `%16`'lık çözümlenmemiş onay uyuşmazlığını (`[P:0005]`) $\kappa$/$\alpha$ katsayısı vermeden üçüncü hakemle kapatmak ve `6.930` nötr özeti örneklem dışı bırakmak.
5. **Betimsel Veriden Normatif Politika Köprüsü (`K7`):** Bibliyometrik sınıflandırmayı doğrudan kamu politikası desteği yaratma aracına bağlamak (`[P:0008]`).

---

## KATMAN 8: İDDİA-KAYNAK DENETİM MATRİSİ

`L5` Tek-Belge disiplini altında her temel iddianın birincil metin içindeki (`[P:0001]`–`[P:0009]`) gerçek dayanağı:

| Tez / İddia | Dayandığı Temel Kaynak | Kaynak Durumu & Türü | Metodolojik Hüküm |
| :--- | :--- | :--- | :--- |
| Pozisyon bildiren özetlerin `%97.1`'i AGW'yi onaylar (tüm `11.944` özetin `%32.6`'sı; `%66.4` görüş yok) (`[P:0003]`, `[P:0006]`) | Cook et al. (`2013`), Section `3.1`, Table 2, Table 3 (`[P:0005]`–`[P:0006]`) | `[BİRİNCİL VERİ]` — `11.944` Web of Science özeti (`23.668` ikili puanlama) | **Aritmetik Olarak Tutarlı / Alt Kırılım Gizli:** Birleştirilmiş gruplarda `3.896 / 4.014 = %97.06` doğrudur; ancak `Düzey 3 (örtük)` ile `Düzey 1 (>%50)` ayrı verilmediğinden (`[P:0005]`) nedensellik eşiği denetlenemez. |
| Hakemli literatürde AGW reddi yok denecek düzeydedir (`%0.7` özet / `%1.8` öz-değerlendirme) (`[P:0003]`, `[P:0006]`, `[P:0007]`) | Cook et al. (`2013`), Table 3 (`78`), Table 4 (`39`), Figure 2 (`p = 0.01`) (`[P:0006]`–`[P:0007]`) | `[BİRİNCİL VERİ]` — Körlenmiş özet taraması + yazar öz-puanlaması | **Sağlam Desteklenen Çekirdek:** `Schulte (2008)` (`%6` `[P:0008]`) duyarlılık farkı gözetilse bile taranan literatürde aktif ret son derece nadirdir (`<%2`). |
| Yazar öz-değerlendirmeleri (`%97.2`) suskun özetlerin çoğunlukla konsensüsü benimsediğini doğrular (`[P:0003]`, `[P:0006]`, `[P:0007]`) | Cook et al. (`2013`), Section `3.2`, Table 4, Table 5 (`53.8%` `[P:0006]`–`[P:0007]`) | `[ANKET VERİSİ]` — Gönüllü e-posta anketi (`1.200 / 8.547 = %14` yanıt oranı) | **Kısmen Destekli / Düzeltilmemiş Katılım Kaybı:** Tam metinlerin özetten fazla görüş içerdiğini gösterir; ancak `%86` yanıtsız grup ve Tablo 5'teki `12 -> 39` (`3.25×`) ret sıçraması modellenmemiştir. |
| Kodlayıcı ideolojisi ile bilimsel çekingenlik çoklu kör hakemlikle dengelenmiştir (`[P:0004]`, `[P:0005]`, `[P:0008]`) | Section 2; Section `4.1`; `Skeptical Science` (`[P:0004]`, `[P:0005]`, `[P:0008]`) | `[YÖNTEM BEYANI]` — Ham anlaşmazlık oranı (`%33` -> `%16`) | **Eksik Temellendirme (`K1`, `K6`):** Yazarların şeffaflığı yüksektir (`[P:0008]`), ancak $\kappa$/$\alpha$ yokluğu, hakem yönü eksikliği ve `6.930` nötr özetin incelenmemesi güveni sınırlar. |
| Olgun paradigma `%66.4` sessizliği açıklar ve `Oreskes (2004)` ile uyumludur (`[P:0004]`, `[P:0007]`, `[P:0008]`) | Oreskes (`2004`, `2007`); Shwed and Bearman (`2010`); Schulte (`2008`) `[P:0004]`, `[P:0007]`–`[P:0008]` | `[KARŞILAŞTIRMALI LİTERATÜR]` + `894` makale alt-küme denetimi `[P:0008]` | **Öğretici Yöntemsel Kıyaslama:** `1993–2003` Oreskes kümesinde ret çıkmadığını (`0 / 894`) doğrular; öte yandan `%75` vs `%28` farkı örtük kodlamaya hassasiyeti açığa vurur (`[P:0008]`). |
| `'global warming'` + `'global climate change'` (`11.944`) iklim literatürünü temsil eder (`[P:0004]`, `[P:0008]`) | Section `4.1` (`43 548` `'climate change'`, `128 440` `'climate'`) `[P:0008]` | `[BİBLİYOMETRİK TARAMA ÖLÇÜMÜ]` | **Kapsam Sınırı Teyidi:** Daha geniş `'climate change'` (`~%73` dışarıda) ve `'climate'` (`~%91` dışarıda) külliyatı test edilmeden bırakılmıştır. |

---

## 3. OTO-FALSİFİKASYON

Denetimin kendisini zorunlu 7 soruluk Bilişsel Öz-Denetim (`K2.9`) ve `L5` Tek-Belge şeffaflığına tabi tutuyoruz:

1. **Sorgulanmamış Varsayım Taraması:** Bu denetim ölçüm hassasiyetine (`Düzey 1` vs `Düzey 3`) ve anket yanıt kaybına (`%14`) odaklandı; bu tutum okuyucuda hakemli ret makalelerinin gerçek nadirliğini (`78 / 11.944` `[P:0006]`) küçültme riski doğurabilir. Kodlama eşiklerindeki pürüzler `78` makaleyi eşit ağırlıklı bir bilimsel bölünmeye dönüştürmez.
2. **Çelik Adam Adalet Testi:** Cook et al.'ın Düzey 3'ü `>%50` iddiasıyla karıştırdığını söyleyerek aşırı yüklenmiş olabilir miyiz? Adil savunma: Tablo 2 basamakları açıkça tanımlar (`[P:0005]`), Özetin ilk cümlesi `%97.1`'in hemen önünde `%32.6` ve `%66.4` rakamlarını yazar (`[P:0003]`), Tablo 3 sütunu ise başlığında `"% among abstracts with AGW position"` (`[P:0006]`) etiketini korur. Eleştirimiz yayımlanan metinden Düzey 1–3 alt kırılımının çıkarılmasına ve `%97` sayısının politik iletişimde merkezileştirilmesine (`[P:0008]`) yöneliktir.
3. **Bu Denetime Karşı En Güçlü Karşı-Argüman:** Yetkin bir bibliyometrist şu yanıtı verir: *İklim biliminde AGW'nin temel nedeni hakkında hakikaten yaygın bir çatışma olsaydı, reddeden makaleler `11.944` içinde `%0.7` oranında kalmaz ve makale başına yazar ortalaması `2.0` vs `3.4–3.6` düşüşü göstermezdi (`[P:0006]`); üstelik `3.25×` öz-puanlama sıçraması dahi ret oranını yalnızca `%1.8`'e (`39 / 2.142`) taşımaktadır (`[P:0007]`).* Dolayısıyla yönelim sonucu Düzey 1–3 sınır tartışmasından bağımsız olarak ayaktadır.
4. **Retorik ve Kanıt Ayrımı:** "Klinik Şiddet Sepeti" veya "Etiket Şartları" gibi örnekler pedagojik açıklamadır; çıkarıldıklarında dahi somut bulgular yerindedir: `%11`/`%16` çözülmemiş uyuşmazlık (`[P:0005]`), ayrıştırılmamış `3.896` toplamı (`[P:0006]`), `%14` anket yanıtı (`[P:0006]`), Tablo 5 `12 -> 39` sıçraması (`[P:0007]`) ve `43.548`/`128.440` tarama açığı (`[P:0008]`).
5. **Tek-Belge ve Ek Veri Sınırı (`L5` Şeffaflık Beyanı):** CRUCIBLE `L5` (`Alternatif 1`) uyarınca bu denetim **yalnızca** sunulan 7 sayfalık `Cook_2013` PDF metnine (`[P:0001]`–`[P:0009]`) ve yerleşik `Sınıf 1` ölçüm/anket kurallarına dayanır. `[P:0003]`, `[P:0005]`, `[P:0006]` ve `[P:0008]`'de bağlantısı verilen çevrimiçi ek veri dosyaları (`stacks.iop.org/ERL/8/024024/mmedia`), Düzey 1/2/3'ün ham makale sayıları ve 2013 sonrası ekonometrik eleştiriler (ör. *Tol*) bu PDF'te yer almadığından hüküm dışı bırakılmış ve `[DIŞ DOĞRULAMA ADAYI]` olarak Bölüm 5'e yönlendirilmiştir.
6. **Bayesçi İnanç Güncellemesi (Yalnızca Yön — K4.2.1):**
   - *Tez A ("Hakemli literatürde AGW'yi aktif reddeden makaleler ihmal edilebilir düzeydedir, <%2"):* Güven güçlü biçimde artar (**↑↑**), hem özet (`%0.7`) hem yazar öz-puanlamalarıyla (`%1.8`) desteklenir (`[P:0006]`–`[P:0007]`).
   - *Tez B ("Taranan özetlerin %97.1'i ısınmanın >%50'sinin insandan kaynaklandığını açıkça ölçmektedir"):* Güven keskin biçimde düşer (**↓↓**), çünkü Düzey 1–3 birleştirilmiş ve Düzey 3 örtük arka plan varsayımlarını içine almıştır (`[P:0005]`).
7. **Genellenebilirlik ve Zaman Sınırı:** Hüküm `1991–2011` Web of Science `'article'` külliyatındaki `'global warming'` / `'global climate change'` sorgusuyla sınırlıdır (`43.548` `'climate change'` / `128.440` `'climate'` dışarıda `[P:0008]`).

---

## 4. HASAR RAPORU

### Epistemik Hasar Tablosu ve Asgari İddia Çekirdeği (`K1.5`, `K10`)

| Denetlenen Bileşen | Denetim Sonrası Statü | Alınan Yapısal Hasarın Niteliği |
| :--- | :---: | :--- |
| **1. Düşük Ret Yaygınlığı Çekirdeği** *(AGW reddi `<%1` özet / `<%2` öz-değerlendirme)* | **AYAKTA (GÜÇLÜ)** | `11.944` özet (`78` ret, `%0.7` `[P:0006]`) ve `2.142` tam metin öz-puanlaması (`39` ret, `%1.8` `[P:0007]`) ile sağlam biçimde doğrulanmıştır. |
| **2. Birleştirilmiş `%97.1` / `%97.2` Sayısının `>%50` İnsan Nedenselliğine Eşitlenmesi** | **HASARLI (BÜYÜK REVİZYON)** | `1–3` kategorilerinin birleştirilmesi yayımlanan tablolarda **Düzey 1 (`>%50`)** ile **Düzey 3 (`örtük varsayım`)** paylarını gizleyerek (`[P:0005]`–`[P:0006]`) kamusal anlam taşmasına yol açmaktadır. |
| **3. Gönüllü Kodlayıcı Tarafsızlığı** | **KISMİ HASARLI** | `%16`'lık çözümlenmemiş onay uyuşmazlığı $\kappa$/$\alpha$ katsayısı verilmeden kapanmıştır (`[P:0005]`); taraf gönüllülük beyan edilmiş (`[P:0004]`, `[P:0008]`) ve `6.930` nötr özet yeniden örneklenmemiştir (`[P:0005]`). |
| **4. Yazar Öz-Puanlaması ve Politika Çerçevesi** | **KOŞULLU / ÇERÇEVE AŞIMI** | Tam metinlerin özetten fazla görüş içerdiğini (`%53.8` `[P:0006]`) gösterse de düzeltilmemiş `%14` yanıt oranı (`[P:0006]`), `3.25×` ret artışı (`[P:0007]`) ve normatif politika yönlendirmesi (`[P:0008]`) taşır. |

**Bilimsel Sağkalım İçin Asgari Epistemik Bedel:**
1. **Kategori Düzeylerini Ana Tabloda Ayrıştırmak:** **Düzey 1 (`>%50` açık nicel onay)**, **Düzey 2 (`nicel olmayan açık onay`)** ve **Düzey 3 (`örtük varsayım`)** sayılarını hem `%32.6` koşulsuz hem de `%97.1` koşullu paydalarla birlikte yayımlamak.
2. **Güvenirlik ve Yanıtsızlık Düzeltmesi Sunmak:** Cohen $\kappa$ / Krippendorff $\alpha$, üçüncü hakem dağılımı (`%16` kısım `[P:0005]`), yanıtsız `%86` eğilim analizi (`[P:0006]`) ve Tablo 5'teki `12 -> 39` ret artışını simetrik olarak raporlamak (`[P:0007]`).
3. **Manşet Dilini Sınırlandırmak:** Kamusal özeti *"tarama çerçevesinde pozisyon bildiren özetlerde açık veya örtük onay oranı %97.1 vs ret %1.9'dur (%66.4 tutumsuz)"* sınırına çekmek.

**Ayakta Kalan Asgari Çekirdek:** `1991–2011` arasında `'global warming'` veya `'global climate change'` sorgusuyla taranan `11.944` hakemli özette antropojenik küresel ısınmayı reddeden çalışmalar (`%0.7` özet; `2.142` öz-puanlamada `%1.8`) son derece küçük bir azınlıkta kalmaktadır; ancak `%97.1` başlık oranı, `>%50` nicel atıf çalışmalarını örtük arka plan varsayımlarıyla (`Düzey 3`) tek sepette birleştirmektedir.

---

## 5. CERRAH DENETİM KARTI

Dış İrade (İnsan Araştırmacı) için 3 dakikalık doğrulama protokolü:

- [ ] `[DIŞ DOĞRULAMA ADAYI]` **Çevrimiçi Ek Veri Tablosunu (`stacks.iop.org/ERL/8/024024/mmedia`) İndir:** `[P:0003]` ve `[P:0005]`'te atıflanan ham kodlama dosyasından Tablo 3'te (`[P:0006]`) birleştirilen **Düzey 1 (`>%50` açık)**, **Düzey 2**, **Düzey 3 (`örtük`)**, **Düzey 4a/4b** ve **Düzey 5–7** ayrı makale sayılarını çıkart.
- [ ] `[DIŞ DOĞRULAMA ADAYI]` **2013 Sonrası Harici Ekonometrik İtirazları (ör. Tol 2016 *ERL* Yorumu ve Cook et al. Yanıtları) Denetle:** Harici literatürde `23.668` kodlama üzerinde hesaplanan Krippendorff $\alpha$ güvenirlik değerlerini ve payda hassasiyet analizlerini kontrol et.
- [ ] `[DIŞ DOĞRULAMA ADAYI]` **Yazar Anketi Yanıtsızlık Eğilimini (`Table S1` & Anket Metni `[P:0005]`–`[P:0006]`) İncele:** `91` ülkeden gelen `1.189` yanıtçı yazarın (`%14` yanıt oranı), yanıt vermeyen `7.358` yazardan kurumsal veya coğrafi olarak ayrışıp ayrışmadığını ek tablolardan sorgula.
- [ ] **`Tablo 5` (`[P:0007]`) Çift Yönlü Özet Daralması Aritmetiğini Doğrula:** Öz-değerlendirmede `Onay` grubunun `791 -> 1.342` (`1.70×`), buna karşılık `Ret` grubunun `12 -> 39` (`3.25×`) oranında büyüdüğünü kontrol ederek özetlerin her iki yönde de tutum gizlediğini teyit et.
- [ ] **Tarama Kümesi Sınırlarını Kontrol Et (`[P:0008]`):** Bulgular tüm iklim bilimine genellenmeden önce Bölüm 4.1'deki `11.944` vs `43.548` (`'climate change'`) vs `128.440` (`'climate'`) farkını doğrula.
- [ ] **Ölümcül Yanlışlama Testini Uygula:** Kendine şu soruyu sor: *"Yalnızca Düzey 1 (`>%50` birincil insan nedenselliğini açıkça ölçen) makaleleri toplam `11.944` özet içine böldüğümüzde çıkan oran ile `Düzey 1–3`'ü pozisyon bildirenlere bölünce çıkan `%97.1` sayısı aynı olguyu mu, yoksa iki farklı kavramı mı ölçmektedir?"*
