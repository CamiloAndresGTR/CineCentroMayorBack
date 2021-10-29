
from flask import Blueprint, request, jsonify

from data.database import db
from models.calificacion import Calificacion, calificacion_schema

routes_Calificaciones = Blueprint("routes_Calificaciones", __name__)
############################################################
##################### 4.CALIFICACION #######################
############################################################

# 1. Metodo para listar las calificaciones
@routes_Calificaciones.route('/calificaciones', methods=['GET'])
def getCalificaciones():
    all_calificaciones = Calificacion.query.all()
    result = calificacion_schema.dump(all_calificaciones)
    return jsonify(result)
