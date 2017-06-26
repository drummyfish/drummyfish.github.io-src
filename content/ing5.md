Title: Ing. na FIT – 5. a 6. semestr
Date: 2017-01-30 00:44
Author: tastyfish
Category: Articles
Tags: study
Slug: ing5
Lang: cs
Status: published

{% import 'macros.html' as m %}

Zimní semestr
=============

Tak a mám za sebou všechny předměty na FITu. Na doktorském další
předměty jsou, to ano, ale rozhodl jsem se, možná trochu zbaběle leč
racionálně, že kvůli svým (nyní už dlouhodobým) psychickým problémům své
působení na VŠ ukončím inženýrem. Tedy snad. Zde je zhodnocení
posledních předmětů, které po dalším semestru doplním o státnice a
postřehy ze studia.

Počítačové vidění (POV)
-----------------------

{{ m.fit_but_cheatsheet('POV','2','Kwz87uu') }}
{{ m.fit_but_cheatsheet('POV','1','BbFhksA') }}

POV pokládám za výjimečně užitečný a zajímavý předmět. Rozhodně mě bavil
a klidně bych se přikláněl k jeho zařazení mezi povinné předměty.

Přednášky byly nesmírně užitečné a skoro z každé jsem odcházel se
znalostí nového "mind blown" algoritmu (např. Houghova transformace,
Adaboost apod.). Opravdu, choďte tam. Zářili zde skvělí přednášející -
prof. Zemčík, doc. Čadík, dr. Španěl a dr. Hradiš. Klasicky mi moc
nesedla přednáška dr. Berana - přišel mi nepřipravený, vynucoval si
pozornost pokládáním otázek, jejichž formulace si rozmýšlel hrozně
dlouho apod. Probraly se užitečné věci, jako např. neuronové sítě (ty
jsem bohužel ve škole zatím nepotkal, jaká to škoda!).

{{ m.fit_but_cheatsheet('POV','3','t6SjVuo') }}

Poctivých 10 bodů šlo získat z pěti domácích úloh, které však byly
trochu slabinou předmětu. Měl se doplňovat kód, kterému jako celku nikdo
moc nerozuměl, takže se postupovalo většinou metodou pokus/omyl. I proto
jsem se na úkoly trochu vykašlal a získal celkově jenom 8 bodů.

Dále jsme psali půlsemestrálku za 9 bodů. Tady už se mi podařilo získat
plný počet, protože písemka byla spíš jednoduchá, neboť se skládala z
většiny z testu (jedna správná odpověď, bez strhávání!).

Projekt byl taky celkem zábavný a smířil jsem se díky němu s knihovnou
OpenCV (to, co mi na ní dřív vadilo, jsou spíš všeobecné problémy jazyka
C++). Pracovalo se v týmech jednoho až tří lidí. Já jsem se přihlásil
spolu s dalším náhodným studentem na téma přepisu skenovaného textu
(OCR). Projekt jsme si ze srandy upřesnili na přepis textu ve fontu
Comic Sans. Bylo třeba, abychom si udělali dataset (vytiskli jsme sedm
A4 stran textu a znovu je naskenovali, segmentací získali výřezy
písmenek a anotovali je), implementovali segmentaci znaků a poté jejich
klasifikaci. Pro klasifikaci jsme experimentovali s několika
klasifikátory (SVM, KNN, neuron. sítě, ...) a výsledky porovnávali s
programem Tesseract. Na závěr jsme absolvovali povinnou prezentaci
výsledků a získali jsme 27/30 bodů (3 body šly dolů, protože jsem
absolutně špatně trénoval neuronovou síť). Celkově pokládám projekt za
užitečnou zkušenost.

K projektu se navíc konaly předběžné a dobrovolné prezentace, krátce po
jeho zadání. Celkem se vyplatilo tam zajít, protože nám tam v podstatě
řekli, co za výsledek očekávají a jak přesně k němu dospět.

Zkouška se hodně podobala půlsemestrálce, tzn. byl zde test plus několik
fulltextových otázek. Ani jsem se moc neučil a podařilo se mi získat
46/51 bodů, přesně na A, nevím ani jak. Otázky nešly moc do hloubky,
ptali se nás spíš na obecné věci typu "Jak byste navrhli aplikaci pro
sledování myši v bludišti?". Písemka byla opravená za pár hodin od
odevzdání, což velmi chválím a děkuji za to dr. Hradišovi.

Takže POV musím vynachválit. Nemá zápočtu a vedou jej pohodoví lidé.
Naučí vás hodně a není extrémně těžký. Tedy vřele doporučuju.

