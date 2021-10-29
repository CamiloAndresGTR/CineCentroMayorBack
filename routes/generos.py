from flask import Blueprint, request, jsonify

from data.database import db
from models.compras import Compras, compras_schema, comprass_schema
from models.genero import Genero, generos_schema

routes_Genero = Blueprint("routes_Genero", __name__)


########################################################
##################### 9.GENEROS ########################
########################################################

# 1. Metodo para listar las compras
@routes_Genero.route('/generos', methods=['GET'])
def getGeneros():
    generos = Genero.query.all()
    return jsonify(generos_schema.dump(generos))