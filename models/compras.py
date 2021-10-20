from data.database import db, ma
from models.pelicula import Pelicula
from models.usuario import Usuario


class Compras(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    sillas = db.Column(db.Integer, unique = True)
    valorUnitario = db.Column(db.Integer)
    valorTotal = db.Column(db.Integer)
    id_pelicula = db.Column(db.Integer, db.ForeignKey(Pelicula.id))
    id_usuario = db.Column(db.Integer, db.ForeignKey(Usuario.id))


    def __init__(self, sillas, valorUnitario,valorTotal,id_pelicula,id_usuario):
        self.sillas = sillas
        self.valorUnitario = valorUnitario
        self.valorTotal = valorTotal
        self.id_pelicula = id_pelicula
        self.id_usuario = id_usuario

class ComprasSchema(ma.Schema):
    class Meta:
        fields=('id','sillas','valor','id_pelicula','id_usuario')

compras_schema = ComprasSchema()
comprass_schema = ComprasSchema(many=True)