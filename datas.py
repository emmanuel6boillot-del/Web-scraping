import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
#db = DatabaseManager("database.db")
cursor.execute("CREATE TABLE IF NOT EXISTS Books (id INTEGER PRIMARY KEY AUTOINCREMENT, titre TEXT NOT NULL, prix TEXT, note TEXT NULL, catégorie TEXT)")
conn.commit()

cursor.execute("INSERT INTO Books (titre,prix,note,catégorie) VALUES (?,?,?,?)",("Livre","5","3.5","Horreur"))
conn.commit()
conn.close()

# Exécuter une requête



import sqlite3

#connexion
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

#Classe de la database
class DatabaseManager:
    def __init__ (self,nom_fichier):
        self.nom = nom_fichier

    def connexion_SQLite(self):
        self.conn = None
        self.conn = sqlite3.connect(self.nom)
        self.cursor = self.conn.cursor()

    def creation_tables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Books (id INTEGER PRIMARY KEY AUTOINCREMENT, titre TEXT NOT NULL, prix TEXT, note TEXT NULL, catégorie TEXT)")
        self.conn.commit()

    def insertion_annonces(self,ligne):
        titre,prix,note,catégorie = ligne[0],ligne[1],ligne[2],ligne[3]
        self.cursor.execute("INSERT INTO Books (titre,prix,note,catégorie) VALUES (?,?,?,?)",(titre,prix,note,catégorie))
        self.conn.commit()
    
    def lecture_donnees(self): #catégorie séparer par une virgule
        self.connexion_SQLite()
        self.cursor.execute("SELECT * FROM livres    ")  #titre, prix, note, catégorie   WHERE,ORDER BY, ASC, DESC, LIMIT
        res = self.cursor.fetchall()
        self.fermeture_base()
        return res

    def score_moyen_catégorie(self):
        self.connexion_SQLite()
        self.cursor.execute("SELECT categorie, AVG(note) as note_moyenne FROM livres GROUP BY categorie ORDER BY AVG(note) DESC LIMIT 10")
        res = self.cursor.fetchall()
        ax,ay=[res[k][0] for k in range(len(res))],[res[k][1] for k in range(len(res))]
        fig, axe = plt.subplots()
        ax.bar(ax, ay, color="skyblue")
        plt.xticks(rotation=45, ha='right') 
        ax.set_title("Note moyenne par catégorie")
        ax.set_xlabel("Catégorie") 
        ax.set_ylabel("Note sur 5")
        plt.tight_layout()
        plt.show()
        self.fermeture_base()

    def meilleurs_livres_catégorie():
        self.connexion_SQLite()
        self.cursor.execute("SELECT categorie, MAX(note) as meilleure_note, titre FROM livres WHERE (categorie, note) IN ( SELECT categorie, MAX(note) FROM livres GROUP BY categorie ) GROUP BY categorie ORDER BY MAX(note) DESC LIMIT 10")
        res = self.cursor.fetchall()
        ax,ay = [res[k][0] + " : " + res[k][2] for k in range(len(res))],[res[k][1] for k in range(len(res))]
        fig, axe = plt.subplots()
        ax.bar(ax, ay, color="skyblue")
        plt.xticks(rotation=45, ha='right') 
        ax.set_title("Meilleurs livres par catégorie")
        ax.set_xlabel("Catégorie : Titre du livre") 
        ax.set_ylabel("Note sur 5")
        plt.tight_layout()
        plt.show()
        self.fermeture_base()

    def titre_le_plus_long():
        self.connexion_SQLite()
        self.cursor.execute("SELECT titre, LENGTH(titre) as longeur FROM livres ORDER BY longeur DESC LIMIT 10")
        res = self.cursor.fetchall()
        print("Les 10 livres avec les titres les plus longs sont :")
        for ligne in res:
            print(ligne)
        self.fermeture_base()

    def mots_récurrent():
        self.connexion_SQLite()
        self.cursor.execute("SELECT titre FROM livres")
        res = self.cursor.fetchall()
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
                    fin + = 1
            sortie.append txt[deb,-1]
            return res
        
        for ligne in res:
            sortie = cut(ligne[0])
            for x in sortie:
                if x in dictionnaire:
                    dictionnaire[x] + = 1
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
        ax.bar(ax, ay, color="skyblue")
        plt.xticks(rotation=45, ha='right') 
        ax.set_title("Les mots les plus utilisés dans les titres")
        ax.set_xlabel("Mots") 
        ax.set_ylabel("Nombre d'occurence sur le site")
        plt.tight_layout()
        plt.show()
        self.fermeture_base()

    def fermeture_base(self):
        self.conn.close()

db = DatabaseManager("database.db")