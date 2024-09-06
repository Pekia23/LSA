
from flask import Flask, render_template, request,jsonify
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/LSA', methods=['POST', 'GET'])
def lsa():
    searchbox = request.form.get("text")
    result = buscar_equipos(searchbox)  # Llama a la función que está en database.py
    return jsonify(result)

@app.route('/LSA/equipo-nuevo', methods=['POST','GET'])
def equipo_nuevo():
    return render_template('equipo_nuevo.html')

@app.route('/LSA/equipo')
def mostrar_equipo():
    return render_template('mostrar_equipo.html')

@app.route('/LSA/equipo/FMEA')
def fmea():
    return render_template('mostrar_FMEA.html')

@app.route('/LSA/equipo/MTA')
def mta():
    return render_template('mostrar_MTA.html')

@app.route('/LSA/equipo/RCM')
def rcm():
    return render_template('mostrar_RCM.html')

@app.route('/LSA/equipo/LORA')
def lora():
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

@app.route('/LSA/equipo/repuestos')
def repuestos():
    return render_template('mostrar_repuesto.html')

@app.route('/LSA/prueba')
def prueba():
    return render_template('prueba.html')


@app.route('/LSA/registro-mta-2')
def registro_mta_2():
    return render_template('registro_mta_2.html')

@app.route('/LSA/registro-mta')
def registro_mta():
    return render_template('registro_mta.html')

@app.route('/LSA/registro-rcm-2')
def registro_rcm_2():
    return render_template('registro_rcm_2.html')

@app.route('/LSA/registro-rcm')
def registro_rcm():
    return render_template('registro_rcm.html')

@app.route('/LSA/generalidades')
def generalidades():
    return render_template('generalidades.html')

@app.route('/LSA/ingresar-fmea')
def ingresarFMEA():
    return render_template('ingresar_FMEA.html')

@app.route('/LSA/ingresar-fmea-2')
def ingresar_fmea_2():
    return render_template('fmea-form-2.html')

@app.route('/LSA/analisis-funcional')
def analisis_funcional():
    return render_template('analisis_funcional.html')

@app.route('/LSA/herramientas-especiales')
def herramientas_especiales():
    return render_template('herramientas_especiales.html')

@app.route('/LSA/repuesto')
def repuesto():
    return render_template('repuesto.html')



if __name__ == '__main__':
    app.run()








