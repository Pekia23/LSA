# src/__init__.py

from flask import Flask
from flask_mysqldb import MySQL

db = MySQL()

def create_app():
    app = Flask(__name__)

    # Configuraciones de la base de datos
    app.config.from_pyfile('config.py')

    # Inicializar la base de datos
    db.init_app(app)

    return app
