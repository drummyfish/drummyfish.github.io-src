Title: Základy objektově orientovaného programování
Date: 2012-12-11 17:10
Author: tastyfish
Category: Articles
Lang: cs
Status: published

S objekty se dnes v informatice setkáváme nejen při programování,
ale zcela běžně také při návrhu aplikací, jejich testování, budování
databází a u nespočtu dalších klíčových činností. Zjednodušeně řečeno,
objekty jsou všude kolem nás.

Proč tomu tak je? Protože koncept objektů velmi dobře koresponduje s
povahou našeho světa, který se většinou snažíme s jistou abstrakcí svými
programy zachytit. Řekněme, že programujeme hru s různými postavami a
zbraněmi. Automaticky tyto postavy a zbraně vidíme jako objekty, které
spolu nějak interagují – postavy komunikují, sbírají a používají zbraně
atd. Jiným příkladem může být třeba matematická aplikace, kde budou
našimi objekty rovnice, výrazy a matematické funkce. Pokud program takto
rozdělíme na vzájemně komunikující objekty, jež programujeme nezávisle
na sobě, jsme schopni si v programu udržet lepší logickou strukturu, než
když používáme pouze podprogramy.

Chci se zde pokusit vysvětlit princip objektově orientovaného
programování (dále raději jen OOP), nikoliv prezentovat konkrétní
objektově orientovaný jazyk, místo kterého pro obecnost a jednoduchost
použiju pseudokód, i když ke konci mám ke stažení i zdrojový kód v C++.
Článek píšu pro čtenáře, kteří mají s programováním základní zkušenosti
(zhruba do té míry, že vědí, co je to ukazatel) a chtějí se posunout o
kousek dál k něčemu, co je dnes ve světě informatiky jedním z
nejrozšířenějších přístupů k řešení problémů.

