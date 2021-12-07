# Arkkitehtuuri

## Luokka/pakkauskaavio

![pakkauskaavio](/dokumentaatio/pakkauskaavio.png "pakkauskaavio")

Pakkauskaavio esittää sovellusta tämän hetkisessä tilassa (pl. LoginService, jonka refaktorointi on vielä kesken).


## Sekvenssikaaviot

![kirjautuminen-sekvenssi](/dokumentaatio/kirjautuminen-sekvenssikaavio.png "kirjautumisen sekvenssikaavio")

Kaavio esittää ohjelman kulun kun käyttäjä syöttää salasanan, sekä klikkaa kirjaudu painiketta. UserService vertaa käyttäjän syöttämä salasana UserRepositorysta saatuun salasanaan. UserService palauttaa totuusarvon UI:lle, jonka pohjalta UI päättää mikä näkymä näytetään seuraavaksi (joko listanäkymä, tai kirjautumisnäkymä uudelleen).