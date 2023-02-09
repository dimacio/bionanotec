from app import db


class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, index=True)
    name = db.Column(db.String(128), index=True, unique=True)
    author = db.Column(db.String(128))
    cite = db.Column(db.String(128))
    abstract = db.Column(db.String(256))
    doi = db.Column(db.String(128))
    grafical = db.Column(db.String(128))
    
    def __repr__(self):
        return '<Paper {}>'.format(self.name)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    puesto = db.Column(db.String(128))
    titulo = db.Column(db.String(128))
    mail = db.Column(db.String(128))
    imagen = db.Column(db.String(128))
    comentario = db.Column(db.String(256))

    def __repr__(self):
        return '<Team {}>'.format(self.nombre)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    novedad = db.Column(db.String(256))
    imagen = db.Column(db.String(128))
    fuente = db.Column(db.String(128))    

    def __repr__(self):
        return '<News {}>'.format(self.titulo)

class Linea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    descripcion = db.Column(db.String(256))
    imagen = db.Column(db.String(128))
    categoria = db.Column(db.String(128))    

    def __repr__(self):
        return '<Linea {}>'.format(self.nombre)

