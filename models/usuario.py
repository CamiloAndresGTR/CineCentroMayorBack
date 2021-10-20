from data.database import db, ma

from models.tipoUsuario import TipoUsuario


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tipoId = db.Column(db.String(30))
    numeroId = db.Column(db.Integer, unique = True)
    nombres = db.Column(db.String(100))
    apellidos = db.Column(db.String(100))
    email = db.Column(db.String(100))
    nombreUsuario = db.Column(db.String(100))
    password = db.Column(db.String(20))
    estado = db.Column(db.Boolean)
    idTipoUsuario = db.Column(db.Integer, db.ForeignKey(TipoUsuario.id))


    def __init__(self, tipoId, numeroId, nombres, apellidos,email, nombreUsuario, password, estado, idTipoUsuario):
        self.tipoId = tipoId
        self.numeroId = numeroId
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.nombreUsuario = nombreUsuario
        self.password = password
        self.estado = estado
        self.idTipoUsuario = idTipoUsuario

class UsuarioSchema(ma.Schema):
    class Meta:
        fields=('id', 'tipoId', 'numeroId', 'nombres', 'apellidos', 'email','nombreUsuario', 'password', 'estado', 'idTipoUsuario')

usuario_Schema = UsuarioSchema()
usuarios_Schema = UsuarioSchema(many=True)