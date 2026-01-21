import requests
from bs4 import BeautifulSoup
import sqlite3
from src.datas import DatabaseManager

db = DatabaseManager("database.db")
db.connexion_SQLite()
db.creation_tables()

url = "https://books.toscrape.com/"
response = requests.get(url)
html = response.text

if response.status_code != 200:
    print("Erreur :", response.status_code)

soup = BeautifulSoup(html, "html.parser")

def trad_score(m : str) : # Code pour traduire un chiffre écrit en lettre en un entier
    if m == "One" :
        return 1
    elif m == "Two" :
        return 2
    elif m == "Three" :
        return 3
    elif m == "Four" :
        return 4
    elif m == "Five" :
        return 5

liens = soup.find("ul", class_="nav nav-list")
liens1 = liens.find("ul") # étapes intermédiaires pour avoir accès à tout les liens.
links = liens1.find_all("li") # contient tout les liens de toutes les pages correspondants chacunes à une catégorie de livre.

for x in links :

    new_url = f"https://books.toscrape.com/{x.a["href"]}"
    catégorie = x.text.strip()
    response = requests.get(new_url)
    html = response.text # on extrait le code html de la nouvelle page qui correspond à la catégorie "catégorie"
    if response.status_code != 200:
        print("Erreur :", response.status_code)
    new_soup = BeautifulSoup(html, "html.parser")

    livres = new_soup.find_all("article", class_="product_pod") #liste de tout les livres de la catégorie

    for livre in livres : # pour chaque livre, on extrait titre, prix et note (on connait déjà la catégorie)
        titre = livre.h3.a["title"]
        try:
            note = trad_score(livre.find("p", class_="star-rating")["class"][1])
        except TypeError: # au cas où il n'y a pas de note car alors livre.find("p", class_="star-rating") est de type None donc il y a un problème de type
            note = None
            
        try:
            prix = livre.find("p", class_="price_color").text
        except AttributeError:
            prix = None

        db.insertion_annonces([titre, float(prix[2:]), note, catégorie]) # les deux premiers caractères du prix sont pour l'unité £ donc on les rétires

"""   while new_soup.find("li", class_="next") != None :

        livres = new_soup.find_all("article", class_="product_pod") #liste de tout les livres de la catégorie

        for livre in livres : # pour chaque livre, on extrait titre, prix et note (on connait déjà la catégorie)
            titre = livre.h3.a["title"]
            try:
                note = trad_score(livre.find("p", class_="star-rating")["class"][1])
            except TypeError: # au cas où il n'y a pas de note car alors livre.find("p", class_="star-rating") est de type None donc il y a un problème de type
                note = None
            
            try:
                prix = livre.find("p", class_="price_color").text
            except AttributeError:
                prix = None

            db.insertion_annonces([titre, float(prix[2:]), note, catégorie]) # les deux premiers caractères du prix sont pour l'unité £ donc on les rétires

        url = f"https://books.toscrape.com/{x.a["href"]}/{new_soup.find("li", class_="next").a["href"]}"
        response = requests.get(url)
        html = response.text
        if response.status_code != 200:
            print("Erreur :", response.status_code)
        new_soup = BeautifulSoup(html, "html.parser")

    livres = new_soup.find_all("article", class_="product_pod") #liste de tout les livres de la catégorie

    for livre in livres : # pour chaque livre, on extrait titre, prix et note (on connait déjà la catégorie)
        titre = livre.h3.a["title"]
        try:
            note = trad_score(livre.find("p", class_="star-rating")["class"][1])
        except TypeError: # au cas où il n'y a pas de note car alors livre.find("p", class_="star-rating") est de type None donc il y a un problème de type
            note = None
            
        try:
            prix = livre.find("p", class_="price_color").text
        except AttributeError:
            prix = None

        db.insertion_annonces([titre, float(prix[2:]), note, catégorie]) # les deux premiers caractères du prix sont pour l'unité £ donc on les rétires
"""
db.fermeture_base()