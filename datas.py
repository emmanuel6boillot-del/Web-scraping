import sqlite3

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
        self.cursor.execute("SELECT * FROM Books    ")  #titre, prix, note, catégorie   WHERE,ORDER BY, ASC, DESC, LIMIT
        res = self.cursor.fetchall()
        return res
        
    def fermeture_base(self):
        self.conn.close()