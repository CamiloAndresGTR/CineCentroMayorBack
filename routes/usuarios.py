from flask import Blueprint, request, jsonify
from models.usuario import Usuario, usuario_Schema, usuarios_Schema
from data.database import db

routes_Usuarios = Blueprint("routes_Usuarios", __name__)
########################################################
##################### 3.USUARIOS #######################
########################################################

# 1. Metodo para crear usuaios

@routes_Usuarios.route('/create-usuario',methods=['POST'])
def createUsuario():
    # 'id', 'tipoId', 'numeroId', 'nombres', 'apellidos', 'nombreUsuario', 'password', 'estado', 'idTipoUsuario'
    tipoId = request.json['tipoId']
    numeroId = request.json['numeroId']
    nombres = request.json['nombres']
    apellidos = request.json['apellidos']
    email = request.json['email']
    nombreUsuario = request.json['nombreUsuario']
    password = request.json['password']
    estado = request.json['estado']
    idTipoUsuario = request.json['idTipoUsuario']

    new_Usuario = Usuario(tipoId, numeroId, nombres, apellidos,email, nombreUsuario, password, estado, idTipoUsuario)
    db.session.add(new_Usuario)
    db.session.commit()

    return usuario_Schema.jsonify(new_Usuario)

# 2. Metodo para listar los usuarios
@routes_Usuarios.route('/usuarios', methods=['GET'])
def getUsuarios():
    all_Usuarios = Usuario.query.all()
    result = usuarios_Schema.dump(all_Usuarios)
    return jsonify(result)

# 3.Metodo para ver un Usuario por id
@routes_Usuarios.route('/usuarios/<id>', methods=['GET'])
def getUsuario(id):
    usuario = Usuario.query.get(id)

    return usuario_Schema.jsonify(usuario)


# 4. Metodo para actualizar un usuario
@routes_Usuarios.route('/usuarios/<id>', methods=['PUT'])
def updateUsuario(id):
    usuario = Usuario.query.get(id)

    tipoId = request.json['tipoId']
    numeroId = request.json['numeroId']
    nombres = request.json['nombres']
    apellidos = request.json['apellidos']
    email = request.json['email']
    nombreUsuario = request.json['nombreUsuario']
    password = request.json['password']
    estado = request.json['estado']
    idTipoUsuario = request.json['idTipoUsuario']

    usuario.tipoId = tipoId
    usuario.numeroId = numeroId
    usuario.nombres = nombres
    usuario.apellidos = apellidos
    usuario.email = email
    usuario.nombreUsuario = nombreUsuario
    usuario.password = password
    usuario.estado = estado
    usuario.idTipoUsuario = idTipoUsuario

    db.session.commit()
    return usuario_Schema.jsonify(usuario)

# 5. metodo para eliminar un Usuario
@routes_Usuarios.route('/usuarios/<id>', methods=['DELETE'])
def deleteUsuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return usuario_Schema.jsonify(usuario)

