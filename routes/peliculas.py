from flask import Blueprint, request, jsonify

from data.database import db
from models.pelicula import Pelicula, pelicula_schema, peliculas_schema

routes_peliculas = Blueprint("routes_peliculas", __name__)


#########################################################
##################### 1. PELICULAS ######################
#########################################################
# 1. Metodo para crear una pelicula nueva y almacenarla en la base de datos
@routes_peliculas.route('/create-pelicula',methods=['POST'])
def create_pelicula():
    titulo = request.json['titulo']
    idioma = request.json['idioma']
    duracion = request.json['duracion']
    sinopsis = request.json['sinopsis']
    genero_id = request.json['genero_id']
    urlImagen = request.json['urlImagen']

    new_pelicula = Pelicula(titulo,idioma,duracion,sinopsis, genero_id, urlImagen)
    db.session.add(new_pelicula)
    db.session.commit()

    return pelicula_schema.jsonify(new_pelicula)

# 2. Metodo para listar todas las peliculas
@routes_peliculas.route('/peliculas', methods=['GET'])
def getPeliculas():
    all_peliculas = Pelicula.query.all()
    result = peliculas_schema.dump(all_peliculas)
    return jsonify(result)


# 3. Metodo para ver una pelicula por Id
@routes_peliculas.route('/peliculas/<id>', methods=['GET'])
def get_pelicula(id):
    pelicula = Pelicula.query.get(id)
    #Retorna un objeto json con el listado de peliculas
    return pelicula_schema.jsonify(pelicula)

# 4. Metodo para actualizar una pelicula
@routes_peliculas.route('/peliculas/<id>', methods=['PUT'])
def update_pelicula(id):
    pelicula = Pelicula.query.get(id)

    titulo = request.json['titulo']
    idioma = request.json['idioma']
    duracion = request.json['duracion']
    sinopsis = request.json['sinopsis']

    pelicula.titulo = titulo
    pelicula.idioma = idioma
    pelicula.duracion = duracion
    pelicula.sinopsis = sinopsis

    db.session.commit()
    return pelicula_schema.jsonify(pelicula)

# 5. metodo para eliminar una pelicula
@routes_peliculas.route('/peliculas/<id>', methods=['DELETE'])
def delete_pelicula(id):
    pelicula = Pelicula.query.get(id)
    db.session.delete(pelicula)
    db.session.commit()
    return pelicula_schema.jsonify(pelicula)
