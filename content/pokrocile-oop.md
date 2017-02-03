Title: Pokročilé objektově orientované programování
Date: 2012-12-11 17:14
Author: tastyfish
Category: Articles
Tags: source
Lang: cs
Slug: pokrocile-oop
Status: published

V článku o základech OOP jsem se věnoval tomu nejdůležitějšímu, co je
třeba umět k psaní objektového kódu. Nyní se zaměřím na pokročilé
nástroje a techniky, kterými OOP vybrušuje krásu své koncepce a
eliminuje některé své neduhy. Po osvojení těchto věcí získáte především
nový pohled na řešení složitějších problémů a nemělo by pro vás být
těžké osvojit si jakýkoliv konkrétní objektově orientovaný jazyk.

Modifikátory přístupu
---------------------

Na úvod začneme něčím, co by s klidem mohlo být zahrnuto ještě v
základech OOP. Modifikátory přístupu jsou v podstatě klíčová slova
umožňující do velké míry manipulovat se zapouzdřením a říkat
kompilátoru, kdo a kdy má k jakým vlastnostem a metodám daného objektu
přístup. Různé jazyky mají různé modifikátory přístupu, které se mohou
mírně lišit sémantikou. Nejčastěji jsou to však tyto tři:

-   veřejný (public) – K atributu/metodě má přístup každý, kdo má
    přístup k objektu. Tento modifikátor bývá implicitně použit, pokud
    žádný neuvedeme, a z venčí umožní uživateli naší třídy volný přístup
    k danému atributu/metodě. Metody většinou veřejně přístupné mít
    chceme, ale u atributů musíme zvážit, zda jejich zpřístupněním
    příliš neporušíme zapouzdření.
-   soukromý (private) – K atributu/metodě má přístup pouze objekt,
    kterému náleží, a pouze tehdy, pokud je instancí třídy, v níž je
    tento atribut deklarován (tzn. objekty potomků této třídy k
    atributu/metodě přístup nemají, i když jej zdědí). Jde o přísnou
    kontrolu přístupu, jíž se využívá asi nejméně často.
-   chráněný (protected) – K atributu/metodě má přístup pouze objekt,
    kterému náleží. Na rozdíl od soukromého modifikátoru je zde umožněn
    přístup i potomkům dané třídy. Použití tohoto modifikátoru je
    rozumnou volbou pro zachování zapouzdření atributů, případně i
    některých metod (které nemají být součástí rozhraní objektu).

Kromě modifikátorů přístupu se v jazycích typicky setkáme s celou řadou
dalších klíčových slov deklarujících různá pravidla, co s čím lze a
nelze dělat. Např. u tříd máme často možnost uvést, že je ukončená
(final) a nelze od ní dále dědit. Chci říct, že OOP není žádný přísný
standard a záleží na jazyku, jak si jej uzpůsobí. Já se zde snažím
probrat obecné věci, s nimiž se setkáme ve většině jazyků, a
modifikátory přístupu si mezi tyto záležitosti dovolím klasifikovat,
neboť jsou velmi frekventovaně využívané. Při použití konkrétního jazyka
si nejdřív nastudujte, jak přesně v něm modifikátory přístupu fungují!
Nyní uvedu jednoduchý příklad, jak modifikátory používat (můžete si
stáhnout zdrojový kód v C++):

<pre> 
třída Geometrický tvar  
{  
atributy:  
název, chráněný atribut // pro tuto třídu a potomky  
poznámka, veřejný atribut // zvenku lze přistupovat  
id číslo, soukromý atribut // pouze pro tuto třídu

metody:  
změň id(číslo) // bez modifikátoru = veřejná  
zjisti id()  
změň název(nový název)  
zjisti název()  
}

třída Úsečka, potomek třídy Geometrický tvar  
{  
atributy:  
první bod, chráněný atribut // zvenku nelze přistupovat  
druhý bod, chráněný atribut  
metody:  
nastav body(a,b) // bez modifikátoru = veřejná  
vzdálenost bodů(a,b), soukromá metoda // pomocná, soukromá  
délka(), veřejná metoda // využívá metodu vzdálenost bodů  
metoda s chybou()  
}  
// definice metod:  
Geometrický tvar:změň id(číslo)  
{  
id číslo := číslo  
}

