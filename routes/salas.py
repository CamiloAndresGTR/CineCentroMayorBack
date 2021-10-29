
from flask import Blueprint, request, jsonify

from data.database import db
from models.salas import Sala, salas_schema, sala_schema

routes_Salas = Blueprint("routes_Salas", __name__)
############################################################
##################### 8.SALAS #######################
############################################################

# 1. Metodo para listar las salas

@routes_Salas.route('/salas', methods=['GET'])
def getSalas():
    all_Salas = Sala.query.all()
    result = salas_schema.dump(all_Salas)
    return jsonify(result)

# 2. Metodo para retornar una sala por id
@routes_Salas.route('/salas/<id>', methods=['GET'])
def getSala(id):
    sala = Sala.query.get(id)
    result = sala_schema.dump(sala)
    return jsonify(result)