Grafická uživatelská rozhraní v X Window (GUX)
----------------------------------------------

Tenhle předmět mě zase tak nezaujal. Nesetkal jsem se se žádnou
zlomyslností, spíš jen obsahově mohl být kurz lépe vystavěný. I tak
odcházím s pár zajímavými znalostmi.

Předmět měl na starosti ing. Lampa (od pohledu typický Unix guy).
Probrali jsme s ním v podstatě tři věci - X Window systém, OSF/Motif a
GTK+. Posud je všechno OK. Neprobrali jsme bohužel ale nic víc a tyto
tři věci byly až moc rozpitvávány, v podstatě na úroveň zdlouhavého
procházení jednotlivých funkcí těchto knihoven. Byla to dost nuda a lidi
přestali na přednášky chodit. Předmět by se měl rozhodně updatovat,
možná přestat probírat Motif, a učit třeba o Waylandu,  
různých window managerech a desktop prostředích.

{{ m.fit_but_cheatsheet('GUX','2','aBF7OWv') }}
{{ m.fit_but_cheatsheet('GUX','1','dTsnYWy') }}

V předmětu existují dva projekty - grafický editor za 8 bodů a druhý
projekt vybíraný z několika témat za 12 bodů. Každý šlo implementovat
buď v Motifu nebo GTK. Někdo chtěl pracovat v Qt, ale to vyžadovalo
individuální domluvu. Já jsem se rozhodl udělat první v Motifu a druhý,
v mém případě generátor fraktálů, v GTK. Žádný z projektů nepředstavoval
velký problém, chtělo to jenom dát si práci s nastudováním základního
API, což se zároveň hodilo na zkoušky. GTK mi přišlo rozhodně lepší než
Motif. Z prvního projektu jsem získal 7 bodů a z druhého 9 (příčinu
ztráty bodů jsem nezkoumal). Projekty byly opraveny až po prvním termínu
zkoušky. Fuj!

Na půlsemestrálku se to chtělo připravit ze starších zadání, otázky byly
často stejné. Nebudu zapírat, že jsem se neučil na 100 % a získal tak
jenom 14 z 20 bodů.

Řádný termín zkoušky se rovněž příliš nelišil. Kdo si prošel starší
zadání, musel alespoň polovinu bodů získat, i když minimum nasazeno
nebylo. Já jsem se učil standardně a získal 35 bodů ze 60 na známku D.

Předmět mi přišel bohužel trochu odbytý a učivo zastaralé, a opravy
všeho navíc trvaly hrozně dlouho. Odnesl jsem si alespoň obecný přehled
o celkem komplikovaném systému GUI na Unixech. Jelikož v předmětu není
zápočet ani minimum ze zkoušky, stojí za zvážení v případě neodbytné
potřeby kreditů.

