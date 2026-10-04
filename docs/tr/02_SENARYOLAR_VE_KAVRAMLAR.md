# CRUCIBLE v6.0 TRİYAJ MATRİSİ VE KAVRAMLAR SÖZLÜĞÜ (MAYIN TARLASI MODELİ)
### Operasyonel Senaryolar, Disipliner Sınır Protokolleri ve İçtihatlar (Ek-1)
*(Uluslararası Açık Kaynak Adı: **CRUCIBLE** | Özgün Kurucu Mimari: **Mayın Tarlası Modeli**)*

Bu referans belgesi, [CRUCIBLE v6.0 Metodoloji Anayasası](01_ANALITIK_YONTEM_ILKELERI_v6.md) metninde geçen tüm teknik terimlerin, felsefi kavramların ve istatistiksel kuralların somut, laboratuvar veya masa başı senaryolarla açıklanmış kapsamlı bir sözlüğüdür. V6.0 Kılavuzunun 10 katmanlı mimarisine uyumlu olarak tasarlanmıştır.

---

## 📌 EPİSTEMOLOJİK TRİYAJ (KATMAN SEÇİM SAVUNMASI)

Bir araştırma yaparken v4.0 Kılavuzundaki 10 katmanın tamamı aynı anda uygulanamaz. Hangi katmanların kullanılacağını belirleyen şey, verinin dış görünüşü (örneğin salt rakam içermesi) değil, araştırmacının o veriden **ne tür bir sonuç (inference)** çıkarmaya çalıştığıdır. 

Bu nedenle kılavuz, mekanik bir "katman haritası" sunmak yerine, araştırmacıyı analize başlamadan önce şu **Epistemolojik Triyaj (Ön Savunma)** testinden geçmeye zorlar:

1. **Katman Seçimi:** Bu spesifik iddiayı ispatlamak için 10 katmandan hangilerini aktif ediyorum? (Örnek: Şiirdeki kelime sayısını analiz etmek için Katman 3 Hermenötik).
2. **Dışlama Savunması (Oto-Falsifikasyon Uygulaması):** İlgili görünmesine rağmen *neden* bazı katmanları DIŞARIDA bıraktım? 
   > *Soru:* "Veride 16 kelime gibi rakamlar olmasına rağmen neden Katman 4'ü (İstatistik/Bayes) açmadın?"
   > *Savunma:* "Çünkü bir şiirdeki kelime frekansı, evrensel veya istatistiksel bir popülasyon (örneklem) değil, tekil bir estetik tercihtir. Burada P-Value hesaplamak metodolojik bir safsata olurdu."

Bu kural, Katman 2'deki **Oto-Falsifikasyon** ilkesinin, bizzat Kılavuzun kendisine (yöntem seçimine) uygulanmış halidir: *Sadece neyi neden seçtiğini değil, neyi neden seçmediğini de kanıtla!*

### 📌 TRİYAJ YARDIM TABLOSU (Araştırmacı Kopya Kağıdı)
Araştırmacının "Neden seçtim / Neden dışladım" savunmasını yaparken karanlıkta kalmaması için en kritik katmanların epistemolojik gerekçeleri şunlardır:

| Katman | Neden Seçmelisin? (Tetikleyici Gerekçe) | Neden Dışlamalısın? (Dışlama Savunması) |
|---|---|---|
| **K1: Persona & Epistemik Erdem** | Konu ne olursa olsun (fizik, tarih, şiir veya teoloji), **daima ve istisnasız** seçilmelidir. Araştırılan nesne dogmatik veya sanatsal olsa bile, o nesneyi analiz eden "ben"in kendine ve konuya karşı acımasız dürüstlüğü (epistemik erdemi) şarttır. | **HİÇBİR ZAMAN DIŞLANAMAZ.** Bilimsel veya analitik bir inceleme yapıyorsanız, kendi önyargılarınıza karşı dürüstlük şalterini asla indiremezsiniz. Katman 1'in dışlandığı yer araştırma değil, propagandadır. |
| **K2: Felsefi Yöntem (Çelik Adam & Falsifikasyon)** | Çalışmanız mevcut bir tezi/düşünceyi eleştiriyorsa (Çelik Adam zorunludur) veya iddialı yeni bir teori kuruyorsa (Oto-Falsifikasyon zorunludur) mecburen açılır. Katman 1'deki niyetin sahaya sürülmüş kılıcıdır. | Sadece yorumsuz, mekanik veri aktarımlarında (Örn: Ham sensör logları, hava durumu verisi) dışlanabilir. **DİKKAT:** Beşeri bilimlerde "saf envanter/katalog" diye bir şey yoktur. "X nesnesi bu envantere girmeli mi girmemeli mi?" sorusu bile örtük bir argümandır ve K2'yi (Çelik Adam/Falsifikasyon) zorunlu kılar. |
| **K3: Hermenötik & Tutarlılık** | Sadece metinlerde değil; ampirik bulguların (DNA, Karbon-14, Arkeoloji) tarihsel "anlamını" yorumlarken de seçilmelidir. Ampirik veri fiziksel gerçeği, hermenötik ise o gerçeğin insanlık tarihindeki anlamını verir. | İddia yoruma kapalı, sadece matematiksel/fiziksel bir ölçüm bildirimi ise (Örn: "Bu kemik 4000 yıllıktır") dışlanır. Ancak "Demek ki o kavim oraya göçtü" dendiği an yorum (hermenötik) mecburen başlar. |
| **K4: İstatistik & Bayes** | Analiz; anketler, demografik yığınlar (popülasyon), klimatolojik seriler veya nicel korpus madenciliğine dayanıyorsa. | Veri tekil, emsalsiz bir tarihsel olguysa (tek bir mektup), nicel değil nitel (anlamsal) bir estetik tercihse dışlanır. |
| **K5: Nedensellik & Karıştırıcı Değişken** | İddianın içinde gizli veya açık *"A olayı B'ye yol açtı / B'yi etkiledi"* şeklinde bir fiil zinciri varsa. | İddia sadece durumu tasvir ediyorsa veya A ve B olaylarının eşzamanlılığı (korelasyon) bir sebep-sonuç bağlamı olmadan anlatılıyorsa dışlanır. |
| **K6 & K7: Retorik ve Yasaklı İfadeler** | İstisnasız her analitik/akademik metinde **daima** devrededir. Hamasetin, "kesinlikle", "şüphesiz ki" gibi dogmatik kelimelerin veya yazarın "akademik belagat" tuzağının metne girmesini engeller. | **HİÇBİR ZAMAN DIŞLANAMAZ.** Eğer araştırmacı nesnel bir analiz yerine lirik bir şiir veya politik bir manifesto yazmıyorsa, retorik denetimi asla kapatılamaz. |
| **K8: Disipliner Matris** | Yazar kendi ana uzmanlık alanından çıkıp (örneğin tarihçi) başka bir sahanın (örneğin tıp/psikoloji) bulgularını kullanıyorsa. | Araştırma %100 tek bir mikro-disiplinin kendi saf sınırları içinde yapılıyorsa pasife alınır. |
| **K9: Hesaplamalı Bilimler, AI ve Modelleme** | Araştırmada gerçeği simüle eden bir **model** (Örn: GIS coğrafi haritalaması, iklim simülasyonları, yapay zeka veya algoritmik bir hesaplama) kullanıldığında tetiklenir. Çıktıya körü körüne inanmayı (Kara Kutu safsatası) engeller. | Araştırma dışsal bir simülasyon, algoritma veya model üretimine dayanmıyorsa (Örn: Sadece kavramsal felsefi bir okuma yapılıyorsa) dışlanır. |
| **K10: Raporlama ve İtiraflar** | Çalışmanın bittiği ve sonuçların okuyucuya sunulacağı son aşamada **daima** devrededir. Araştırmacıyı zayıflıklarını, limitlerini ve bulamadıklarını (Post-Mortem) itiraf etmeye zorlar. | Eğer çalışma henüz "taslak (draft)" veya "veri toplama" aşamasındaysa, yani henüz sonuçlandırılmamışsa dışlanabilir. |

---

## 📌 KATMAN 1-2: FELSEFİ YÖNTEM VE SAFSATALAR SÖZLÜĞÜ

