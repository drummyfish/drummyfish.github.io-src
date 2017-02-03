Title: Bc. na FIT - 7. a 8. semestr
Date: 2014-07-01 16:31
Author: tastyfish
Category: Articles
Tags: study
Slug: bc7
Lang: cs
Status: published

{% import 'macros.html' as m %}

Tento rok jsem studoval rozvolněně, což znamená, že v zimním
semestru jsem si prošel pouze jeden volitelný předmět a v letním mě pak
čekaly jenom státnice. Navíc jsem ale dělal na bakalářce, kterou jsem
značně rozšířil, takže zase taková flákačka to nebyla {{m.e(':)')}}

Pokročilé asemblery (IPA)
-------------------------

{{ m.fit_but_cheatsheet('IPA','1','TsejqZz') }}
{{ m.fit_but_cheatsheet('IPA','2','snoxpFV') }}

Volba předmětu pro zimní semestr bylo IPA, protože jsem na něj slyšel
dobrá hodnocení a taky předmět IAS v prvním ročníku byl fajn. Pozitivní
faktem ohledně předmětu bylo, že si studenti částečně mohli pomocí
dotazníku zvolit, co se bude probírat. Jde přeci jenom o volitelný
předmět, takže je to logické a velmi vítané.

Začnu klasicky přednáškami, které měl dr. Orság. Byl jsem celkem
spokojen se vším ohledně výkladu, i když detaily byly někdy
komplikované, možná proto, že už uplynul nějaký ten pátek, co jsem
prošel asemblery v prváku, takže stihnul proběhnout garbage collecting a
věci se mi vykouřily z hlavy. Navíc je tenhle předmět částečně o
operačních systémech a naráží na věci jako je třeba virtuální paměť.
Všechno se oficiálně probíralo pro systém Windows a taky jeho rozhraní
WinApi se objevilo v rozvrhu přednášek. Přiznám se, že jsem se zde
WinApi naučil líp než v povinných předmětech. Kdo chtěl pracovat v
Linuxu, měl možnost, ale musel si všechno zprovoznit sám, jelikož z
přednášek se mu k tomuto tématu informací nedostalo. Předmět se týkal
hlavně multimediálních instrukcí MMX/SSE a chráněného režimu, ale
dozvěděli jsme se taky něco málo třeba o 64 bitovém programování.

Podle některých recenzí minulých let byla v IPA cvičení nebodovaná a na
body se psala půlsemestrálka. V našem ročníku to bylo jinak -
půlsemestrálka byla zrušena a body se přesunuly do cvičení. Ta u mě vedl
ing. Klubal a celkem jich bylo 7 po 2 bodech. Podařilo se mi sice získat
plný počet, ale většinou to nebylo zcela triviální. Nešlo ani tak o
výsledné řešení, kdy stačilo dopsat někdy jenom 10 řádků do kostry kódu,
ale vždycky mi hrozně dlouho trvalo pochopit, co dělá ten kód okolo a co
se po mě vůbec chce za použití čeho. Zdá se mi, že nás, nebo alespoň mě,
v asmblerových schopnostech cvičící trochu přecenil {{m.e(':)')}} Na druhou stranu
zůstával klidně přesčas a ochotně pomáhal podobným zoufalým případům,
které tam seděly stejně dlouho jako já.

Musím pochválit projekt, který byl hodně volný asi díky tomu, že
studentů předmětu nebylo mnoho. Mám rád, když si můžu projekt sám zadat
a když z něj vznikne něco užitečného a ne jenom kód, který se po
odevzdání zmuchlá a zahodí. V podstatě byla na výběr dvě témata:
libovolná aplikace a benchmark. V benchmarku jste si vybrali z nabídky
algoritmů a museli jste se jej pokusit co nejvíc urychlit. Já jsem
zvolil vlastní aplikaci, konkrétně hru hledání min ve WinApi (výsledek
[ke stažení](/ke_stazeni)) následně ohodnocenou 20 body z 26.

Další pochvala patří studijní opoře, která mi pomohla v přípravě na
zkoušku. Na té se objevilo bohužel něco trochu jiného, než jsem čekal,
takže nedopadla nic moc. Předpokládal jsem něco podobného jako v IAS,
tzn. psaní programů s tím, že budeme mít k dispozici seznam alespoň
složitějších instrukcí, ale nic takového se v písemce neobjevilo, místo
toho se testovala znalost instrukcí z hlavy. Základní instrukce nebyly
problém, ale u těch složitějších jsem musel střílet a ty byly samozřejmě
za víc bodů. Jinak se vyskytla jedna teoretická otázka a taky pár
testových. Celkem jsem tedy dostal 23 bodů z 60, takže nic moc, ale
aspoň na první termín.

