
# Si actualizamos la tabla o clase modelo usar los siguientes comandos:
# flask db stamp head
# flask db migrate
# flask db upgrade
from app import db
from data.database import ma

# Inicio clases Modelo con su respectivo constructor
from models.genero import Genero


class Pelicula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(70), unique=True)
    idioma = db.Column(db.String(100))
    duracion = db.Column(db.Time)
    genero_id = db.Column(db.Integer, db.ForeignKey(Genero.id))
    sinopsis = db.Column(db.String(500))

    def __init__(self, titulo, idioma, duracion, sinopsis):
        self.titulo = titulo
        self.idioma = idioma
        self.duracion = duracion
        self.sinopsis = sinopsis

# Fin clases Modelo

#Schema
class PeliculaSchema(ma.Schema):
    class Meta:
        fields=('id','titulo', 'idioma','duracion','sinopsis')

pelicula_schema = PeliculaSchema()
peliculas_schema = PeliculaSchema(many=True)