Geometrický tvar:zjisti id()  
{  
vrať id číslo  
}

Geometrický tvar:změň název(nový název)  
{  
název := nový název  
}

Geometrický tvar:zjisti název()  
{  
vrať název  
}

Úsečka:nastav body(a,b)  
{  
první bod := a  
druhý bod := b  
}

Úsečka:vzdálenost bodů(a,b)  
{  
vrať odmocnina ((a.x – b.x) \^2 – (a.y – b.y) \^2)  
}

Úsečka:délka()  
{  
vrať vzdálenost bodů(první bod,druhý bod)  
}

Úsečka:metoda s chybou()  
{  
první bod := bod(1,2) // OK  
poznámka := "..." // OK  
název := "..." // OK  
změň id(12345) // OK  
id číslo := 12345 // CHYBA! atribut je soukromý pro G. tvar  
}

// zde se začne vykonávat program

Geometrický tvar tvar  
Úsečka moje úsečka

tvar := nový Geometrický tvar  
úsečka := nový Úsečka  
tvar.změň id(123) // OK  
vypiš(tvar.zjisti id()) // OK  
moje úsečka.nastav body(bod(1,2),bod(5,0)) // OK  
vypiš(moje úsečka.délka()) // OK  
tvar.poznámka := "obecný tvar" // OK  
moje úsečka.poznámka = "nějaká úsečka" // OK  
moje úsečka.změň id(12345) // OK  
vypiš(moje úsečka.zjisti id()) // OK

tvar.id číslo := 456 // CHYBA! přístup k soukromému atributu  
tvar.název := "můj tvar" // CHYBA! přístup k chráněnému atributu  
moje úsečka.první bod := bod (1,2) // CHYBA! chráněný atribut  
vypiš(Úsečka.vzdálenost bodů(bod(1,2),bod(3,4))) // CHYBA!  
moje úsečka.id číslo := 321 // CHYBA! přístup k soukromému atributu  
</pre>

Dodejme, že chyby se neprojeví až za běhu programu, nýbrž vždycky při
překladu. Modifikátory přístupu používáme k tomu, aby potenciálně špatně
napsaný program nešel přeložit, čímž se vyhneme sémantickým chybám,
které, jak víme, jsou nejvíce nežádoucím druhem chyb.

Statické metody a atributy
--------------------------

Doposud jsme pojem třídy chápali čistě jen jako šablonu pro objekty.
Metody a atributy, ač tak možná nebylo přímo řečeno, náležely vždy
objektům - všechny objekty stejné třídy měly stejné atributy co do jména
a datového typu, ale každý měl vždy své vlastní hodnoty těchto atributů.
Obdobně nebylo možné volat metody jenom tak, ale musel se vždy uvést
objekt, nad nímž se volání provádělo.

Takový pohled je správný, avšak nemusí být úplný. Existuje možnost, jak
metody a atributy dát do vlastnictví třídě samotné. Uděláme to označením
dané metody či atributu klíčovým slovem, většinou static. Typickým
příkladem je v mnoha jazycích matematická třída, která má metody jako
např. sinus, kosinus, odmocnina či atributy, mezi něž může patřit např.
konstanta pí.

Kdy použít statické metody a atributy? Zkrátka tehdy, pokud nedává
smysl, aby bylo potřeba vytvářet instanci pro volání metody nebo tehdy,
když má atribut uchovávat nějakou globální informaci pro všechny
objekty. Zkusme si uvést malý příklad:

<pre> 
třída Soubor  
{  
atributy:  
cesta  
je otevřen  
počet otevřených := 0, statický atribut // náleží třídě  
metody:  
otevři(cesta)  
zavři()  
vypiš počet otevřených(), statická metoda // patří třídě  
}

Soubor:vypiš počet otevřených()  
{  
vypiš("otevřených souborů: " + počet otevřených)  
}