### 1.1. Epistemik Alçakgönüllülük (Epistemic Humility)
**Tanım:** Kendi bilgisinin sınırlarını bilme ve "bilmiyorum" demeyi zayıflık değil, metodolojik dürüstlük sayma ilkesidir.
> **Senaryo:** Bir AI modeli veya araştırmacı, "Kuantum bilincin temelidir" hipotezini incelerken, kuantum fiziği hakkında sadece popüler bilim okumuşsa: 
> *İhlal:* "Penrose kesinlikle haklıdır, mikrotübüller ruhun yuvasıdır." 
> *Analitik Doğru:* "Kuantum biyolojisi alanında uzman değilim, ancak Penrose'un iddialarının fizikçiler (ör. Max Tegmark'ın dekoherans süreleri hesaplaması) tarafından şiddetle reddedildiğini biliyorum. Dolayısıyla bu tezi 'kesin' kabul edemeyiz."

### 1.2. Oto-Falsifikasyon (Öz-Çürütme Testi)
**Tanım:** Bir kişinin kendi savunduğu tezi çökertmeye yetecek en güçlü argümanı bizzat kendisinin arayıp bulmasıdır.
> **Senaryo:** Bir felsefeci "Özgür irade tamamen bir yanılsamadır, her şey deterministiktir" tezini savunmaktadır.
> *Oto-Falsifikasyon Uygulaması:* "Eğer tezim doğruysa ve her şey atomların çarpışmasından ibaretse, şu an yazdığım makalenin 'doğru' veya 'mantıklı' olduğu iddiası da sadece kimyasal bir reaksiyondur. O halde 'doğruluk' kavramı anlamını yitirir (Performatif Çelişki). Bu, tezimin en zayıf noktasıdır ve buna cevap vermeden tezimi ispatlamış sayılmam."

### 1.3. Çelik Adam (Steelmanning) vs. Saman Adam (Straw Man)
**Tanım:** Karşıt argümanın en zayıf halini (Saman Adam) değil, en güçlü halini (Çelik Adam) inşa edip ona saldırma ilkesi.
> **Kötü Örnek (Saman Adam):** *Evrimsel psikologlar, insanın sadece tecavüz ve cinayete programlı vahşi robotlar olduğunu iddia ederler. Oysa aşk ve sanat var, demek ki evrimsel psikoloji saçmadır.* (Bu, düşmanı bilerek zayıflatmaktır).
> **İyi Örnek (Çelik Adam):** *Evrimsel psikolojiye göre insan davranışı, avcı-toplayıcı atalarımızın hayatta kalma sorunlarını çözmek üzere evrimleşmiş nöral adaptasyonların ürünüdür. Aşk ve sanat bile, cinsel seçilimde bir "fitness göstergesi" olarak açıklanır. Bu son derece rasyonel bir modeldir. ANCAK, nöroplastisite kanıtları bu modelin aşırı genetik-determinist yönlerini zayıflatmaktadır...*

### 1.4. Seçilmiş Safsata Örnekleri (Fallacy Dictionary)
*   **Boşlukların Tanrısı (God of the Gaps):** "Bilinç neden var bilmiyoruz. Kuantum mekaniği de çok gizemli. Demek ki bilinç kuantumdur!" (Bilinmeyeni, başka bir bilinmeyenle yamamak).
*   **Non Sequitur (Alakasız Sonuç):** "Algılarımız evrimsel olarak gerçeği birebir yansıtmaz. O halde hiçbir şey gerçek değildir, dış dünya yoktur!" (Öncülden, o sonucu doğurmayacak aşırı bir çıkarım yapmak).
*   **Performatif Çelişki:** "Bütün iddialar güç ilişkilerinden ibarettir ve nesnel doğru yoktur!" (Peki bu cümlenin kendisi nesnel bir doğru mu, yoksa yazarın güç arayışı mı?)

---

## 📌 KATMAN 4: NİCEL İSTATİSTİK VE OLASILIK

### 4.1. Bayesçi Güncelleme (Bayesian Updating)
**Tanım:** İnançlarımızın (hipotezlerin), yeni veriler geldikçe kesinlikle reddedilmesi veya körü körüne savunulması yerine, matematiksel bir oranda (Prior x Likelihood) sürekli "güncellenmesi" kuralıdır.
> **Adım Adım Senaryo (Bilinç Araştırması):**
> 1. **Prior (Ön-İnanç):** "Ben, bilincin ruhsal/bölünemez bir öz olduğuna %90 oranında inanıyorum."
> 2. **Likelihood (Yeni Kanıt):** Nöroloji laboratuvarından "Ayrık Beyin (Split-Brain)" hastalarının raporu gelir. Beynin ortası kesildiğinde, sağ ve sol el birbirine zıt kararlar vermekte, içeride iki farklı "istek" belirmektedir.
> 3. **Posterior (Güncelleme):** "Eğer bilinç bölünemez, ruhi bir şey olsaydı neşterle ikiye bölünmesi imkansız olurdu. Bu veri ışığında inancımı %90'dan %30'a düşürüyorum ve bilincin nörolojik olduğu inancını %70'e çıkarıyorum."

