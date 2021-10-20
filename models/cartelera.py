from data.database import db, ma
from models.horarios import Horario
from models.pelicula import Pelicula
from models.salas import Sala


class Cartelera(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    FechaInicio = db.Column(db.String(70), unique = True)
    FechaFin = db.Column(db.Integer)
    id_pelicula = db.Column(db.Integer, db.ForeignKey(Pelicula.id))
    id_horario = db.Column(db.Integer, db.ForeignKey(Horario.id))
    id_sala = db.Column(db.Integer, db.ForeignKey(Sala.id))


    def __init__(self, FechaInicio, FechaFin,id_pelicula,id_horario,id_sala):
        self.FechaInicio = FechaInicio
        self.FechaFin = FechaFin
        self.id_pelicula = id_pelicula
        self.id_horario = id_horario
        self.id_sala = id_sala

class CarteleraSchema(ma.Schema):
    class Meta:
        fields=('id','FechaInicio','FechaFin','id_pelicula','id_horario','id_sala')

cartelera_Schema = CarteleraSchema()
carteleras_Schema = CarteleraSchema(many=True)