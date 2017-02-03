Title: Linux - dosavadní zkušenosti
Date: 2015-07-04 14:21
Author: tastyfish
Category: Posts
Lang: cs
Tags: linux
Slug: linux-dosavadni-zkusenosti
Status: published

Podle data předchozího článku používám Linux jako primární
operační systém asi měsíc a půl. Není to příliš dlouho, ale už teď
vidím, že trend mé spokojenosti je stoupající, na rozdíl od Windows, kde
tomu bylo naopak. Nezáleží však jen na operačním systému. Jsou to hlavně
nástroje, které každý den používáme, jenž se podílí na celkovém dojmu z
dané platformy. Při přechodu na jiný operační systém se tedy nejdříve
potýkáme s hledáním nových programů pro každodenní práci. Na Linuxu mě
pátrání po programech baví, protože vím, že si můžu každý zdarma
stáhnout, vyzkoušet a případně odinstalovat, aniž bych se bál
postranních úmyslů softwaru, zaplácání registrů nebo nakažení viry. V
tomto článku uvedu seznam nástrojů, které jsem zatím za ten měsíc a něco
zvolil pro běžné práce, které na počítači provádím. Všechno jsou to
open-source, multiplatformní nástroje.

3D - Blender
------------

Blender se v poslední době stal mým oblíbeným programem a čím více s ním
pracuji, tím ho mám rád víc. 3D grafiku jsem dříve provozoval v 3DS Maxu
a zvykl jsem si s ním poměrně plynule pracovat. Stejně jako u Photoshopu
jsem se ale nakonec nechal zlákat kouzlem open-source softwaru a přešel
jsem na Blender. Přechod to nebyl vůbec jednoduchý, Blender má bohužel
poněkud specifické rozhraní, které se skládá z nepřekrývajících se oken
a připomíná palubní desku letadla. Je navíc naprosto odlišné od rozhraní
3DS Maxu. Učení základů tedy zabere spoustu času, ale jakmile je
zvládnete, je další učení vyložená radost. Dokonce bych řekl, že Blender
je ve většině ohledů lepší než 3DS Max. Nabízí např. různé styly
modelování, včetně 3D sculptingu, což je úžasné. Mám pořád co se učit,
ale s Blenderem je učení radost.

video - Blender
---------------

Ano, Blender je i editor videa. Tady bohužel nevyniká tak, jako v
oblasti 3D modelování, ale jelikož Linux není editací videa příliš
vyhlášený, je to asi nejlepší editor videa, jaký seženete. Dříve jsem
používal Sony Vegas a srovnání s ním by asi nebylo ani příliš fér,
nicméně Blender ke sestříhání dobrého videa i se základními efekty
použít lze. Někdy je jenom nutné vynaložit trochu větší úsilí - pokud
chcete např. v jednom projektu použít více klipů s různými FPS, narazíte
na problémy, je proto nutné klipy před importem konvertovat, což hravě
zvládá ffmpeg. Platí zde navíc to, co pro 3D editaci - není jednoduché
se editaci videa naučit. Pokud chcete např. udělat fade-out zvuku,
musíte použít klíčové snímky na atribut volume, tzn. nenajdete zde žádné
intuitivní posouvátko. Programátoři se ale tohle všechno naučí. Pokud
nejste profesionální stříhač videa, je Blender poměrně dobrý editor,
avšak je nutné mít počítač s velkou RAM - na mém notebooku při velkém
množství klipů bohužel pravidelně padal, až byl naprosto nepoužitelný.
Na PC s 8 GB už šlo všechno krásně.

hudba - LMMS
------------

LMMS je zatím nový program ve verzi 1.0, proto se potýká s absencí
některých důležitých funkcí, avšak nemělo by trvat dlouho, než se
dočkáme jejich doimplementace. Už teď je vidět obrovský potenciál a z
toho, co zatím funguje, jsem nadšený. Program je graficky pěkný,
jednoduchý a mocný zároveň a hlavně, oproti jiným, které jsem zkoušel,
jako např. Rosegarden, funguje bez problémů se zvukem. Z funkcí mi chybí
export do MIDI a nemožnost přehrávat importovaný zvuk z libovolné
pozice. Obě tyto funkce jsou ale plně ve vývoji a budou brzy k
dispozici. Pro nahrávání a základní editaci používám vedle LMMS ještě
Audacity, což je opět úžasný program, ale bohužel nepodporuje editaci
MIDI.