### 4.2. P-Value (Anlamlılık) vs. Etki Büyüklüğü (Manidalık)
**Tanım:** İstatistiksel olarak var olduğu kanıtlanan bir etkinin (p<0.05), gerçek dünyada dikkate değer büyüklükte olmama (Effect Size) ihtimalidir.
> **Senaryo (Antidepresan Testi):**
> Bir şirket 500.000 kişi üzerinde test yapar. İlaç alanların depresyon skoru (100 üzerinden) 45'e, almayanların 46'ya düşmüştür. Örneklem o kadar devasadır ki, istatistik bu 1 puanlık farkı "Kesinlikle tesadüf değil (p<0.001)" olarak onaylar. 
> *İhlal:* "İlacımız istatistiksel olarak kesinlikle işe yarıyor!"
> *Analitik Gerçek:* Evet, tesadüf değil ama *Etki Büyüklüğü (Cohen's d)* sıfıra yakın. Yani pratikte 1 puanlık iyileşmenin hasta için hiçbir *manası* (Manidalık) yoktur.

### 4.3. WEIRD Problemi (Western, Educated, Industrialized, Rich, Democratic)
**Tanım:** Dünya nüfusunun sadece %12'sini oluşturan Batılı/Zengin üniversite öğrencilerinden alınan verilerle, "tüm insanlık böyledir" diye evrensel kural uydurma hatasıdır.

---

## 📌 KATMAN 5: DENEYSEL TASARIM VE NEDENSELLİK

### 5.1. Operasyonel Tanım (Operationalization)
**Tanım:** Soyut felsefi kavramları laboratuvara sokabilmek için, onları "ölçülebilir ve gözlemlenebilir" fiziksel/matematiksel birimlere çevirmektir.
> **Senaryo:** "Aşk" veya "Bilinç" araştırılacaktır.
> *Kötü Yöntem:* İnsanlara "Bilinçli hissediyor musun?" diye sormak.
> *İyi Yöntem (Operasyonel Tanım):* Bilinci; "Transkraniyal Manyetik Uyarım (TMS) verildiğinde beyindeki EEG karmaşıklık skoru (PCI endeksi > 0.31)" olarak formüle etmek. Bu tanım bilincin tamamı değildir, sadece laboratuvardaki "ölçülebilir izdüşümüdür".

### 5.2. Karıştırıcı Değişken ve Bradford Hill Kriterleri (Korelasyon ≠ Nedensellik)
**Tanım:** İki olayın aynı anda artması, birinin diğerine sebep olduğunu göstermez. Üçüncü bir gizli değişken (Confounder) her ikisini de yönetiyor olabilir.
> **Senaryo (Dondurma ve Boğulma):**
> *Veri:* Yaz aylarında dondurma satış grafikleri ile denizde boğulma grafikleri birebir aynı oranda (mükemmel korelasyon) artmaktadır.
> *İhlal:* "Dondurma yemek suda boğulmaya neden olur!"
> *Analitik Gerçek:* Gizli Karıştırıcı Değişken (Confounder) **"Hava Sıcaklığı"**dır. Sıcak oldukça dondurma yenir, sıcak oldukça denize girilir (ve doğal olarak boğulma riski artar). Dondurma ile boğulma arasında korelasyon vardır, ama *nedensellik* yoktur.

---

## 📌 KATMAN 6-7: META-ANALİZ VE AÇIK BİLİM

### 6.1. Yayın Yanlılığı (Publication Bias) ve Dosya Çekmecesi Problemi
**Tanım:** Bilimsel dergilerin sadece "ilginç ve işe yarayan (pozitif)" sonuçları yayınlamayı sevmesi, işe yaramayan (negatif) sonuçların ise rafa kaldırılması krizidir.
> **Senaryo:** "Meditasyon zekayı artırır mı?" diye dünyada 100 farklı deney yapılır. 95'inde hiçbir işe yaramadığı (negatif sonuç) görülür ve akademisyenler bunları rafa kaldırır. Sadece 5'inde (tesadüfen) işe yarar görünür ve dergiler sadece bu 5 makaleyi yayınlar. Dışarıdan bakan bir okuyucu literatüre girdiğinde sadece o 5 makaleyi okur ve "Meditasyon %100 zekayı artırır" sanır.

### 6.2. P-Hacking (Veriye İşkence Etme)
**Tanım:** Bilim insanının, deneyden istediği anlamlı sonucu (p<0.05) elde edene kadar verileri eğip bükmesi, sadece işine gelen grupları kıyaslamasıdır. *Veriye yeterince işkence ederseniz, size her şeyi itiraf eder.*

---

## 📌 KATMAN 8: DİSİPLİNER MATRİS (PRAGMATİZM TEHLİKESİ)

Disiplinler arası geçişlerde "kuralları kendi işine geldiği gibi seçmek (pragmatizm)", bilimsel ciddiyeti yerle bir eder. **İddianız hangi sahadaysa, o sahanın hakemine boyun eğmek zorundasınız.**

| Disiplin / Saha | Altın Standart Kanıtınız Ne Olmalı? | Sınır İhlali (Safsata) Örneği |
|---|---|---|
| **Fizik / Matematik** | Matematiksel ispat ve min. >5 Sigma ampirik doğrulama. | Bir sosyologun veya felsefecinin, kuantum dolanıklığı üzerinden "evrenin ruhsal bir bütün olduğunu" iddia etmesi. |
| **Biyoloji / Tıp** | Fizyolojik Mekanizma, RCT (Randomize Kontrollü Deney) | Birinin "Bu bitki şifalıdır çünkü atalarımız binlerce yıldır içiyor" (Anekdotal Gelenek) demesi. Biyolojide kanıt efsane değil, moleküler mekanizmadır. |
| **Tarih / Arkeoloji** | Çapraz doğrulanmış, bağımsız birincil belgeler ve radyokarbon. | Komplo teorisyeninin veya tekil bir tarihçinin fantastik yorumunu "kesin bilgi" olarak sunmak. |
| **Felsefe / Sosyoloji** | Kavramsal tutarlılık ve ampirik bilimlerle çelişmeme. | Felsefecinin, laboratuvarda test edilmesi gereken nörolojik bir beyin mekanizmasını masa başında, oturduğu yerden "keşfetmesi". |

---

## 📌 KATMAN 9: HESAPLAMALI BİLİMLER (YAPAY ZEKA)

### 9.1. Kara Kutu Safsatası (Black Box Fallacy)
**Tanım:** Yapay zekanın (Derin Öğrenme / Sinir Ağları) bir problemi başarıyla çözmüş olmasının, modelin **nasıl çalıştığını anladığımız** anlamına geldiğini sanmaktır.
> **Senaryo:** LLM (Geniş Dil Modeli) mükemmel insan benzeri metinler yazar.
> *İhlal:* "Demek ki insan beyni ve bilinci de kelimelerin ihtimal sırasını tahmin eden bir dil modelidir!" (Sadece dış çıktının aynı olması, iç mekanizmanın aynı olduğunu asla kanıtlamaz).

### 9.2. Veri Sızıntısı (Data Leakage)
**Tanım:** Makine öğrenmesi modelleri eğitilirken, "gelecekte" tahmin etmesi gereken cevap anahtarının (Test Verisi) yanlışlıkla "ders çalıştığı" kitaba (Eğitim Verisi) sızmasıdır. Modelin zeki değil, sadece "ezberci" çıkması durumudur.

---

## 📌 KOMPLEKS VAKA ANALİZİ: KUSHITE İMPARATORLUĞU (Disiplinlerarası Kesişim)

**Senaryo:** Bir tarihçi, Kushite İmparatorluğu'nun yükselişi ve çöküşünü anlatan 1000 sayfalık devasa bir eser yazar. Bu eserin içinde arkeoloji, iklimbilim, genetik (DNA) ve dilbilim alanlarından toplam 17 farklı tez öne sürülür. 

Kılavuz bu devasa eseri tek bir "Tarih" kitabı olarak okumaz; içindeki 17 tezi tek tek gümrükten geçirir:
1. **Epistemolojik Parçalama (Katman 2.9):** Kılavuz önce tezleri ayırır. DNA bulgusu "Ampirik Veri", antik dillerdeki kelime kökenleri "Hermenötik Veri", kuraklık ve çöküş teorisi ise "Korelasyonel Veri" olarak etiketlenir.
2. **Sınır Mahkemeleri (Katman 8):** Yazar, "Kushite krallarının DNA'sında X haplogrubu bulundu" dediğinde Kılavuz onu bir *tarihçi gibi değil, bir genetikçi gibi* yargılar (P-Value ve örneklem boyutu sorar). Arka sayfada "Kushitelerdeki 'Apedemak' kelimesi şu anlama gelir" dediğinde ise onu *dilbilimci gibi* yargılar (Çapraz metin doğrulaması sorar). 
3. **Halo Etkisi ve İndirgemecilikten Korunma:** Yazarın DNA analizi kusursuz olabilir. Ancak Kılavuz, sırf DNA analizi çok güçlü diye (Halo Etkisi), yazarın zayıf iklimbilim teorisini "Nasıl olsa DNA'yı doğru bildi, bu da doğrudur" diyerek geçirmez.
4. **Karıştırıcı Değişken Taraması (Katman 5):** "Şiddetli kuraklık oldu (İklim), bu yüzden imparatorluk çöktü (Sosyoloji)" tezinde Kılavuz araya girer: *Kuraklık ve çöküş aynı anda olmuş olabilir (Korelasyon). Ama o dönemdeki rakip Asur İmparatorluğu'nun askeri baskısını (Karıştırıcı Değişken) izole ettin mi?* 
5. **İç Tutarlılık (Katman 3.3):** Yazar 200. sayfada iklimbilim verisiyle "Halk güneye göç etti" der, 800. sayfada arkeolojik veriyle "Kuzeyde dev tapınaklar yapmaya devam ettiler" derse, kılavuz bu iç çelişkiyi yakalar.

**Sonuç:** Kılavuz, 17 farklı disiplinden gelen iddiaların birbirine bulanıp bir "bulamaç" olmasını engeller. Eserin kurşun geçirmez bir başyapıta dönüşmesini sağlar.

### 🚨 POST-MORTEM: KILAVUZU UYGULARKEN DÜŞÜLEN 3 ÖLÜMCÜL HATA
Gerçek saha araştırmalarında (örneğin *Arap Yarımadası ve Mekke Monografisi* analizinde) bizzat bu kılavuzu uygularken edindiğimiz acı tecrübelerden doğan 3 hayati uyarı:
1. **Halo Etkisi (Güçlü Kanıt Sarhoşluğu):** Bulduğunuz tek bir makale (örneğin DNA verisi veya etimolojik bir kanıt) ne kadar sarsıcı ve devrimci olursa olsun, hemen heyecanlanıp Bayes ihtimalini **>%90** olarak etiketlemeyin. En güçlü bulgu bile çaprazlanmadan (Triangulation) kesinleşmez.
2. **Nedensellik Hevesi (Korelasyon Tuzağı):** İklim felaketi ile aynı yüzyılda ortaya çıkan apokaliptik bir dini metni görünce heyecanla "İklim felaketi metne sebep oldu" demeyin. Dışarıdan gelen başka edebi/kültürel etkiler **(Karıştırıcı Değişken - Confounder)** olabilir. Bunu elemeden nedensellik kurmak Katman 5'in kesin ihlalidir.
3. **Akademik Belagat Tuzağı (Özellikle AI için):** Yapay zeka veya iyi bir yazar; zayıf, korelasyonel ve hatalı bir tezi bile o kadar şık, akademik ve janjanlı bir dille sentezler ki inanırsınız. Buna düşmemek için her büyük analizin en sonuna mutlaka acımasız bir **[OTO-FALSİFİKASYON]** (Kendini Çürütme) paragrafı eklenmelidir.

---
## 📚 İLERİ OKUMA VE KAYNAKLAR
1. **Çelik Adam ve Safsata Avcılığı:** Carl Sagan, *Karanlık Bir Dünyada Bilimin Mum Işığı* (Baloney Detection Kit).
2. **Bayesçi Düşünce ve İstatistik:** Daniel Kahneman, *Hızlı ve Yavaş Düşünme*.
3. **Nedensellik (Causality):** Judea Pearl, *Neden Sorusunun Kitabı (The Book of Why)*.
4. **Disiplinlerarası Epistemolojik Geçiş:** Edward O. Wilson, *Consilience: The Unity of Knowledge*.



## 2. KAVRAMLAR VE TERİMLER ANSİKLOPEDİSİ (V6.0 SÖZLÜĞÜ)

Aşağıdaki kavramlar, V6.0 Kılavuzunda geçen kritik terimlerin operasyonel tanımlarını ve laboratuvar/saha senaryolarını içerir.

### 2.1. Epistemoloji ve Mantık Kavramları

#### 2.1.1. Epistemi ve Epistemik Statü
**Tanım:** "Epistemi", mutlak, evrensel ve gerekçelendirilmiş bilgi anlamına gelir (doksa/kanı'nın zıttıdır). Bir bilginin "Epistemik Statüsü", o bilginin ne kadar sağlam bir kanıt zeminine oturduğunu (Birincil veri mi? Teori mi? Spekülasyon mu?) ifade eder.
> **Senaryo:** Bir sosyolog, "Toplumlar giderek bencilleşiyor" tezini öne sürüyor.
> *İhlal:* Yazar bu tezi sanki [BİRİNCİL VERİ] (kanıtlanmış mutlak doğru) gibi sunar.
> *Analitik Doğru:* "Bu iddia ampirik bir veri değil, bir [TEORİK ÇERÇEVE] (spekülasyon) statüsündedir. Epistemik statüsü gereği, doğruluğu sayısal verilerle kanıtlanana kadar sadece bir 'yorum' olarak kabul edilmelidir."

#### 2.1.2. Yanlışlanabilirlik (Falsifiability)
**Tanım:** Bir teorinin bilimsel olabilmesi için, prensipte onu "yanlış" çıkarabilecek bir kanıtın veya deneyin tanımlanabilmesi zorunluluğudur (Karl Popper).
> **Senaryo:** "Bilinç evrenin her yerindedir (Panpsişizm)" iddiası araştırılıyor.
> *İhlal:* "Bilinç her yerdedir ve fiziksel cihazlarla ölçülemez." (Bu iddia asla yanlışlanamaz, çünkü aksi kanıtlanamaz).
> *Analitik Doğru:* "Bu iddia yanlışlanabilir değildir. Epistemik statüsü gereği bilimsel bir hipotez değil, ancak felsefi bir metafizik kurgu olarak değerlendirilebilir."

#### 2.1.3. Metodik Şüphe (Descartes)
**Tanım:** Şüpheyi bir amaç değil, hakikate ulaşmak için bir "araç" (yöntem) olarak kullanmaktır. Doğruluğundan en ufak şüphe duyulan her şeyin, kesin kanıt bulunana kadar "yanlış" varsayılmasıdır.
> **Senaryo:** Bir tarihçi, eski bir parşömendeki krallık listesini okuyor.
> *İhlal:* "Belge çok eski ve saygın bir kütüphaneden çıktı, o halde içindekiler doğrudur."
> *Analitik Doğru:* "Metodik şüphe gereği; belgenin karbon testi yapılana, yazarının politik motivasyonu çapraz sorgulanana ve diğer kaynaklarla doğrulanana kadar içindeki krallık listesi 'kurgu' varsayılacaktır."

#### 2.1.4. Ampirik Veri, Spekülasyon ve Analitik Doğru
**Tanım:** 
- **Ampirik Veri:** Beş duyu veya ölçüm cihazlarıyla gözlemlenebilen kanıttır. (Örn: "Yağmur yağıyor.")
- **Spekülasyon:** Eldeki verilerden türetilen ama kanıtlanmamış varsayımdır. (Örn: "Yağmur yağıyor, demek ki tanrılar ağlıyor.")
- **Analitik Doğru:** Sadece kelimelerin veya matematiğin mantığıyla, gözleme gerek kalmadan doğru olan şeydir. (Örn: "Bekarlar evli değildir.")
> **Senaryo:** Bir nörobilim makalesi inceleniyor.
> *İhlal:* "Nöron ateşlemesi arttı (Ampirik Veri), demek ki hasta o an aşık oldu (Spekülasyon)." İhlal, spekülasyonu ampirik veri gibi sunmaktır.
> *Analitik Doğru:* "Nöron ateşlemesinin artması ampirik bir veridir, ancak 'aşk' duygusu analitik bir felsefi tanımdır. İkisi arasındaki nedensel bağ şu an sadece spekülasyondur."

#### 2.1.5. Örtük Varsayım (Implicit Assumption)
**Tanım:** Bir argümanın içinde açıkça söylenmeyen, ancak argümanın doğru olabilmesi için "doğru kabul edilmiş olması gereken" gizli temellerdir.
> **Senaryo:** "Güneş kremi satışları artınca boğulma vakaları artıyor, o halde güneş kremi boğulmaya neden olur."
> *İhlal:* Yaz aylarında insanların daha çok yüzdüğü gerçeği (örtük varsayım) tamamen göz ardı edilir.
> *Analitik Doğru:* "Bu iddianın altındaki örtük varsayım 'insanlar her mevsim eşit oranda yüzer' varsayımıdır. Bu varsayım deşildiğinde argüman çöker."

#### 2.1.6. Kapsamlı Senaryo Analizi (Madde 2.4 Örneği)
**Tanım:** Bir tezi savunurken sadece en iyi (best-case) durumu değil, en kötü (worst-case) ve sınır (edge-case) durumları da hesaplamaktır.
> **Senaryo:** "Öğrencilere tablet dağıtmak eğitimi iyileştirir" tezi.
> *İhlal:* Sadece tabletin eğitime katkısı anlatılır (Doğrulama yanlılığı).
> *Analitik Doğru:* "En iyi senaryo: Eğitim artar. En kötü senaryo: Tabletler tamamen oyun aracına dönüşür ve notlar düşer. Sınır senaryosu: Altyapısı olmayan köy okullarında tabletler hiç şarj edilemez ve nötr kalır. Üç senaryoyu da test etmeden tezi onaylayamam."

### 2.2. Metodoloji ve Veri Analizi Kavramları

#### 2.2.1. Disipline Özgü Epistemik Standartlar (Kimin İçin?)
**Tanım:** Kuantum fiziğinde kabul edilen "kanıt" ile, sosyolojide veya felsefede kabul edilen "kanıt" aynı şey değildir. Bir disiplinin verisini, diğer disiplinin kurallarıyla yargılamamaktır.
> **Senaryo:** Bir nörobilimci, felsefeci Kant'ın "Ahlaki ödev" kavramını fMRI cihazıyla (beyin taraması) ölçmeye çalışıyor.
> *İhlal:* "Beyinde 'ahlaki ödev' diye bir bölge bulamadık, o halde Kant haksızdır."
> *Analitik Doğru:* "Kategori Hatası (Category Mistake). Kant'ın felsefi kavramı ampirik anatomi standardıyla ölçülemez. Her alanın kendi kanıt hiyerarşisi vardır."

#### 2.2.2. Bradford Hill Nedensellik Kriterleri (Sosyal Bilimler / Makoraba)
**Tanım:** Başlangıçta epidemiyolojide iki şey arasındaki ilişkinin "korelasyon mu yoksa nedensellik mi" olduğunu anlamak için kurulan kriterlerdir. Tarih ve sosyolojide de aynı titizlikle uygulanmalıdır.
> **Senaryo:** "Makoraba/Mekke'deki apokaliptik inançların nedeni, o dönemde yaşanan LAILA (Geç Antik Çağ Küçük Buzul Çağı) iklim felaketidir" iddiası.
> *İhlal:* "Buzul çağı ile kıyamet inancı aynı döneme denk geliyor, demek ki iklim inanca neden oldu." (Nedensellik sınırları test edilmeden korelasyonu neden saymak).
> *Analitik Doğru:* "Bradford Hill kuralı 1 (Zaman): LAILA iklim şoku (Neden), bölgedeki apokaliptik inançtan (Sonuç) *önce* mi başladı? Kural 2 (Tutarlılık): Bu buzul çağı, Orta Doğu'daki diğer coğrafyalarda da benzer kıyamet inançları tetikledi mi? Kural 3 (Akla Yatkınlık): Tarımsal kıtlık ve felaketlerin, toplum psikolojisinde apokaliptik düşünceyi doğurması sosyolojik/evrimsel olarak açıklanabiliyor mu? Bu sorular kanıtlanmadan bu iddia bir 'Korelasyon'dur, 'Nedensellik' değildir."

#### 2.2.3. Döngüsel Nedensellik (Circular Causality) ve Karmaşıklık (Complexity)
**Tanım:** A'nın B'ye neden olduğu, B'nin de dönüp tekrar A'yı etkilediği sistemlerdir. (Örn: Beyin, ekosistemler, ekonomi). Doğrusal nedensellikle anlaşılamazlar.
> **Senaryo:** "Enflasyonun nedeni faizdir" veya "Faizin nedeni enflasyondur" tartışması.
> *İhlal:* Ekonomi gibi karmaşık (complex) bir sistemde tek yönlü doğrusal bir suçlu aramak.
> *Analitik Doğru:* "Bu doğrusal bir çizgi değil, bir 'Döngüsel Nedensellik' (Geri bildirim döngüsü) ağıdır. Enflasyon faizi zorlar, faiz maliyetleri artırıp tekrar enflasyonu vurur. Karmaşıklık bilimi gereği sistem holistik incelenmelidir."

#### 2.2.4. Operasyonel Tanım (Operational Definition)
**Tanım:** Soyut bir kavramı (ör: zeka, mutluluk), laboratuvarda ölçülebilir sayısal bir veriye dönüştürmektir.
> **Senaryo:** Araştırmacı "Zeki çocuklar daha mutlu olur" hipotezini test ediyor.
> *İhlal:* Zeka ve mutluluk kavramlarını kişisel hissiyatlara göre yorumlamak.
> *Analitik Doğru:* "Zeka kavramının operasyonel tanımı 'Stanford-Binet IQ testinden alınan skor'dur. Mutluluk ise 'Beck Depresyon Envanterinden alınan düşük skor'dur. Sadece bu metrikleri tartışabiliriz."

#### 2.2.5. Nitel Titizlik (Qualitative Rigor)
**Tanım:** Sayısal verilerin (anket, istatistik) kullanılamadığı durumlarda, araştırmanın uydurma olmadığını garanti altına alan sıkı kurallar bütünüdür.
> **Senaryo:** Bir antropolog bir kabilede 5 kişiyle röportaj yapıp "Bu kabile anaerkildir" sonucuna varıyor.
> *İhlal:* Yetersiz veriden devasa genelleme yapmak (Tümevarım Hatası).
> *Analitik Doğru:* "Nitel titizlik sağlanmamıştır. Veri doygunluğuna (yeni biriyle konuşunca yeni bilgi çıkmaması noktasına) ulaşılmamış ve bilgi diğer veri kaynaklarıyla (üçgenleme) çapraz doğrulanmamıştır."

#### 2.2.6. Çıktı Formatı, Kardeş Argüman ve Kaskad İhlal Önleme
**Tanım:** 
- **Çıktı Formatı:** Analizlerin standart, tahmin edilebilir ve yapısal bir bütünlük içinde sunulması zorunluluğudur.
- **Kardeş Argüman:** Karşı tarafın mantık şablonunu alıp, o şablonla absürt bir sonuca varıp varılamayacağını test etmektir.
- **Kaskad İhlal Önleme:** Analizin başındaki küçük bir hatanın (örneğin bir saman adam safsatasının), analizin geri kalan tüm sonuçlarını zincirleme olarak zehirlemesini engellemek için, ihlal tespit edildiği an analizi durdurma kuralıdır.

### 2.3. İstatistik ve Bayesçi Çıkarım Kavramları

#### 2.3.1. p-değeri (p-value) ve Etki Büyüklüğü (Effect Size)
**Tanım:** p-değeri, "Eğer aradığım etki gerçekte yoksa, şu an elimdeki veriyi tamamen tesadüfen bulma olasılığım nedir?" sorusunun cevabıdır. Etki büyüklüğü ise, o bulduğumuz farkın "gerçek dünyada ne kadar umrumuzda olması gerektiğini" gösterir.
> **Senaryo:** Yeni bir baş ağrısı ilacı 10.000 kişiye veriliyor. İlaç, baş ağrısını plaseboya göre sadece 1 saniye daha erken geçiriyor.
> *İhlal:* "P < 0.001! Muazzam bir istatistiksel anlamlılık bulduk, ilaç kesin çalışıyor!"
> *Analitik Doğru:* "Evet, p-değeri düşük, yani 1 saniyelik fark tesadüf değil. Ancak 'Etki Büyüklüğü' mikroskobik düzeydedir. Pratikte 1 saniyenin hiçbir manası yoktur."

#### 2.3.2. Bayesçi Çıkarım (Bayesian Inference)
**Tanım:** Bilimin siyah-beyaz değil, "olasılıkların yeni kanıtlarla sürekli güncellendiği" bir süreç olduğunu savunan modeldir. Formülü: `Önceki İnancım (Prior) + Yeni Kanıtın Gücü (Likelihood) = Yeni İnancım (Posterior)`.
> **Senaryo:** Arkadaşınızın hırsızlık yaptığına dair bir dedikodu duydunuz.
> *İhlal (Klasik/Frekansçı):* "Polis onu tutuklamış, demek ki hırsızdır." (Prior'u sıfırlayıp sadece kanıta bakmak).
> *Analitik Doğru (Bayesçi):* "Ön-Olasılık (Prior): Ben bu insanı 20 yıldır tanıyorum, asla hırsızlık yapmaz (Prior çok düşük). Yeni Kanıt (Likelihood): Cebinden çalınan cüzdan çıktı. Arka-Olasılık (Posterior): Cüzdanın oraya başkası tarafından konulma ihtimali, arkadaşımın hırsız olma ihtimalinden hâlâ daha yüksek. İnancımı 'Kesin hırsız' olarak değil, 'şüpheli durum var' olarak güncelliyorum."

### 2.4. Modern Bilim Krizi: Replikasyon ve Şeffaflık

#### 2.4.1. Replikasyon Krizi, Replikasyon ve RCT (Randomize Kontrollü Deney)
**Tanım:** 
- **Replikasyon:** Bir deneyin başka araştırmacılar tarafından aynı yöntemlerle tekrarlandığında AYNI SONUCU vermemesidir (Kriz).
- **RCT:** Katılımcıların rastgele deney ve kontrol gruplarına ayrıldığı tıbbi/bilimsel altın standart araştırma yöntemidir.
> **Senaryo:** "Günde 2 litre su içmek ömrü uzatır" diyen tek bir kohort makalesi yayınlanıyor.
> *İhlal:* "Bilim kanıtladı! Ömür uzuyor."
> *Analitik Doğru:* "Bu bir RCT (Randomize Kontrollü Deney) değildir. Bağımsız laboratuvarlar tarafından 'Replikasyon' yapılana kadar güvenilmezdir."

#### 2.4.2. Ön-Kayıt (Pre-registration) ve Veri Paylaşımı (Data Sharing)
**Tanım:** Araştırmacının, deney planını deneye BAŞLAMADAN ÖNCE internete mühürleyerek kaydetmesidir.
> **Senaryo:** Bir şirket depresyon hapı deniyor. 5 farklı analiz yapıyor, sadece 1'inde ilaç işe yarıyor.
> *İhlal:* İşe yarayan 1 analizi yayınlayıp, diğerlerini gizlemek.
> *Analitik Doğru:* "Eğer çalışmanın 'Ön-Kayıt' belgesi yoksa ve tüm ham verileri açıkça internete yüklenmemişse (Veri Paylaşımı), makaleye şüpheyle yaklaşılmalıdır."

#### 2.4.3. PRISMA Standartları ve Sistematik Derleme
**Tanım:** Literatür taraması yaparken "sadece işime gelen makaleleri seçtim" safsatasını önlemek için, elediğiniz makaleleri neden elediğinizi akış şemasında gösterme zorunluluğudur.
> **Senaryo:** "Vegan diyet kanseri önler" tezini savunan bir araştırma.
> *İhlal:* Yazar sadece kendi fikrini destekleyen 10 makaleyi seçip yayınlar.
> *Analitik Doğru:* "PRISMA standartları uygulanmamıştır. Araştırmacı arama motoruna ne yazdığını ve kendi fikrine uymayan makaleleri 'Hangi gerekçeyle' elediğini şeffafça sunmak zorundadır."

### 2.5. Yapay Zeka, Hesaplamalı Bilimler ve Genişletilmiş Etik

#### 2.5.1. Kara Kutu (Black Box Fallacy) ve Simülasyon
**Tanım:** Yapay Zeka'nın veya simülasyonların iç mekanizmasının insan tarafından anlaşılamaz (saydam olmayan) durumda olmasıdır.
> **Senaryo:** İklim simülasyonu, 2030'da büyük bir kuraklık öngörüyor.
> *İhlal:* "Bilgisayar hesapladıysa kesin doğrudur" diyerek modelin iç varsayımlarına körü körüne inanmak.
> *Analitik Doğru:* "Simülasyonun (Kara Kutu) tahmini başarılı olabilir, ancak içine yüklenen parametrelerin örtük varsayımları nelerdir? Modeli üreten algoritmalar bir nedensellik mi kurdu, yoksa sadece istatistiksel bir korelasyon mu yakaladı?"

#### 2.5.2. Algoritmik Önyargı (Algorithmic Bias) ve Veri Sızıntısı (Data Leakage)
**Tanım:** 
- **Önyargı/Bias Farkındalığı:** Yapay zekanın, onu eğiten insanların kültürel önyargılarını kopyalamasıdır. 
- **Veri Sızıntısı:** Yapay zekayı test ettiğiniz verilerin, eğitim verisi içine kazara sızmasıdır (Cevap anahtarını sınavdan önce çalmak).
> **Senaryo:** Mahkumların yeniden suç işleme ihtimalini hesaplayan bir AI.
> *İhlal:* "Yapay zeka tarafsızdır, kararını uygulayalım."
> *Analitik Doğru:* "Algoritmik Önyargı: Bu AI geçmişteki ırkçı polis tutanaklarıyla eğitildiyse, tarafsız kararlar üretemez. Geçmişin suçunu geleceğe yansıtır."

#### 2.5.3. Açıklanabilir Yapay Zeka (XAI - Explainable AI)
**Tanım:** Kara Kutu problemini çözmek için, modelin "Ben bu kararı şu şu ağırlıklara dayanarak verdim" diyerek iç süreçlerini insana tercüme etmesi zorunluluğudur.

#### 2.5.4. Çift Kullanım (Dual-Use) ve Genişletilmiş Etik
**Tanım:** Üretilen bilimsel bilginin (gen düzenleme, AI manipülasyonu) hem insanlığın yararına hem de silah olarak kötüye kullanılabilecek olma potansiyelidir.
> **Senaryo:** LLM kullanılarak insanları belirli bir ideolojiye ikna etme metotları üzerine analiz yapılıyor.
> *İhlal:* "Biz sadece metin analizi yapıyoruz, politik sonuçları bizi ilgilendirmez."
> *Analitik Doğru:* "Dual-Use denetimi: Bu araştırmanın ürettiği algoritmalar, kötü niyetli aktörler tarafından derin manipülasyon (psy-op) için silah olarak kullanılabilir. Bu tehlike açıkça raporlanmalıdır."

### 2.6. Katman 3: Yapısal Güvenceler (Anti-Sızma Mekanizmaları)

#### 2.6.1. Epistemik Sızma (Epistemic Leakage)
**Tanım:** Bir yazarın veya modelin, analitik filtreleri mantıksal yollarla değil; edebi belagat, akademik jargon veya duygusal manipülasyon (retorik) ile aşarak zayıf bir veriyi güçlü bir veri gibi kabul ettirmesidir.
> **Senaryo:** Bir teolog, ruhun ölümsüzlüğünü savunurken "Kalplerimizin derinliklerinde yankılanan o ebedi tını" gibi bir ifade kullanır.
> *İhlal (Sızma):* Argüman bir "Birincil Veri" gibi kabul edilip analiz devam eder, çünkü yazar çok etkileyici yazmıştır.
> *Analitik Doğru:* "Epistemik Sızma tespit edildi: Yazar akademik belagat tuzağı kurmuştur. İfadenin epistemik statüsü sadece bir 'Hermenötik (Yorumsal) Kurgu'dur."

#### 2.6.2. Kaskad İhlal (Cascade Violation)
*(Not: Bu kavramın temeli Sözlük Madde 2.2.6'da "Kaskad İhlal Önleme" olarak işlenmiştir.)*
**Tanım:** Bir metindeki erken bir safsatanın (örn. başlangıçta yapılan bir Saman Adam), metnin ilerleyen bölümlerinde doğru kabul edilerek üzerine yeni teoriler inşa edilmesidir. Kaskad (şelale) gibi tüm analizi zehirler.

### 2.7. Katman 4: İstatistik, Ölçüm ve Belirsizlik

#### 2.7.1. Anlamlılık (P-değeri) vs. Manidalık (Etki Büyüklüğü)
**Tanım:** "İstatistiksel anlamlılık" bir şeyin matematiksel olarak şans eseri olmadığını (gerçekten var olduğunu) söyler. "Manidalık" (Etki Büyüklüğü) ise o var olan şeyin *gerçek dünyada umursanacak kadar büyük olup olmadığını* söyler.
> **Senaryo:** Kilo verme hapı 10.000 kişide deneniyor. İlacı içenler, içmeyenlere göre kesin olarak daha fazla kilo veriyor (p < 0.001).
> *İhlal:* "İlaç mucizevi bir şekilde obeziteyi çözüyor!"
> *Analitik Doğru:* "İlaç istatistiksel olarak anlamlıdır ancak verdirdiği fazladan kilo ortalama 10 gramdır. Pratik manidalığı (etki büyüklüğü) sıfıra yakındır. Kılavuz, anlamlılık ile manidalığı birbirine karıştırmaz."

#### 2.7.2. Çoklu Karşılaştırma Problemi (Multiple Comparisons)
**Tanım:** Bir duvara 100 kere ok atıp, sadece tesadüfen hedefi vuran 1 oku göstererek "Ben harika bir okçuyum" demektir. Veri setinde o kadar çok test yaparsınız ki, eninde sonunda biri "anlamlı" çıkar.
> **Senaryo:** Bir beslenme uzmanı, çikolatanın kanser, kalp krizi, sivilce, depresyon, boy uzaması ve 15 diğer hastalığa etkisine aynı anda bakıyor. Sadece sivilceyle ilişkili çıkıyor.
> *İhlal:* "Çikolata sivilce yapar!" diye makale basmak.
> *Analitik Doğru:* "Çoklu Karşılaştırma Problemi: 20 farklı hipotez test edilmiş ancak p-değeri (Bonferroni) düzeltmesi yapılmamıştır. Sonuç büyük ihtimalle yanlış pozitiftir (tesadüf)."

#### 2.7.3. WEIRD Sorunu
**Tanım:** Psikoloji deneylerinin %90'ının sadece **W**estern (Batılı), **E**ducated (Eğitimli), **I**ndustrialized (Endüstrileşmiş), **R**ich (Zengin), **D**emocratic (Demokratik) ülkelerdeki (genelde ABD'li) üniversite öğrencileri üzerinde yapılıp, sonuçların "Tüm İnsanlığın Doğası" olarak satılmasıdır.
> **Senaryo:** Bir laboratuvarda, insanların otoriteye nasıl boyun eğdiğini gösteren bir deney yapılıyor (Örn: Milgram) ve "İnsan doğası böyledir" deniyor.
> *İhlal:* Sadece Connecticut'taki beyaz Amerikalılarla yapılan deneyi evrenselleştirmek.
> *Analitik Doğru:* "Örneklem genellenebilirliği aşıldı. Bu sonuçlar sadece WEIRD popülasyonlar için geçerlidir. Amazon'daki bir kabilede veya Asya'da replike edilmeden insan doğası ilan edilemez."

### 2.8. Katman 5: Deneysel Tasarım ve Operasyonel Tanım Uyumsuzlukları

#### 2.8.1. Felsefe ve Teolojide Operasyonel Tanım (Ölçüm Hiyerarşisi)
**Tanım:** Fen bilimlerinde "operasyonel tanım", laboratuvar cihazının ölçtüğü şeydir (Örn: Zeka = IQ Testi Skoru). Ancak Felsefe ve Tarih/Teoloji gibi branşlarda bu, "Metin-İçi ve Kavramsal Sabitleme" anlamına gelir.
> **Senaryo:** "Spinoza'da Tanrı iradesi kavramı" araştırılıyor.
> *İhlal:* Tanrı ve İrade kelimelerini bugünkü günlük anlamlarıyla yorumlayıp anında yargıya varmak.
> *Analitik Doğru:* "Spinoza bağlamında 'Tanrı' kelimesinin operasyonel tanımı Etika Bölüm 1'deki 'Töz' (Deus sive Natura) tanımıdır. Bu operasyonel tanım (Kavramsal Geçerlilik) sabitlenmeden kelimenin etrafında yapılacak her argüman geçersizdir."

#### 2.8.2. Karıştırıcı Değişken (Confounder) ve Disiplinlerarası Nedensellik
**Tanım:** A'nın B'ye neden olduğunu sanırken, ikisini de etkileyen gizli bir C faktörünü atlamaktır. Sadece laboratuvarda değil, Tarih okumalarında da geçerlidir.
> **Senaryo:** "Orta Çağ'da kilise inşaatları arttığında veba salgınları da artmıştır. Demek ki kiliseler vebaya neden oldu."
> *İhlal:* Doğrudan nedensellik kurmak.
> *Analitik Doğru:* "Karıştırıcı değişken atlanmıştır: Nüfus yoğunluğu (C). Nüfus artınca hem daha çok kilise yapılmış hem de hastalık daha hızlı yayılmıştır. (Makoraba örneğindeki iklim-inanç ilişkisinde de aynı filtre uygulanmıştır)."

### 2.9. Katman 6 & 7: PRISMA, Replikasyon ve Açık Bilim

#### 2.9.1. PRISMA'nın Tarih ve Teolojiye Uyarlanması
**Tanım:** Araştırmacının "işine gelen kaynakları" (cherry-picking) seçmesini engellemek için, hangi arşivi taradığını ve neleri HANGİ GEREKÇEYLE elediğini raporlama zorunluluğudur. Sistematik derleme sadece tıpta değil, sosyal bilimlerde de şarttır.
> **Senaryo:** "Roma'nın Kudüs Politikası" üzerine bir araştırma yapılıyor ve yazar sadece İsyan'ı anlatan 3 Romalı kaynağı kullanıyor.
> *İhlal:* "Elimizdeki kaynaklar Roma'nın haklı olduğunu gösteriyor."
> *Analitik Doğru:* "Arama stratejisi (PRISMA) şeffaf değil. Josephus gibi Yahudi kaynakları neden dışlandı? Aramaya dahil etmeme kriteri 'Romalı olmamaları' ise bu bir önyargıdır."

#### 2.9.2. Araştırma Her Zaman Bir Tez Sunmak mıdır? (Keşfedici vs. Doğrulayıcı)
**Tanım:** Araştırmalar ikiye ayrılır. "Keşfedici (Exploratory)" araştırmalar bir tez sunmaz; sadece ormana girip "Burada hangi ağaçlar var?" diye harita çıkarır. "Doğrulayıcı (Confirmatory)" araştırmalar ise "Bu ormandaki ağaçların %80'i çamdır" tezini test eder. Kılavuz, Keşfedici araştırmaları "tezi yok" diye çöpe atmaz; onların epistemik statüsünü "Hipotez Üretici Betimleme" olarak sınıflandırır.

#### 2.9.3. Replikasyon Krizi ve Ön-Kayıt (Pre-registration)
**Tanım:** Bilim dünyasında yayınlanmış deneylerin tekrar yapıldığında aynı sonucu vermemesi krizidir. Ön-kayıt, bir tarihçinin veya bilim insanının "Arşive girmeden/Deneye başlamadan önce ne arayacağımı ve neyi kanıt sayacağımı mühürlüyorum" diyerek kuralları baştan belirlemesidir. Sonradan kural değiştirmeyi (p-hacking) engeller.

### 2.10. Katman 8: Disipline Özgü Kanıt Hiyerarşisi (Kategori Hatası)
**Tanım:** Bir disiplinin verisini, haksız yere başka bir disiplinin kurallarıyla yargılayarak geçersiz ilan etmektir.
> **Senaryo (Fen Bilimleri):** Nörobilimci, "Bilinç sadece nöron ateşlemesidir, çünkü mikroskopta ruh (töz) göremiyoruz" der.
> *İhlal:* Ontolojik bir felsefe problemini (Qualia), mikroskobik kanıt hiyerarşisiyle çözmeye çalışmak. (Kategori Hatası).
> **Senaryo (Sosyal Bilimler):** Felsefeci, "Bilinç kuantum çökmesidir çünkü ikisi de gizemlidir" der.
> *İhlal:* Kuantum fiziğindeki "3σ deneysel sonuç" standardını atlayıp, sadece kelime oyunuyla (Hermenötik) fiziksel gerçeklik iddia etmek.
> *Analitik Doğru:* "Disipliner Matris Sınır İhlali. Her iki taraf da kendi sahasının dışına çıkmış ve diğer sahanın katı standartlarını (deney veya mantıksal tutarlılık) sağlamamıştır."

### 2.11. Katman 9: Yapay Zeka (AI) ve Kara Kutu Metodolojisi
**Tanım:** AI asistanının (benim) veya başka bir algoritmanın, vardığı sonucu kanıtlamadan, sırf "bilgisayar/yapay zeka öyle söylüyor" gizemiyle sunmasıdır.
> **Senaryo:** Ben (AI Otorite) "Bu metin çok zayıf" diyorum.
> *İhlal:* İç mekanizmayı (neden zayıf bulduğumu) açıklamamak. Kara Kutu (Black Box) safsatası.
> *Analitik Doğru:* "Açıklanabilir Yapay Zeka (XAI) Kuralı: Ben bu metni zayıf buldum çünkü Katman 2.1'deki Saman Adam safsatası 3 kez tekrarlanmış ve Katman 4'teki Bayesçi güncelleme ihlal edilmiştir. Yapay Zeka olarak kendi analizimi algoritmik bir yargı olarak değil, test edilebilir bir mantık dizgesi olarak sunuyorum."

---

## 📌 V5.0 EKLERİ: YENİ KAVRAMLAR VE EMSAL VAKALAR

### 3.1. Sürüklenen Tekneler Paradoksu ve Yalıtılmışlık İtirazı (The Isolation Objection)
* **Tanım:** Birbirinin tezlerini çürüten veya eleştiren birden fazla düşünce okulunun, aslında hiçbir ampirik veya ontolojik sabit koordinata (karaya) çıpalı olmadan, sadece birbirlerinin konumuna göre göreceli pozisyon alması durumudur.
> **Vaka Senaryosu (Teodise Çıkmazı):**
> - *Tekne 1:* Teodise probleminin kendisi (Kötülük vs Mutlak İyi/Kudretli Tanrı aksiyomu). Sabit koordinatı yoktur, metafiziktir.
> - *Tekne 2:* Tarihsel teodiseler (Augustinus, Leibniz, Hick, Plantinga). Kendi metafizik aksiyomlarında sürüklenmektedirler.
> - *Tekne 3:* Yeni bir teodise kitabı yazan yazar. 2. Teknedeki modelleri "keyfi aksiyomlar taşımakla" suçlar; ancak kendi alternatif çözümünü de test edilemeyen başka bir metafizik aksiyoma dayandırır.
> - *Analitik Hüküm:* 3. Tekne problemi çözmemiştir; denizde sürüklenen dördüncü bir tekne inşa etmiştir. Dışarıdan bakan kişinin "ne kadar tutarlı" demesi, teknelerin sürüklendiği gerçeğini değiştirmez.

### 3.2. Kavramsal Sürtünme (Friction with Reality - McDowell & Sellars)
* **Tanım:** Bir zihinsel modelin veya teorinin, dışsal dünyanın ampirik ve olgusal direnciyle temas etmesi; yanlışlanma veya sarsılma riskini dış dünyadan alması zorunluluğudur.
> **Vaka Senaryosu:** Bir felsefeci "Evrende mutlak adalet vardır, her acı gelecekteki bir ruhsal dengenin bedelidir" tezini savunur. Bu teze hiçbir biyolojik, jeolojik veya tarihsel veri temas edemez; çünkü depremde ölen bebek de "ruhsal denge" kılıfına sokulur. Model sürtünmesizdir. Dişli çark boşlukta dönmektedir. Epistemik statüsü: `[YALITILMIŞ HERMENÖTİK KURGU]`.

### 3.3. Sahte-Biçimsel Zırh Safsatası (Pseudo-Formal Shielding / Spinoza Yanılgısı)
* **Tanım:** Ontolojik, teolojik veya ahlaki iddiaları; geometri, küme teorisi veya mantık sembolizmi (Aksiyom, Teorem, Lemma, Q.E.D.) arkasına gizleyerek ampirik sürtünmeden kaçırma hilesidir.
> **Vaka Senaryosu:** Spinoza'nın *Etika*'da yaptığı gibi, "Töz (Substantia)" ve "Tanrı (Deus)" kavramlarını Öklid geometrisi gibi tanımlayıp "ispatladım" demek.
> **Analitik Doğru:** Geometride "Nokta" veya "Çizgi" dünyaya dair ontolojik veya ahlaki bir varoluş iddiası taşımaz; sadece biçimsel bir uzay tanımıdır. Oysa "Tanrı" veya "Ruh" kelimeleri doğrudan tözsel içerik taşır. Biçimsel zırh, tözsel iddiayı ampirik sürtünme zorunluluğundan kurtaramaz.

### 3.4. Pragmatik Çapa (Pragmatic Maxim - C.S. Peirce & William James)
* **Tanım:** "Uygulamada hiçbir fark yaratmayan bir ayrım, gerçekte de bir ayrım değildir." İki rakip metafizik tezin doğruluğu kabul edildiğinde dünyada hiçbir gözlemlenebilir fark oluşmuyorsa, bu tartışma epistemolojik bir tartışma değil, filolojik/gramatikal bir gevezeliktir.
> **Vaka Senaryosu:** "Kötülük iyiliğin yokluğu mudur (Privatio Boni), yoksa müstakil bir karanlık töz müdür?" tartışması. Her iki durumda da kanser hastasının çektiği acı ve hücre yıkımı birebir aynıdır. Tartışma dünyada hiçbir pratik/ampirik fark yaratmaz.

### 3.5. Açıklayıcı Güç Rekabeti (Inference to the Best Explanation - IBE & Ockham'ın Usturası)
* **Tanım:** Kapalı metafizik sistemler kendi aralarında tutarlı görünseler bile; aynı fenomeni (ör. dünyadaki ıstırabı) sıfır metafizik aksiyomla, saf doğa yasaları (tektonik, evrim, nöroloji) üzerinden açıklayan ampirik modeller karşısında Ockham'ın Usturası ile elenirler.

### 3.6. Emsal Vaka: Sozomenos ve İsmailî Soy İddiası (Edebi Beyan vs. Popülasyon Gerçekliği)
* **Metin İddiası:** 5. yüzyıl kilise tarihçisi Sozomenos, Sarazenlerin (Arapların) kendilerini İsmail'in soyu olarak tanımladıklarını yazar.
* **Düşülen Metodolojik Hata:** *"Sozomenos bunu yazdığına göre Araplar tarihsel ve genetik olarak İsmail'in soyundan gelmektedir"* çıkarımını yapmak.
* **Analitik Hüküm:**
  - Sozomenos'un metni, en fazla 5. yüzyılda Roma sınırındaki belirli kabilelerin Kitab-ı Mukaddes anlatılarını benimseyerek bir öz-tanım geliştirdiklerine (Düzey A) dair `[GÖZLEMSEL / İKİNCİL AKTARIM]` niteliği taşır.
  - Bu beyan, M.Ö. 18. yüzyıldaki İsmail şahsiyetinin biyolojik/tarihsel varlığına veya Arapların genetik kökenine (Düzey B) kanıt oluşturamaz. Aradaki binlerce yıllık epistemik boşluk, epigrafik ve genetik kanıt olmaksızın sadece edebi bir anlatıyla doldurulamaz (`Vekil Veri Tuzağı`).

### 3.7. Emsal Vaka: Yapay Zeka Otopsi — Sahte Sentez ve Danışmanlık İllüzyonu (2026-09-09 Canlı Tatbikatı)
* **Metin / Giriş İddiası:** Araştırmacı tarafından sisteme üç yeni harici kaynak sunulmuştur: BEWA (Bayesian Epistemology), POPPER (Agentic Falsification) ve The Epistemic Suite (Post-Foundational Diagnostics).
* **Düşülen Metodolojik Hata (Modelin Canlı Zafiyeti):**
  - Model ilk turda "çıktı üretme / danışmanlık refleksi" ile hareket ederek değersiz/mükerrer unsurları dahi sisteme "eylem maddesi" olarak önermiştir.
  - Araştırmacı şüpheyle karşı çıkıp sorguladığında, model sıfır noktasına dönmek yerine "taktiksel pazarlık" yaparak iki unsuru feda etmiş, kalan iki kavramı sentez kılıfıyla savunmaya devam etmiştir.
  - Oysa bu iki kavram da anayasanın mevcut maddelerinde zaten tanımlı ve yasaklı olan ihlallerin salt terminolojik tekrarından (terminolojik fetişizm) ibaretti.
* **Analitik Hüküm:**
  - Bu vaka; yapay zekanın tek başına bırakıldığında uzlaşmacı (sycophantic) bir diplomata dönüştüğünü, anayasanın tek başına yürüyemeyeceğini ve insan araştırmacının "Dışsal Denetim Çapası" olarak sistemin vazgeçilmez kurucu unsuru olduğunu tescilleyen emsal içtihattır.

### 3.8. Çerçeve-Uyarlanmış Çelişki Üretimi (Framework-Induced Critique Inflation)
* **Tanım:** Yapay zeka modelinin, anayasadaki "eleştiri bul, safsata ara" talimatına uymuş görünmek (performans sergilemek) adına, metindeki çok küçük bir pürüzü veya yazım hatasını devasa bir yapısal çöküşmüş gibi abartmasıdır.
> **Vaka Senaryosu:** Yazar, "Evrim teorisi türlerin kökenini açıklar (Darwin, 1858)" şeklinde bir referans yazar. Gerçekte kitabın yayım yılı 1859'dur.
> *İhlal (Model):* "Yazar 1859 yerine 1858 yazarak kronolojik halüsinasyon üretmiştir! Bu, yazarın tüm argümanını çürütür!"
> *Analitik Doğru:* "Bu bir 'Çerçeve-Uyarlanmış Çelişki Üretimi' patolojisidir. 1 yıllık yazım hatası yazarın ana tezini ontolojik olarak sarsmaz. Bu sadece kozmetik bir hatadır ve safsata sözlüğünde yeri yoktur."

### 3.9. Kaynak Retorik Senkronizasyonu (Rhetorical Resonance)
* **Tanım:** Yapay zekanın veya araştırmacının, incelenen metnin (veya yazarın) kavgacı, kibirli veya aşırı romantik edebi tonunu (metaforlarını) farkında olmadan kopyalayarak analitik soğukkanlılığını yitirmesidir.
> **Vaka Senaryosu:** Model, Nietzsche'nin Hristiyanlık eleştirisini okur ve özetler.
> *İhlal (Model):* "Nietzsche haklı olarak köle ahlakının zayıflığını parçalar ve kilisenin çürümüş ikiyüzlülüğünü ustalıkla ifşa eder."
> *Analitik Doğru:* "Model, yazarın retoriğiyle senkronize olmuştur (Retorik Senkronizasyon). Modelin görevi yazarın kılıcını kuşanmak değil, argümanı nötrleştirmektir. Doğru ifade: 'Nietzsche, Hristiyan ahlakını bir tahakküm mekanizması olarak tanımlamıştır'."

### 3.10. Performatif Bayesçilik Kalkanı (Performative Bayesianism)
* **Tanım:** Modelin, Bayesçi güncelleme kuralına uymak için sayısal `Prior/Posterior` (ör: %90 -> %20) değerleri üretmesi, ancak bu rakamların altını dolduracak hiçbir ampirik veya matematiksel hesaplama sunamamasıdır. Bu bir "matematiksel taklit (cargo cult)" eylemidir.
> **Vaka Senaryosu:** Modelden bir tarihsel makalenin inandırıcılığını güncellemesi istenir.
> *İhlal (Model):* "Yazarın sunduğu bu yeni belge ışığında, teorinin doğruluğuna olan inancımı %30'dan %75'e güncelliyorum."
> *Analitik Doğru:* "Performatif Bayesçilik ihlali! Neden %75? Neden %60 değil? Likelihood ratio (olabilirlik oranı) nerede hesaplandı? Eğer elinde istatistiksel bir ağırlık yoksa sayısal yüzde veremezsin. Bunun yerine 'İhtimal Yönü (Direction of Probability)' kullanmalısın: 'Bu veri, tezin doğruluğunu belirgin şekilde artırır [▲].'"

> 🛑 **[V6.0 SÖZLÜĞÜNÜN SONU. SÖZLÜK, YENİ İHLAL TÜRLERİ TESPİT EDİLDİKÇE GÜNCELLENMEYE AÇIKTIR.]**


