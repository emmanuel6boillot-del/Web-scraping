**Rapport scraping de Books to scrape**

I - Le scraping.

Nous avons utilisé la bibliothèque requests pour récupérer les informations de la page web et la bibliothèque BeautifulSoup pour l'organiser et pouvoir extraire les données. L'importation de ces bibliothèques nous a appris qu'il faut toujours vérifié les actuelles et les commandes d'importations des bibliothèques car ils sont souvent actualisés et ça peut causer des erreurs d'importation. 

Initialement, l'idée était de rester sur la page principale et de parcourir les livres là pour ne pas avoir à changer de site. En revanche, cela ne nous permettait pas d'avoir accès à la catégorie. Il a donc fallu extraire tout les liens de la page principale correspondant à des catégories différentes et sur chacune de ces pages, nous avons parcourus les différents livres pour extraire les informations d'intérêt : titre, prix et note. L'implémentation c'est faite à l'aide d'une boucle sur les liens que nous avions stocké préalablement dans une liste. 

Il a alors fallu modifier les donnés pour qu'elles soient utilisables : retirer les espaces libres autour de la catégorie, convertir le prix en un chiffre et traduire les notes écrites de lettres à chiffre. Et au fur et à mesure, nous avons ajouté les valeurs à la base de donnée grâce à l'interface codé dans datas.py.

II - La base de donnée.

Nous avons appris à faire une interface entre une base de donnée et python à l'aide de la création d'une classe python. Cette interface nous permet de modifier et de travailler sur un tableau SQL en langage Python. 