Počítám, že IPA je přínosné hlavně studentům chystajícím se na
magisterské studium hardwaru, avšak mně jako studentovi se zájmem o
grafiku se znalost multimediálních instrukcí potenciálně hodí taky. Koho
baví především optimalizace a snaha urychlovat aplikace o každou
nanosekundu a nebo se jenom chce přiučit, jakými instrukcemi operační
systém zajišťuje multitasking, ochranu paměti atd., přijde si zde na
své.

Celkové výsledky (zimní semestr)
--------------------------------

  předmět                    |získaných bodů  |známka
  ---------------------------|----------------|--------
  Pokročilé asemblery (IPA)  |57/100          |E

průměr: 3
pořadí v ročníku: 125.-138. místo z 164
prospěchové stipendium: 0 Kč

Bakalářská práce (IBP)
----------------------

Co se týká bakalářky, pokračoval jsem stejným tématem jako loni: nástroj
pro návrh procedurálních textur. Svou knihovnu jsem rozšířil o Phongův
osvětlovací model, L-systémy, částicové systémy, celulární automaty a
další zajímavé metody. Můj vedoucí mě ke konci semestru dokonce pozval
na setkání doktorandské renderingové skupiny, kde jsem v prezentaci
krátce předvedl své výsledky (přičemž těsně před začátkem prezentace mi
bylo sděleno, že by vzhledem k zahraničním hostům bylo vhodné
prezentovat anglicky, což jsem samozřejmě vůbec nečekal, takže dostala
zabrat i moje schopnost improvizace v cizím jazyce {{m.e('^^')}}).

