import MySQLdb
from flask import Flask, render_template, request,jsonify
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/LSA', methods=['POST','GET'])
def lsa():
    searchbox = request.form.get("text")
    cursor = db.connection.cursor()
    query = "SELECT nombre_equipo FROM equipo_info WHERE nombre_equipo LIKE '{}%' ORDER BY nombre_equipo".format(searchbox)
    cursor.execute(query)
    result = cursor.fetchall()
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

@app.route('/LSA/equipo/analisis-funcional')
def analisis_funcional():
    return render_template('mostrar_analisis-funcional.html')

@app.route('/LSA/equipo/herramientas-especiales')
def herramientas_especiales():
    return render_template('mostrar_herramientas-especiales.html')

@app.route('/LSA/equipo/analisis-herramientas')
def analisis_herramientas():
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

@app.route('/LSA/ingresar-FMEA')
def ingresarFMEA():
    return render_template('ingresar_FMEA.html')

@app.route('/LSA/fmea-form-2')
def fmea_form_2():
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








