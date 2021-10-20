from data.database import db, ma

class Genero(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(70), unique = True)
    descripcion = db.Column(db.String(100))


    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

class GeneroSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','descripcion')

genero_schema = GeneroSchema()
generos_schema = GeneroSchema(many=True)