rastrová grafika - GIMP
-----------------------

GIMP používám už delší dobu. Přešel jsem na něj z Photoshopu, protože
nerad kradu a protože nemám rád Windows. Nebudu lhát, GIMP ve srovnání
kvality a produktivity s komerčním nástrojem číslo jedna, tedy s
Photoshopem, prohraje. Ne však o mnoho a produktivita a kvalita nejsou
jediné použitelné metriky. GIMP je zdarma, je svobodný a multiplatformní
a jeho kvalita je opravdu vysoká. Běžným lidem i poloprofesionálům
bohatě postačí. Víceméně platí, že co uděláte ve Photoshopu, uděláte i v
GIMPu, jenom Photoshop to umí pohodlněji, např. díky lepším náhledům, a
znatelně svižněji (předpokládám díky SSE optimalizaci nebo něčemu
podobnému). Rozhraní obou programů jsou velmi podobná a přechod je proto
jednoduchý.

2D animace - Synfig Studio
--------------------------

Program na 2D animaci pomocí klíčových snímků jsem hledal dlouho, až
jsem naštěstí našel Synfig Studio. Na první pohled se mi zdál trochu
divný, nedokázal jsem v něm např. pohybovat nebo rotovat objekty. To
bylo však způsobeno tím, že jsem neznal filosofii tohoto softwaru. Je
potřeba se podívat na základní tutoriál, abyste pochopili, že v Synfig
Studiu je všechno vrstva (tzn. obrázky, transformace, skupiny apod.) a
všechny vrstvy tvoří hierarchii, podobnou např. scene graphu ve 3D.
Každá vrstva má atributy, které lze animovat pomocí klíčových snímků.
Pak už jde všechno samo a s programem se pracuje velmi dobře. Setkal
jsem se jen s pár bugy, které ale nebyly zásadního charakteru.

vektorová grafika - Inkscape
----------------------------

Tady není o čem diskutovat, Inkscape používám dlouho a se softwarem snad
ani nemůžu být spokojenější. Nástroj je mocný, ale zachovává si
jednoduché rozhraní. Je v něm možné vytvářet krásná vektorová
díla, diagramy a podobné věci. Kdybych se měl pokusit alespoň o nějakou
kritiku, tak se mi v poslední verzi příliš nelíbí změna práce s
barevnými přechody, a bylo by opravdu úžasné, kdyby byla podporována
animace.

programovací editor - Kate
--------------------------

Tady ještě nejspíš nejsem u svého finálního programovacího editoru,
protože všichni víme, že ultimátním editorem je Vim, a k tomu bych se
taky rád jednou dopracoval. Základy Vimu už zvládám, ale nejsem v něm
příliš rychlý, a tak jsem si dal malou práci prohledat momentální stav
GUI editorů a najít něco normálního. Chtěl jsem něco, co umí rozdělovat
obrazovku a pokud možno minimapu dokumentu (protože ta je opravdu hodně
cool). Tomu nakonec vyhověl(a ?) Kate, editor se sympatickým jménem,
který zatím zvládá svou práci velmi dobře.

internetový prohlížeč - Chromium
--------------------------------

Už na Windows jsem používal Google Chrome. Chromium je pro uživatele v
podstatě stejný prohlížeč. Pro informatiky je v oblasti browserů jenom
jedna skutečná alternativa - Firefox. Ten je ale příliš složitý a
pomalý, takže asi tak.

kancelářské programy - LibreOffice
----------------------------------

Opět není moc o čem mluvit, velmi kvalitní software, který by s
přehledem mohl úplně nahradit MS Office a bylo by o jeden komerční shit
míň. Kdyby ho alespoň dávali k Windows zdarma, možná bych si to označení
odpustil. Pokud potřebuji vysázet vysoce hezký dokument, použiju
samozřejmě LaTeX.

multimediální přehrávač - VLC player
------------------------------------

Tady jsem zase tak moc nepátral, využil jsem jeden z prvních přehrávačů,
na které jsem narazil. Ale vyhovuje mi dobře. Prakticky můj jediný
požadavek byl, aby přehrávač uměl krokovat video po jednotlivých
snímcích, protože to se občas hodí při stříhání videí. VLC player tohle
samozřejmě zvládá, taky umí dělat snímky z videí, přehrávat různými
rychlostmi apod.
