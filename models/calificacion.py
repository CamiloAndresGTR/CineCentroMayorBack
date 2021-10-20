from data.database import db, ma
from models.pelicula import Pelicula


class Calificacion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    comentario = db.Column(db.String(70), unique = True)
    valor = db.Column(db.Integer)
    id_pelicula = db.Column(db.Integer, db.ForeignKey(Pelicula.id))


    def __init__(self, comentario, valor,id_pelicula):
        self.comentario = comentario
        self.valor = valor
        self.id_pelicula = id_pelicula

class CalificacionSchema(ma.Schema):
    class Meta:
        fields=('id','comentario','valor','id_pelicula')

calificacion_schema = CalificacionSchema()
calificaciones_schema = CalificacionSchema(many=True)