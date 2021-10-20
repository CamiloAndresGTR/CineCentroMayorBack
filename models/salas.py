from data.database import db, ma

class Sala(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cantidadSillas = db.Column(db.Integer)
    estado = db.Column(db.Boolean)


    def __init__(self, cantidadSillas, estado):
        self.cantidadSillas = cantidadSillas
        self.estado = estado

class SalaSchema(ma.Schema):
    class Meta:
        fields=('id','cantidadSillas','estado')

sala_schema = SalaSchema()
salas_schema = SalaSchema(many=True)