Soubor:otevři(cesta)  
{  
počet otevřených := počet otevřených + 1  
\\\\ nějaký kód k otevření souboru  
}

Soubor:zavři()  
{  
\\\\ nějaký kód k zavření souboru  
počet otevřených := počet otevřených - 1  
}  
// zde se začne vykonávat program  
Soubor můj soubor // odkaz na objekt typu Soubor

Soubor.vypiš počet otevřených() // voláme metodu třídy  
můj soubor := nový Soubor() // vytvoříme nový objekt  
vypiš("otevírám soubor...")  
můj soubor.otevři("soubor.txt") // voláme metodu objektu  
Soubor.vypiš počet otevřených()  
vypiš("zavírám soubor...")  
můj soubor.zavři()  
Soubor.vypiš počet otevřených()  
</pre>

Vidíme, že statické metody se volají pomocí jména třídy a nikoliv
objektu, jak by mělo být zřejmé. V příkladu máme jednu statickou
proměnnou uchovávající informaci o počtu celkově otevřených souborů a
jednu metodu, která vypisuje hodnotu tohoto atributu. Výstup programu
bude následující:

<pre> 
otevřených souborů: 0  
otevírám soubor...  
otevřených souborů: 1  
zavírám soubor...  
otevřených souborů: 0  
</pre>

Výjimky
-------

Mechanismus výjimek (exceptions) je nástrojem k efektivnějšímu
ošetřování chybových stavů. Tento mechanismus sice není při programování
nezbytný a nemusí se nutně vyskytovat spolu s OOP, ale je to velmi
osvědčený a rozšířený mechanismus, který se s OOP velmi dobře kombinuje.
Není proto divu, že jej podporuje drtivá většina významnějších objektově
orientovaných jazyků.

Výjimkou rozumíme stav způsobující chybu při běhu aplikace, neboli stav,
který by za správných okolností neměl nastat (tzn. jeho výskyt je
výjimkou). Jako takovou situaci si představme třeba dělení nulou,
přístup za hranici pole, neplatný vstup, převod řetězce "abc" na číslo
apod. Výjimku tedy způsobí nějaký konkrétní příkaz a když k ní dojde, je
spuštěn mechanismus zpracování výjimky, který si popíšeme dále. Pojďme
se podívat, jak bychom ošetřili např. potenciální chybu dělení nulou
klasickým způsobem bez výjimek:

<pre>  
načti x ze vstupu  
načti y ze vstupu

pokud y != 0  
{  
z = x / y // spousta kódu okolo  
}  
jinak  
{  
vypiš ("chyba: neumím dělit nulou.")  
ukonči program  
}

vypiš(z)  
</pre>

Tento způsob není špatný, ale jeho nevýhodou je kód navíc okolo příkazu
dělení a prolínání kódu výkonného algoritmu s kódem ošetřujícím chyby.
Jistě si dokážete představit, že ve složitějším kódu může tento přístup
vést k nepřehlednosti.

Nyní se podívejme, jak stejnou situaci ošetříme pomocí mechanismu
výjimek. Nejdříve vytvoříme tzv. zkušební blok (často se nazývá try) a
do něj zapíšeme čistý algoritmus bez ohledu na možné chybové stavy. Za
tímto blokem následují bloky zachytávající výjimky (v praxi nazývané
catch). Nakonec můžeme a nemusíme uvést ještě speciální blok, který se
provede vždy nakonec, ať už k nějaké výjimce došlo nebo ne (tzv. finally
blok). V našem případě máme jeden odchytávací blok. V případě dělení
nulou se přeruší vykonávání algoritmu na daném příkazu ve zkušebním
bloku a přesune se do bloku odpovídajícímu vyvolané výjimce. Kód vypadá
následovně:

<pre>  
zkušební blok // zde provedeme výkonný algoritmus  
{  
načti x ze vstupu  
načti y ze vstupu  
z = y / x  
vypiš(z)  
}  
odchyť výjimku (dělení nulou) // zde ošetříme případnou výjimku  
{  
vypiš(„chyba: neumím dělit nulou.“)  
}

