# Käyttöohje

## Lataaminen ja asentaminen

- Käyttöohje olettaa että ohjelman käyttäjällä on Poetry asennettunna. Ohjeet Poetryn asentamiseen löytyy mm. täältä: https://python-poetry.org/docs/#installation

- Lataa ja pura ohjelman viimeisin version täältä: https://github.com/nabelosaurus/ot-harjoitustyo/releases


## Konfigurointi

Ohjelma käyttää tietokantaa, joka löytyy projektijuuren data-kansiosta. Mikäli tietokantaa ei löydy (esim. ennen ensimmäistä suorituskertaa), luo ohjelma sellaisen. Tietokanta-tiedostonimen voi konfiguroida tiedostossa *.env*. Mikäli käyttäjä haluaa ylläpitää useampaa kokonaisuutta, onnistuu se muuttamalla DATABASE_FILENAME kohtaa *.env* tiedostossa käynnistyskertojen välillä.

    DATABASE_FILENAME=datastore.sqlite


## Ohjelman suoritus

Avaa komentorivitulkki, ja navigoi projektin juurikansioon.

Asenna projektin riippuvuudet komennolla:

    poetry install

Alusta projekti komennolla:

    poetry run invoke build

Suorita projekti komennolla:

    poetry run invoke start


## Rekisteröidy

Ensimmäisellä käynnistyskerralla ohjelma käynnistyy rekiströitymisnäkymään. Valitse itsellesi salasana, joka on vähintään 10 merkin pituinen. Syötä salasana myös vahvistuskentään ja paina *Set*. Tällä salasanalla ohjelmaan pääsee jatkossa kirjautumaan. Salasana tallentuu tietokantaan salattuna argon2:lla.

![Rekiströityminen](/dokumentaatio/käyttöohjeen-kuvat/register.png "Rekisteröityminen")


## Kirjautiminen

Kirjautuminen onnistuu rekisteröinnin yhteydessä luodulla *master* salasanalla. Syötä salasana, ja valitse login.

![Kirjautuminen](/dokumentaatio/käyttöohjeen-kuvat/login.png "Kirjautuminen")


## Kirjautumiskohteen lisääminen

Uuden kirjautumiskohteen (login) pääsee lisäämään valitsemalla ohjelman päänäkymästä *Add new*.

![Lisää](/dokumentaatio/käyttöohjeen-kuvat/add_new_1.png "Lisää")

Syötä kirjautumiskohteen tiedot (verkkosivu, sähköposti, käyttäjänimi, sekä salasana), ja valitse *Add / Update*. Salasana näkyy tässä kohtaa selkokielisenä, mutta tallennetaan tietokantaan salattuna ja suolattuna.

![Lisää 2](/dokumentaatio/käyttöohjeen-kuvat/add_new_2.png "Lisää 2")

## Kirjautumiskohteen muokkaaminen

Kirjautumiskohdetta pääsee tarkastamaan, sekä muokkaamaan valitsemalla *View*. Prosessi on muutoin sama kuin uuden kohteen lisääminen.

![Näytä](/dokumentaatio/käyttöohjeen-kuvat/view_copy_logout.png "Näytä")


## Kirjautumiskohteen salasanan kopioiminen leikepöydälle

Kirjautumiskohteen salasanan saa kopioitua leikepöydälle painamalla *Copy*. Tällä tavalla salasanan saa kopioitua käyttöön, ilman että salasana näkyisi ruudulla.

![Kopioi](/dokumentaatio/käyttöohjeen-kuvat/view_copy_logout.png "Kopioi")


## Kirjautuminen ulos

Lopuksi ohjelmasta kirjaudutaan ulos painamalla *Logout*, jolloin ohjelma palaa takaisin kirjautumisnäkymään.

![Kirjaudu ulos](/dokumentaatio/käyttöohjeen-kuvat/view_copy_logout.png "Kirjaudu ulos")
![Kirjaudu](/dokumentaatio/käyttöohjeen-kuvat/login.png "Kirjaudu")