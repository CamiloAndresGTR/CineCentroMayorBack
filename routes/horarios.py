from flask import Blueprint, request, jsonify

from data.database import db
from models.horarios import Horario, horarios_schema, horario_schema

routes_Horarios = Blueprint("routes_Horarios", __name__)

########################################################
##################### 5.HORARIOS #######################
########################################################

# 1. Metodo para listar los tipos de usuario
@routes_Horarios.route('/horarios', methods=['GET'])
def getHorarios():
    horarios = Horario.query.all()
    result = horarios_schema.dump(horarios)
    return jsonify(result)

# 2. Metodo para mostrar un horario por id
@routes_Horarios.route('/horarios/<id>', methods=['GET'])
def getHorario(id):
    horario = Horario.query.get(id)
    return horario_schema.jsonify(horario)

# 3. Metodo para actualizar un horario
@routes_Horarios.route('/horarios/<id>', methods=['PUT'])
def updateHorario(id):
    horario = Horario.query.get(id)
    horaInicio = request.json['horaInicio']
    horaFin = request.json['horaFin']

    horario.horaInicio = horaInicio
    horario.horaFin = horaFin

    db.session.commit()
    return horario_schema.jsonify(horario)

# 4. Metodo para eliminar un horario
@routes_Horarios.route('/horarios/<id>', methods=['DELETE'])
def deleteHorario(id):
    horario = Horario.query.get(id)
    db.session.delete(horario)
    db.session.commit()
    return horario_schema.jsonify(horario)