// mohly by následovat další odchytávací bloky nebo finally blok  
</pre>

Tento případ je evidentně přehlednější, není proto důvod jej nepoužívat.
Pojďme se ale teď podívat, proč jsou výjimky tak hezky použitelné právě
spolu s OOP.

Odpověď je prozaická – výjimky totiž mohou být objekty. Co je na tomto
faktu tak úžasného? Především to, že existuje spousta druhů výjimek a je
jasné, že každá se ošetřuje potenciálně jiným způsobem – chyba při čtení
souboru se ošetří chybovým hlášením a zavřením souboru, kdežto chyba při
převodu řetězce na číslo se ošetří třeba výzvou k novému zadání řetězce.
Výjimek je ve skutečnosti nekonečně mnoho, protože si dokonce ve svém
programu můžeme dle potřeby vymýšlet výjimky vlastní - např. při psaní
ovladače nějakého hardwarového zařízení si můžeme vymyslet výjimku typu
chyba při připojování zařízení. Výjimky jsou tedy objekty různých tříd a
mohou mít své atributy využitelné při jejich ošetřování (např. čas
výskytu výjimky, místo v paměti, kde k výjimce došlo, slovní popis
apod.). Jazyky často implicitně obsahují obecnou třídu *Výjimka*, od níž
dědí konkrétnější a konkrétnější výjimky. V odchytávacích blocích potom
vždy uvádíme, jakou třídu výjimky odchytáváme a případná výjimka je nám
do odchytávacího bloku předána jako objekt, s nímž můžeme pracovat např.
následovně:

<pre> 
zkušební blok  
{  
soubor := nový Soubor("soubor.txt")  
soubor.vypiš obsah()  
soubor.zavři soubor()  
}  
odchyť výjimku (chyba otvírání souboru: chyba)  
{  
vypiš("chyba při otevírání souboru " + chyba.cesta() + "!")  
}  
</pre>

Pokud je tedy výjimek velmi mnoho, nabízí se otázka, zda musíme vždy
všechny odchytávat. Z hlediska množství kódu je asi jasné, že to po nás
jazyky nevyžadují, ale některé výjimky mohou být speciálně označené tak,
že odchyceny být musí. Tím však vyvstává otázka další a to co se stane,
pokud nastane nějaká výjimka a my ji neodchytíme? Představme si metodu,
v níž provádíme dělení a neodchytáváme výjimku dělení nulou. Pokud tato
výjimka nastane, přeruší se vykonávání metody a jakmile se zjistí, že
neexistuje blok, jenž by ji ošetřil, ukončí se naše metoda a sama
jakožto příkaz volaný odjinud tuto výjimku vyvolá. Takto se předává
zpracování výjimky stále "výš", dokud se pro výjimku nenajde vhodný
ošetřovací blok. Pokud se to nestane nikdy, je zde implicitní funkce
zpracování výjimek, která jako poslední záchrana odchytává obecné
výjimky a ošetří je většinou zprávou uživateli o chybě neošetřené
výjimky (jistě jste se s tím setkali u nějaké ne příliš dobře napsané
Javové aplikace).

Snad je už trochu jasné, jak to celé funguje. Naše metody mohou
vyvolávat výjimky podle toho, jaké výjimky mohou nastat v nich (pokud je
tam neošetříme) a nebo tehdy, pokud výjimku uvnitř metody vyvoláme sami
příkazem daného jazyka (podle konvence většinou nazýván throw). Výjimku
můžeme vyvolat buď již existující a nebo vlastní – stačí nám vytvořit
třídu vlastní výjimky a tu potom vyvolat. Vytváření vlastních výjimek
ale skoro jistě nepoužijete ani ve větších programech, proto zde tuto
možnost zmiňuji jen pro úplnost. Znalost základního principu fungování
výjimek je ale dnes skutečně nezbytná, neboť programátoři chtějí psát
především robustní aplikace a k tomuto účelu jsou výjimky jako dělané.

