import MySQLdb
from flask import Flask, redirect, render_template, request,jsonify, url_for
from flask_mysqldb import MySQL
from config import config
from flask import Flask, jsonify


app = Flask(__name__)
db = MySQL(app)
app.config.from_object(config['development'])

@app.route('/check', methods=['GET'])
def check_db_connection():
    try:
        # Crear un cursor para realizar la consulta
        cursor = db.connection.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        return jsonify({"status": "success", "message": "Database connection successful"}), 200
    except MySQLdb.Error as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/', endpoint ='inicio')
def home():
    return render_template('index.html')

@app.route('/LSA', methods=['POST','GET'])
def lsa():
    searchbox = request.form.get("text")
    cursor = db.connection.cursor()
    query = "SELECT nombre_equipo FROM equipo_info WHERE nombre_equipo LIKE '{}%' ORDER BY nombre_equipo".format(searchbox)
    cursor.execute(query)
    result = cursor.fetchall()
    return redirect(url_for('inicio'))

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
def mostrar_analisis_herramientass():
    return render_template('mostrar_analisis-herramientas.html')

@app.route('/LSA/equipo/mostrar-repuestos')
def mostrar_repuesto():
    return render_template('mostrar_repuesto.html')

@app.route('/LSA/registro-MTA-2')
def registro_MTA_2():
    return render_template('registro_MTA_2.html')

@app.route('/LSA/registro-MTA')
def registro_MTA():
    return render_template('registro_MTA.html')

@app.route('/LSA/registro-RCM-2')
def registro_RCM_2():
    return render_template('registro_RCM_2.html')

@app.route('/LSA/registro-RCM')
def registro_RCM():
    return render_template('registro_RCM.html')

@app.route('/LSA/registro-generalidades')
def registro_generalidades():
    return render_template('registro_generalidades.html')

@app.route('/LSA/registro-FMEA')
def registro_FMEA():
    return render_template('registro_FMEA.html')

@app.route('/LSA/registro-FMEA-2')
def registro_FMEA_2():
    return render_template('registro-FMEA_2.html')

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








