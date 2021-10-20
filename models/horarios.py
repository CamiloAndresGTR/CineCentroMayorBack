from data.database import db, ma

class Horario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    horaInicio = db.Column(db.Time)
    horaFin = db.Column(db.Time)


    def __init__(self, horaInicio, horaFin):
        self.horaInicio = horaInicio
        self.horaFin = horaFin

class HorarioSchema(ma.Schema):
    class Meta:
        fields=('id','horaInicio','horaFin')

horario_schema = HorarioSchema()
horarios_schema = HorarioSchema(many=True)