from flask import Blueprint, request, jsonify

from data.database import db

routes_tipoUsuario = Blueprint("routes_tipoUsuario", __name__)

################################################################
###################### 2. TIPOS DE USUARIO #####################
################################################################
# 1. Metodo para crear Tipos de usuaio
from models.tipoUsuario import TipoUsuario, tipoUsuario_schema, tipoUsuarios_schema


@routes_tipoUsuario.route('/create-tipoUsuario',methods=['POST'])
def createTipoUsuario():
    descripcion = request.json['descripcion']

    new_TipoUsuario = TipoUsuario(descripcion)
    db.session.add(new_TipoUsuario)
    db.session.commit()

    return tipoUsuario_schema.jsonify(new_TipoUsuario)



# 2. Metodo para listar los tipos de usuario
@routes_tipoUsuario.route('/tiposUsuario', methods=['GET'])
def getTiposUsuario():
    all_tipoUsuario = TipoUsuario.query.all()
    result = tipoUsuarios_schema.dump(all_tipoUsuario)
    return jsonify(result)

# 3. Metodo para ver un TipoUsuario por id
@routes_tipoUsuario.route('/tiposUsuario/<id>', methods=['GET'])
def getTipoUsuario(id):
    tipoUsuario = TipoUsuario.query.get(id)

    return tipoUsuario_schema.jsonify(tipoUsuario)

# 4. Metodo para actualizar un TipoUsuario
@routes_tipoUsuario.route('/tiposUsuario/<id>', methods=['PUT'])
def updateTipoUsuario(id):
    tipoUsuario = TipoUsuario.query.get(id)

    descripcion = request.json['descripcion']

    TipoUsuario.descripcion = descripcion

    db.session.commit()
    return tipoUsuario_schema.jsonify(tipoUsuario)

# 5. Metodo para eliminar un TipoUsuario
@routes_tipoUsuario.route('/tiposUsuario/<id>', methods=['DELETE'])
def deleteTipoUsuario(id):
    tipoUsuario = TipoUsuario.query.get(id)
    db.session.delete(tipoUsuario)
    db.session.commit()
    return tipoUsuario_schema.jsonify(tipoUsuario)

