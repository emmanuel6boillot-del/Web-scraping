import requests
from bs4 import BeautifulSoup
import json
import sqlite3
from datas import DatabaseManager

db = DatabaseManager("database.db")
db.connexion_SQLite()

url = "https://books.toscrape.com/"
response = requests.get(url)
html = response.text

if response.status_code != 200:
    print("Erreur :", response.status_code)

soup = BeautifulSoup(html, "html.parser")

data = {}

def trad_score(m : str) :
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
liens1 = liens.find("ul")
links = liens1.find_all("li")

for x in links :

    new_url = f"https://books.toscrape.com/{x.a["href"]}"
    catégorie = x.text.strip()
    response = requests.get(new_url)
    html = response.text
    if response.status_code != 200:
        print("Erreur :", response.status_code)
    new_soup = BeautifulSoup(html, "html.parser")

    livres = new_soup.find_all("article", class_="product_pod") #liste de tout les livres de la catégorie

    for livre in livres :
        titre = livre.h3.a["title"]
        try:
            note = trad_score(livre.find("p", class_="star-rating")["class"][1])
        except TypeError:
            note = None
        
        try:
            prix = livre.find("p", class_="price_color").text
        except AttributeError:
            prix = None

        data[titre] = {"prix" : float(prix[2:]) , "note" : note, "catégorie" : catégorie }

        db.insertion_annonces([titre, float(prix[2:]), note, catégorie])

db.fermeture_base()