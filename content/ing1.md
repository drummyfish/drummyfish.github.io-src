Title: Ing. na FIT – 1. semestr
Date: 2015-03-06 16:40
Author: tastyfish
Category: Articles
Tags: study
Slug: ing1
Lang: cs
Status: published

{% import 'macros.html' as m %}

První semestr magisterského studia grafiky je úspěšně za mnou a
už se těším, co pěkného o něm napíšu. To ovšem neznamená, že o něm
napíšu jenom samé pěkné věci - tak třeba za prvé: byl hodně náročný.
Jeden z nejnáročnějších vůbec. Dobrá zpráva však je, že jakmile jej máte
za sebou, jste prý prakticky za vodou. Navíc se mi jej nějak podařilo
zvládnout i s celkem slušnými známkami.

Na začátku semestru jsem se hecnul a zúčastnil jsem se každoročně
pořádaného programátorského maratonu
[MediaContest@FIT](http://www.fit.vutbr.cz/events/McFIT/). Byla to
zajímavá zkušenost, kterou vřele doporučuji všem. Nebo se alespoň
přijďte podívat a povzbudit soutěžící týmy.

Ještě než se dostanu k samotným předmětům, bych rád naznačil, jak zatím
studium vnímám oproti bakaláři. Především bych nový nádech učiva shrnul
jedním slovem: formalismy. Prakticky ve všech předmětech jsme všechno
důležité zapisovali precizně matematicky. Není náhodou, že hned první
semestr jsme měli dva stěžejní předměty, které nás tomu měly důkladně
naučit: TIN a MAT... ale o těch až za chvíli. Jestliže typickým úkolem
na bakaláři bylo: "najděte řešení problému X", nyní je to: "formálně
popište řešení X problému Y a dokažte, že Y skutečně řešením je". Nebo
nás alespoň k něčemu podobnému vedou. Na druhou stranu byl semestr
jednodušší např. po stránce cvičení, kterých nebylo mnoho a byla
jednoduchá.

Náročnost učiva taky o něco vzrostla. Ne extrémně, avšak znatelně - o
zkouškovém jsem se nestíhal všechno učit hezky v předstihu a ještě si
dát občas volno - učil jsem se od konce semestru až do poslední zkoušky
prakticky každý den a často ještě v den zkoušky jsem narychlo
propočítával příklady, které jsem do té doby nestihl, což se mi na
bakaláři nestávalo. Ale pojďme se podívat, jak na tom byly konkrétní
předměty.

Teoretická informatika (TIN)
----------------------------

{{ m.fit_but_cheatsheet('TIN','1','Wxykk3g') }}
{{ m.fit_but_cheatsheet('TIN','3','P3aOnlw') }}
{{ m.fit_but_cheatsheet('TIN','2','Ie0xdbk') }}

Na TIN jsem se samozřejmě těšil už od prázdnin, protože mělo jít údajně
o nejtěžší předmět studia. Dle mého názoru tomu tak není, i když je
velmi těžký. Já jsem ale měl tu výhodu, že mě předmět bavil, a naučil
jsem se spoustu věcí, které by měl znát každý, kdo chce patřit mezi
informatiky k těm lepším - Turingovy stroje, základy složitosti a
především matematické důkazy.

Přednášky vedl prof. Češka, s nímž jsem doposud neměl čest se setkat.
Přednáší pomalu, což je podle mě u tak náročného předmětu výhoda. Navíc
je jeho výklad logický, srozumitelný, nedělá chyby a neztrácí se v něm
(jak se to některým vyučujícím občas stává). Jde vidět, že svému oboru
opravdu rozumí a taky jsem si všiml, že velmi dbá na kvalitu předmětu.
Co se týká učiva, začali jsme opakováním z předmětu IFJ - definice
jazyka, gramatik, Chomského hierarchie. Postupně jsme probírali
regulární, bezkontextové a rekurzívně vyčíslitelné jazyky a nakonec jsme
se dostali i k teorii složitosti (např. k problému P vs NP). Na
přednáškách očekávejte především definice, věty a důkazy. Právě důkazy
jsou potom jednou z hlavních věcí, kterou se v TINu naučíte, což je
podle mě velice dobře, jelikož informatika je v podstatě odvětví
matematiky a pilířem matematiky jsou důkazy.

Předmět zahrnoval čtyři domácí úkoly po 5 bodech. Navzdory zvěstem o
jejich obtížnosti jsem je zvládal celkem dobře a musím říct, že mě hodně
dobře připravily na zkoušku - proto úkoly neopisujte a snažte se je
nejdřív vyřešit sami, opravdu vám to hodně pomůže. Těžší mi přišly až
některé příklady třetího a čtvrtého úkolu, a to hlavně proto, že nám
občas omylem zadali mnohem těžší příklad, než měli v úmyslu (jednou šlo
dokonce o dosud nevyřešený problém teoretické informatiky {{m.e('^^')}}). Chyby
byly sice opraveny, ale vždy až na poslední chvíli. Celkově vzato úkoly
mohl člověk zvládnout sám, ale jelikož v TINu je potřeba sbírat co
nejvíc bodů a nehrát si na hrdinu, je mnohem lepší dát dohromady skupinu
spolužáků, s nimiž si alespoň zkontrolujete řešení, popř. zapracujete na
obtížnějších příkladech. Ani tak ale z úkolů nepočítejte s plným počtem
bodů, to se nepodaří prakticky nikomu. Má bodová hodnocení byla po řadě
5, 4, 4,2 a 5.

Zápočet je v TINu za 15 bodů, přičemž se ale nepočítá čtvrtý úkol (takže
se na něj hodně lidí v praxi vykašle). Jelikož ze tří úkolů na 99,999 %
nedostanete plný počet, musíte posbírat alespoň pár bodů na
půlsemestrálce. Po získání zápočtu je dalším cílem získat 25 bodů za
semestr, aby vám stačilo minimum ze zkoušky, protože ta může být opravdu
nemilosrdná.

Půlsemestrálku proto není radno podceňovat. Dovolím si říct, že alespoň
v mém ročníku nebyla tak hrozná, neboť se stihly probrat jen regulární a
bezkontextové jazyky. Navíc, a tento krok velmi chválím, přidali oproti
minulým letem trochu času na psaní, takže člověk nemusel panikařit. V
písemce byly čtyři příklady, z nich dva poměrně jednoduché, takže jsem
skončil trochu s předstihem s tím, že jsem napsal všechno až na jeden
důkaz, který jsem neměl naučený a sepsal jsem jej pouze slovně a ne moc
elegantně. Prof. Češka mě velmi mile překvapil, když mi písemku
ohodnotil 19 body z 20, v což jsem vůbec nedoufal.

Zbývala semestrální zkouška. Nechtěl jsem nechat nic náhodě a začal jsem
se učit hned po skončení přednáškového období. Zkouška byla nakonec
hrozně rozsáhlá a tak tak mi na ni stačily dvě a půl hodiny, které jsme
na vypracování dostali. Příklady Byly ale férová a neobjevily se žádné
zákeřnosti - letmo si tak vzpomínám na nějaký parametrizovaný konečný
automat, pumping lemma pro bezkontextové jazyky (formulovat, dokázat a
použít) a ideje složitějších důkazů. Po celkem dlouhém čekání mi přišlo
49 bodů z 60, velká radost a úleva, že to mám za sebou. B z údajně
nejtěžšího předmětu na FITu jsem opravdu nečekal. Dle mého názoru se
zkouška dá zvládnout dobře, ale vyžaduje opravdu hodně učení a to i
během semestru.

TIN patřil mezi mé oblíbenější předměty ze dvou důvodů: jednak mě zajímá
teoretická oblast informatiky a formálních jazyků a jednak byl předmět
jako takový velmi dobře zvládnutý. Na rozdíl od PDB nebo MATu se
skutečně detailně probere všechno, co může být na zkoušce. Problémy mají
studenti jen s objemem látky, který je ohromný, ale myslím si, že pokud
někdo chce magisterský titul z jedné z předních vysokých škol, musím si
přesně tímhle projít. Hodně štěstí budoucím generacím a ať žije TIN.

Pokročilé databázové systémy (PDB)
----------------------------------

{{ m.fit_but_cheatsheet('PDB','1','XdxiRxD') }}
{{ m.fit_but_cheatsheet('PDB','2','ch6fEwz') }}

PDB bylo bohužel asi největším zklamáním semestru. Na grafice je tenhle
předmět povinný asi jenom kvůli probíraným prostorovým indexům, které
jsou opravdu důležité, avšak zbytek látky byl pro mě ne moc zajímavý a
užitečný. To ale nebyl pravý důvod mého zklamání. Tím byly totiž
přednášky.

Těch se ujímal doc. Dušan Kolář známý z IPP. Nic proti němu nemám, je to
bezpochyby velký odborník v dané oblasti, jenom se mi nelíbil jeho styl
přednášek a hlavně struktura předmětu, za kterou jako garant zodpovídá.
Celý kurz se přednáší podle ohromné bible asi tisíce slajdů, která je
poslepovaná ze vzorců povytahovaných z vědeckých článků a často se
stává, že k nim není uvedený kontext, takže jsem se musel párkrát
uchýlit ke studiu právě z těch článků, což rozhodně není ideální a
jednoduché čtení. Nikde není moc naznačená struktura přednášených pojmů,
všechno je jen lineární sled termínů, takže většinou nevíte, o čem je
řeč. Na Wikipedii taky nic nenajdete, protože přednášené věci jsou na to
příliš specializované - to by samozřejmě nebyl problém, pokud by vše
bylo dobře vysvětlené v rámci předmětu. Od přednášek vždycky očekávám
přinejmenším zdůraznění toho, co je podstatné se později naučit, čehož
jsem se zde dočkal snad jenom v minimálních náznacích. Takové jsou
alespoň mé pocity.

PDB mělo jinak i svou praktickou část ve formě cvičení. Ta nebyla
bodovaná a šlo jenom o vyzkoušení věcí, abychom věděli co a jak na
projektu. Celkem se vyplatilo si na ně zajít, nebo si alespoň projít
materiály k nim. Zdrojové kódy ze cvičení velmi dobře posloužily jako
základ projektu.

Projekt byl mírně (ale zase ne tolik jako třeba HSC) drsný. Psal se v
trojčlenném týmu s využitím Javy a muselo se přitom použít školní SVN.
Měli jsme si vymyslet nějaký systém využívající multimediální,
prostorové a temporální databáze a ten implementovat. Hned na začátku
semestru jsem si sehnal [kolegy](http://itlenka.blogspot.cz/) a začali
jsme projekt řešit, alespoň ve fázi konceptů. Řekli jsme si, že uděláme
policejní systém, a každý jsme si vybrali jednu část - já samozřejmě tu
multimediální. Jak se postupně probíraly věci na cvičeních, začali jsme
i něco programovat, ale nebylo na to kvůli jiným věcem moc času, proto
jsme se rozhodli udělat ke konci semestru radikální krok a zorganizovali
jsme programovací víkend. V podstatě jsme se na dva dny zavřeli všichni
do pokoje, kde jsme chtěli všechno hezky dokončit, avšak trochu jsme se
přepočítali a po dvou dnech intenzivního programování od rána do večera
a totálním vyčerpání stále ještě nebylo hotovo. Opravdu jsme si sáhli
skoro až na dno, abychom všechny části dokázali do odevzdání integrovat
a zprovoznit. Pak nás ještě čekala obhajoba - ta byla naštěstí velmi
jednoduchá a šlo jenom o předvedení funkcionality. Byl nám sdělen
maximální počet 20 bodů, nicméně později jsme o 3 přišli kvůli nějakým
chybkám v dokumentaci k temporálním dotazům. Shodli jsme se, že to bylo
trochu nepřiměřeně dost, avšak nechtěli jsme to už řešit, tak jsme to
nechali být.

Půlsemestrálka mě taky trochu vytočila. Troufnu si tvrdit, že první běh
byl o něco jednodušší. Na tom se totiž vyskytly všechny "obvious"
otázky, kdežto na druhý, na kterém jsem samozřejmě byl já, zbyly
specialitky. I když jsem se poctivě učil, tak mi přišly otázky velmi
"WTF" - ne "WTF, tohle jsme se učili, ale nečekal jsem to na písemce",
ale spíš "WTF, co to po mě tady vlastně chtějí?". Vyplnil jsem všechno
dle nejlepšího vědomí a svědomí a dostal jsem 14 bodů z 20. Těžko říct,
jestli šlo o úspěch nebo fail.

Inu a zbývá nám zkouška. Jak jsem psal, z materiálů k předmětu se učit
moc nedá a klíčovou přípravu tak tvoří hlavně procházení starých zadání,
abyste si udělali představu o tom, co čekat a co se učit. Jediná jistota
jsou asi prostorové indexovací struktury. Takových sedmdesát procent
toho, co jsem se nakonec naučil, jsem uměl nazpaměť, aniž bych tomu
nějak rozuměl a nepotkal jsem člověka, který by to měl jinak. Otázky
byly naštěstí podobné těm, které jsem si procházel, takže jsem ke všemu
něco vyplnil. Nakonec jsem obdržel 38 bodů ze 60, takže mi o jeden bod
uteklo C.

Normálně bych to nechal takhle být, ale měl jsem jinak docela dobré
známky, tak padlo rozhodnutí jít na reklamaci. Měl jsem z pana Koláře
trochu strach, ale říkal jsem si, že není co ztratit. Musím říct, že mě
docela podusil. Písemku jsem opravdu nenapsal dobře, to uznávám, i když
si myslím, že je to částečně i vina předmětu. Vypadalo to, že žádný bod
nakonec nedostanu, tak jsem naznačil, že se tedy nedá nic dělat a že už
půjdu, když mi pan Kolář najednou řekl, že mi ten bod s přimhouřenýma
očima nakonec dá. Alespoň tohle mu tedy připisuju k dobru.

Souhrnně by se dalo říct, že předmět potřebuje předělat svou strukturu,
nebo lépe řečeno nějakou zavést. Není to čisté zlo, naučil jsem se
zajímavé věci - např. už jenom to, že existují nějaké databáze pro práci
s geometrickými daty, multimédii, časem apod. Rovněž jsem si osahal JDBC
a projekt nakonec taky nebyl nejhorší. Bohužel těch pozitivních věcí je
tady málo v porovnání s tím, co je špatně. Chtělo by to občas nějaký
příklad na přednášce, vyškrtat zbytečnosti ze slajdů, zdůrazňovat učivo,
které je hodně důležité a tomu taky věnovat čas navíc... zkrátka udělat
učení pro studenty trochu příjemnějším.

![projekt](http://i.imgur.com/9aca8n1.png){.center width="640"}

Seminář teoretické informatiky (STI)
------------------------------------

STI je pomocný předmět k předmětu TIN a jedná se v podstatě o taková
demonstrační cvičení. TIN totiž sám o sobě je tak nabitý informacemi, že
potřebuje další předmět k tomu, aby se všechno úspěšně vysvětlilo a
demonstrovalo. V STI vás nečeká žádná zkouška, jen zápočet za docházku.

Semináře vede prof. Vojnar a musím uznat, že se mu to daří velmi dobře.
Z IOS jsem si jej pamatoval jako nekompromisního a přísného člověka, ale
na STI nám naopak neskutečně pomohl pochopit všechny složité věci, které
bylo potřeba zvládnout, např. pro domácí úkoly do TINu. Je to nejenom
vynikající odborník, ale umí látku podat správně, tzn. nejdřív stručně
intuitivně vysvětlit, poukázat na nějakou paralelu z programování a až
potom věc podat formálně. Za pana Vojnara párkrát zaskočil dr.
Rogalewicz, který taky semináře zvládal obstojně, avšak občas se do
příkladů sám zapletl.

Jeden malý nedostatek měl seminář v tom, že byl hrozně dlouhý a mně
zrovna vycházel tak krásně, že byl do devíti hodin večer na konci dne,
kdy jsem měl deset hodin vyučování vkuse. Po vzoru IOSu navíc pan Vojnar
dělal jen jednu krátkou přestávku a přetahování přes čas si bohužel taky
neodpustil - poslední seminář se dokonce natáhl o hodinu. Nevím, čí to
byla vina, ale možná vypustit pár extra dlouhých a těžkých příkladů,
které stejně nemůžou být ani na písemce ani v úkolu, by nebylo na škodu.

STI celkově hodnotím velmi kladně, pomůže vám prohloubit znalosti z TINu
a připravit se na všechny typy příkladů. O užitečnosti předmětu svědčí i
fakt, že na něj chodila spousta studentů, kteří jej neměli ani zapsaný.
V prváku si proto STI nezapoměňte zapsat.

Dějiny a filozofie techniky (FIT)
---------------------------------

Tak zde jsem zbaběle zvolil "docházkový" předmět pana mgr. Klapetka,
abych měl z krku PVH předmět a zároveň abych si moc nepřitížil v poměrně
těžkém semestru. FIT byl ne příliš překvapivě podobný PRM na bakaláři.

Přednášky probíhaly dle očekávání v přátelském duchu. Dozvěděli jsme se
spoustu zajímavých věcí o dějinách techniky od pravěku až do moderní
doby. I když mě dějepis nikdy extra moc nezajímal, myslím si, že dějiny
svého oboru bychom alespoň letmo znát měli, a tak jsem se snažil dávat
alespoň trochu pozor, i když mě nečekala žádná zkouška. Musím opět říct,
že mgr. Klapetek je velmi dobrý přednášející a prokládá svůj výklad
zajímavými pointami.

Jedna malá věc se po nás nicméně chtěla - měli jsme napsat krátkou esej
na libovolné téma související s předmětem. Zaslechl jsem zvěsti, že
zápočet dostane každý, i když esej neodevzdá. To by ale podle mě nebylo
moc fér, tak jsem napsal alespoň jednu stránku o Severní Ferdinandově
dráze, i když oficiálně měla mít alespoň tři stránky. Zápočet jsem
dostal bez problémů.

FIT je pohodový předmět. Kdo chce, něco si odnese, ostatní si odnesou 3
kredity. Osobně jsem přednášky navštěvoval rád a nezřídka jsem se
dozvěděl něco zajímavého.

Hardware/Software Codesign (HSC)
--------------------------------

{{ m.fit_but_cheatsheet('HSC','1','eO1QXuj') }}
{{ m.fit_but_cheatsheet('HSC','2','j7EWulA') }}
{{ m.fit_but_cheatsheet('HSC','3','CnkhpbZ') }}

HSC mě potěšilo a nepotěšilo. Byl to takový normální hardwarový předmět,
ale bohužel jsem nenáviděl projekt a po jeho absolvování jsem si
předsevzal, že už nechci nikdy mít nic společného s Fitkitem.

Musím říct, že přednášky byly kvalitní. Doc. Fučík přednášel velice
dobře a počítal spoustu příkladů, aby nás připravil na zkoušku. Prvních
pár prezentací měl navíc dr. Rychlý o prostředí Catapult C, v němž jsme
měli dělat projekt - všechno bylo OK, s přednáškami žádný problém.
Probíraly se hlavně různé algoritmy rozdělování úloh mezi hardware a
software a nějaká ta teorie ohledně syntézy kódu na logický obvod při
daných omezeních např. na propustnost, plochu na čipu nebo příkon.

Dočkali jsme se samozřejmě i půlsemestrálky. Na té se objevily jenom
příklady a nebyla vůbec zákeřná, všechny se propočítaly na přednáškách.
Bohužel jsem se vlastní vinou zapomněl naučit list-based scheduling a
tak jsem z maxima 20 bodů dostal jenom 16.

Jak jsem předeslal, čekal nás v HSC projekt na Fitkitu, který je dle
mých zdrojů každý rok víceméně stejný - rozdělit úlohu filtrace obrazu
mezi hardware (FPGA) a software (MCU). FPGA je rychlé, ale nevleze se do
něj vše, MCU je pomalé, ale může vykonávat úlohy, které se do FPGA
nevejdou. Úkolem je sprasit vše tak, aby to celé fungovalo dostatečně
rychle, tzn. na dostatečném FPS. Posud celkem dobrý nápad. První
problémy přichází s tím, jak se snažíte vše prakticky rozjet. Nemyslete
si, že si prostředí Catapult C jen tak nainstalujete na svůj operační
systém - vyžaduje tolik závislostí a licencí, že radši dostanete ISO s
předinstalovaným OS a patřičným softwarem pro VirtualBox. Já jakožto
command line člověk z takových věcí samozřejmě šílím, navíc ale nestačí
ISO jenom nabootovat, musí se podle nějakého návodu instalovat další
licence a skripty pro překlad, k tomu musím běhat po Brně a shánět USB
kabel pro Fitkit, který se uráčí fungovat, prostě hnus. Návod na řešení
projektu je v PDF rozsahu krátkého románu (OK, trochu přeháním, ale i
tak). Nejhorší ze všeho ale je, že potřebujete z projektu dostat alespoň
5 bodů, abyste obdrželi zápočet, takže se nejde na tuhle útrpnou práci
vykašlat. S projektem jsem se tak opravdu pral, až jsem byl občas
zoufalý, jelikož jsem nevěděl, jestli dělám něco špatně, nebo mám jenom
vadný Fitkit, nebo mám špatně nastavenou nějakou věc ve VirtualBoxu. Po
spoustě hodin se mi nakonec podařilo udělat zkušební, čistě softwarovou
implementaci, udělat profiling, navrhnout komunikaci mezi MCU a FPGA a
vypracovat dokumentaci. To hlavní na projektu se mi sice nepodařilo
realizovat, ale měl jsem v dokumentaci alespoň popsaný hrubý postup, jak
bych to udělal, takže jsem čekal možná i 10 bodů z celkových 25. Nakonec
jich přišlo přesně 5. Na jednu stranu jsem tedy slavil zápočet, na
stranu druhou mi kvůli tomu nestačilo minimum ze zkoušky a byl jsem
trochu smutný.

Takže jsem se musel nakopnout a naučit se něco extra na zkoušku. Ta se
skládala stejně jako půlsemestrálka jenom ze samých příkladů. Někdy se
prý objeví i teoretická otázka, avšak dle slov samotného doc. Fučíka je
v HSC zkoušení praktických znalostí výrazně preferováno. Času jsme na
řešení dostali víc než dost, a tak se dala spousta nenaučených postupů
vymyslet přímo na místě. Abych to shrnul, čekal jsem to horší, a ze
zkoušky jsem odcházel se všemi otázkami vyplněnými. Nakonec jsem dostal
45 bodů z 55 a tedy známku D.

Celkový verdikt pro HSC je tedy: všechno OK, až na projekt. Chápu, že
hardwarové projekty se asi těžko navrhují, ale takový argument mi ve
chvíli, kdy se s ním musím potýkat, moc nepomůže. Nejradši bych viděl
zrušení minima a možná trochu mírnější hodnocení nebo zadání s
jednodušším algoritmem, protože student má už tak dost práce vůbec
rozjet vývojové prostředí. Pozitivně naopak hodnotím férovost písemek -
je na ně dost času, všechno se propočítá na přednáškách, příklady jsou
rozumné a jde vidět, že se dané algoritmy dají uplatnit v praxi.

Počítačová grafika (PGR)
------------------------

{{ m.fit_but_cheatsheet('PGR','1','zpjHt95') }}
{{ m.fit_but_cheatsheet('PGR','2','QJQhbGI') }}

Na tenhle předmět jsem se docela těšil, jednak kvůli jeho náplni a
jednak proto, že jej garantuje a přednáší doc. Herout - známá osobnost
FITu.

Pan Herout mě překvapil hned na první přednášce. Všechny studenty v
místnosti vyzval, aby se ostatním představili a sdělili nějaký highlight
z prázdnin plus očekávání kladená na předmět PGR. Velmi zajímavý úvod
musím říct. Podobně pak probíhala každá další přednáška - jeden po
druhém jsme na konci a na začátku hodiny sdělovali, co jsme si
zapamatovali. Na jednu stranu se tak zabila spousta času, na stranu
druhou však čas vynaložený na opakování učiva a učitelův feedback není
dle mého názoru čas promrhaný. Hrozně se mi líbilo, že se spousta učiva
točila kolem her. Jednu přednášku jsme dokonce asi půl hodiny věnovali
procházení screenshotů ze starých games a zkoumali jsme, jak se v nich
řeší 3D vykreslování. Pouštělo se taky hodně krásných videí z vědeckých
článků. Přednášky mě tedy opravdu bavily.

V PGR byla taky cvičení. Ta měla jednu výhodu a jednu nevýhodu. Výhodou
byla krásná doktorandka, ing. Pavelková, a nevýhodou fakt, že jste úkoly
museli dělat doma, protože se v CVT nedaly stihnout. To se taky občas
lidem stávalo, a tak bylo povoleno úkoly odevzdávat i dodatečně bez
jakýchkoliv penalizací, takže to zase taková hrůza nebyla. Navíc si
myslím, že kdyby člověk rychle něco nabouchal během cvičení, aby měl
pokoj, nenaučil by se toho tolik, jako když se na to podívá v klidu
doma. Věci, které jsme si prakticky procvičili, pokládám pro grafiky za
naprosto nezbytné - základy OpenGL, vykreslování průhledných objektů a
dokonce stíny pomocí shadow volumes. Cvičení byla tři po 4 bodech,
získat plný počet ze všech nebyl problém. Zdrojové kódy úkolů navíc
spousta studentů úspěšně využila jako kostru pro projekt.

Velmi zajímavé byly projekty, jejichž tématem byly např. 3D hry,
raytracing, radiozita, animace apod. Spousta věcí se mi zamlouvala,
avšak nejdřív jsem potřeboval tým - jelikož jsem měl v předmětu
kamaráda, dali jsme dohromady dvojici a společně jsme sepsali seznam
zadání, o něž bychom měli zájem. Ač se nám při následném refresh waru
nepodařilo nic ze seznamu ukořistit, dostali jsme nakonec po prosebném
e-mailu panu Heroutovi pěkné zadání "realistické generování oblohy" a
mohli jsme konečně začít pracovat. Nejdřív jsem se iniciativy chopil
sám, zašel jsem téma prokonzultovat s panem Heroutem a následně jsem
začal psát ray tracer, který jsem průběžně zdokonaloval. Všechno se to
celkem s předstihem stihlo, kolega ještě na závěr zparalelizoval
výpočet, udělal pár optimalizací a společně jsme sesmolili dokumentaci.
Zbývalo ještě projekt obhájit, což se nám povedlo - celá obhajoba
spočívala v krátkém předvedení programu a odpovědích na pár otázek,
trvala celkově cca pět minut. Dostali jsme plný počet 30 bodů, k čemuž
si myslím, že nám pomohlo pár věcí, jež jsme udělali nad rámec, jako
např. generování animací nebo zmiňovaný paralelní výpočet.

Půlsemestrální písemka byla celá formou testu s jednou správnou
odpovědí, přičemž se strhávaly body za špatnou odpověď. Rozdat test
trvalo mnohem déle, než jej napsat - hotovo jsem měl během pár minut. Co
se týká otázek, byly hodně jednoduché a ptali se hlavně na základní
koncepty OpenGL, které jsem měl nastudované už z prázdnin. Dostal jsem
plných 7 bodů.

Tím jsem tedy měl 49 bodů za semestr a tak byla výhledově naděje i na
dobrou známku. Avšak na písemku jsem se moc neučil - nevěděl jsem moc
co. Jediné, co jsem stoprocentně čekal, byla otázka, která se v PGR
objevuje každý rok - OpenGL pipeline. Zkouška byla nakonec podobná jako
půlsemestrálka - skládala se z několika otázek testových a tří otázek
fulltextových a ano, jedna z nich byla na OpenGL pipeline. Další se
potom týkala šumů a paprsků v ray tracingu. Bohužel právě v OpenGL
pipeline jsem udělal chybu - suverénně jsem písemku odevzdal a záhy si
uvědomil, že jsem zapomněl na rasterizaci. Tohle mě hrozně žralo,
protože to byla hloupá chyba, navíc jsem taky mohl něco víc napsat k těm
šumům. Nakonec mi přišlo 41 bodů, což mi vyšlo přesně na A.

Předmět PGR byl v porovnání s ostatními v semestru skutečně easy. Ale
byl taky užitečný. Líbil se mi projekt a líbily se mi přednášky. S ničím
nebyl problém a s ničím nebyly nervy. Myslím, že to potvrzuje to, co
říkám pořád - ústav UPGM zaměstnává nejpohodovější lidi na FITu.

![projekt](http://i.imgur.com/YjaDlcS.png){.center width="640"}

Pokročilá počítačová grafika (PGP)
----------------------------------

{{ m.fit_but_cheatsheet('PGP','1','EJfGbnp') }}
{{ m.fit_but_cheatsheet('PGP','2','WMaJfIW') }}

Tento předmět mě zaujal svou anotací - generování terénů, realistické
stíny, velké scény apod. Až na první přednášce jsem zjistil, že jsem se
nepodíval na prerekvizity, mezi nimiž bylo PGR, kterým jsem zrovna
procházel :D Naštěstí jsem si s OpenGL o prázdninách už trochu hrál a
předmět navíc nebyl vůbec hardcore. Plusem bylo, že jej vedli převážně
doktorandi z ústavu grafiky, což jsou podle mě nejvíc v pohodě lidi, jak
už jsem psal u PGR.

Přednášky byly organizovány trochu chaoticky - každou měl totiž na
starosti jiný člověk, většinou některý z už zmíněných doktorandů, ale i
pár externistů (např. animátor z Illusion Softworks nebo grafik z
matfyzu Karlovy Univerzity). O pokročilém OpenGL nám přednášel vedoucí
mojí bakalářky, ing. (brzodoktor) Milet. Probírané věci byly velmi
zajímavé - hodně mě zaujala např. přednáška o HDR. Škoda jenom, že
slajdy ke spoustě z nich nebyly ke stažení. Nezřídka se přetahovalo
třeba i půl hodiny, avšak nemám to doktorandům za zlé, vyčítal bych to
spíš zkušeným docentům a profesorům. Celkově se přednášky nesly ve velmi
přátelském duchu, obzvlášť ke konci, kdy se nás v místnosti scházelo do
deseti lidí - z pedagogického hlediska to byla výhoda, neboť se nám pak
přednášející mohl věnovat mnohem individuálněji a mohli jsme lépe
diskutovat.

V předmětu se průběžně zadávaly malé domácí úkoly za 2 body, jež se mi
podařilo úspěšně vypracovat vždy za plný počet. Jednalo se o různé
probrané věci, např. shadow mapping s průhlednými objekty, tessellation
shader, geometry shader apod. Ke splnění stačilo většinou dopsat do
dodaného kódu pár řádků, nicméně před tím zabralo trochu času si dané
téma projít a pochopit a našli se studenti, kteří s tímto měli problém.

Dále zde byl projekt až za 30 bodů, buď pro jednotlivce nebo malé týmy.
Já jsem nechtěl řešit komunikaci a sdílení kódu s někým jiným, tak jsem
si zaregistroval samostatný projekt na téma distribuovaný ray tracing,
které se ukázalo velmi zajímavým. Každý grafik by si měl co nejdříve
napsat ray tracer, protože je to velmi jednoduché, přínosné z hlediska
zkušeností a poměrně snadno dosáhnete pěkných vizuálních výsledků.
Projekty se po novém roce obhajovali formou prezentace, na niž byl brán
velký ohled při bodovém hodnocení. Prezentaci jsem napěchoval pěknými
obrázky a podařilo se mi dostat plných 30 bodů.

Půlsemestrálka byla hodně OK. Psali jsme ji na začátku přednášky cca 20
minut a přibližně za stejnou dobu byla taky od odevzdání opravena - to
musím skutečně pochválit. Šlo o test typu jedna správná odpověď, dokonce
bez strhávání bodů. Vytěžil jsem 7 z 9, což se dalo považovat dle
histogramu celkem za úspěch.

Na semestrálku jsem se moc neučil. Důvody byly dva: jednak jsem měl
zrovna v té době zkoušku z HSC a PDB, na které bylo třeba se učit
přednostně, a jednak jsem moc nevěděl, co se vlastně učit, protože jsem
nesehnal staré písemky. Základní zopakování látky samozřejmě proběhlo,
ale nevěděl jsem moc co čekat. Zkouška byla kombinovaná - pár testových
otázek s jednou správnou odpovědí plus asi tři fulltextové na probírané
metody a techniky. Pár věcí jsem věděl, ale taky jsem dost tipoval,
objektivně ale písemka nebyla těžká. Co mě velice překvapilo, bylo A,
které se mi za pár dní objevilo ve wisu - byla to moje první známka na
magisterském a měl jsem z ní velkou radost, navíc když nikdo jiný A
neměl. Myslím, že nebylo úplně náhodou, že mi písemka vyšla přesně na 90
bodů, ale jak už jsem psal, lidi z grafiky jsou hrozně přátelští a pokud
se dá někde najít bodík na lepší známku, určitě vám ho dají {{m.e(':)')}}

Celkově je PGP parádní předmět. Nemá možná stoprocentně zvládnutou
organizaci, ale přednášející jsou přímo nadšení pro své téma, jsou
přátelští a ochotní s čímkoliv pomoct. Písemky a projekty jsou rychle
opravené, hodiny mají příjemnou atmosféru, zajímavá témata, a navíc si
vyzkoušíte pěkný projekt. PGP určitě doporučuju, a to i zájemcům z
negrafických oborů, pokud je grafika trochu zajímá a prošli si PGR.

![projekt](http://i.imgur.com/o20fwVq.png){.center width="640"}

Matematické struktury v informatice (MAT)
-----------------------------------------

{{ m.fit_but_cheatsheet('MAT','1','VQQ2M7c') }}
{{ m.fit_but_cheatsheet('MAT','2','xQSEt97') }}

Při hodnocení studia vždycky přemýšlím, jak bych každý předmět co
nejvýstižněji shrnul pár krátkými větami. K MATu bych řekl asi toto: jde
o zopakování látky z IDA s trochou vaty navíc, předmět nemá dobrou
pověst a z přednášek nikdo nic nechápe. Asi to nezní jako moc pozitivní
začátek, ale je to bohužel tak. Pár pozitiv by se samozřejmě našlo -
např. písemky jsou opravovány velmi rychle. Ale pozitiva jsou bohužel až
příliš zastíněna spoustou nedostatků a pokud vás matematika moc
nezajímá, radši se na MAT pořádně připravte.

Jak jsem psal, přednášky skutečně nejsou to pravé. Má je na starosti
proslulý prof. Šlapal, který je známý tím, že mluví tak rychle, jako
když si pouštíte čtyřikrát zrychlenou přednášku běžného přednášejícího.
Vzhledem k náročnosti učiva je potom přirozeným výsledkem přednáškovka
plná zoufalých, spících, nebo nepřítomných (v jakékoli kombinaci)
studentů. Já osobně jsem se držel prvních pár přednášek, než jsem se
někde u jedné věci ztratil, a dál už jsem se jenom vezl. U každého nově
probíraného tématu to potom bylo podobně, ať jsem se snažil, jak jsem
chtěl. Tato velká témata byla čtyři: logika (výroková a predikátová),
matematické struktury, funkcionální analýza a grafy.

V MATu naštěstí existuje jedna věc, která obyčejně studenty zachraňuje -
demonstrační cvičení s doc. Hrdinou a dr. Pavlíkem. Ta je ovšem nutné si
domluvit a konají se mimo oficiální rozvrh. Většina příkladů, které se
objevují na písemkách, se tady hodně srozumitelně probere.

Půlsemestrálka by se dala shrnout slovem katastrofa. Z organizačních
důvodů jsme dostali na písemku padesát minut, což bylo prostě strašně
málo na čtyři poměrně složité příklady, které bylo potřeba opravdu
dlouho počítat a jeden měl asi desetiřádkové zadání. Asi dvacet minut
jsem hleděl do papírů s tím, že za tohle dostanu stoprocentně 0 bodů.
Nakonec jsem si řekl, že se nevzdám, a začal jsem něco honem honem
počítat a kupodivu jsem vypotil víceméně tři příklady plus část
čtvrtého. Úplným zázrakem jsem za práci potom dostal 14 bodů z 20, ale
většina lidí takové štěstí neměla - nejčastější bodové hodnocení bylo,
myslím, kolem 4 až 5 bodů. Půlsemestrálka je přitom klíčová, protože
jiné body za semestr nezískáte.

Jelikož měla spousta studentů s MATem problém, někdo z ročníku uspořádal
před zkouškou hromadné opakování příkladů v rezervované učebně. Zájem
byl obrovský a cvičení mělo úspěch - příštím ročníkům bych rovněž
doporučil, aby nespoléhaly pouze na školu.

No a dostáváme se ke zkoušce. Když vyučující trochu klopýtne a dá omylem
trochu těžší půlsemestrálku, než chtěl, dá se očekávat, že zkoušku udělá
na oplátku trochu mírnější, že ano? Chyba - alespoň podle pana Šlapala
tohle není přiměřený postup. Obtížnost příkladů byla, myslím si, docela
přiměřená, ale co je to platné, když nemáte na zkoušku dost času. I když
byly vyhrazeny tři hodiny, na psaní jsme měli striktně jenom hodinu a
půl. Při daných příkladech to pro mě znamenalo rychle a bez kontroly
počítat, psát první věc, co mi vyjde, a neohlížet se zpět. Jakmile se
člověk na něčem zasekne, zpanikaří, protože mu běží čas. Po hodině a půl
samozřejmě nikdo nic neměl, studenti opravdu nestíhali a doprošovali se
času navíc, takže jsme "milosrdně" dostali ještě patnáct minut. Nějakým
zázrakem se mi podařilo "nějak" dodělat všechny příklady a odevzdat pár
minut před koncem prodloužení, ale většina lidí to prostě nestihla.
Písemka byla naštěstí opravena asi za čtyři dny, což je jedno z mála
pozitiv MATu. Dostal jsem nakonec 66 bodů z 80 a tedy mi známka vyšla na B.

MAT má bohužel seriózní problémy po pedagogické stránce, a to už dlouhé
roky. Především jde o špatné přednášky, málo času na písemky a výsměch
do očí zoufalých studentů. Já mám naštěstí matematiku rád, a jsem
ochotný jí věnovat extra čas, který na přednáškách ztratím. A od toho se
odvíjí moje rada budoucím generacím, jak předmět zvládnout -
nepropadejte panice, zorganizujte si cvičení, ať už s vyučujícími MATu
nebo jen se spolužáky. Snažte se co nejlíp napsat půlsemestrálku - hodně
vám to pomůže. Tohle budou asi jediné užitečné rady do doby, než se
předmět trochu zlepší.

{{ m.study_semester_summary("Ing.",0,"cs") }}

