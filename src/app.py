
from flask import Flask, render_template, request,jsonify, redirect, url_for
from database import buscar_equipos 
from config import config
from flask import Flask, jsonify
from database import verificar_conexion
from __init__ import create_app

app = create_app()
app = Flask(__name__)

app.config.from_object(config['development'])

@app.route('/check', methods=['GET'])
def check_db_connection():
    # Llamar a la función que verifica la conexión a la base de datos
    result, status_code = verificar_conexion()
    return jsonify(result), status_code

@app.route('/', endpoint ='inicio')
def home():
    return render_template('index.html')

@app.route('/LSA', methods=['POST', 'GET'])
def lsa():
    searchbox = request.form.get("text")

    result = buscar_equipos(searchbox)  # Llama a la función que está en database.py
    return jsonify(result)


@app.route('/LSA/equipo/editar-analisis-funcional')
def editar_analisis_funcional():
    return render_template('editar_analisis_funcional.html')

@app.route('/LSA/equipo/editar-FMEA')
def editar_FMEA():
    return render_template('editar_FMEA.html')

@app.route('/LSA/equipo/editar-herramientas-especiales')
def editar_herramientas_especiales():
    return render_template('editar_herramientas-especiales.html')


@app.route('/LSA/mostrar-equipo')
def mostrar_equipo():
    return render_template('mostrar_equipo.html')

@app.route('/LSA/equipo/mostrar-FMEA')
def mostrar_FMEA():
    return render_template('mostrar_FMEA.html')

@app.route('/LSA/equipo/mostrar-MTA')
def mostrar_MTA():
    return render_template('mostrar_MTA.html')

@app.route('/LSA/equipo/mostrar-RCM')
def mostrar_RCM():
    return render_template('mostrar_RCM.html')

@app.route('/LSA/equipo/mostrar-LORA')
def mostrar_lora():
    return render_template('mostrar_lora.html')

@app.route('/LSA/equipo/mostrar-analisis-funcional')
def mostrar_analisis_funcional():
    return render_template('mostrar_analisis-funcional.html')

@app.route('/LSA/equipo/mostrar-herramientas-especiales')
def mostrar_herramientas_especiales():
    return render_template('mostrar_herramientas-especiales.html')

@app.route('/LSA/equipo/mostrar-analisis-herramientas')
def mostrar_analisis_herramientas():
    return render_template('mostrar_analisis-herramientas.html')

@app.route('/LSA/equipo/mostrar-repuestos')
def mostrar_repuesto():
    return render_template('mostrar_repuesto.html')

@app.route('/LSA/registro-MTA')
def registro_MTA():
    return render_template('registro_MTA.html')

@app.route('/LSA/registro-RCM')
def registro_RCM():
    return render_template('registro_RCM.html')

@app.route('/LSA/registro-generalidades')
def registro_generalidades():
    return render_template('registro_generalidades.html')

@app.route('/LSA/registro-FMEA')
def registro_FMEA():
    return render_template('registro_FMEA.html')

@app.route('/LSA/registro-analisis-funcional')
def registro_analisis_funcional():
    return render_template('registro_analisis_funcional.html')

@app.route('/LSA/registro-herramientas-especiales')
def registro_herramientas_especiales():
    return render_template('registro_herramientas_especiales.html')


@app.route('/LSA/registro-repuesto')
def registro_repuesto():
    return render_template('registro_repuesto.html')



if __name__ == '__main__':
    app.run()