Vícenásobná dědičnost a rozhraní
--------------------------------

V článku o základech OOP jsem při výkladu dědičnosti explicitně neuvedl,
že třída nemůže bezprostředně dědit od více než jedné třídy, ale záměrně
jsem se snažil, aby to tak vyznělo. Důvod je ten, že takto dědičnost
skutečně v naprosté většině případů chápeme, používáme a mnohdy ani
jazyk dědění od více tříd neumožňuje. Jsou ale jazyky, mezi něž patří
např. C++, které tuto tzv. vícenásobnou dědičnost podporují. Proč nám
autoři jazyka zbytečně komplikují život, když si jiné jazyky vystačí s
dědičností jednoduchou?

Asi už tušíte, že se čas od času vyskytne situace, jež nemá elegantní
řešení, omezíme-li se na jednoduchou dědičnost. Jednu takovou si
samozřejmě uvedeme a ukážeme si její řešení jednak pomocí vícenásobné
dědičnosti a jednak pomocí alternativního způsobu, s nímž přicházejí
jiné jazyky, jako např. Java, a který se nazývá rozhraní (interface).

Zkusme si představit situaci, kdy máme dvě abstraktní třídy - *Živočich*
a *Stroj*. Od třídy *Živočich* odvodíme za pomoci dědičnosti třídy
*Člověk* a *Kočka* a od třídy *Stroj* rovněž odvodíme třídy *Auto* a
*Robot*. Třída *Živočich* může mít různé atributy a metody typické pro
živočicha, řekněme třeba *datum narození* a stroji přiřkneme *výrobní
číslo* (viz obrázek).

