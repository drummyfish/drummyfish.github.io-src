Title: Pojďte se mnou psát textové RPG ve stylu Skyrimu
Date: 2015-08-16 22:02
Author: tastyfish
Category: Posts
Tags: c, commandline, game, multiplatform, recruit, rpg
Slug: text-skyrim-rpg
Lang: cs
Status: published

{% import 'macros.html' as m %}

Chtěli jste někdy napsat vlastní RPG? Já ano a proto
jsem s tím nedávno začal. Byl bych rád, kdyby se ke mně připojilo víc
lidí - společně třeba vytvoříme dobrou hru. Nechce se mi moc psát, takže
projekt představím v odrážkách:

-   Jde o čistě textové RPG v příkazové řádce ve stylu interaktivní
    knihy, která ale hráči nabídne extrémní svobodu, podobně jako např.
    Skyrim. Neděláme žádnou grafiku (ani ASCII), žádné zvuky, ikony ani
    nic podobného. V budoucnu nicméně uvažuji o samostatné nadstavbě,
    která nabídne 3D nebo 2D grafiku se vším všudy. Tím, že se ze
    začátku vzdáme grafiky, fyziky a dalších věcí, se můžeme soustředit
    na vytvoření dobrého RPG jádra, které bude zároveň hratelnou hrou.
-   Všechno je open-source, multiplatformní, čistě v C++, držíme se
    stylu KISS, používáme minimum knihoven a vždy pouze open-source.
    Nikdo na projektu nevydělá ani korunu, jde čistě o vytvoření dobré
    hry, proto taky nikdo po nikom nechce žádnou práci a každý přispívá
    jenom tehdy, když má čas a chuť.
-   Naprostou většinu informací (koncepty, návrhy, kódové
    konvence apod.) o projektu shromažďuji [v tomto
    dokumentu](https://docs.google.com/document/d/1jq0dE7DdXIpz_ytLAirXNP6_Oi0MdCSoMdU-_P1p9Lk/edit).
-   GitHub:
    [github.com/drummyfish/text-rpg](https://github.com/drummyfish/text-rpg)
-   projektový chat:
    [HipChat](https://skyrimtextrpg.hipchat.com/invite/407349/c1a6369243e2704c33cbc7bd5c11adf7?utm_campaign=add_users_link)

Chcete se připojit? Stačí forknout projektový repozitář na GitHubu,
napsat nějaký kód a poslat jej zpět pull requestem. Nevíte, co máte
programovat? Podívejte se na UML diagram tříd ve složce other na GitHubu
- najdete tam třídy, které je potřeba implementovat. Nebo se zeptejte na
chatu. Nehledáme ale jenom programátory, je nutné dodělat UML diagram a
domyslet spoustu věcí o hře, např. její jméno. Stačí se připojit na
chat. Těšíme se na vás {{m.e(':)')}}
