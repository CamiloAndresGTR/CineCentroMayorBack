from flask import Blueprint, request, jsonify

from data.database import db
from models.compras import Compras, compras_schema, comprass_schema

routes_Compras = Blueprint("routes_Compras", __name__)


########################################################
##################### 6.COMPRAS ########################
########################################################

# 1. Metodo para crear / registrar una nueva compra
@routes_Compras.route('/compras', methods=['POST'])
def createBuy():
    sillas = request.json['sillas']
    valorUnitario = request.json['numeroId']
    valorTotal = sillas * valorUnitario ##################### REVISAR
    id_pelicula = request.json['id_pelicula']
    id_usuario = request.json['id_usuario']

    new_compra = Compras(sillas, valorUnitario, valorTotal, id_pelicula, id_usuario)
    db.session.add(new_compra)
    db.session.commit()
    return compras_schema.jsonify(new_compra)

# 2. Metodo para listar las compras
@routes_Compras.route('/compras', methods=['GET'])
def getCompras():
    compras = Compras.query.all()
    return jsonify(comprass_schema.dump(compras))

# 3. Metodo para mostrar una compra por id
@routes_Compras.route('/compras/<id>', methods=['GET'])
def getCompra(id):
    compra = Compras.query.get(id)
    return compras_schema.jsonify(compra)