import sqlite3

class News:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS news (id INTEGER PRIMARY KEY, titulo text, novedad text, imagen text,fuente text)")
        self.conn.commit()

    def insert(self, titulo ,novedad ,imagen , fuente):
        self.cur.execute("INSERT INTO news VALUES (NULL,?,?,?,?)",(titulo, novedad, imagen, fuente))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM news")
        rows=self.cur.fetchall()
        return rows

    def search(self, titulo = "", novedad = "", imagen = "", fuente = ""):
        self.cur.execute("SELECT * FROM news WHERE OR titulo=? OR novedad=? OR imagen=? OR fuente=?", (titulo, novedad, imagen, fuente))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM news WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, nombre , titulo, novedad, imagen, fuente):
        self.cur.execute("UPDATE news SET  titulo=?, novedad=?, imagen=?, fuente=? WHERE id=?",(titulo, novedad, imagen, fuente, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