![OOP a okolní svět](http://i.imgur.com/trnFGUQ.png){.center}

Jak tedy OOP funguje?
---------------------

Jak jste jistě vytušili, objektové programování je paradigma - určitá
filozofie, podobně jako např. programování imperativní nebo
funkcionální, napomáhající hlavně lepší logické struktuře programu, jeho
přehlednosti a tedy logicky značné eliminaci chyb ve větších projektech.
Objektové programy se zpravidla dobře navrhují, udržují a rozšiřují, jak
zjistíme dále. Je ale nutné dodat, že OOP není lék na všechno a není
automaticky nejlepším řešením pro každý projekt. Vždy je nutné se
zamyslet - třeba při psaní malých programů může být tento přístup
zbytečně složitý. Nicméně s dobrou znalostí problematiky se většinou
jedná o skutečně mocný nástroj a my se zde pochopitelně zaměříme na jeho
přednosti, jichž je opravdu velké množství.

Pojďme si tedy konečně říct, jak se v praxi liší psaní "normálního" a
objektového programu. Když píšeme program klasickým přístupem hledání
algoritmu v podobě příkazů a rozkladem problému na podproblémy, např. v
jazyce C nebo v Pascalu, zaměřujeme se hlavně na příkazy - snažíme se
nalézt posloupnost instrukcí, které vyřeší daný problém. Při tom si
samozřejmě můžeme pomáhat podprogramy, moduly a dalšími pomůckami. V
centru našeho soustředění však neustále zůstává sekvence příkazů řešící
problém.

Při objektovém přístupu se snažíme nalézt objekty, jakési samostatné
jednotky, které problém vyřeší samy vzájemnou spoluprací. Jakmile
objekty identifikujeme, definujeme je v daném programovacím jazyce,
naprogramujeme jejich chování a necháme je problém vyřešit. Programování
objektů v praxi provádíme samozřejmě opět pomocí příkazů, ty však hrajou
jen jakousi vedlejší roli, představují pomůcku pro popis chování
objektů. Při pohledu na problém jako celek se nyní soustředíme především
na objekty a jejich komunikaci.

Objekty a třídy
---------------

Základní koncept známe, ale abychom byli schopni začít objektově
programovat, musíme se ponořit hlouběji, vysvětlit si pár pojmů a
pochopit systém, kterým se OOP realizuje. Velmi základními pojmy jsou
pro nás nyní objekt a třída.

Objekt, jak už bylo řečeno, je určitá samostatná jednotka, popř. jakási
černá skříňka řešící určitou úlohu. Každý objekt má dva typy komponent:

![objekt](http://i.imgur.com/6OeKFQJ.png){.right .aligncenter}

1.  Data, nazývané atributy nebo vlastnosti. Jde v podstatě o vnitřní
    proměnné objektu určující jeho stav. U objektu typu člověk by to
    mohly být např. proměnné jako *jméno*, *věk* nebo *váha*.
2.  Metody sloužící jako rozhraní pro práci s objektem. Metody popisují
    činnost a chování objektu a jsou to v podstatě funkce (podprogramy)
    patřící objektu. Tyto funkce je možné volat a donutit tak objekt
    k činnosti. Člověk může mít např. metodu *pozři jídlo*, která jako
    parametr přebírá jídlo k pozření a na základě této informace se
    patřičně zvýší hodnota atributu *váha* tohoto člověka.

Objekt by měl být vytvořen podle určitých zásad, aby zachovával výhody
OOP. Jednak by měl mít na starost pouze jeden úkol, podobně jako
podprogram řeší jen jeden podproblém celkového problému. Dále by neměl
poskytovat přímý přístup ke svým atributům, i když to programovací
jazyky téměř vždy umožňují. Důvod, proč atributy skrývat, je ten, že
zkrátka jde programovat bez přístupu k nim a hlavně se tak napomáhá
jednoduchosti rozhraní objektu. Atributy by měly sloužit jen jako
vnitřní paměť objektu a veškerá manipulace s ním by měla být umožněna
jen skrze metody, které tvoří jakousi slupku zakrývající data (viz
obrázek). U objektu člověka by tedy nemělo být možné přímo přistupovat
např. k jeho atributu *váha* a pokud by jej bylo potřeba změnit, měla by
být k dispozici metoda *Změň váhu*.

Dobrou otázkou může být, jak objekty identifikovat. Je zřejmé, že vždy
existuje mnoho možností, jak svět na objekty rozdělit, a je to ve
skutečnosti jedna z nejdůležitějších otázek, které se při velkých
projektech řeší. Odpověď tedy není vždy jednoduchá a záleží na
programátorovi, aplikaci a míře abstrakce, kterou zvolíme. Platí zde víc
než kde jinde dvakrát navrhuj, jednou programuj – je potřeba používat
mozek a nepouštět se bez rozmyslu do bušení kódu.

Nyní se podívejme na další důležitý pojem, jímž je třída. Ta je
jednoduše řečeno šablonou pro objekt. Na základě toho, co známe, si
třídu můžeme představit jako datový typ, přičemž objekty budou svým
způsobem proměnné tohoto datového typu. Třídy vždy definujeme jako první
podobně jako to děláme se složenými datovými typy (např. záznamy).
Popíšeme v nich jména a datové typy atributů a také hlavičky (jméno,
atributy a návratovou hodnotu) metod. Od takto definované třídy můžeme
potom v programu začít vytvářet objekty, tzn. konkrétní výskyty neboli
instance. Pokud bychom uvažovali výše zmíněný příklad, pak bychom
definovali třídu *Člověk* a byli tak schopni vytvářet libovolné množství
objektů této třídy, každý s rozdílnými hodnotami svých atributů *jméno*,
*věk* a *váha*.

![třídy a objekty](http://i.imgur.com/ThpLXzH.png){.right .aligncenter}

Je nutné říct, že existují jazyky, které třídy nepoužívají a pracují
pouze s objekty, jež vytvářejí ne na základě tříd, ale díky tzn.
klonování. Při programování běžných aplikací se však častěji setkáme s
jazyky třídními a proto zde budeme třídy i nadále uvažovat.

Zkusme si nyní cvičně, jak by mohla vypadat deklarace třídy *Člověk* a
vytváření objektů této třídy. Všimněte si speciální metody
*konstruktor*, kterou má vždy automaticky každá třída a která se
automaticky volá při vytváření objektu této třídy. Konstruktory se
jmenují v různých jazycích různě, často bývá jeho název identický s
názvem třídy. Do konstruktoru můžeme napsat kód, kterým chceme objekt
inicializovat. Všimněte si taky, že může mít parametry. Podobně jako
konstruktor existuje i destruktor, který se volá při rušení objektu, ale
ten zde nebudeme zatím pro jednoduchost uvádět (destruktory se používají
např. u složitějších datových struktur, kdy je potřeba při rušení
objektu uvolňovat paměť či jiné zdroje). Při deklaraci atributů nebudeme
uvádět datové typy a předpokládáme, že do ní lze přiřadit "cokoliv" (jak
tomu většinou bývá ve skriptovacích jazycích).

Je důležité si všimnout, jak pracujeme s objekty. Nejdřív deklarujeme
proměnnou, která bude odkazem na objekt, nikoliv objektem samotným. Do
této proměnné poté přiřadíme adresu objektu při jeho vytváření – k tomu
dojde použitím klíčového slova (zde nový), které vytvoří nový objekt,
nad ním zavolá konstruktor a uloží jej do nově alokované paměti. S
objekty poté pracujeme právě pomocí proměnné s uloženým odkazem.

Zapouzdření, dědičnost a polymorfismus
--------------------------------------

Nyní se pomalu dostáváme k pravé síle objektového programování, jíž jsou
možnosti zapouzdření objektů (encapsulation), dědičnosti tříd
(inheritance) a polymorfismu (polymorphism). Uznávám, že se nám množina
pojmů začíná nepříjemně rozrůstat, ale slibuji, že těmito třemi již
pomalu budeme končit. Jedná se skutečně o podstatu OOP, bez níž nemá
cenu se jím zabývat z jiného úhlu, proto si všechny tři pojmy vysvětlíme
hezky popořadě.

Se zapouzdřením jsme se již setkali. Nejde o nic složitého, byť je
význam tohoto principu větší, než se začátečníkům mnohdy zdá.
Zapouzdřený objekt je takový, který se chová jako černá skříňka a
neumožňuje přístup ke svým vnitřnostem, jimiž se myslí jeho soukromé
atributy (popř. i soukromé metody, které může objekt rovněž mít). Jak
jsem již psal, objekt by pro svou manipulaci měl programátorovi
poskytovat pouze rozhraní ve formě metod, které by mělo být co
nejjednodušší a oproštěné od vnitřního fungování objektu. Zapouzdření
velmi napomáhá abstrakci, přehlednosti, umožňuje rozdělovat práci na
projektu mezi více programátorů a považuje se za jeden ze základních
návyků v OOP.

Trochu méně triviálním pojmem je dědičnost, která umožňuje vytvářet nové
třídy na základě již existujících. Nejlépe asi bude demonstrovat
dědičnost na příkladu. Výše jsme se bavili o třídě *Člověk*, od které
jsme schopni vytvářet objekty představující konkrétní lidi. Nyní si
představme, že chceme do svého programu zahrnout navíc třeba ještě psy.
Klidně bychom mohli vytvořit novou třídu *Pes* tak, že bychom
zkopírovali kód pro třídu *Člověk*, umazali bychom vlastnosti a metody,
které u psa nechceme mít, a zároveň bychom nové věci přidali, např.
metodu *sedni*. Jak ale víme, kopírování zdrojového kódu je známka
redundance a především špatného programátora. Psi mají s lidmi spoustu
společného, ale mají zároveň své specifické vlastnosti a chování, proto
by bylo dobré vytvořit třídu *Pes*, která by měla něco společného s
třídou *Člověk* a něco si k ní mohla přidat. Takové situace nastávají
často a OOP pro ně má řešení, jímž je právě možnost dědičnosti tříd. Ta
nám umožňuje, pokud máme vytvořenou nějakou třídu A, vytvořit třídu B,
která zdědí všechny vlastnosti (atributy) a metody třídy A tak, že je
již nemusíme explicitně deklarovat a zároveň můžeme deklarovat nové
atributy a metody pouze pro třídu B. Dědičnost vnáší do tříd hierarchii
a můžeme se proto bavit o třídách, které jsou rodiči a potomky jiných
tříd (rodičovské třídy jsou obecnější, potomci představují konkrétnější
objekty světa).

Zkusme si tedy představit, že vytvoříme třídu se jménem *Živočich*,
která bude mít vlastnost *jméno* a metodu *vydej zvuk*. Tato třída
představuje obecného živočicha, např. člověka nebo psa, přičemž
předpokládáme, že každý živočich má jméno a umí vydávat zvuk. Nyní
můžeme vytvořit třídy *Pes* a *Člověk* a u každé uvedeme jako rodiče
třídu *Živočich*, čímž jsme uvedli dědičnost v praxi. Třídy *Pes* a
*Člověk* mají automaticky vlastnost *jméno* a metodu *vydej zvuk* a
pokud v některé z nich vytvoříme nový atribut či novou metodu, např.
metodu *sedni* u psa nebo atribut *příjmení* u člověka, bude ji mít už
pouze tato třída sama. Ještě dodejme, že třída *Živočich* je typem
třídy, která se označuje jako abstraktní – je to třída, která slouží
pouze k dědění a nelze na jejím základě vytvářet žádné objekty.
Pochopitelně ne vždy musí být rodičovská třída abstraktní, označují se
tak zkrátka třídy, od nichž nemá smysl vytvářet instance.

Nejsložitějším z pojmů je nejspíš polymorfismus neboli tzv.
mnohotvarost. Umožňuje nám řešit další problém, který se v souvislosti s
dědičností může vyskytnout a zároveň při správném využití poskytuje
ohromné programátorské možnosti. Jak je zřejmé, třídy *Člověk* a *Pes*
mají obě metodu *vydej zvuk*, což je naprosto v pořádku, neboť pes i
člověk jistě dokáží nějaké zvuky vyluzovat. Problém je, že pes vydává
jiné zvuky než člověk. Máme tedy implementovat metodu *vydej zvuk* ve
třídě *Živočich* podle toho, jaké zvuky vydává pes nebo člověk? Odpověď
zní, že díky polymorfismu můžeme udělat obojí. Nejdřív musíme označit
metodu *vydej zvuk* ve třídě *Živočich* jako tzv. virtuální. Co to
znamená? Znamená to, že tato metoda bude naprogramována různě pro různé
třídy, i když bude mít stejné jméno. Co metoda ve skutečnosti udělá, se
rozhodne až za běhu programu podle toho, nad kterým objektem bude
volána. Nyní, když je metoda označena jako virtuální, můžeme napsat
jeden kód pro třídu *Pes* (např. vypsání řetězce „haf“) a jeden pro
třídu *Člověk* (např. vypsání „ahoj, já jsem ...“). Polymorfismus má
opravdu velmi široké uplatnění.

Představme si např. jinou situaci, kdy máme pole odkazů (ukazatelů) na
objekty tříd, které jsou potomkem abstraktní třídy *Tvar* představující
obecný geometrický útvar. Tyto objekty tedy můžou být instance třídy
*Kružnice*, *Čtverec*, *Úsečka* apod. Nyní chceme vykreslit objekty v
poli na obrazovku. Nezkušený programátor by nejspíš procházel pole po
každém prvku a podmínkami zjišťoval, jaké je každý objekt třídy, podle
čehož by objekty různým způsobem kreslil (neboť kružnice se bez pochyby
kreslí jinak než čtverec). Mnohem výhodnější je ale deklarovat virtuální
metodu *Vykresli se* třídě *Tvar* a u jejích potomků (*Kružnice*,
*Čtverec*, *Úsečka*, ...) ji poté jen implementovat podle daného
konkrétního tvaru. Potom stačí projít pole a nad každým objektem zavolat
metodu *Vykresli se*. Program za běhu zjistí, kterou implementaci má u
každého objektu použít a vykreslí správné tvary.

Příklad na závěr
----------------

Pochopit OOP jen z teoretického výkladu je skoro nemožné, proto si
zkusíme uvést jeden konkrétní příklad, na němž ukážeme zapouzdření,
dědičnost i polymorfismus. Využijeme v něm naše třídy *Živočich*, *Pes*
a *Člověk*, které trochu upravíme. Zkuste si tedy projít následující kód
a všimněte si, jak se deklarují třídy (velmi podobně jako datový typ
záznam), jak se implementují jejich metody, jak se vytváří objekty
(nejdřív vytvoříme ukazatele, do nichž uložíme adresy dynamicky
vytvořených objektů) a jak se s nimi pracuje (volání metod). Jako bonus
si můžete stáhnout zdrojový kód programu v C++ a rovnou si jej spustit,
abyste viděli, že si nevymýšlím.

Po spuštění nám dá program následující výstup:

A na závěr ještě obrázek, jak náš program vlastně vypadá - obdelníky
představují třídy a kolečka objekty. Rovné čáry naznačují dědičnost,
zaoblené čáry ukazují, od kterých tříd jsou objekty odvozeny a
přerušované čáry vyjadřují vztah "vlastnictví psa".

![obrázek programu](http://i.imgur.com/t3NWNUt.png){.center .aligncenter}

Příklad je snad víceméně jasný. Naučit se OOP důkladně samozřejmě není
triviální věc a vyžaduje určitý čas. Jako vždy platí, nejlépe se
programovat naučíte programováním. Proto si zkuste vybrat vhodný
programovací jazyk, prohlédněte si svět kolem sebe plný objektů a zkuste
jej nějakým způsobem ztvárnit. Uvidíte, že si OOP oblíbíte.
