from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
from data.database import db, ma

from routes.auth import routes_auth
from routes.calificaciones import routes_Calificaciones
from routes.compras import routes_Compras
from routes.horarios import routes_Horarios
from routes.peliculas import routes_peliculas
from routes.tiposUsuario import routes_tipoUsuario
from routes.usuarios import routes_Usuarios

app = Flask(__name__)
CORS(app)
load_dotenv()
#Configuracion de la base de datos
USER_DB = 'admin'
PASS_DB = 'SISTEMAS.2021'
URL_DB = 'pruebasproduccion.ct3cxvrmhjjq.us-east-2.rds.amazonaws.com:3306'
NAME_DB = 'CineCentroMayor'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Inicializacion del objeto db de SQLAlchemy y ma de MarshMellow
db.init_app(app)
ma.init_app(app)

#migracion a la base de datos con flask-migrate
migrate = Migrate()
migrate.init_app(app, db)

app.register_blueprint(routes_auth)
app.register_blueprint(routes_peliculas)
app.register_blueprint(routes_tipoUsuario)
app.register_blueprint(routes_Usuarios)
app.register_blueprint(routes_Calificaciones)
app.register_blueprint(routes_Horarios)
app.register_blueprint(routes_Compras)
