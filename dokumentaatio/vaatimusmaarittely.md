# Vaatimusmäärittely

## Sovelluksen tarkoitus

Yksinkertainen sovellus salasanojen hallintaa varten.

## Käyttäjät

Sovelluksella on vain yksi normaali käyttäjä. Käyttäjä kirjautuu sovellukseen itse asettamallaan salasanalla.

## Käyttöliittymäluonnos

![user interface](/dokumentaatio/ui.png "user interface")


Ensimmäinen näkymä on master salasanan asettamista varten. Kun salasana on kerran valittu, sovellus ei enää tätä näkymää esitä. Kirjautumisnäkymästä siirrytään listanäkymään kirjautumalla sisään master salasanalla. Listanäkymä listaa tallennetut kohteet. Listanäkymästä voidaan siirtyä kahteen eri näkymään, uuden kohteen lisääminen ja olemassa olevan kohteen katsominen. ✅ **tehty**

## Perusversion tarjoama toiminnallisuus

### Ensimmäinen käynnistyskerta

- Käyttäjä valitsee itsellensä salasanan, joka on vähintään 10 merkkiä pitkä. Käyttäjä myös vahvistaa salasana, ja järjestelmä varmistaa että salasanat täsmäävät keskenään. Jos salasanat eivät täsmää, tai salasano on liian lyhyt, palaa näkymä alkutilaan. **tehty aiemmin**
- Jos käyttäjä ei saa asetettua salasanaa itsellensä tässä vaiheessa, aukeaa sovellus tähän samaan näkymään kunnes tässä onnistutaan. **tehty aiemmin**
- Kun käyttäjä on asettanut itsellensä salasanan, siirtyy ohjelma kirjautumisnäkymään. **tehty aiemmin**

### Ennen kirjautumista

- Käyttäjä kirjautuu syöttämällä ensimmäisellä käynnistyksellä asettamallaan salasanallaan. **tehty aiemmin**
- Jos käyttäjä syöttää väärän salasanan, ilmoittaa ohjelma tästä. **tehty aiemmin**

### Kirjautuneena

- Käyttäjä pystyy selaamaan omia kohteitaan listalta. ✅ **tehty viikolla 5**
- Käyttäjä voi lisätä uuden kohteen listalle. **tehty aiemmin**
    - Lisääminen aukeaa eri näkymään, ja vaatii sen että käyttäjä syöttää: ✅ **tehty viikolla 5**
        1. Verkkosivun (vaaditaan)
        1. Käyttäjänimen (vaihtoehtoinen)
        1. Sähköpostin (vaihtoehtoinen)
        1. Salasanan (vaaditaan)
- Käyttäjä voi avata listan kohteita omaan näkymään, josta salasanan voi kopioida leikepöydälle. **tehty aiemmin**
- Käyttäjä voi kirjautua ulos. **tehty aiemmin**

## Jatkokehitysideoita

- Kehityksen alkuvaiheessa sovellus saattaa tallentaa salasanat turvattomasti. Tämä on korkein prioriteetti heti kun perusversion toiminnot implementoitu.
- Alkuvaiheen sovellus tukee ainoastaan tietojen lisäämistä ja lukemista. Tavoite on että sovellukselle saadaan myös seuraavat toiminnot myöhemmässä vaiheessa:
    - Tietojen muokkaaminen.
    - Tiedon poistaminen.
- Työkalu jolla voidaan generoida salasana automaattisesti.
- Ajan salliessa: Ilmoitus jos jollain verkkosivulla tietovuoto.
    - Tähän voisi hyödyntää haveibeenpwned.com API:a.