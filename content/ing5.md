Title: Ing. na FIT – 5. semestr
Date: 2017-01-30 00:44
Author: tastyfish
Category: Articles
Tags: study
Slug: ing5
Lang: cs
Status: published

{% import 'macros.html' as m %}

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

{{ m.study_semester_summary("Ing.",4,"cs") }}