![příklad](http://i.imgur.com/QOD0at7.png){.center}  
<pre>
třída Živočich  
{  
atributy:  
datum narození

metody:  
}

třída Stroj  
{  
atributy:  
výrobní číslo

metody:  
}

třída Člověk, potomek třídy Živočich  
{  
atributy:  
metody:  
}

třída Kočka, potomek třídy Živočich  
{  
atributy:  
metody:  
}

třída Robot, potomek třídy Živočich  
{  
atributy:  
metody:  
}

třída Auto, potomek třídy Živočich  
{  
atributy:  
metody:  
}  
</pre>

Všechno je zatím evidentně v pořádku, kočky a lidé budou mít svá data
narození a auta a roboti výrobní čísla. Nyní nás ale může napadnout
přidat např. metodu *mluv*, již budou zcela logicky implementovat pouze
třídy představující entity, které jsou schopny mluvit, a to napříč všemi
třídami, nezávisle na vztazích dědičnosti. Chceme, aby schopnost mluvit
měl člověk a robot, ale ne kočka a auto. Chceme tedy vytvořit metodu
společnou dvěma třídám, které jinak nemají společného nic. Kde ale
takovou metodu máme deklarovat? Nemůžeme to udělat ve třídě *Živočich*
ani ve třídě *Stroj*, jinak by ji zdědila třída *Kočka* a *Auto* a ty
mají zůstat nemluvné. Stejně tak není možné metodu *mluv* definovat ve
třídě *Člověk* a *Robot* zvlášť, protože bychom se jednak dopouštěli
zatraceníhodné redundance a jednak by šlo o dvě různé metody (což je
velmi podstatné, jak se ukáže dále).

V tuto chvíli zkušený programátor vytáhne zbraň zvanou vícenásobná
dědičnost a vytvoří novou třídu *Mluvící*, která bude představovat
entity světa schopné mluvit. Této třídě přiřkne metodu *mluv* a třídám
*Člověk* a *Robot* přikáže dědit vedle svých rodičovských tříd ještě
navíc od třídy *Mluvící*, čímž právě tyto třídy zdědí požadovanou metodu
(viz obrázek). Rázem vidíme, jak elegantní naše řešení je.

![příklad](http://i.imgur.com/EGsk1He.png){.center}  
<pre>  
třída Živočich  
{  
atributy:  
datum narození

metody:  
}

třída Stroj  
{  
atributy:  
výrobní číslo

metody:  
}

třída Mluvící  
{  
atributy:  
metody:  
mluv  
}

třída Člověk, potomek třídy Živočich a Mluvící  
{  
atributy:  
metody:  
}

třída Kočka, potomek třídy Živočich  
{  
atributy:  
metody:  
}

třída Robot, potomek třídy Živočich a Mluvící  
{  
atributy:  
metody:  
}

třída Auto, potomek třídy Živočich  
{  
atributy:  
metody:  
}  
</pre>

Celé to má obrovskou výhodu – představme si nějakou funkci nebo metodu,
která jako parametr požaduje objekt, který umí mluvit, a přitom je jí
úplně jedno všechno ostatní ohledně tohoto objektu. Můžeme si představit
třeba funkci *vypiš rozhovor*, která vezme dva mluvící objekty a donutí
je, aby začaly mluvit. Parametry této funkce budou potom objekty třídy
*Mluvící* a půjde jí tak předat skutečně pouze mluvící objekty.
Kdybychom třídu *Mluvící* neměli, museli bychom složitě kontrolovat,
jaké třídy předané objekty jsou a zda jsou schopny mluvit. Takto máme
jistotu, že nad objekty předanými naší funkci můžeme vždycky zavolat
metodu mluv.

![příklad](http://i.imgur.com/FEgwqqx.png){.right}

Druhou stranou mince jménem vícenásobná dědičnost je však řada problémů
vyplývajících z možných konfliktů. Co když mají obě rodičovské třídy
stejně pojmenovaný atribut ale s rozdílným datovým typem? Který z nich
se má zdědit? Podobný problém se týká metod a nazývá se problém diamantu
(viz obrázek). Tyto konflikty se musí různými způsoby řešit a proto
spousta moderních jazyků, např. Java, přichází s alternativním řešením
jménem rozhraní.

Rozhraní je novým aspektem jazyka a trochu se podobá třídě, avšak nelze
od něj vytvářet instance (objekty). Jak je zřejmé z názvu, je to něco,
co definuje, jak lze s určitými objekty zacházet, konkrétněji jaké
metody objekt s tímto rozhraním zaručeně umí vykonat (kromě svých
vlastních). Při řešení našeho problému bychom tedy vytvořili rozhraní
(syntakticky podobným způsobem jako např. třídu) a uvedli u něj, že se
skládá z jediné metody *mluv*, která nemá žádné parametry a nevrací
žádnou hodnotu, tedy vlastně hlavičku této metody, ne však její definici
- ta součástí rozhraní není. U tříd *Člověk* a *Robot* bychom potom
uvedli, že tzv. implementují rozhraní *Mluvící*, čímž říkáme, že tyto
třídy musí kromě svých vlastních metod implementovat ještě všechny
metody rozhraní, v našem případě tedy jedinou metodu *mluv*. Třída může
bez problémů implementovat neomezený počet rozhraní, musí však vždy
implementovat všechny jejich metody. Tím je zaručené, že nad objekty
můžeme volat metodu mluv a dosahujeme stejné výhody jako u vícenásobné
dědičnosti - jako parametr funkce můžeme místo názvu třídy uvést název
rozhraní a očekávat zde objekt, který toto rozhraní implementuje. Náš
problém řešený pomocí rozhraní vypadá takto:

![příklad](http://i.imgur.com/LT4pJIX.png){.center}

Návrhové vzory
--------------

Po nějakém čase stráveném programováním nevyhnutelně zjistíte, že řešíte
nějaký problém podobný jinému, který jste už v minulosti řešili. Je
zřejmé, že četnost těchto situací bude stále narůstat, až si položíte
otázku, proč nesepsat nějaký seznam častých problémů a jejich
osvědčených řešení? Takový seznam by ušetřil spoustu času, práce a vždy
by nabídl elegantní, ověřené řešení. Tématem, o němž zde mluvíme, jsou
právě návrhové vzory (design patterns).

Tento nápad není ničím novým, koneckonců všechna rutinní činnost se řídí
zkušenostmi z minulých prací, ať už jde o stavbu domů, návrh letadel
nebo programování. Návrhový vzor je tedy popsané řešení definovaného
problému, které má navíc své vlastní jméno. Některé z nich jsou skutečně
jednoduché a možná je používáte, aniž o tom víte. Pokud nyní obohatíte
své povědomí o znalost základních návrhových vzorů, můžete při
prezentaci řešení svého problému stejně znalému programátorovi namísto
zdlouhavého vysvětlování prostě říct: "použil jsem návrhový vzor XYZ" a
ušetřit si spoustu času.

Uvedeme si jeden velmi jednoduchý návrhový vzor jako příklad. Nazývá se
Singleton a používá se tehdy, když chceme zajistit, aby od určité třídy
bylo možné vytvořit pouze jedinou instanci. To můžeme požadovat např.
tehdy, pokud objekt uchovává nějaké globální informace (např. statistiky
hráče ve hře) nebo pokud má využívat nějaký výlučný zdroj, u nějž by
vícenásobný přístup způsobil chybu. Našeho cíle dosáhnete tak, že
konstruktor třídy označíme jako soukromý, takže jej uživatel naší třídy
nebude moci volat k vytváření instancí této třídy, a místo něj mu dáme k
dispozici statickou metodu pro vytvoření jediné instance třídy. Ta
funguje tak, že při prvním zavolání zavolá konstruktor, čímž vytvoří
instanci sebe sama, tuto instanci vrátí a poznačí si do statické
proměnné, že objekt byl již vytvořen. Při každém dalším volání podle
této proměnné pozná, že už nemá vytvářet další instance, a vrací už
pouze prázdnou hodnotu.

Probrat více návrhových vzorů by bylo na samostatný článek a proto bych
toto téma prozatím uzavřel – pokud nepracujete na obřím projektu, pak
postačí znalost faktu, že návrhové vzory existují a pro zvídavé jsou
informace všude kolem, stačí jen hledat.

Nakonec trocha klasifikace
--------------------------

Nyní známe dostatek pojmů, abychom si mohli v objektových jazycích
udělat určitou logickou strukturu, neboť jak jsem už zmínil, neexistuje
jedno jediné "pravé" OOP, ale celá řada různých jazyků se svými
unikátními přístupy. Každý přístup se pochopitelně hodí na něco jiného –
někdy preferujeme rychlost psaní kódu, jindy přehlednost a dobrou
schopnost předcházet chybám. Následuje tedy základní klasifikace podle
různých kritérií, abychom se v objektových jazycích lépe vyznali a mohli
zvolit ten pravý pro náš projekt.

-   dle striktnosti dodržování objektového konceptu
    -   čistě objektové - V těchto jazycích je všechno objektem – čísla,
        řetězce, soubory, atd. Neexistuje zde sekvence výkonných
        instrukcí, která by nebyla součástí nějaké metody - tělo
        hlavního programu musí být také zapsáno jako metoda
        nějaké třídy. Neexistují funkce samy o sobě. Sem patří např.
        jazyk Java.
    -   hybridní – Použití objektů není povinné a dá se kombinovat s
        běžným imperativním kódem. Patří sem např. jazyky Python nebo
        známé C++, které se vyvinulo z jazyka C a vylepšilo jej o
        objekty, proto můžeme dál psát klasické funkce a objekty použít
        dle uvážení. Jednoduché datové typy jako čísla nebo znaky
        nejsou objekty.
-   dle orientace na třídy nebo prototypy
    -   třídní – Jazyky, které vytvářejí objekty jako instance tříd –
        těmi jsme se zabývali my. Při běžném programování jsou
        používané nejčastěji.
    -   beztřídní (prototypově orientované) – Většinou skriptovací,
        dynamicky typované jazyky, které neznají pojem třídy a vytvářejí
        objekty buď "odnikud" nebo klonováním již existujících
        objektů (tzv. prototypů, odtud prototypově orientované).
        Klonovaný objekt je přesnou kopií prototypu se všemi jeho
        atributy a jejich hodnotami. Klony si navíc uchovávají odkaz na
        svůj prototyp a pokud nad nimi zavoláme nějakou metodu, kterou
        neznají, provedou tzv. delegování, tzn. zkusí tuto metodu nalézt
        u svého prototypu. Mezi tyto jazyky patří např. JavaSrcipt.

A konečně ještě uvedu alespoň krátký výčet oblíbených objektově
orientovaných jazyků:

-   C++ - Objektová varianta velmi oblíbeného jazyka C, jde o hybridní,
    třídní jazyk s vícenásobnou dědičností. Jelikož je kompilovaný,
    programy v něm napsané běží velmi rychle, proto dominuje např. v
    oblasti her.
-   Java - Velmi oblíbený moderní jazyk. Je třídní a čistě objektový.
    Kompiluje se do tzv. bajtkódu, který se následně dá spustit na
    libovolné platformě s Javovým virtuálním strojem. Jazyk je velmi
    přehledný, má kvalitní dokumentaci a nativní podporu pro spoustu
    pokročilých věcí, jako je grafické uživatelské rozhraní nebo
    síťové programování. Nevýhodou je pomalý start aplikací kvůli
    optimalizacím před spuštěním.
-   JavaScript - Beztřídní, hybridní, skriptovací jazyk pro
    internetové prohlížeče. Hodí se na programování doplňků webových
    stránek spíš než pro větší aplikace. Program běží na straně klienta
    a proto nezatěžuje webový server. Aplikace se píší velmi rychle, na
    druhou stranu se hůře zbavují chyb a, jak to tak bývá s
    internetovými prohlížeči, co běží v jednom, nemusí běžet v jiném.
-   Python – Oblíbený třídní, hybridní, skriptovací jazyk. Hodí se jak
    pro malé skripty tak i pro větší projekty. Nevýhodu a zároveň výhodu
    vidím v tom, že každá nová verze jazyka obecně nezachovává zpětnou
    kompatibilitu s verzí předchozí – důvodem je snaha o vybrušování
    jazyka tak, aby programy v něm byly co nejkratší a dobře čitelné.
-   Perl – Skriptovací jazyk vhodný pro psaní systémových skriptů. Umí
    dobře pracovat s textem např. pomocí regulárních výrazů.
-   Object Pascal – Objektová varianta jazyka Pascal. Jde o třídní,
    hybridní, kompilovaný jazyk, který je využívám v komplexním
    vývojovém prostředí Delphi. Programy v něm napsané jsou rychlé,
    jednodušší než v C++ a začátečníkům učícím se Pascal se na něj
    dobře přechází.
-   C\# - Jazyk vyvinutý firmou Microsoft pro platformu .NET. Je
    hybridní, třídně orientovaný a kompilovaný. Důraz se klade na
    robustnost a programátorskou produktivitu.
-   PHP – Skriptovací, hybridní, třídní jazyk určený k programování
    webových serverů, kde si vydobyl své místo na vrcholu oblíbenosti.
    Umožňuje programování jednoduchých skriptů i složitých informačních
    systémů či her. Nevýhodou oproti konkurenci může být někdy dlouhý a
    méně čitelný kód.
-   Lua – Jednodušší skriptovací, hybridní, beztřídní jazyk masivně
    využívaný pro skriptování her (např. World of Warcraft).
-   ...

Závěrem
-------

Mimo to, abych tímto článkem shrnul pokročilé aspekty OOP, jsem se také
snažil poukázat na fakt, že různé jazyky se mohou se stejnými problémy
vypořádávat rozdílnými způsoby – typickým příkladem je vícenásobná
dědičnost v C++ oproti mechanismu rozhraní v Javě. Rád bych poukázal na
to, že ač zde probrané věci pro OOP obecně platí a hojně se využívají,
můžete se místy setkat s odlišnostmi v syntaxi i sémantice a proto jsem
se zde neomezil na žádný konkrétní jazyk, čistě pro účel obecnosti. Byl
bych rád, kdyby si čtenář odnesl znalost principů, které mu usnadní
učení konkrétního objektově orientovaného jazyka.
