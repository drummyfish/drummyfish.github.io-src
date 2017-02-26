Title: Nové stránky, jsou open-source!
Date: 2017-02-26 20:12
Author: tastyfish
Category: Posts
Lang: cs
Status: published

{% import 'macros.html' as m %}

Nastal u mne lavinový efekt:

1. Updatoval jsem tabulku na stránkách.
2. Všiml jsem si, že teď je už moc velká a mohl bych napsat skript, který by ji generoval.
3. Když už to napíšu, mohl bych to zveřejnit na GitHubu, aby to mohli použít i ostatní.
4. Proč vlastně nemám celé stránky na GitHubu? Jde to vůbec?
5. Zjišťuju, že GitHub má přímou podporu pro hostování stránek, ale jenom statických.
6. Na co vlastně potřebuju dynamické stránky? Odpověď zní: nepotřebuju.
7. Není přechod na statické stránky krok zpět? Odpověď zní: ne.
8. Instaluju Pelican a jdu předělávat a migrovat celé stránky.

Teď, o pár týdnů později, mám nové stránky připravené ke spuštění. Důsledky jsou následující:

- Stránky jsou teď [open-source](https://github.com/drummyfish/drummyfish.github.io-src)! Z toho plyne milion výhod, o kterých bych rád napsal a snad i napíšu.
- Stránky už nejedou na Wordpressu, ale na méně populárním Pythonovém mikroframeworku [Pelican](http://docs.getpelican.com/en/stable/), jehož podvýhody jsou:
    - Je lightweight a KISS, jednoduchý, snadno modifikovatelný, transparentní.
    - Python!
    - Stránky jsou statické! Žádné PHP/SQL, jenom HTML/MD. Načítají se jak blesk a dají se hostovat úplně všude. Paráda.  
- Hosting mám úplně zdarma na GitHubu, spolu se všemi svými ostatními projekty, tzn. všechno pěkně na jednom místě, updaty dělám z terminálu, mám uloženou historii atd.
- Žádné komentáře, komentáře jsou na prd.

Užívejte brouzdání {{m.e(':)')}}