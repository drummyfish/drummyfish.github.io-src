Title: Google Earth 3D buildings - how to
Date: 2012-05-03 17:36
Author: tastyfish
Category: Articles
Tags: 3d, graphics
Slug: google-earth-3d-buildings-how-to
Status: published

\[:cs\]

Virtuání glóbus [Google
Earth](http://www.google.com/intl/cs/earth/index.html) jistě netřeba
nikomu představovat, ale pro jistotu: tato zajímavá, volně dostupná
aplikace umožňuje prohlížet si zemský povrch v neuvěřitelných detailech
a to díky satelitním snímkům a trojrozměrnému terénu. Některá větší
města jako např. New York nebo Londýn nabízí dokonce trojrozměrné modely
budov, takže se mezi nimi může člověk krásně prolétávat. Zajímavé je, že
k těmto velkým 3D velkoměstům se může s trochou snahy přidat třeba i
vaše vesnice :) Pokud vás zajímá jak, čtěte dál. Na tvorbu 3D budovy
budeme potřebovat:

-   vhodné a dostatečně kvalitní fotografie budovy
-   software na úpravu 2D grafiky (na tvorbu textur z fotek, např.
    bitmapový editor Photoshop nebo varianta zdarma
    [Gimp](http://www.gimp.cz/ke-stazeni/))
-   software na tvorbu 3D modelu (co umí vytvářet soubory ve formátu
    *3ds*, např. 3DS Max)
-   program [Goole Sketchup](http://sketchup.google.com/) (pro samotné
    umístení modelu na Zeměkouli)
-   internetové připojení a trochu praxe s výše uvedenými programy (o
    editaci 2D a 3D grafiky se zde z pochopitelných důvodů nemůžu do
    detailů rozepisovat)

Ještě jedna poznámka: k tvorbě budov lze použít jednoduchý a trochu
omezenější webový nástroj [Building
Maker](http://sketchup.google.com/3dwh/buildingmaker.html), k němuž snad
ani není potřeba žádný tutoriál. Tento nástroj ale nemusí mít ve vaší
lokaci dostupné letecké snímky nezbytné pro tvorbu modelu a tak se tento
článek zaměřuje na vytváření modelu zcela na vlastní pěst a bude
fungovat na kterémkoli místě na Zemi.

Krok 1: pořizování fotografií budovy
------------------------------------

![fotky
domu](http://i.imgur.com/nH5Zy.png "pár fotografií budovy"){.right}

Ze všeho nejdřív je nutné pořídit dostatečně kvalitní fotografie
zvoleného objektu. Máme k tomu dva důvody. Za prvé: z fotek se vytváří
textury, kterými se "potáhne" trojrozměrný model, takže bude hezky
barevný a realistický. Za druhé: fotografie nám poskytnou cenné
informace o tvaru a proporcích budovy při vytváření modelu. K těmto
věcem musíme při pořizování fotek přihlížet.

Vždycky je lepší nafotit víc materiálu než míň. Budovu tedy foťte ze
všech stran, pokud možno kolmo na každou stěnu (třeba i víckrát). Pokud
před stěnou zavazí např. lampa, strom apod., vyfoťte ji i z jiného úhlu
tak, aby bylo vidět, co za překážkou je. Důležité také je, aby na
fotkách bylo zachyceno co nejvíc informací, tzn. každý skrytý kout
(nezdá se to, ale neustále vyjíždět zpátky do terénu kvůli maličkostem
je přinejmenším pěkná otrava). Problém bývá (překvapivě) s focením
střechy shora, v takovém případě můžou posloužit satelitní snímky přímo
z aplikace Google Earth, byť nejsou tak kvalitní, jak bychom si přáli -
nicméně dají se slušně vylepšit ve Photoshopu, v nejhorším případě
poslouží i textury nalezené na internetu (prostě vyhledáte na Googlu
obrázky podobné budovy, ale vždy až jako poslední možnost).

Krok 2: tvorba textury
----------------------

![textura](http://i.imgur.com/gVQVQ.png "textura"){.right}  
![model
domu](http://i.imgur.com/KVQio.png "model domu bez textury a s texturou"){.right}

Tvorba textur může následovat klidně až po tvorbě modelu, já ale
preferuju mít fotky už předem zpracované a zároveň si při tvorbě textur
ujasníme, jak bude model zhruba vypadat. Jak už bylo řečeno, textura je
obrázek vytvořený z fotek, který se nanese na trojrozměrný model domu
(jinak bychom měli pouze jakousi bílou krabici). Jak by tedy měla
správná textura vypadat?

Všechny části (tzn. obrázky stěn, střechy atd.) by měly být naskládány
vedle sebe tak, aby měl celý obrázek co nejmenší plochu (výrazně se tak
zmenší velikost textury). Textura by taky měla mít přiměřené rozlišení -
obrázek dveří rozhodně nebude mít několik megapixelů tak, jako na
pořízené fotografii, proto ji vhodně zmenšíme. Velmi důležitou roli
hraje odstín a jas, které by měly mít všechny stěny stejné a vůbec
sladění veškerých částí musí být takové, aby na sebe co nejlépe
navazovaly, jinak bude model působit dojmem krabičky poslepované z
náhodně povystřihovaných fotek.

Texturu vytvoříme ve vhodném bitmapovém editoru, který umí zmenšovat
části obrázku, měnit jas, kontrast, odstíny barev, prolínat části
obrázku atd., ideální je samozřejmě známý editor Photoshop, popř.
varianta zdarma - Gimp. Pokud jste neměli tu čest setkat se s nějakým
podobným programem, bohužel vás teď zklamu, ale nemůžu se zde
rozepisovat o tom, jak editovat 2D grafiku. Avšak nezoufejte, na
internetu je spousta tutoriálů a návodů, které vás to jistě slušně
naučí. Výsledný soubor textury uložte nejlépe ve formátu *png* a
pojmenujte jej jedním slovem malými písmeny bez speciálních znaků (jinak
se můžete později setkat s problémy).

Krok 3: tvorba modelu
---------------------

![model v 3DS
Maxu](http://i.imgur.com/8jwOI.png "model v 3DS Maxu"){.right}

Model vytvoříme ve 3D editoru - opět musím zklamat čtenáře neznalé práce
v tomto oboru, ale toto téma je opravdu obrovsky rozsáhlé a vydalo by na
několik článků. Já jsem se modelovat naučil z knížky *3ds Max - Výukový
průvodce tvorbou postav, vozidel, budov a prostředí* (autor Andrew
Gahan) a můžu ji vřele doporučit - jednoduchý model zvládnete vytvořit
už po přečtení prvních pár kapitol.

Model budovy dá v mnoha případech největší práci. Pokud je váš dům ale
spíše "krabicovitého" typu, určitě se přiliš nenadřete. Ono vůbec s
modely pro Google Earth by se to nemělo příliš přehánět co do míry
detailů. Spousty detailů se dá efektivně dosáhnout např. pomocí
průhledných textur. Rozhodně nemodelujte např. zábradlí nebo každý malý
schodek trojrozměrně - pamatujte, že na modely se většinou dívá z dálky
a množství polygonů rapidně zvyšuje "sekání" aplikace na pomalejších
počítačích, proto buďme trochu ohleduplní :) Taky nezapomeňte, že
modelujeme pouze statickou budovu a nikoliv stromy, lidi a podobné věci.
Pro jistotu si přečtěte [zásady tvorby modelů přímo od
Googlu](http://sketchup.google.com/intl/cs/3dwh/acceptance_criteria.html).

Cílem je dostat model ve formátu *3ds* (v 3DS Maxu tento formát
dostanete volbou *File* -&gt; *Export*, běžným *File* -&gt; *Save* to
nelze!). Ještě jednou upozorňuji, abyste si dali pozor na jméno souboru
textury, které může být příčinou jejího nenačtení v pozdější fázi.

Krok 4: umístění modelu
-----------------------

![vyhledání lokace
budovy](http://i.imgur.com/2pzVn.png "vyhledání lokace budovy"){.right}  
![umístění
modelu](http://i.imgur.com/0YH5u.png "umístění modelu v Google SketchUp"){.right}

Zde budeme potřebovat aplikaci Google SketchUp, kterou lze snadno a
bezplatně stáhnout. Nebojte se, nijak zvlášť pracovat s ní nemusíte
umět, jde pouze o umístění modelu na Zeměkouli, natočení a změnu
měřítka. Ze všeho nejdřív tlačítkem *Add Location* vyberte místo, kde má
být model umístěn. Vámi vybraný náhled zvolené lokace se promítne do
editačního okna, kde na něj za chvíli umístíte model. Nyní volbou *File*
-&gt; *Import* nahrajte váš *3ds* model. Nejspíš bude hodně malý/velký a
špatně natočený, proto jej musíte upravit tak, aby seděl co možná
nejpřesněji na svém místě - použijte k tomu nástroje *Move* (přesun),
*Rotate* (otáčení) a *Scale* (změna měřítka). Chce to trochu cviku, ale
věřím, že to nakonec zvládnete. Tlačítkem *Prewiev Model in Google
Earth* si můžete prohlédnout vaši budovu přímo v aplikaci Google Earth
tak, jak bude vypadat ve výsledku. Jakmile budete s umístěním spokojeni,
zbývá už jen poslední věc.

Krok 5: zaslání modelu Googlu
-----------------------------

![výsledek v Google
Earth](http://i.imgur.com/IcXBc.png "výsledek v Google Earth"){.right}

V této fázi máme veškerou kreativní činnost za sebou a zbývá nám jen
poslední krok. Námi vytvořený a umístěný model musíme zaslat Googlu, kde
model ověří a případně zařadí do vrstvy 3D budov (takže se bude
zobrazovat v aplikaci Google Earth). Ověření většinou Googlu trvá zhruba
měsíc a informace o schválení modelu vám přijde e-mailem. Takže jak
model Googlu odeslat?

Ze všeho nejdřív si musíte zaregistrovat účet na stránkách [Google
Warehouse](https://www.google.com/accounts/ServiceLogin?service=warehouse&passive=1209600&continue=http://sketchup.google.com/3dwarehouse/?hl%3Den&followup=http://sketchup.google.com/3dwarehouse/?hl%3Den)
(jde o Googlovskou databázi volně dostupných 3D modelů, kde se mj.
shromažďují i modely do Google Earth). Jakmile budete hotovi, existují
dvě možnosti jak váš model do databáze nahrát. Tou první je přímo přes
aplikaci Google SketchUp volbou *File* -&gt; *3D Warehouse* -&gt;
*Share* (musíte mít samozřejmě otevřený model vaší budovy). Ve formuláři
následně vyplníte informace o budově (komentář, adresu, fotku, ...) a
potrvrdíte odeslání k inspekci (nezapomeňte zaškrtnout volbu *Google
Earth Ready*, jinak se váš model k prověření vůbec nedostane!). Druhou
možností, kterou často využívám (jelikož se u té první občas vyskytují
technické problémy), je nahrání modelu přes webové rozhraní (tlačítko
*upload* na stránkách Google Warehouse). Postup je podobný jako u první
možnosti, jenom musíte svůj model vyexportovat z aplikace Google
SketchUp volbou *File* -&gt; *Export* -&gt; *3D Model* do formátu *kmz*,
který nahrajete přes prohlížeč na server Googlu.

Nyní zbývá už jen čekat na e-mail s gratulacemi a oznámením o schválení
vámi vytvořeného modelu a chlubit se svým známým s krásným mini-modelem
třeba vašeho obydlí :)

\[:\]
