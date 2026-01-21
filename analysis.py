from datas import DatabaseManager
import matplotlib.pyplot as plt


def score_moyen_catégorie(data):
    data.cursor.execute("SELECT catégorie, AVG(note) as note_moyenne FROM Books GROUP BY catégorie ORDER BY AVG(note) DESC LIMIT 10")
    res = data.cursor.fetchall()
    ax,ay=[res[k][0] for k in range(len(res))],[res[k][1] for k in range(len(res))]
    fig, axe = plt.subplots()
    axe.bar(ax, ay, color="skyblue")
    plt.xticks(rotation=45, ha='right') 
    axe.set_title("Note moyenne par catégorie")
    axe.set_xlabel("Catégorie") 
    axe.set_ylabel("Note sur 5")
    #plt.plot(ax,ay)
    plt.tight_layout()
    plt.show()

def meilleurs_livres_catégorie(data):
    data.cursor.execute("SELECT catégorie, MAX(note) as meilleure_note, titre FROM Books WHERE (catégorie, note) IN ( SELECT catégorie, MAX(note) FROM Books GROUP BY catégorie ) GROUP BY catégorie ORDER BY MAX(note) DESC LIMIT 10")
    res = data.cursor.fetchall()
    ax,ay = [res[k][0] + " : " + res[k][2] for k in range(len(res))],[res[k][1] for k in range(len(res))]
    fig, axe = plt.subplots()
    axe.bar(ax, ay, color="skyblue")
    plt.xticks(rotation=45, ha='right') 
    axe.set_title("Meilleurs livres par catégorie")
    axe.set_xlabel("Catégorie : Titre du livre") 
    axe.set_ylabel("Note sur 5")
    #plt.plot(ax,ay)
    plt.tight_layout()
    plt.show()

def titre_le_plus_long(data):
    data.cursor.execute("SELECT titre, LENGTH(titre) as longeur FROM Books ORDER BY longeur DESC LIMIT 10")
    res = data.cursor.fetchall()
    print("Les 10 livres avec les titres les plus longs sont :")
    for ligne in res:
        print(ligne)

def mots_récurrent(data):
    data.cursor.execute("SELECT titre FROM Books")
    res = data.cursor.fetchall()
    dictionnaire = {}

    def cut(txt):
        sortie=[]
        deb=0
        fin=0
        for x in txt:
            if x == " ":
                sortie.append(txt[deb,fin-1])
                deb = fin
            else: 
                fin += 1
        sortie.append(txt[deb,-1])
        return res
    
    for ligne in res:
        sortie = cut(ligne[0])
        for x in sortie:
            if x in dictionnaire:
                dictionnaire[x] += 1
            else:
                dictionnaire[x] = 1
    
    def dix_premiers(d):
        inf=0
        L = [(None,0) for k in range(10)]
        for x in d:
            if d[x] > inf :
                k = 0
                for k in range(10) :
                    if L[k][1]>d[x]:
                        k+=1
                    else:
                        L = L[1:k+1] + [(x,d(x))] + L[k+1:]
        return L
    
    L = dix_premiers(dictionnaire)
    ax,ay = [L[k][0] for k in range(10)],[res[k][1] for k in range(10)]
    fig, axe = plt.subplots()
    axe.bar(ax, ay, color="skyblue")
    plt.xticks(rotation=45, ha='right') 
    axe.set_title("Les mots les plus utilisés dans les titres")
    axe.set_xlabel("Mots") 
    axe.set_ylabel("Nombre d'occurence sur le site")
    #plt.plot(ax,ay)
    plt.tight_layout()
    plt.show()

db = DatabaseManager("database.db")
db.connexion_SQLite()
titre_le_plus_long(db)
meilleurs_livres_catégorie(db)
score_moyen_catégorie(db)
mots_récurrent(db)
dn.fermeture_base