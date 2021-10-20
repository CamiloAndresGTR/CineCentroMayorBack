from data.database import db, ma



class TipoUsuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(100))


    def __init__(self, descripcion):
        self.descripcion = descripcion

class TipoUsuarioSchema(ma.Schema):
    class Meta:
        fields=('id','descripcion')

tipoUsuario_schema = TipoUsuarioSchema()
tipoUsuarios_schema = TipoUsuarioSchema(many=True)