Po zimním semestru přišla řada na implementaci grafického nástroje a
taky na psaní technické dokumentace. Díky dostatku volného času to nebyl
problém a zanedlouho jsem měl hotovo, celkem v předstihu. Práci jsem
nechal svázat v [copycentru na
Purkyňkách](http://www.milangruber.cz/rubrika/copycentrum/) - na poprvé
sice udělali na mých deskách malou chybu, tu však po reklamaci ještě ten
samý den bez problémů opravili, takže všem můžu doporučit tisk práce
právě zde. Po odevzdání nastal čas učit se na státnice, nicméně ještě
jsem se stihl se svou bakalářkou zúčastnit akce multimediální demo 2014,
kde jsem dokonce za umístění vyhrál kus nějaké luxusní uzeniny a
prohlédl jsem si spoustu zajímavých diplomek. Účast na soutěži a podobné
aktivity jsou zmiňovány v posudku, takže pokud máte příležitost svou
práci někde prezentovat, doporučuji tak učinit.

Výsledek svojí práce jsem zveřejnil pod licencí GPL, takže si ji můžete
[stáhnout](/ke_stazeni). Teď jsem sice už rád, že mám bakalářku za sebou
a že se konečně můžu začít zabývat jiným tématem než texturami, nicméně
práce na ní mi dala velmi mnoho zkušeností v konkrétně zaměřeném oboru
grafiky a velmi jsem si ji užil. Velkou zásluhu na tom měl i vedoucí
mojí práce, který mi nechával hodně volnosti a hodně mě podporoval.

[BPtext](https://www.dropbox.com/s/2uslhok32tg7p7c/BP%20elektronicka%20verze.pdf?dl=0)

![projekt](http://i.imgur.com/SsHGDo4.png)

Státní závěrečná zkouška (ISZ)
------------------------------

Nepamatuju si, kdy jsem byl naposledy před nějakým zkoušením tak
nervózní jako před ISZ. Ke zkoušce jsem měl jít v pořadí jako třetí hned
první státnicový den, a to k poměrně pohodové komisi vedené panem prof.
Zemčíkem.

Když pominu fakt, že jsem si celý rok vytvářel vlastnoruční souhrn všech
otázek (jenž je zde samozřejmě ke stažení), tak samotné učení mi trvalo
asi měsíc. Každou otázku jsem důkladně několikrát prošel, ale i tak jsem
se nemohl zbavit pocitu, že spoustu věcí umím jenom povrchně. Naštěstí
byl na učení docela klid díky rozvolněnému roku. Z dojmů studentů z
minulých let bohužel vyplývalo, že u státnic chtějí někteří zkoušející
znát věci do větších podrobností než u zkoušek z konkrétně zaměřených
předmětů, což byl hlavní důvod mé nervozity. Státnice jsou v někdy dost
o štěstí a na studentovi je, aby si co nejvíce naklonil pravděpodobnost
úspěchu.

V den D jsem měl natočené dva budíky na 6:30 ráno, ale nebyly vůbec
potřeba, moc jsem toho nenaspal. Před zkouškovou místností v CVT jsem
tedy byl přítomný velmi brzo se spoustou nervozity, která naštěstí
trochu opadla ve chvíli, kdy dorazili ostatní studenti a začali jsme si
trochu povídat. Hodně z nich teprve předchozí den prošlo poslední
otázku, takže na tom asi nebyli o moc líp než já. Zanedlouho se
odstartovalo a pak už to šlo rychlejším tempem. První oběť z naší
skupiny bohužel dostala za bakalářku F, takže rozhodně neplatí, že se
první nevyhazuje. Potom šel kolega číslo dvě a následně konečně já.

Když jsem vstoupil, předseda komise mě přivítal, stručně mi popsal
průběh zkoušky a pak mi předal slovo k prezentaci. Tu jsem měl naučenou
slovo od slova, takže jsem se mohl plně soustředit na to, jak vystupuju
a ne jenom na to, co říkám. Skončil jsem v časovém limitu pěti minut,
jak to má být. I když členové komise dávali pozor spíše místy a dokonce
se během mého výkladu polohlasně o něčem bavili, zřejmě je moje práce
aspoň trochu zaujala. Následovalo čtení posudků, které práci poměrně
chválily a navrhovaly mi známky A (vedoucí) a B (oponent). Pak přišla
řada na dotazy, ale nebyly žádné, ani z posudku oponenta, ani od komise.

Už během prezentace jsem tušil, že mě bude zkoušet pan doc. Kotásek,
protože ten mi věnoval asi nejvíc pozornosti. To se mi taky po přečtení
posudků potvrdilo, když mi podali otázku s číslem 2 - kombinační obvody,
zaměření na multiplexor. Nebudu zapírat, že taková otázka víceméně
každého potěší, takže jsem si celkem oddechl. Po minutě přípravy, kdy
jsem si na papír načmáral realizaci multiplexoru pomocí logických
hradel, jsem přistoupil k tabuli a začal povídat o kombinačních obvodech
a následně o multiplexoru. Nakreslil jsem to, co jsem měl na papíře, a
pan Kotásek mi položil otázku, jaké je typické využití multiplexoru.
Tady jsem se trochu zarazil a nemohl jsem si vzpomenout na dobrý
příklad. Pan docent mě začal povzbuzovat tím, že jsem u něj měl z IPZ za
A, načež jsem uvedl, že multiplexorem můžeme realizovat logické funkce,
což je sice pravda, ale není to to, co chtěl slyšet. Nakonec se mi
dostalo nápovědy, že teda serializér, a to už jsem se chytil a všechno
vysvětlil. Další otázkou bylo, kde se serializér používá, na což jsem
odpověděl, že v pevných discích a při sériových síťových přenosech.
Komise mi poděkovala a poslala mě spolu se spolužáky (kteří mě přišli
jako veřejnost sledovat) ven, aby se poradila o známkách.

Oproti předchozím kolegům se radili jen krátce a hned mě zase zavolali
zpátky. Pan Zemčík se usmíval a sdělil mi, že moje známky jsou A
(bakalářka) a B (ústní část), celkově B. Taky zmínil, že jsem díky této
známce a průměru pod dva prospěl "velmi dobře" (za což mi došlo nějakých
600 Kč jako "mimořádné stipendium"). Pogratuloval mi a bylo po všem.

Takže má rada ke státnicím zní: nepodceňujte ústní část, je velmi
krátká, což znamená, že pokud dostanete konkrétní podotázku, o které nic
neřeknete, můžete snadno vyletět - nikoho moc nezajímá, že víte tuny
věcí o něčem jiném. Na druhou stranu bylo příjemným zjištěním, že komise
má informace o vašich dosavadních výsledcích a přihlíží k nim, stejně
jako ke kvalitě bakalářské práce, která vám může pomoct. Naučte se
všechny otázky, ať máte jakoukoli komisi, a věnujte dost času
prezentaci, jak kvalitě slajdů, tak nacvičení prezentace - dobrým dojmem
na začátku si jenom pomůžete a zvýšíte pravděpodobnost úspěchu (viz
[blog pana doc. Herouta](http://www.herout.net/tao-diplomky/)).

[státnice
otázky](https://www.dropbox.com/s/aq30uwvws1snj3q/otazky%20bc.zip?dl=0)

Celkové výsledky (letní semestr)
--------------------------------

  předmět                 |získaných bodů          |známka
  ------------------------|------------------------|------------------------
  SZZ - bakalářská práce  |                        |A
  SZZ - ústní část        |                        |B
  SZZ - celkově           |                        |B

průměr celého studia: 1,948

pořadí v ročníku: 6. místo z 164

prospěchové stipendium: 600 Kč

Závěrem k bakalářskému studiu
-----------------------------

Tímto bych tedy rád uzavřel své články o bakalářském studiu na FITu,
nicméně na základě průměru jsem byl přijat na magisterský obor
počítačová grafika a multimedia a pokusím se tedy stejným způsobem
pokračovat v psaní dál. Na závěr bych rád uvedl několik (snad)
užitečných informací pro ty, kteří třeba o této škole uvažují a chtějí
vědět, co všechno se naučí.

Fakulta je obecně na velmi vysoké úrovni, určitě mezi prvními v
republice. Nikoho proto nemůže překvapit, že studium je poměrně těžké
(pokud člověk není vyloženě génius), ale na druhé straně nesmírně
přínosné a obohacující. Je časově náročné a to v průběhu celého
semestru, hlavně kvůli velkému množství projektů, proto není dobré při
škole pracovat, i když to spousta lidí dělá (a spousta jich taky
vyletí). Pokud se někdo snaží studiem jenom prolézt, a že je takových
lidí dost, pak musím říct, že si zbytečně komplikuje život, protože
titul bez námahy se dá získat mnohem jednodušeji na jiných školách.

Abych jenom nechválil, pokusím se taky pár věcí zkritizovat, nicméně jde
jenom o maličkosti. Menza na FITu je otevřená jenom na oběd. Studijní
poradce píše e-maily v šifrách. Občas musíme chodit na hnusný FEKT.
Posudky diplomek a bakalářek nejsou (např. oproti MUNI) veřejné, takže
se nemůžu po večerech bavit pročítáním hodnocení prací špatných
studentů. Takových detailů bych našel ještě víc, ale nemá to valného
smyslu, neboť nejde o nic světoborného. Pokud něčeho za dobu studia
lituji, tak snad jenom toho, že jsem si nezapsal předmět IKR.

Dal jsem si tu práci a sestavil pár statistik. Za dobu studia jsem
absolvoval/získal:

-   37 předmětů
-   30 zkoušek (z toho 2 ústní)
-   185 kreditů (dle definice 11100 hodin studia a práce)
-   cca 43 projektů (od malých domácích úkolů až po větší týmové
    projekty a kvalifikační práci)
-   cca 30 semestrálních testů
-   6 obhajob
-   2622 bodů

A konečně malý výčet toho, co jsem se (konkrétně já) naučil:

-   vysokoškolskou matematiku a trochu fyziky (hlavně elektroniky),
    především diskrétní matematiku, analýzu, pravděpodobnost, numerické
    metody a teorii signálů.
-   teorii informatiky: algoritmy, formální jazyky, fungování
    překladačů, principy operačních systémů, základy algoritmické
    složitosti
-   teoreticky rozumět jednoduchému hardwaru prakticky na všech
    úrovních, tj. od elektronických a logických obvodů až po návrh
    procesoru a celého počítače jako celku
-   pracovat se systémy Windows a Linux
-   dobře a efektivně programovat, především imperativně a objektově,
    ale také na nízké úrovni (jazyk symbolických instrukcí), programovat
    vícevláknové, událostmi řízené, grafické a síťové aplikace
-   navrhnout a implementovat celý informační systém pro danou firmu
-   vytvářet dynamické webové stránky pomocí HTML, CSS, PHP, SQL,
    JavaScriptu atd.
-   programovací jazyky: velmi dobře C a C++, dále alespoň na základní
    úrovni běžné jazyky jako Java, JavaScript, Perl, Python, PhP, IA32
    apod., částečně Bash, Lisp, Prolog, C\#, VHDL, apod.
-   jiné jazyky: XML, SQL, Latex, ...
-   pracovat v malém týmu (2 - 5 lidí), v časovém presu a paralelně na
    více projektech
-   rozumět počítačovým sítím a Internetu
-   psát dokumentace a technické zprávy, psát a prezentovat v angličtině
-   rozumět cizímu kódu a hledat informace v literatuře, i cizojazyčné
-   základy důležitých odvětví informatiky jako jsou grafika, umělá
    inteligence, databáze, uživatelská rozhraní, počítačové simulace
    nebo softwarové inženýrství
-   pár věcí z volitelných předmětů jako španělština, typografie,
    psychologie nebo právní minimum



