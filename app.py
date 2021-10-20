from flask import Flask, jsonify, request

from flask_migrate import Migrate


#from Logic.horario import getHorarios
#from Logic.pelicula import getPeliculas
from data.database import db, ma
from models.pelicula import Pelicula, pelicula_schema , peliculas_schema
from models.tipoUsuario import TipoUsuario, tipoUsuario_schema, tipoUsuarios_schema
from models.usuario import Usuario, usuario_Schema, usuarios_Schema
from models.compras import Compras, compras_schema, comprass_schema
from models.cartelera import Cartelera, cartelera_Schema
from models.calificacion import Calificacion, calificacion_schema
from models.horarios import Horario, horarios_schema, horario_schema
from models.salas import Sala, salas_schema
from models.genero import Genero, genero_schema

app = Flask(__name__)

#Configuracion de la base de datos
USER_DB = 'root'
PASS_DB = ''
URL_DB = 'localhost'
NAME_DB = 'CineCentroMayor'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USER_DB}@{URL_DB}/{NAME_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Inicializacion del objeto db de SQLAlchemy y ma de MarshMellow

db.init_app(app)

ma.init_app(app)

#migracion a la base de datos con flask-migrate
migrate = Migrate()
migrate.init_app(app, db)
#########################################################
####################### PELICULAS #######################
#########################################################
#Metodo para crear una pelicula nueva
@app.route('/create-pelicula',methods=['POST'])
def create_pelicula():
    titulo = request.json['titulo']
    idioma = request.json['idioma']
    duracion = request.json['duracion']
    sinopsis = request.json['sinopsis']

    new_pelicula = Pelicula(titulo,idioma,duracion,sinopsis)
    db.session.add(new_pelicula)
    db.session.commit()

    return pelicula_schema.jsonify(new_pelicula)

#Metodo para listar todas las peliculas
@app.route('/peliculas', methods=['GET'])
def getPeliculas():
    all_peliculas = Pelicula.query.all()
    result = peliculas_schema.dump(all_peliculas)
    return jsonify(result)


#Metodo para ver una pelicula por Id
@app.route('/peliculas/<id>', methods=['GET'])
def get_pelicula(id):
    pelicula = Pelicula.query.get(id)
    #Retorna un objeto json con el listado de peliculas
    return pelicula_schema.jsonify(pelicula)

#Metodo para actualizar una pelicula
@app.route('/pelicula/<id>', methods=['PUT'])
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

#metodo para eliminar una pelicula
@app.route('/pelicula/<id>', methods=['DELETE'])
def delete_pelicula(id):
    pelicula = Pelicula.query.get(id)
    db.session.delete(pelicula)
    db.session.commit()
    return pelicula_schema.jsonify(pelicula)

################################################################
####################### TIPOS DE USUARIO #######################
################################################################
#Metodo para crear Tipos de usuaio
@app.route('/create-tipoUsuario',methods=['POST'])
def createTipoUsuario():
    descripcion = request.json['descripcion']

    new_TipoUsuario = TipoUsuario(descripcion)
    db.session.add(new_TipoUsuario)
    db.session.commit()

    return tipoUsuario_schema.jsonify(new_TipoUsuario)



#Metodo para listar los tipos de usuario
@app.route('/tiposUsuario', methods=['GET'])
def getTiposUsuario():
    all_tipoUsuario = TipoUsuario.query.all()
    result = tipoUsuarios_schema.dump(all_tipoUsuario)
    return jsonify(result)

#Metodo para ver un TipoUsuario por id
@app.route('/tiposUsuario/<id>', methods=['GET'])
def getTipoUsuario(id):
    tipoUsuario = TipoUsuario.query.get(id)

    return tipoUsuario_schema.jsonify(tipoUsuario)

#Metodo para actualizar un TipoUsuario
@app.route('/tiposUsuario/<id>', methods=['PUT'])
def updateTipoUsuario(id):
    tipoUsuario = TipoUsuario.query.get(id)

    descripcion = request.json['descripcion']

    TipoUsuario.descripcion = descripcion

    db.session.commit()
    return tipoUsuario_schema.jsonify(tipoUsuario)

#metodo para eliminar un TipoUsuario
@app.route('/tiposUsuario/<id>', methods=['DELETE'])
def deleteTipoUsuario(id):
    tipoUsuario = TipoUsuario.query.get(id)
    db.session.delete(tipoUsuario)
    db.session.commit()
    return tipoUsuario_schema.jsonify(tipoUsuario)


########################################################
####################### USUARIOS #######################
########################################################

#Metodo para crear usuaios
@app.route('/create-usuario',methods=['POST'])
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

#Metodo para listar los usuarios
@app.route('/usuarios', methods=['GET'])
def getUsuarios():
    all_Usuarios = Usuario.query.all()
    result = usuarios_Schema.dump(all_Usuarios)
    return jsonify(result)

#Metodo para ver un Usuario por id
@app.route('/Usuarios/<id>', methods=['GET'])
def getUsuario(id):
    usuario = Usuario.query.get(id)

    return usuario_Schema.jsonify(usuario)


#Metodo para actualizar un TipoUsuario
@app.route('/usuarios/<id>', methods=['PUT'])
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

#metodo para eliminar un Usuario
@app.route('/usuarios/<id>', methods=['DELETE'])
def deleteUsuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return usuario_Schema.jsonify(usuario)



############################################################
####################### CALIFICACION #######################
############################################################

#Metodo para listar las calificaciones
@app.route('/calificaciones', methods=['GET'])
def getCalificaciones():
    all_calificaciones = Calificacion.query.all()
    result = calificacion_schema.dump(all_calificaciones)
    return jsonify(result)



########################################################
####################### HORARIOS #######################
########################################################

#Metodo para listar los tipos de usuario
@app.route('/horarios', methods=['GET'])
def getHorarios():
    horarios = Horario.query.all()
    result = horarios_schema.dump(horarios)
    return jsonify(result)

#Metodo para mostrar un horario por id
@app.route('/horarios/<id>', methods=['GET'])
def getHorario(id):
    horario = Horario.query.get(id)
    return horario_schema.jsonify(horario)

#Metodo para actualizar un horario
@app.route('/horarios/<id>', methods=['PUT'])
def updateHorario(id):
    horario = Horario.query.get(id)
    horaInicio = request.json['horaInicio']
    horaFin = request.json['horaFin']

    horario.horaInicio = horaInicio
    horario.horaFin = horaFin

    db.session.commit()
    return horario_schema.jsonify(horario)

#Metodo para eliminar un horario
@app.route('/horarios/<id>', methods=['DELETE'])
def deleteHorario(id):
    horario = Horario.query.get(id)
    db.session.delete(horario)
    db.session.commit()
    return horario_schema.jsonify(horario)



########################################################
####################### COMPRAS ########################
########################################################

#Metodo para crear / registrar una nueva compra
@app.route('/compras', methods=['POST'])
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

#Metodo para listar las compras
@app.route('/compras', methods=['GET'])
def getCompras():
    compras = Compras.query.all()
    return jsonify(comprass_schema.dump(compras))

#Metodo para mostrar una compra por id
@app.route('/compras/<id>', methods=['GET'])
def getCompra(id):
    compra = Compras.query.get(id)
    return compras_schema.jsonify(compra)

