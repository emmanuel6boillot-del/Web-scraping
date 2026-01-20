import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
html = response.text

if response.status_code != 200:
    print("Erreur :", response.status_code)

soup = BeautifulSoup(html, "html.parser")

data = {}

livres = soup.find_all("article", class_="product_pod") #liste de tout les livres

for x in livres :
    titre = livre.h3.a["title"]
    try:
        prix = livre.find("p", class_="price_color").text
    except AttributeError:
        prix = None
    data[titre] = [prix, ]