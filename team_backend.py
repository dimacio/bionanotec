import sqlite3

class Team:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS team (id INTEGER PRIMARY KEY, nombre text, puesto text, titulo text, mail text, imagen text,comentario text)")
        self.conn.commit()

    def insert(self, nombre , puesto, titulo, mail, imagen, comentario):
        self.cur.execute("INSERT INTO team VALUES (NULL,?,?,?,?,?,?)",(nombre, puesto, titulo, mail, imagen, comentario))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM team")
        rows=self.cur.fetchall()
        return rows

    def search(self, nombre = "", puesto = "", titulo = "", mail = "", imagen = "", comentario = ""):
        self.cur.execute("SELECT * FROM team WHERE nombre =? OR puesto=? OR titulo=? OR mail=? OR imagen=? OR comentario=?", (nombre, puesto, titulo, mail, imagen, comentario))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM team WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, nombre , puesto, titulo, mail, imagen, comentario):
        self.cur.execute("UPDATE team SET nombre=?, puesto=?, titulo=?, mail=?, imagen=?,comentario=? WHERE id=?",( nombre , puesto, titulo, mail, imagen, comentario, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