![projekt](http://i.imgur.com/TxkrkiX.png)

{{ m.study_semester_summary("Ing.",4,"cs") }}

Semestrální projekt (SEP)
-------------------------

Semestrálním projektem student začíná diplomovou práci. V mém případě
šlo o téma zobrazování pokřivených zrcadel, které jsem měl rozpracované
už z minulého roku, a tedy jsem na něm pouze dál pracoval. Cca každé dva
týdny jsem chodil na konzultace k ing. Miletovi a snažil se posouvat
vpřed svůj algoritmus. Teoretická část práce mě hodně baví, ale bohužel
mi moc nesedí práce s OpenGL, takže jsem nepostupoval tak rychle, jako u
bakalářky, avšak i tak jsem s projektem pohnul. Ing. Mileta (popř.
kohokoli z renderingové skupiny na grafice) jako vedoucího stejně jako u
bakalářky moc doporučuju.

Zatím jsem implementoval přesné zobrazování zrcadel a jeho akceleraci.
Oproti bakalářce je v SEP vyžadována i obhajoba práce a výstup ve formě
textové zprávy, z níž později vzejde text diplomky. Obhajoby probíhaly v
kruhu studentů a vedoucích a byly studentům hodně užitečné, protože se
jednalo v podstatě o přípravu na závěrečnou obhajobu u státnic, s cenným
feedbackem. Prezentace měly být velmi krátké, cca na 5 minut. Moje práce
se celkem líbila a dostal jsem za ni 90 bodů (A), jako asi většina
studentů v naší skupince.

SEP nemá cenu hodnotit, protože zcela záleží na tématu vaší práce, na
vedoucím a na vašem postoji. Zde lze pouze doporučit vybrat zajímavé
téma, průběžně pracovat a konzultovat.

Letní semestr
=============

Poslední semestr na FITu jsem absolvoval z domu s občasnými návštěvami
fakulty kvůli konzultacím. Zde je jeho zhodnocení.

Diplomová práce
---------------

Práce na diplomce pokračovala stejným tempem jako na semestrálním
projektu. Chodil jsem pravidelně na konzultace a čas od času napsal
pár řádků kódu, až jsem si uvědomil, že zbývá asi měsíc do odevzdání.
V té době jsem znervózněl a začaly na mě jít úzkosti, cítil jsem,
že práci nestihnu dodělat. S vypětím posledních sil jsem se ale
přinutil k poslednímu sprintu před cílem a zvládl jsem nějakým
způsobem dopsat zprávu a uzavřít kód tak, abych s nimi mohl být
alespoň částečně spokojený. Ne tak spokojený, jako jsem byl při
odevzdávání bakalářky, ale dost spokojený s ohledem na svůj
psychický stav. Zprávu jsem nechal zhotovit stejně jako na bakaláři v
<a href="http://www.milangruber.cz/rubrika/copycentrum/">Copy Centru na Purkyňově</a>.

Po odevzdání započalo čekání na posudky. Během tohoto období mi přišla zpráva
od mého oponenta, dr. Pečivy, zda bych se mohl dostavit na předvedení
své práce, neboť byl zvědavý, jak vypadá realizace algoritmu, který vymyslel.
Tomu jsem samozřejmě vyhověl a zároveň jsem si uvědomil, že jsem se dopustil menšího
faux pas (či jak se to píše) - dr. Pečiva byl autorem původního konceptu mého
algoritmu, což jsem ale ve zprávě nezmínil, neboť jsem si toho nebyl vědom. Za
toto jsem se mu omluvil a dále jsem jej uvedl jako autora původního konceptu v
repozitáři své práce. On z toho naštěstí nedělal žádnou vědu, ale i tak
cítím, že bych svou chybu měl napravit i zde. Tímto mu tedy děkuji za
původní nápad pro mou diplomku.

Posudky mého vedoucího i oponenta byly velmi pozitivní, oba mi navrhli
známku A. Myslím, že tak dobré hodnocení jsem si ani nezasloužil, a opět to
mi to potvrzuje, že grafici na FITu jsou velmi hodní a pohodoví lidé.
Velice doporučuji kohokoliv z renderingové skupiny (ing. Milet, dr. Pečiva,
ing. Starka atd.) jako vedoucího závěrečné práce. S těmito lidmi jsem se
setkával často a nikdy jsem z jejich strany nezažil sebemenší zákeřnost
nebo problém, naopak vždycky ochotně poskytli svůj čas (i mimo konzultační
hodiny), prostředky a pomoc.

Diplomka je k dispozici na mém <a href="https://github.com/drummyfish/mirrors">GitHubu</a>.

<iframe width="650" height="400" src="https://www.youtube.com/embed/fpDXMgMcpY4" frameborder="0" allowfullscreen></iframe>

Státní závěrečná zkouška
------------------------

Na SZZ jsem se začal připravovat velmi brzy, protože jsem neměl už moc
energie na kratší, intenzivní přípravu. S materiály na přípravu je to
horší, spousta otázek je vypracovaná na Fitušce, ale ne všechny. Okruhy
se taky každý rok mírně mění a jsou různé pro každý obor. Z těchto důvodů
jsem si vypracoval otázky sám a dávám je k dispozici:

<a href="https://www.dropbox.com/s/f9v1v99xnmhnchu/okruhy_new.odt?dl=0"> vypracované okruhy pro rok 2017 </a>

Týden nebo dva před zkouškou jsme dostali seznam komisí, přičemž tu mou tvořili
doc. Černocký (vedoucí), doc. Smrž, doc. Janoušek, doc. Sedlák a dr. Španěl. Uměl
bych si tedy představit i lepší komisi, ale byl jsem rád např. za absenci
síťaře. Pár dní před zkouškou se začal dostavovat velký stres, který jsem špatně
zvládal, ale nedalo se zkrátka nic dělat, musel jsem se vydržet učit. Poslední
den jsem spal extrémně špatně a ráno jsem byl rozklepaný jako válečný veterán.
Jakmile jsem ale dorazil na místo před zkušebnu, stres opadl. Vše šlo pak
už velmi rychle, neboť jsem šel na řadu jako třetí.

Pan Černocký mě pozval do místnosti, všichni byli v pohodové náladě. Přečetly
se posudky, což mi ihned zvedlo šance. Následně jsem hned přistoupil k prezentaci.
I přes technické problémy s ovladačem a přes nepozornost většiny komise jsem
myslím odprezentoval slušně, obzvlášť pan Španěl vypadal, že se mu práce líbí.
Dále jsem zodpověděl otázky oponenta a členů komise. Okamžitě se přistoupilo ke
zkoušení, na stres nebyl vůbec čas.

Na papírku jsem dostal dvě otázky (ano, oproti Bc. dostáváte na magisterské
SZZ dvě otázky, přičemž si můžete vybrat pořadí zodpovězení, ale nesmíte ani
jednu zkazit). Jednalo se o nerozhodnutelnost a výpočetní modely se zaměřením
na statecharts. Po minutě přípravy (rozmýšlení úvodu) jsem začal mluvit o nerozhodnutelnosti.
Řekl jsem základy a mluvil jsem celkem plynule, až mě pan Smrž přerušil otázkou,
jak do nerozhodnutelnosti zapadá doplněk jazyka. To mě hodně rozhodilo a motal
jsem se, zkrátka jsem začal velmi příhodně být nerozhodným, až mi řekl, že mám
radši pokračovat dál. Řekl jsem tedy něco o halting problému a tím byla první
otázka uzavřena. Přistoupil jsem tedy dál k výpočetním modelům, shrnul jsem
úvod a nakreslil statecharts, ale o moc víc jsem dál nevěděl. Pan Janoušek
mi ale ohromě pomáhal - položil otázku, já jsem ji začal okecávat, a jakmile
jsem vyslovil nějaké klíčové slovo, zajásal "výborně" nebo něco podobného
a šlo se dál. Tímto stylem jsme se dobrali ke konci a šel jsem z místnosti.
Za minutu mě pozvali zpět a pan Černocký mi s úsměvem sdělil, že jsem prospěl
velmi dobře, A z diplomky a C/B ze zkoušení, celkově B. Tím ze mě veškerý
stres samozřejmě opadl.

{{ m.study_summary("Ing.","cs") }}

Po vzoru závěrečného článku Bc. studia přidávám i seznam věcí, které jsem se
oproti Bc. naučil:

- formální popis problémů a jejich řešení, konstrukci matematických důkazů, pokročilejší matematiku a formální základy informatiky
- pokročilé věci v oblasti databází, sítí, hardwaru, paralelismu
- OpenGL a obecné principy low-level API pro grafické karty (shadery, Direct3D, grafická pipeline atd.), obecně používané algoritmy (vykreslování stínů, deferred shading atd.)
- vysokoúrovňová API pro grafiku (graf scény, OpenSceneGraph, herní enginy atd.)
- něco o zpracování obrazu a počítačovém vidění
- něco o zvuku, zpracování a rozpoznávání v řeči
- něco o GUI na Linuxu
- velmi dobře umělecké 3D modelování a práci s Blenderem a něco málo o CAD systémech
- formáty a standardy pro multimédia, obraz, 3D data, zvuk atd.
- základy machine learningu (neuronové sítě, HMM, clustering atd.)
- hledat a číst vědecké články
- pár dalších věcí (dějiny techniky, praktická znalost funkcionálního programování, Vim atd.)

No a úplným závěrem bych samozřejmě rád poděkovat všem, kteří mi během studia
pomáhali, tzn. hlavně rodině, kamarádům, vedoucím a vyučujícím na škole. Ano,
připadám si jako herec přebírající Oskara.
Studium mi ze zdravotních důvodů trvalo o dva roky déle, ale
budiž to důkaz toho, že to jde. Při dostatečné motivaci se
FIT dá zvládnout i za velmi nepříznivé situace - je zde možnost rozvolnění,
prodloužení, výjimek, opakování, odvolání atd. Ne že by člověk měl
prolézat za každou cenu, když vidí, že není na správném místě -
to je ale na posouzení každého. Já osobě jsem rád, že jsem studium zvládl
zcela poctivě, nikdy jsem nepodváděl, a občas se zadařilo i získat
dobrou známku. Taky jsem zvládl všechny zkoušky na první pokus
(možná až na jeden sporný případ {{m.e(':)')}}). Jste-li současný
či budoucí student, ať naší fakulty nebo jiné, přeju vám hodně štěstí a pevné
nervy, ať si v budoucnu můžu taky přečíst vaše zkušenosti {{m.e(':)')}}.

