from flask import Blueprint, request, jsonify
from function_jwt import write_token

from models.usuario import Usuario

routes_auth = Blueprint("routes_auth", __name__)

@routes_auth.route("/login",methods=["POST"])
def login():
    data = request.get_json()
    nombreUsuario = data["username"]
    user = Usuario.query.filter_by(nombreUsuario = nombreUsuario).first()

    if data['username'] == user.nombreUsuario and data['password'] == user.password:
        return write_token(data = request.get_json())
    else:
        response = jsonify({"message": "User not found"})
        response.status_code = 404
        return response
