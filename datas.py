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

    def insertion_annonces(self,fichier_jason):
        #self.cursor.execute("INSERT INTO Books (titre,prix,note,catégorie) VALUES (?,?,?,?)",(titre,prix,note,catégorie))
        if self.conn is not None:
            with open(fichier_jason, 'r', encoding='utf-8') as jsonfile: # on ouvre le fichier json situé dans le même dossier que le script python

                json_data = json.load(jsonfile) # on charge les données json dans une variable objet
                #create_database(conn, json_data, table_name, column_name='', fk_column_name='', fk_column_value=0)
                create_database(self.conn, json_data, 'livres') # on créé et on alimente la base de données sqlite        
 
        else:
            print("Erreur! impossible de créer la connexion à la base !")

        self.conn.commit()
    
    def lecture_donnees(self): #catégorie séparer par une virgule
        self.cursor.execute("SELECT * FROM livres    ")  #titre, prix, note, catégorie   WHERE,ORDER BY, ASC, DESC, LIMIT
    
    def score_moyen_catégorie(self):
        self.connexion_SQLite()
        self.cursor.execute("SELECT categorie, AVG(note) as note_moyenne FROM livres GROUP BY categorie ORDER BY AVG(note) DESC LIMIT 10")
        res = self.cursor.fetchall()
        ax,ay=[res[0][k] for k in range(len(res))],[res[1][k] for k in range(len(res))]
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
        ax,ay = [res[0][k] + " : " + res[2][k] for k in range(len(res))],[res[1][k] for k in range(len(res))]
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

    def fermeture_base(self):
        self.conn.close()

db = DatabaseManager("database.db")