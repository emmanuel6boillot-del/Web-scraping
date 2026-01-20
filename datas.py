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


"""
import sqlite3

#connexion
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

#Classe de la database
class DatabaseManager:
    def __init__ (self,nom_fichier):
        self.nom = nom_fichier

    def connexion_SQLite(self):
        self.conn = sqlite3.connect(self.nom)
        self.cursor = self.conn.cursor()

    def creation_tables(self):
        self.cursor.execute("CREATE TABLE Books (id INTEGER PRIMARY KEY AUTOINCREMENT, Titre TEXT NOT NULL, Prix TEXT, Note TEXT NULL, Catégorie TEXT)")
        self.conn.commit()

    def insertion_annonces(self):
        pass
    def lecture_donnees(self):
        pass

    def fermeture_base(self):
        self.conn.close()

db = DatabaseManager("database.db")"""