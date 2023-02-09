import sqlite3

class Linea:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS linea (id INTEGER PRIMARY KEY, nombre text, descripcion text, imagen text, categoria text)")
        self.conn.commit()

    def insert(self, nombre , descripcion, imagen, categoria):
        self.cur.execute("INSERT INTO linea VALUES (NULL,?,?,?,?)",(nombre, descripcion, imagen, categoria))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM linea")
        rows=self.cur.fetchall()
        return rows

    def search(self, nombre = "", descripcion = "", imagen = "", categoria = ""):
        self.cur.execute("SELECT * FROM team WHERE nombre =? OR descripcion=? OR imagen=? OR categoria=?", (nombre, descripcion, imagen, categoria))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM linea WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, nombre , descripcion, imagen, categoria):
        self.cur.execute("UPDATE linea SET nombre=?, descripcion=?, imagen=?, categoria=? WHERE id=?",( nombre , descripcion, imagen, categoria, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()