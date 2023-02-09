import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS paper (id INTEGER PRIMARY KEY, name  text, author text, year integer, doi integer, grafical text,abstract text, cite text)")
        self.conn.commit()

    def insert(self,name , author, year, doi, grafical, abstract,cite):
        self.cur.execute("INSERT INTO paper VALUES (NULL,?,?,?,?,?,?,?)",(name , author, year, doi, grafical, abstract,cite))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM paper")
        rows=self.cur.fetchall()
        return rows

    def search(self,name  = "", author = "", year = "", doi = "", grafical = "", abstract = "",cite= ""):
        self.cur.execute("SELECT * FROM paper WHERE name =? OR author=? OR year=? OR doi=? OR grafical=? OR abstract=? OR cite=?", (name , author, year, doi, grafical, abstract,cite))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM paper WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id, name , author, year, doi, grafical, abstract,cite):
        self.cur.execute("UPDATE paper SET name =?, author=?, year=?, doi=?, grafical=?, abstact=?,cite=? WHERE id=?",(name , author, year, doi, grafical, abstract, cite,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


