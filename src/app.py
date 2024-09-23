from flask import Flask, render_template, request, jsonify, redirect, url_for
from config import config
from database import (
    verificar_conexion,
    obtener_grupos_constructivos,
    obtener_subgrupos,
    obtener_sistemas,
    obtener_equipos,
    buscar_equipos,
    buscar_subgrupos,
    buscar_sistemas,
    obtener_personal,
    obtener_tipos_equipos,
    insertar_procedimiento,
    insertar_diagrama,
    insertar_equipo_info,
    obtener_equipos_por_tipo
)
from __init__ import create_app

app = create_app()
app.config.from_object(config['development'])
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/check', methods=['GET'])
def check_db_connection():
    result, status_code = verificar_conexion()
    return jsonify(result), status_code

@app.route('/api/popup-data', methods=['GET'])
def obtener_datos_popup():
    return render_template('pop.html')

@app.route('/')
def index():
    grupos = obtener_grupos_constructivos()
    return render_template('index.html', grupos=grupos)

@app.route('/api/grupos', methods=['GET'])
def obtener_grupos_api():
    grupos = obtener_grupos_constructivos()
    return jsonify(grupos)

@app.route('/api/subgrupos/<int:id_grupo>', methods=['GET'])
def obtener_subgrupos_api(id_grupo):
    subgrupos = obtener_subgrupos(id_grupo)
    return jsonify(subgrupos)

@app.route('/api/sistemas/<int:id_subgrupo>', methods=['GET'])
def obtener_sistemas_api(id_subgrupo):
    sistemas = obtener_sistemas(id_subgrupo)
    return jsonify(sistemas)

@app.route('/api/equipos/<int:id_sistema>', methods=['GET'])
def obtener_equipos_api(id_sistema):
    equipos = obtener_equipos(id_sistema)
    return jsonify(equipos)

@app.route('/api/buscar_equipos', methods=['GET'])
def buscar_equipos_api():
    busqueda = request.args.get('busqueda', '')
    id_sistema = request.args.get('id_sistema', type=int)
    if busqueda:
        equipos = buscar_equipos(busqueda, id_sistema)
        return jsonify(equipos)
    return jsonify([])

@app.route('/api/buscar_subgrupos', methods=['GET'])
def buscar_subgrupos_api():
    busqueda = request.args.get('busqueda', '')
    id_grupo = request.args.get('id_grupo', type=int)
    if busqueda and id_grupo:
        subgrupos = buscar_subgrupos(busqueda, id_grupo)
        return jsonify(subgrupos)
    return jsonify([])

@app.route('/api/buscar_sistemas', methods=['GET'])
def buscar_sistemas_api():
    busqueda = request.args.get('busqueda', '')
    id_subgrupo = request.args.get('id_subgrupo', type=int)
    if busqueda and id_subgrupo:
        sistemas = buscar_sistemas(busqueda, id_subgrupo)
        return jsonify(sistemas)
    return jsonify([])

@app.route('/LSA/registro-generalidades', methods=['GET', 'POST'])
def registro_generalidades():
    if request.method == 'POST':
        # Extracción de datos del formulario
        fecha = request.form.get('fecha')
        nombre_equipo = request.form.get('nombre_equipo')
        responsable_id = request.form.get('responsable')
        grupo_constructivo_id = request.form.get('grupo_constructivo')
        subgrupo_constructivo_id = request.form.get('subgrupo_constructivo')
        sistema_id = request.form.get('sistema')
        tipo_equipo_id = request.form.get('tipo_equipo')
        equipo_id = request.form.get('equipo')
        aor = request.form.get('aor')
        mtbf = request.form.get('mtbf')
        gres_sistema = request.form.get('gres_sistema')
        fiabilidad_equipo = request.form.get('fiabilidad_equipo')
        criticidad_equipo = request.form.get('criticidad_equipo')
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        peso_seco = request.form.get('peso_seco')
        dimensiones = request.form.get('dimensiones')
        descripcion_equipo = request.form.get('descripcion_equipo')
        procedimiento_arranque = request.form.get('procedimiento_arranque')
        procedimiento_parada = request.form.get('procedimiento_parada')
        # Manejo de archivos
        imagen_equipo = request.files.get('imagen_equipo')
        diagrama_flujo = request.files.get('diagrama_flujo')
        diagrama_caja_negra = request.files.get('diagrama_caja_negra')
        diagrama_caja_transparente = request.files.get('diagrama_caja_transparente')
        # Insertar en la tabla procedimientos
        procedimiento_id = insertar_procedimiento(procedimiento_arranque, procedimiento_parada)
        # Insertar en la tabla diagramas
        diagrama_id = insertar_diagrama(diagrama_flujo, diagrama_caja_negra, diagrama_caja_transparente)
        # Insertar en la tabla equipo_info
        equipo_info_id = insertar_equipo_info(
            nombre_equipo, aor, fecha, fiabilidad_equipo, mtbf, gres_sistema, criticidad_equipo,
            marca, modelo, peso_seco, dimensiones, descripcion_equipo, imagen_equipo,
            responsable_id, diagrama_id, procedimiento_id, sistema_id, equipo_id, tipo_equipo_id,
            grupo_constructivo_id, subgrupo_constructivo_id
        )
        return redirect(url_for('index'))  # Redirige después de guardar
    else:
        grupos = obtener_grupos_constructivos()
        responsables = obtener_personal()
        tipos_equipos = obtener_tipos_equipos()
        return render_template('registro_generalidades.html', grupos=grupos, responsables=responsables, tipos_equipos=tipos_equipos)


@app.route('/api/equipos_por_tipo/<int:id_tipo_equipo>', methods=['GET'])
def obtener_equipos_por_tipo_api(id_tipo_equipo):
    equipos = obtener_equipos_por_tipo(id_tipo_equipo)
    return jsonify(equipos)

@app.route('/LSA/equipo/editar-analisis-funcional')
def editar_analisis_funcional():
    return render_template('editar_analisis_funcional.html')

@app.route('/LSA/equipo/editar-FMEA')
def editar_FMEA():
    return render_template('editar_FMEA.html')

@app.route('/LSA/equipo/editar-herramientas-especiales')
def editar_herramientas_especiales():
    return render_template('editar_herramientas-especiales.html')

@app.route('/LSA/equipo/editar-repuestos')
def editar_repuesto():
    return render_template('editar_repuesto.html')

@app.route('/LSA/equipo/editar-RCM')
def editar_RCM():
    return render_template('editar_RCM.html')

@app.route('/LSA/equipo/editar-MTA')
def editar_MTA():
    return render_template('editar_MTA.html')

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

@app.route('/LSA/registro-FMEA')
def registro_FMEA():
    return render_template('registro_FMEA.html')

@app.route('/LSA/equipo/registro-LORA')
def registro_lora():
    return render_template('registro_lora.html')

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








