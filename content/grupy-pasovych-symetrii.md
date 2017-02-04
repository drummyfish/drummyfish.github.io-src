Title: Grupy pásových symetrií
Date: 2016-08-29 14:16
Author: tastyfish
Category: Articles
Tags: graphics, math
Lang: cs
Status: published

Ve [výtvarné informatice](http://tastyfish.cz/?p=307&lang=cs)
jsme kdysi letmo probírali [grupy symetrií v
rovině](https://en.wikipedia.org/wiki/List_of_planar_symmetry_groups) -
zajímavé učivo, ale v té rychlosti jsem pobral jenom to, že se dají
symetrické mozaikové vzory nějak popisovat pomocí grup. Jak ale tyto
grupy vypadají, co představují jejich prvky a co reprezentuje jejich
operace, to jsem nevěděl. Chtěl jsem se to někdy doučit, a to někdy
nastalo teď. V tomto článku proberu jednoduchou formu dláždění, z níž se
dá snadno pochopit princip složitějších dláždění.

Předpokládám, že čtenář zná pojem
[grupy](https://en.wikipedia.org/wiki/Group_(mathematics)). Jenom pro
zopakování: grupa je matematická struktura (konkrétně algebra), která se
skládá z množiny nějakých prvků a má jednu operaci, kterou zde budeme
označovat prostě +. Aby se jednalo o grupu, musí tato struktura splňovat
určité podmínky: uzavřenost (operace + nám nikdy nedá prvek, který není
v grupě), asociativitu (nepotřebujeme závorky), musí v ní existovat
neutrální prvek a ke každému prvku musí existovat tzv. inverzní prvek.
Grupy jsou v matematice dobře prozkoumané, známe o nich spoustu fakt a
můžeme je použít k popisu různých symetrických věcí z reálného života,
např. Rubikovy kostky.

Budeme se zaobírat tzv. pásovým dlážděním (line groups, frieze groups).
U tohoto dláždění máme 2D vzor, který se ale opakuje jen v horizontálním
směru, např. takto:

![real life](http://tastyfish.cz/wp-content/uploads/2016/08/real-life.jpg){.alignnone .size-full .wp-image-779 width="640" height="208"}

Intuitivně vidíme, že tento vzor v sobě má něco symetrického. Naším
úkolem je nyní toto intuitivní tušení vyjádřit matematicky. Abychom to
však mohli udělat, musíme nejdřív, jako všechno v matematice, pojem
symetrie přesně definovat.

Vezměme si příklad z reálného života - když řekneme, že tvář modelky je
symetrická, máme vlastně na mysli následující: Kdybychom její tvář
zrcadlově překlopili, vypadala by pořád stejně. Právě tato "odolnost"
tváře vůči operaci zrcadlení je to, co nazýváme symetrií. Podle použité
operace můžeme mít symetrií spoustu, např. čtverec je symetrický vůči
otočení o 90 stupňů, neboť po této transformaci zůstává pořád stejný.
Definujme si tedy symetrii.

**Symetrie** vzoru vzhledem k nějaké transformaci je vlastnost vzoru
zůstat stejným po provedení této transformace.

Při hledání symetrií pásu nás budou tedy zajímat prostorové
transformace, po jejichž provedení se vzor pásu nezmění. Potenciálně
mezi tyto operace může patřit (předpokládejme, že pás je nekonečně
dlouhý na obě strany a nezajímá nás, jak se mění jeho "konce"):

-   P - posunutí vzoru o určitou délku.
-   H - horizontální překlopení (překlopení podle vertikální osy).
-   V - vertikální překlopení (překlopení podle horizontální osy).

Existují další transformace, které jsou však buď složením našich
základních transformací (např. otočení o 180° = horizontální +
vertikální překlopení) nebo je nebereme jako základní geometrické
operace (např. nakreslení tučňáka na vzor, nebo co já vím :)). Proto
nechť nás zajímají jen výše uvedené tři základní transformace: P, V a H.

Teď už se tedy konečně pojďme podívat na to, jak to s těmi pásovými
symetriemi je. Pásových vzorů existuje samozřejmě nekonečně mnoho -
každá šikovná babička vám dokáže uplést nespočet šál, každou s jiným
motivem, s jinými barvami apod. Nezapomeňme ale, že nás nezajímají přímo
vzory, ale symetrie, tedy jakési typy vzorů. A těch je, jak bylo
dokázáno, pro pásové vzory pouze 7. Jsou následující:

  číslo  |symetrie        |příklad                                                                                                              |odborná označení
  -------|----------------|---------------------------------------------------------------------------------------------------------------------|------------------
  1      |P               |![](http://upload.wikimedia.org/wikipedia/commons/1/10/Frieze_example_p1.png)                                        |p1
  2      |P, P+V          |![](http://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Frieze_example_p11g.png/150px-Frieze_example_p11g.png)  |p11g
  3      |P, H            |![](http://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Frieze_example_p1m1.png/150px-Frieze_example_p1m1.png)  |p1m1
  4      |P, V+H          |![](http://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Frieze_example_p2.png/150px-Frieze_example_p2.png)      |p2
  5      |P, H, V+H, P+V  |![](http://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Frieze_example_p2mg.png/150px-Frieze_example_p2mg.png)  |p2mg
  6      |P, V            |![](http://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Frieze_example_p11m.png/150px-Frieze_example_p11m.png)  |p11m
  7      |P, V, H         |![](http://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Frieze_example_p2mm.png/150px-Frieze_example_p2mm.png)  |p2mm

Takže např. symetrie č. 2 má dvě symetrie (vůči posunu a vůči posunu
plus vertikálnímu překlopení, což se také nazývá gliding reflection):

![animaion](http://tastyfish.cz/wp-content/uploads/2016/08/animaion.gif)

Zkuste si ověřit, že všechny zbývající vzorové příklady vykazují uvedené
symetrie (a popřípadě napište, že jsem udělal chybu :D).

Co mají ale s tímhle vším společného grupy? Vezmeme-li totiž naše
základní transformace (P,V,H) jako množinu a skládání transformací (tj.
+) jako operaci, dostaneme grupu pro každou ze sedmi uvedených symetrií.
Můžeme si např. nakreslit graf prvků grupy symetrie č.1:

![g1](http://tastyfish.cz/wp-content/uploads/2016/08/g1.png)

Vidíme, že platí všechno, co v grupě platit má - máme zde neutrální
prvek (P), který když složíme (pomocí +) s jakýmkoliv prvkem, dostaneme
vždy ten samý prvek. Každý prvek má svůj opačný prvek, tedy prvek, který
když s ním složíme, dostaneme neutrální prvek (P) - v tomto případě je
každý prvek zároveň svým inverzním prvkem. Můžete si ověřit zbytek
požadavků pro grupu (a také např. zjistit, zda jde o abelovskou grupu).

Grupy ostatních symetrií budou vypadat podobně, ale budou se vždycky
něčím lišit - např. počtem prvků, výsledky operace skládání (tedy
šipkami v grafu) apod. Zkuste si některé grafy nakreslit. Důležité je,
že za daných podmínek (při pásové symetrii a při povolených
transformacích P, V a H) existuje přesně 7 grup symetrií, ačkoliv
samotných dláždění existuje nekonečně mnoho.

Toto je tedy popis pásových symetrií pomocí grup. Obdobně se dají popsat
obecnější dláždění, např. rovinná, která vidíme třeba na stěnách
koupelen, na kobercích nebo tapetách. Ta mají celkem 17 grup symetrií, k
nimž se snad někdy dostanu v dalším článku. Zajímavá jsou rovněž různá
označování těchto symetrií podle oboru, v jehož kontextu je
zmiňujeme. Pokud vás téma zaujalo, určitě zavítejte na Wikipedii, která
o dláždění nabízí spoustu kvalitních článků.
