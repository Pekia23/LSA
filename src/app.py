
from flask import Flask,session,flash, render_template, request, jsonify, redirect, url_for, make_response, g, send_file

from markupsafe import Markup

import uuid
import MySQLdb.cursors
import uuid  # Para generar un token único
from __init__ import db

from config import config
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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
    obtener_equipos_por_tipo,
    obtener_sistema_por_id, 
    obtener_subsistemas_por_equipo, 
    insertar_analisis_funcional,
    obtener_usuario_por_correo,
    insertar_repuesto,
    eliminar_repuesto,
    actualizar_repuesto,


    obtener_repuestos_por_equipo_info,
    obtener_repuesto_por_id,
    obtener_herramientas_especiales_por_equipo,
    obtener_tipos_herramientas,
    insertar_analisis_herramienta,
    obtener_analisis_herramientas_por_equipo,
    insertar_herramienta_requerida,
    insertar_herramienta_especial,
    



    insertar_fmea,
    obtener_subsistema_por_id,
    insertar_falla_funcional,
    insertar_descripcion_modo_falla,
    insertar_causa,
    

    #Obtener para desplegables FMEA
    obtener_componentes_por_subsistema,
    obtener_mecanismos_falla,
    obtener_codigos_modo_falla,
    obtener_metodos_deteccion_falla,
    obtener_fallos_ocultos,
    obtener_seguridad_fisica,
    obtener_impacto_operacional,
    obtener_medio_ambiente,
    obtener_costos_reparacion,
    obtener_flexibilidad_operacional,
    obtener_Ocurrencia,
    obtener_probablilidad_deteccion,

    obtener_fmeas,
    obtener_fmea_por_id,
    actualizar_fmea,
    obtener_id_equipo_info_por_fmea,
    obtener_id_sistema_por_fmea_id,
    obtener_id_subsistema_por_componente_id,
    obtener_id_componente_por_fmea_id,
    obtener_ID_FMEA,
    obtener_lista_riesgos,

    eliminar_herramienta_especial,
    actualizar_herramienta_especial,
    obtener_herramienta_especial_por_id,
    eliminar_analisis_herramienta,
    actualizar_analisis_herramienta,
    obtener_analisis_herramienta_por_id,
    actualizar_equipo_info,
    obtener_equipo_info_por_id,

    
    obtener_diagramas_por_id,
    obtener_responsables,
    eliminar_equipo_info,


    

    #MTA
    insertar_mta,
    obtener_nombre_componente_por_id,
    obtener_tipos_mantenimiento,
    obtener_tareas_mantenimiento,

    obtener_subsistema_por_id,
    obtener_procedimiento_por_id,
    obtener_personal_por_id,
    obtener_tipo_equipo_por_id,
    obtener_grupo_constructivo_por_sistema_id,
    obtener_datos_equipo_por_id,
    obtener_subgrupo_constructivo_por_sistema_id,

    ##analisis funcional

    obtener_analisis_funcionales_por_equipo_info,
    obtener_analisis_funcional_por_id,
    actualizar_analisis_funcional,
    eliminar_analisis_funcional,
    insertar_analisis_funcional,
    obtener_subsistemas_por_equipo,
    obtener_nombre_sistema_por_id,
    obtener_subsistemas_por_equipo_mostrar,





    #RCM
    insertar_rcm,
    obtener_rcm_por_fmea,
    obtener_rcms_completos,
    obtener_fmeas_con_rcm,
    eliminar_rcm,
    actualizar_rcm,

    obtener_lista_acciones_recomendadas

)

from __init__ import create_app


app = Flask(__name__)
app = create_app()
app.config.from_object(config['development'])
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = 'tu_clave_secreta'
app.config['SECRET_KEY'] = 'tu_clave_secreta_aquí'



@app.route('/check', methods=['GET'])
def check_db_connection():
    result, status_code = verificar_conexion()
    return jsonify(result), status_code

@app.route('/api/popup-data', methods=['GET'])
def obtener_datos_popup():
    return render_template('pop.html')

@app.route('/LSA')
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
def registro_generalidades(id_sistema=None, id_equipo=None):
    token = g.user_token
    if request.method == 'POST':
        # Extracción de datos del formulario
        fecha = request.form.get('fecha')
        nombre_equipo = request.form.get('nombre_equipo')
        id_personal = request.form.get('responsable')
        id_sistema = request.form.get('sistema')
        id_equipo = request.form.get('equipo')
        AOR = request.form.get('aor')
        MTBF = request.form.get('mtbf')
        GRES = request.form.get('gres_sistema')
        fiabilidad_equipo = request.form.get('fiabilidad_equipo')
        criticidad_equipo = request.form.get('criticidad_equipo')
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        peso_seco = request.form.get('peso_seco')
        dimensiones = request.form.get('dimensiones')
        descripcion = request.form.get('descripcion_equipo')
        procedimiento_arranque = request.form.get('procedimiento_arranque')
        procedimiento_parada = request.form.get('procedimiento_parada')

        # Manejo de archivos
        imagen_file = request.files.get('imagen_equipo')
        if imagen_file and imagen_file.filename != '':
            imagen = imagen_file.read()
        else:
            imagen = None

        diagrama_flujo_file = request.files.get('diagrama_flujo')
        if diagrama_flujo_file and diagrama_flujo_file.filename != '':
            diagrama_flujo = diagrama_flujo_file.read()
        else:
            diagrama_flujo = None

        diagrama_caja_negra_file = request.files.get('diagrama_caja_negra')
        if diagrama_caja_negra_file and diagrama_caja_negra_file.filename != '':
            diagrama_caja_negra = diagrama_caja_negra_file.read()
        else:
            diagrama_caja_negra = None

        diagrama_caja_transparente_file = request.files.get('diagrama_caja_transparente')
        if diagrama_caja_transparente_file and diagrama_caja_transparente_file.filename != '':
            diagrama_caja_transparente = diagrama_caja_transparente_file.read()
        else:
            diagrama_caja_transparente = None

        # Insertar en la tabla procedimientos
        id_procedimiento = insertar_procedimiento(procedimiento_arranque, procedimiento_parada)

        # Insertar en la tabla diagramas
        id_diagrama = insertar_diagrama(diagrama_flujo, diagrama_caja_negra, diagrama_caja_transparente)

        print(f"Nombre del tipo de equipo recibido: {id_equipo}")

        # Insertar en la tabla equipo_info
        equipo_info_id = insertar_equipo_info(
            nombre_equipo, AOR, fecha, fiabilidad_equipo, MTBF, GRES, criticidad_equipo,
            marca, modelo, peso_seco, dimensiones, descripcion, imagen,
            id_personal, id_diagrama, id_procedimiento, id_sistema, id_equipo
        )

        guardar_info_usuario(
            token,
            id_sistema=id_sistema,
            id_equipo=id_equipo,
            id_equipo_info=equipo_info_id,
            usuario_id=g.usuario_id

        )

        return redirect(url_for('registro_analisis_funcional'))
    else:
        grupos = obtener_grupos_constructivos()
        responsables = obtener_personal()
        tipos_equipos = obtener_tipos_equipos()

        return render_template('registro_generalidades.html', grupos=grupos, responsables=responsables, tipos_equipos=tipos_equipos)



##################################################################################################################3















###########################################################################################################

@app.route('/api/equipos_por_tipo/<int:id_tipo_equipo>', methods=['GET'])
def obtener_equipos_por_tipo_api(id_tipo_equipo):
    equipospro = obtener_equipos_por_tipo(id_tipo_equipo)
    return jsonify(equipospro)


@app.route('/LSA/registro-analisis-funcional', methods=['GET', 'POST'])
def registro_analisis_funcional():
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_sistema = user_data.get('id_sistema')
    id_equipo = user_data.get('id_equipo')
    id_equipo_info = user_data.get('id_equipo_info')

    # Agregar prints para depuración
    print(f"Token: {token}")
    print(f"id_sistema: {id_sistema}")
    print(f"id_equipo: {id_equipo}")
    print(f"id_equipo_info: {id_equipo_info}")
    # Si no se proporciona id_sistema, sistema es None
    if id_sistema is None:
        sistema = None
        subsistemas = []
    else:
        # Obtener información del sistema
        sistema = obtener_sistema_por_id(id_sistema)
        
        # Verificar si el sistema existe
        if sistema:
            if id_equipo:
                subsistemas = obtener_subsistemas_por_equipo(id_equipo)
            else:
                subsistemas = []
        else:
            # Si no se encuentra el sistema, no hay subsistemas
            subsistemas = []        

    # Renderizar la plantilla con los datos obtenidos
    return render_template('registro_analisis_funcional.html', sistema=sistema,subsistemas=subsistemas)

@app.route('/api/analisis-funcional', methods=['POST'])
def api_analisis_funcional():
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')
    subsistema_id = user_data.get('subsistema_id')


    data = request.get_json()
    sistema_id = data.get('sistema')
    subsistema_id = data.get('subsistema')
    verbo = data.get('verbo')
    accion = data.get('accion')
    estandar_desempeño = data.get('estandar_desempeño')



    print('Datos recibidos:', data)
    print('id_equipo_info:', id_equipo_info)
    print('subsistema_id:', subsistema_id)
    print('verbo:', verbo)
    print('accion:', accion)
    print('estandar_desempeño:', estandar_desempeño)
    # Guardar subsistema_id en la sesión de Flask
    session['subsistema_id'] = subsistema_id

    
    # Validar los datos recibidos (puedes agregar más validaciones)
    if not sistema_id or not subsistema_id or not verbo or not accion or not estandar_desempeño or not id_equipo_info:
        return jsonify({'error': 'Faltan datos obligatorios'}), 400
    


    guardar_info_usuario(token, subsistema_id=subsistema_id)

    # Insertar en la base de datos
    
    analisis_funcional_id = insertar_analisis_funcional(
    verbo,
    accion,
    estandar_desempeño,
    id_equipo_info,
    subsistema_id
    )
    return jsonify({'message': 'Análisis funcional agregado', 'id': analisis_funcional_id}), 200




# Diccionario global para almacenar la información temporal de los usuarios
usuario_info_temporal = {}

def generar_token():
    return str(uuid.uuid4())

@app.before_request
def before_request():
    rutas_sin_autenticacion = ['login', 'static']  # Rutas que no requieren autenticación
    if request.endpoint not in rutas_sin_autenticacion:
        token = request.cookies.get('user_token')  # Leer la cookie 'user_token'
        print(f"Token en before_request: {token}")
        if not token or token not in usuario_info_temporal:
            return redirect(url_for('login'))  # Redirigir al login si no está autenticado
        else:
            g.user_token = token  # Almacenar el token en 'g' para usarlo en las vistas
            g.usuario_id = usuario_info_temporal[token]['usuario_id']
    else:
        g.user_token = None

# No es necesario 'after_request' en este caso

def guardar_info_usuario(token, id_sistema=None, id_equipo=None, id_equipo_info=None, usuario_id=None,subsistema_id=None):
    
    if token in usuario_info_temporal:
        # Actualizar la información existente
        if id_sistema is not None:
            usuario_info_temporal[token]['id_sistema'] = id_sistema
        if id_equipo is not None:
            usuario_info_temporal[token]['id_equipo'] = id_equipo
        if id_equipo_info is not None:
            usuario_info_temporal[token]['id_equipo_info'] = id_equipo_info
        if usuario_id is not None:
            usuario_info_temporal[token]['usuario_id'] = usuario_id
        if subsistema_id is not None:
            usuario_info_temporal[token]['subsistema_id'] = subsistema_id
    else:

        usuario_info_temporal[token] = {
            'id_sistema': id_sistema,
            'id_equipo': id_equipo,
            'id_equipo_info': id_equipo_info,
            'usuario_id': usuario_id,
            'subsistema_id': subsistema_id
        }

def obtener_info_usuario(token):
    return usuario_info_temporal.get(token, {})

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('correo')
        password = request.form.get('password')

        # Verificar las credenciales del usuario
        usuario = obtener_usuario_por_correo(correo)
        if usuario and usuario['password'] == password:
            # Autenticación exitosa
            token = generar_token()  # Generar un token único
            # Guardar la información del usuario en el diccionario temporal
            guardar_info_usuario(token, usuario_id=usuario['id'])
            # Crear la respuesta y configurar la cookie
            response = make_response(redirect(url_for('registro_generalidades')))
            response.set_cookie('user_token', token, httponly=True, secure=True, samesite='Lax')  # Establecer la cookie con el token
            return response
        else:
            # Autenticación fallida
            return render_template('login.html', error='Correo o contraseña incorrectos')
    else:
        # Mostrar el formulario de inicio de sesión
        return render_template('login.html')

@app.route('/logout')
def logout():
    token = request.cookies.get('user_token')
    if token and token in usuario_info_temporal:
        usuario_info_temporal.pop(token)  # Eliminar la información del usuario
    response = make_response(redirect(url_for('login')))
    response.set_cookie('user_token', '', expires=0)  # Eliminar la cookie
    return response



#Rutas para repuesto
# app.py
@app.route('/LSA/mostrar-repuesto', methods=['GET'])
def mostrar_repuestos():
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')

    if id_equipo_info is None:
        return redirect(url_for('registro_generalidades'))

    repuestos = obtener_repuestos_por_equipo_info(id_equipo_info)
    return render_template('mostrar_repuesto.html', repuestos=repuestos)



# app.py
@app.route('/api/repuesto', methods=['POST'])
def agregar_repuesto():
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')

    print(f"id_equipo_info en agregar_repuesto: {id_equipo_info}")

    # Si estás manejando archivos (imágenes), debes usar request.form en lugar de request.get_json()
    nombre_repuesto = request.form.get('nombre_repuesto')
    valor = request.form.get('valor')
    dibujo_transversal = request.files.get('dibujo_transversal')
    notas = request.form.get('notas')
    mtbf = request.form.get('mtbf')
        
    codigo_otan = request.form.get('codigo_otan')

    
    print(f"nombre_repuesto: {nombre_repuesto}")
    print(f"valor: {valor}")
    print(f"dibujo_transversal: {dibujo_transversal}")
    print(f"notas: {notas}")
    print(f"mtbf: {mtbf}")
    print(f"codigo_otan: {codigo_otan}")



    if not id_equipo_info or not nombre_repuesto:
        return jsonify({'error': 'Faltan datos obligatorios'}), 400
    
     # Validar y convertir 'valor' a float
    try:
        valor = float(valor) if valor else None
    except ValueError:
        return jsonify({'error': 'El valor debe ser un número decimal'}), 400

    # Validar y convertir 'mtbf' a float
    try:
        mtbf = float(mtbf) if mtbf else None
    except ValueError:
        return jsonify({'error': 'El MTBF debe ser un número decimal'}), 400

    # Leer los datos de la imagen si existe

    # Procesar la imagen 'dibujo_transversal' si existe
    dibujo_transversal_data = dibujo_transversal.read() if dibujo_transversal else None

    repuesto_id = insertar_repuesto(
        id_equipo_info, nombre_repuesto, valor,
        dibujo_transversal_data, notas, mtbf, codigo_otan
    )
    return jsonify({'message': 'Repuesto agregado correctamente', 'id': repuesto_id}), 200


# app.py
@app.route('/api/repuesto/<int:id_repuesto>', methods=['POST'])
def actualizar_repuesto_route(id_repuesto):
    nombre_repuesto = request.form.get('nombre_repuesto')
    valor = request.form.get('valor')
    dibujo_transversal = request.files.get('dibujo_transversal')
    notas = request.form.get('notas')
    mtbf = request.form.get('mtbf')
    codigo_otan = request.form.get('codigo_otan')

    if not nombre_repuesto:
        return jsonify({'error': 'Faltan datos obligatorios'}), 400

    # Validar y convertir los valores numéricos
    try:
        valor = float(valor) if valor else None
        mtbf = float(mtbf) if mtbf else None
    except ValueError:
        return jsonify({'error': 'Valor o MTBF deben ser números válidos'}), 400

    # Leer los datos del archivo si se ha subido uno nuevo
    dibujo_transversal_data = dibujo_transversal.read() if dibujo_transversal else None

    # Llamar a la función para actualizar el repuesto en la base de datos
    actualizar_repuesto(id_repuesto, nombre_repuesto, valor, dibujo_transversal_data, notas, mtbf, codigo_otan)
    return jsonify({'message': 'Repuesto actualizado correctamente'}), 200


# app.py
@app.route('/api/repuesto/<int:id_repuesto>', methods=['DELETE'])
def eliminar_repuesto_route(id_repuesto):
    eliminar_repuesto(id_repuesto)
    return jsonify({'message': 'Repuesto eliminado correctamente'}), 200




@app.route('/LSA/editar-repuesto/<int:id_repuesto>', methods=['GET'])
def editar_repuesto(id_repuesto):
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')

    if id_equipo_info is None:
        return redirect(url_for('registro_generalidades'))

    # Obtener los datos del repuesto
    repuesto = obtener_repuesto_por_id(id_repuesto)

    if not repuesto:
        return 'Repuesto no encontrado', 404

    return render_template('editar_repuesto.html', repuesto=repuesto)


@app.template_filter('b64encode')
def b64encode_filter(data):
    if data:
        import base64
        return Markup(base64.b64encode(data).decode('utf-8'))
    return ''









# app.py


@app.route('/api/analisis-herramientas', methods=['POST'])
def agregar_analisis_herramienta():
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')

    nombre = request.form.get('nombre')
    valor = request.form.get('valor')
    parte_numero = request.form.get('parte_numero')
    id_tipo_herramienta = request.form.get('tipo_herramienta')
    
    # Aquí se captura el archivo de dibujo seccion transversal
    dibujo_seccion_transversal = request.files.get('dibujo_seccion_transversal')

    if not nombre:
        return jsonify({'error': 'Faltan datos obligatorios'}), 400

    # Convertir 'valor' a float
    try:
        valor = float(valor) if valor else None
    except ValueError:
        return jsonify({'error': 'El valor debe ser numérico'}), 400


    # Leer el archivo si existe
    dibujo_data = dibujo_seccion_transversal.read() if dibujo_seccion_transversal else None

    # Insertar en la tabla herramientas_requeridas y obtener el ID
    id_herramienta_requerida = insertar_herramienta_requerida(nombre, id_tipo_herramienta)

    # Insertar en la tabla herramientas_generales, incluyendo el archivo si está disponible
    analisis_id = insertar_analisis_herramienta(
        nombre, valor, id_equipo_info, parte_numero, id_herramienta_requerida, id_tipo_herramienta, dibujo_data

    )

    return jsonify({'message': 'Análisis de herramienta agregado', 'id': analisis_id}), 200




@app.route('/LSA/editar-analisis-herramienta/<int:id_analisis>', methods=['GET'])
def editar_analisis_herramienta(id_analisis):
    token = g.user_token
    analisis = obtener_analisis_herramienta_por_id(id_analisis)
    if analisis is None:
        return "Análisis no encontrado", 404

    tipos_herramientas = obtener_tipos_herramientas()

    return render_template('editar_analisis_herramienta.html', analisis=analisis, tipos_herramientas=tipos_herramientas)



@app.route('/api/analisis-herramientas/<int:id_analisis>', methods=['PUT'])
def actualizar_analisis_herramienta_route(id_analisis):
    nombre = request.form.get('nombre')
    valor = request.form.get('valor')
    parte_numero = request.form.get('parte_numero')
    id_tipo_herramienta = request.form.get('tipo_herramienta')
    dibujo_seccion_transversal = request.files.get('dibujo_seccion_transversal')

    if not nombre or not id_tipo_herramienta:
        return jsonify({'error': 'Faltan datos obligatorios'}), 400

    try:
        valor = float(valor) if valor else None
    except ValueError:
        return jsonify({'error': 'El valor debe ser numérico'}), 400

    dibujo_data = dibujo_seccion_transversal.read() if dibujo_seccion_transversal else None

    # Si no se sube una nueva imagen, conservar la anterior
    if not dibujo_data:
        analisis = obtener_analisis_herramienta_por_id(id_analisis)
        dibujo_data = analisis['dibujo_seccion_transversal']

    actualizar_analisis_herramienta(id_analisis, nombre, valor, parte_numero, dibujo_data)

    return jsonify({'message': 'Análisis de herramienta actualizado'}), 200


@app.route('/api/analisis-herramientas/<int:id_analisis>', methods=['DELETE'])
def eliminar_analisis_herramienta_route(id_analisis):
    eliminar_analisis_herramienta(id_analisis)
    return jsonify({'message': 'Análisis de herramienta eliminado'}), 200




# Función para obtener el equipo por id_equipo_info
def obtener_equipo_por_id(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT nombre_equipo FROM equipo_info WHERE id = %s"
    cursor.execute(query, (id_equipo_info,))
    equipo = cursor.fetchone()
    cursor.close()
    return equipo

@app.route('/api/herramientas-especiales', methods=['POST'])
def agregar_herramienta_especial():
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')

    parte_numero = request.form.get('parte_numero')
    nombre_herramienta = request.form.get('nombre_herramienta')
    valor = request.form.get('valor')
    dibujo_seccion_transversal = request.files.get('dibujo_seccion_transversal')
    nota = request.form.get('nota')
    manual_referencia = request.form.get('manual_referencia')
    id_tipo_herramienta = request.form.get('tipo_herramienta')
    cantidad = request.form.get('cantidad')

    if not nombre_herramienta or not id_tipo_herramienta:
        return jsonify({'error': 'Faltan datos obligatorios'}), 400

    # Convertir 'valor' a float
    try:
        valor = float(valor) if valor else None
    except ValueError:
        return jsonify({'error': 'El valor debe ser numérico'}), 400

    dibujo_data = dibujo_seccion_transversal.read() if dibujo_seccion_transversal else None

    # Insertar en la tabla herramientas_requeridas y obtener el ID
    id_herramienta_requerida = insertar_herramienta_requerida(nombre_herramienta, id_tipo_herramienta)

    # Insertar en la tabla herramientas_especiales, incluyendo el id_herramienta_requerida
    herramienta_id = insertar_herramienta_especial(
        parte_numero, nombre_herramienta, valor,
        dibujo_data, nota, id_equipo_info,
        manual_referencia, id_tipo_herramienta, cantidad,
        id_herramienta_requerida  # Asegurarse de pasar el id_herramienta_requerida aquí
    )

    return jsonify({'message': 'Herramienta especial agregada', 'id': herramienta_id}), 200


@app.route('/LSA/mostrar-herramientas-especiales', methods=['GET'])
def mostrar_herramientas_especiales():
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')

    if id_equipo_info is None:
        return redirect(url_for('registro_generalidades'))

    analisis = obtener_analisis_herramientas_por_equipo(id_equipo_info)
    herramientas = obtener_herramientas_especiales_por_equipo(id_equipo_info)

    return render_template(
        'mostrar_herramientas-especiales.html',
        analisis=analisis,
        herramientas=herramientas
    )

@app.route('/LSA/registro-herramientas-especiales', methods=['GET'])
def registro_herramientas_especiales():
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')

    if id_equipo_info is None:
        return redirect(url_for('registro_generalidades'))

    tipos_herramientas = obtener_tipos_herramientas()

    # Obtener el nombre del equipo
    equipo = obtener_equipo_por_id(id_equipo_info)

    return render_template(
        'registro_herramientas_especiales.html',
        equipo=equipo,
        tipos_herramientas=tipos_herramientas
    )





@app.route('/LSA/editar-herramienta-especial/<int:id_herramienta>', methods=['GET'])
def editar_herramienta_especial(id_herramienta):
    token = g.user_token
    herramienta = obtener_herramienta_especial_por_id(id_herramienta)
    if herramienta is None:
        return "Herramienta no encontrada", 404

    tipos_herramientas = obtener_tipos_herramientas()

    return render_template('editar_herramienta_especial.html', herramienta=herramienta, tipos_herramientas=tipos_herramientas)


@app.route('/api/herramientas-especiales/<int:id_herramienta>', methods=['PUT'])
def actualizar_herramienta_especial_route(id_herramienta):
    parte_numero = request.form.get('parte_numero')
    nombre_herramienta = request.form.get('nombre_herramienta')
    valor = request.form.get('valor')
    dibujo_seccion_transversal = request.files.get('dibujo_seccion_transversal')
    nota = request.form.get('nota')
    manual_referencia = request.form.get('manual_referencia')
    id_tipo_herramienta = request.form.get('tipo_herramienta')
    cantidad = request.form.get('cantidad')

    if not nombre_herramienta or not id_tipo_herramienta:
        return jsonify({'error': 'Faltan datos obligatorios'}), 400

    try:
        valor = float(valor) if valor else None
    except ValueError:
        return jsonify({'error': 'El valor debe ser numérico'}), 400

    dibujo_data = dibujo_seccion_transversal.read() if dibujo_seccion_transversal else None

    # Si no se sube una nueva imagen, conservar la anterior
    if not dibujo_data:
        herramienta = obtener_herramienta_especial_por_id(id_herramienta)
        dibujo_data = herramienta['dibujo_seccion_transversal']

    actualizar_herramienta_especial(
        id_herramienta, parte_numero, nombre_herramienta, valor,
        dibujo_data, nota, manual_referencia, id_tipo_herramienta, cantidad
    )

    return jsonify({'message': 'Herramienta especial actualizada'}), 200







@app.route('/api/herramientas-especiales/<int:id_herramienta>', methods=['DELETE'])
def eliminar_herramienta_especial_route(id_herramienta):
    eliminar_herramienta_especial(id_herramienta)
    return jsonify({'message': 'Herramienta especial eliminada'}), 200


























"""

@app.route('/LSA/fmea', methods=['GET'])
def registro_FMEA():
    token = g.user_token  # Obtener el token del usuario desde la sesión
    user_data = obtener_info_usuario(token)  # Obtener la información del usuario desde el token
    id_sistema = user_data.get('id_sistema')  # Recuperar el ID del sistema asociado al usuario

    # Obtener la información del sistema desde la base de datos
    if id_sistema:
        sistema = obtener_sistema_por_id(id_sistema)  # Llamar a la función en `database.py`
    else:
        sistema = None

    # Pasar la información del sistema a la plantilla HTML
    return render_template('registro_FMEA.html', sistema=sistema)
"""







































"""

@app.route('/LSA/fmea', methods=['GET'])
def registro_FMEA():
    token = g.user_token  # Obtener el token del usuario desde la sesión
    user_data = obtener_info_usuario(token)  # Obtener la información del usuario desde el token
    id_sistema = user_data.get('id_sistema')  # Recuperar el ID del sistema asociado al usuario

    # Obtener la información del sistema desde la base de datos
    if id_sistema:
        sistema = obtener_sistema_por_id(id_sistema)  # Llamar a la función en `database.py`
    else:
        sistema = None

    # Pasar la información del sistema a la plantilla HTML
    return render_template('registro_FMEA.html', sistema=sistema)
"""

































@app.route('/LSA/equipo/editar-FMEA')
def editar_FMEA_lista():
    fmeas = obtener_fmeas()  #Estoy llamando los fmeas para que salgan en la lista
    #print(f'Para la lista{fmeas}')
    fmeas_con_rcm = obtener_fmeas_con_rcm()
    return render_template('editar_FMEA.html', fmeas=fmeas, fmeas_con_rcm=fmeas_con_rcm)


@app.route('/LSA/editar-FMEA/<int:fmea_id>')
def editar_FMEA(fmea_id):
    # Obtener los datos del FMEA a partir del ID
    fmea = obtener_fmea_por_id(fmea_id)
    fmea_id = obtener_ID_FMEA(fmea_id)
    print(f'\n\n\n\n{fmea}\n\n\n\n') 
    # Cargar la información del sistema
    sistema = fmea.get('sistema')
    sistema_id = fmea_id.get('id_sistema')
    print(f'\n\n\n\n{sistema_id}\n\n\n\n')
    #Obtener datos para desplegables
    componentes = obtener_componentes_por_subsistema(sistema_id)
    print(f'\n\n\n\nlos componentes son: {componentes}\n\n\n\n')
    mecanismos_falla = obtener_mecanismos_falla()
    codigos_modo_falla = obtener_codigos_modo_falla()
    metodos_deteccion_falla = obtener_metodos_deteccion_falla() 
    fallos_ocultos = obtener_fallos_ocultos()
    seguridad_fisica = obtener_seguridad_fisica()
    medio_ambiente_datos = obtener_medio_ambiente()
    impacto_operacional_datos = obtener_impacto_operacional()
    costos_reparacion_datos = obtener_costos_reparacion()
    flexibilidad_operacional_datos= obtener_flexibilidad_operacional()
    ocurrencia_datos = obtener_Ocurrencia()
    probabilidad_deteccion_datos = obtener_probablilidad_deteccion()
    lista_riesgos = obtener_lista_riesgos() or []


    # Renderizar formularios
    return render_template('registro_FMEA.html',fmea=fmea, fmea_id=fmea_id, editar=True,
                           sistema=sistema,
                           componentes=componentes,
                           mecanismos_falla = mecanismos_falla,
                           codigos_modo_falla = codigos_modo_falla,
                           metodos_deteccion_falla = metodos_deteccion_falla,
                           fallos_ocultos=fallos_ocultos,
                           seguridad_fisica=seguridad_fisica,
                           medio_ambiente_datos=medio_ambiente_datos,
                           impacto_operacional_datos=impacto_operacional_datos,
                           costos_reparacion_datos=costos_reparacion_datos,
                           flexibilidad_operacional_datos=flexibilidad_operacional_datos,
                           ocurrencia_datos = ocurrencia_datos,

                           probabilidad_deteccion_datos = probabilidad_deteccion_datos,
                           lista_riesgos= lista_riesgos)

@app.route('/LSA/guardar-FMEA/<int:fmea_id>', methods=['POST'])
def guardar_cambios_fmea(fmea_id):

    # Los siguientes campos no cambian
    id_equipo_info = obtener_id_equipo_info_por_fmea(fmea_id)
    sistema_id = obtener_id_sistema_por_fmea_id(fmea_id)
    
    # Obtener los datos del formulario
    falla_funcional = request.form.get('falla_funcional')
    descripcion_modo_falla = request.form.get('descripcion_modo_falla')
    causas = request.form.get('causas')
    mtbf = request.form.get('mtbf')
    mttr = request.form.get('mttr')

    #campos de los menús desplegables
    id_componente = request.form.get('item_componente')
    id_mecanismo_falla = request.form.get('mecanismo_falla')
    id_detalle_falla = request.form.get('detalle_falla')
    id_codigo_modo_falla = request.form.get('codigo_modo_falla')
    id_consecutivo_modo_falla = request.form.get('id_consecutivo_modo_falla')


    id_metodo_deteccion_falla = request.form.get('metodo_detecion_falla')
    id_fallo_oculto = request.form.get('fallo_oculto')
    id_seguridad_fisica = request.form.get('seguridad_fisica')
    id_medio_ambiente = request.form.get('medio_ambiente')
    id_impacto_operacional = request.form.get('impacto_operacional')
    id_costos_reparacion = request.form.get('costos_reparacion')
    id_flexibilidad_operacional = request.form.get('flexibilidad_operacional')

    calculo_severidad = request.form.get('severidad')
    id_ocurrencia = request.form.get('ocurrencia')
    ocurrencia_mate = request.form.get('ocurrencia_matematica')
    id_probabilidad_deteccion = request.form.get('probabilidad_deteccion') 
    rpn = request.form.get('rpn')
    id_riesgo = request.form.get('id_riesgo')

    
    id_falla_funcional = insertar_falla_funcional(falla_funcional)
    id_descripcion_modo_falla = insertar_descripcion_modo_falla(descripcion_modo_falla)
    id_causa = insertar_causa(causas)

    print(f'\n\n\nValue: {id_probabilidad_deteccion}\n\n')


    # Actualizar el registro FMEA con los nuevos datos
    actualizar_fmea(
        fmea_id, id_equipo_info, sistema_id, id_falla_funcional, id_componente, 
        id_codigo_modo_falla, id_consecutivo_modo_falla, id_descripcion_modo_falla, 
        id_causa, id_mecanismo_falla, id_detalle_falla, mtbf, mttr, id_fallo_oculto, 
        id_seguridad_fisica, id_medio_ambiente, id_impacto_operacional, id_costos_reparacion, 
        id_flexibilidad_operacional, calculo_severidad, id_ocurrencia, ocurrencia_mate,
        id_probabilidad_deteccion, id_metodo_deteccion_falla, rpn, id_riesgo
    )



    # Redireccionar después de guardar los cambios
    return redirect(url_for('mostrar_FMEA'))




@app.route('/LSA/eliminar-FMEA/<int:fmea_id>', methods=['POST'])
def eliminar_FMEA(fmea_id):
    cursor = db.connection.cursor()

    
    #Obtener el id_consecutivo_modo_falla del registro a eliminar desde la tabla fmea
    cursor.execute("SELECT id_consecutivo_modo_falla FROM fmea WHERE id = %s", (fmea_id,))
    result = cursor.fetchone()
    
    if result and 'id_consecutivo_modo_falla' in result:
        id_consecutivo_modo_falla = result['id_consecutivo_modo_falla']
        
        #Contar cuántas veces aparece id_consecutivo_modo_falla en la tabla fmea
        count_query = "SELECT COUNT(*) as count FROM fmea WHERE id_consecutivo_modo_falla = %s"
        cursor.execute(count_query, (id_consecutivo_modo_falla,))
        count_result = cursor.fetchone()
        ocurrencias = (count_result['count'])-1 if count_result else 0
        
        
        #Actualizar la numeración en la tabla consecutivo_modo_falla con el número de ocurrencias
        update_query = """
            UPDATE consecutivo_modo_falla
            SET numeracion = %s
            WHERE id = %s
        """
        cursor.execute(update_query, (ocurrencias, id_consecutivo_modo_falla))
        
        #Eliminar el registro de FMEA
        delete_query = "DELETE FROM fmea WHERE id = %s"
        cursor.execute(delete_query, (fmea_id,))
        
        # Confirmar los cambios en la base de datos
        db.connection.commit()

    cursor.close()

    # Redireccionar a la vista de la tabla después de eliminar
    return redirect(url_for('mostrar_FMEA'))






@app.route('/LSA/equipo/editar-modulo-herramientas')
def editar_modulo_herramientas():
    return render_template('editar_herramientas-especiales.html')

@app.route('/LSA/equipo/editar-analisis-herramientas')
def editar_analisis_herramientas():
    return render_template('editar_analisis_herramientas.html')

@app.route('/LSA/equipo/editar-herramientas-especiales')
def editar_herramientas_especiales():
    return render_template('editar_herramientas_especiales2.html')


@app.route('/LSA/equipo/editar_RCM/<int:fmea_id>')
def editar_RCM(fmea_id):
    rcm = obtener_rcm_por_fmea(fmea_id)
    acciones = obtener_lista_acciones_recomendadas()
    return render_template('registro_rcm.html', rcm=rcm, editar=True, acciones = acciones)
@app.route('/LSA/equipo/editar_RCM')
def editar_RCM_lista():
    rcms = obtener_rcms_completos()  # Obtener todos los registros de RCM desde la base de datos
    return render_template('editar_RCM.html', rcms=rcms)


@app.route('/LSA/equipo/editar-MTA')
def editar_MTA():
    return render_template('editar_MTA.html')
































# app.py

@app.route('/LSA/mostrar-equipo', methods=['GET'])
def mostrar_equipo():
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')
    if id_equipo_info is None:
        return redirect(url_for('registro_generalidades'))


    equipo = obtener_equipo_info_por_id(id_equipo_info)
    if equipo is None:
        return "Equipo no encontrado", 404
    
     # Obtener el grupo constructivo
    grupo_constructivo = obtener_grupo_constructivo_por_sistema_id(equipo['id_sistema']) if equipo.get('id_sistema') else None

    # Obtener el subgrupo constructivo
    subgrupo_constructivo = obtener_subgrupo_constructivo_por_sistema_id(equipo['id_sistema']) if equipo.get('id_sistema') else None


    diagrama = obtener_diagramas_por_id(equipo['id_diagrama']) if equipo['id_diagrama'] else None

     # Obtener procedimiento relacionado si está presente
    procedimiento = obtener_procedimiento_por_id(equipo['id_procedimiento']) if equipo['id_procedimiento'] else None

    # Opcional: Obtener más detalles relacionados, por ejemplo, personal o sistema
    responsable = obtener_personal_por_id(equipo['id_personal']) if equipo['id_personal'] else None
    sistema = obtener_sistema_por_id(equipo['id_sistema']) if equipo['id_sistema'] else None
    datos_equipo = obtener_datos_equipo_por_id(equipo['id_equipo']) if equipo.get('id_equipo') else None
    # Obtener el tipo de equipo
    tipo_equipo = obtener_tipo_equipo_por_id(equipo['id_tipo_equipo']) if equipo.get('id_tipo_equipo') else None


    return render_template('mostrar_equipo.html', 
                           equipo=equipo,
                           datos_equipo=datos_equipo,
                           tipo_equipo=tipo_equipo, 
                           diagrama=diagrama, 
                           procedimiento=procedimiento, 
                           responsable=responsable,
                           sistema=sistema,
                           grupo_constructivo=grupo_constructivo,
                           subgrupo_constructivo=subgrupo_constructivo
                           )



@app.route('/LSA/editar-equipo', methods=['GET', 'POST'])
def editar_equipo():
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')

    if id_equipo_info is None:
        return redirect(url_for('registro_generalidades'))

    if request.method == 'GET':
        equipo = obtener_equipo_info_por_id(id_equipo_info)
        # Obtener datos adicionales si es necesario
        responsables = obtener_responsables()
        grupos = obtener_grupos_constructivos()
        tipos_equipos = obtener_tipos_equipos()
        return render_template(
            'editar_equipo.html',
            equipo=equipo,
            responsables=responsables,
            grupos=grupos,
            tipos_equipos=tipos_equipos
        )
    elif request.method == 'POST':
        # Obtener datos del formulario
        data = request.form.to_dict()
        # Verificar si el archivo de imagen está presente
        imagen_file = request.files.get('imagen_equipo')
        if imagen_file and imagen_file.filename != '':
            data['imagen_equipo'] = imagen_file.read()  # Si hay imagen, la leemos
        else:
            data['imagen_equipo'] = None  # Si no hay imagen, asignamos None

         # Manejo de los diagramas
        diagrama_flujo = request.files.get('diagrama_flujo')
        diagrama_caja_negra = request.files.get('diagrama_caja_negra')
        diagrama_caja_transparente = request.files.get('diagrama_caja_transparente')

        # Procedimientos
        procedimiento_arranque = request.form.get('procedimiento_arranque')
        procedimiento_parada = request.form.get('procedimiento_parada')

        # Insertar o actualizar los procedimientos y diagramas
        id_procedimiento = insertar_procedimiento(procedimiento_arranque, procedimiento_parada)
        data['id_procedimiento'] = id_procedimiento

        id_diagrama = insertar_diagrama(diagrama_flujo, diagrama_caja_negra, diagrama_caja_transparente)
        data['id_diagrama'] = id_diagrama

        # Actualizar la información del equipo
        actualizar_equipo_info(id_equipo_info, data)

        return redirect(url_for('mostrar_equipo'))

@app.route('/LSA/eliminar-equipo', methods=['POST'])
def eliminar_equipo():
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')

    if id_equipo_info is None:
        return jsonify({'error': 'No se ha seleccionado ningún equipo'}), 400

    eliminar_equipo_info(id_equipo_info)
    # Opcionalmente, puedes limpiar el id_equipo_info de la sesión
    user_data['id_equipo_info'] = None
    return jsonify({'message': 'Equipo eliminado exitosamente'}), 200





















@app.route('/LSA/equipo/mostrar-FMEA')
def mostrar_FMEA():
    fmeas = obtener_fmeas()# Obtener todos los registros de FMEA desde la base de datos
    return render_template('mostrar_FMEA.html', fmeas=fmeas)

@app.route('/LSA/equipo/mostrar-MTA')
def mostrar_MTA():
    return render_template('mostrar_MTA.html')

@app.route('/LSA/equipo/mostrar-RCM')
def mostrar_RCM():
    return render_template('mostrar_RCM.html')



@app.route('/LSA/equipo/mostrar-analisis-herramientas')
def mostrar_analisis_herramientas():
    return render_template('mostrar_analisis-herramientas.html')

@app.route('/LSA/equipo/mostrar-repuestos')
def mostrar_repuesto():
    return render_template('mostrar_repuesto.html')

@app.route('/LSA/equipo/mostrar-informe')
def mostrar_informe():
    return render_template('mostrar_informe.html')


@app.route('/LSA/registro-MTA/<int:fmea_id>')
def registro_MTA(fmea_id):
    if fmea_id:
        # Obtener los datos de FMEA por su ID
        fmea = obtener_fmea_por_id(fmea_id)  #obtenemos los nombres en los compos de fmea
        fmea_id = obtener_ID_FMEA(fmea_id) # optenermos el id de fmea 
        print(f'\nfmea:{fmea}\n\nfmea_id:{fmea_id}\n\n') #imprimo a ver
        # Variables precargadas desde el FMEA
        sistema = fmea.get('id_sistema')
        componente = fmea.get('id_componente')
        falla_funcional = fmea.get('id_falla_funcional')
    else:
        sistema = None
        falla_funcional = None
        componente = None
        fmea = []
    

    #Obtener datos para desplegables
    tipo_de_manteniemto = obtener_tipos_mantenimiento()
    tarea_mantenimento = obtener_tareas_mantenimiento()
    herramientas = 0
    return render_template('registro_MTA.html',fmea = fmea, editar = False,
                           sistema=sistema,
                           falla_funcional = falla_funcional,
                           componente = componente,
                           tipo_de_manteniemto = tipo_de_manteniemto,
                           tarea_mantenimento = tarea_mantenimento,
                           herramientas = herramientas
                           )
@app.route('/LSA/registro-MTA/<int:fmea_id>', methods=['POST'])
def guardar_MTA(fmea_id):
     # Obtener los datos del formulario
    fmea_id = obtener_ID_FMEA(fmea_id)
    id_sistema = fmea_id.get('id_sistema')
    id_componente = fmea_id.get('id_componente')
    id_falla_funcional = fmea_id.get('id_falla_funcional')
    
    tipo_mantenimiento = request.form.get('tipo_mantenimiento')
    tarea_mantenimiento = request.form.get('tarea_mantenimiento')
    cantidad_personal = request.form.get('personal_requerido')
    consumibles = request.form.get('consumibles_requeridos')
    duracion_horas = request.form.get('duracion_horas')
    duracion_minutos = request.form.get('duracion_minutos')
    consumibles_requeridos = request.form.get('consumibles_requeridos')
    repuestos_requeridos = request.form.get('repuestos_requeridos')
    requeridos_por_tarea = request.form.get('requeridos_por_tarea')
    condiciones_requeridas_ambientales = request.form.get('condiciones_requeridas_ambientales')
    condiciones_requeridas_estado_equipo = request.form.get('condiciones_requeridas_estado_equipo')
    condiciones_requeridas_especiales = request.form.get('condiciones_requeridas_especiales')
    duracion_tarea_horas = request.form.get('duracion_tarea_horas')
    duracion_tarea_minutos = request.form.get('duracion_tarea_minutos')
    detalle_tarea = request.form.get('detalle_tarea')
    #aca viene la logica pa añadir los datos a sus tablas y devolver el id que sera pasado a insertar_mta
    
    # Guardar en la base de datos
    id_mta = insertar_mta(fmea_id, id_sistema, id_componente, id_falla_funcional)

    
    return redirect(url_for('mostrar_MTA')) 


@app.route('/LSA/registro-RCM')
def registro_RCM():
    return render_template('registro_RCM.html')



@app.route('/LSA/registro-FMEA')
def registro_FMEA():
    subsistema_id = session.get('subsistema_id')  # Obtener el id del subsistema asociado
    sistema = obtener_subsistema_por_id(subsistema_id)  #el sistema de fmea es el subsistema de analisis funcional
    #Obtener datos para desplegables
    componentes = obtener_componentes_por_subsistema(subsistema_id)
    mecanismos_falla = obtener_mecanismos_falla()
    codigos_modo_falla = obtener_codigos_modo_falla()
    metodos_deteccion_falla = obtener_metodos_deteccion_falla() 
    fallos_ocultos = obtener_fallos_ocultos()
    seguridad_fisica = obtener_seguridad_fisica()
    medio_ambiente_datos = obtener_medio_ambiente()
    impacto_operacional_datos = obtener_impacto_operacional()
    costos_reparacion_datos = obtener_costos_reparacion()
    flexibilidad_operacional_datos= obtener_flexibilidad_operacional()
    ocurrencia_datos = obtener_Ocurrencia()
    probabilidad_deteccion_datos = obtener_probablilidad_deteccion()
    lista_riesgos = obtener_lista_riesgos() or []
    

    # Renderizar la plantilla y pasar datos
    return render_template('registro_FMEA.html',fmea=None, fmea_id=None, editar=False,
                           sistema=sistema,
                           componentes=componentes,
                           mecanismos_falla = mecanismos_falla,
                           codigos_modo_falla = codigos_modo_falla,
                           metodos_deteccion_falla = metodos_deteccion_falla,
                           fallos_ocultos=fallos_ocultos,
                           seguridad_fisica=seguridad_fisica,
                           medio_ambiente_datos=medio_ambiente_datos,
                           impacto_operacional_datos=impacto_operacional_datos,
                           costos_reparacion_datos=costos_reparacion_datos,
                           flexibilidad_operacional_datos=flexibilidad_operacional_datos,
                           ocurrencia_datos = ocurrencia_datos,

                           probabilidad_deteccion_datos = probabilidad_deteccion_datos,
                           lista_riesgos= lista_riesgos)


@app.route('/LSA/registro-FMEA', methods=['POST'])
def guardar_fmea():
    # Obtener el token del usuario y la información relacionada
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')
    id_sistema = session.get('subsistema_id')
    
    
    # Obtener los datos del formulario
    falla_funcional = request.form.get('falla_funcional')
    descripcion_modo_falla = request.form.get('descripcion_modo_falla')
    causas = request.form.get('causas')
    mtbf = request.form.get('mtbf')
    mttr = request.form.get('mttr')

    #campos de los menús desplegables
    id_componente = request.form.get('item_componente')
    session['id_componente'] = id_componente
    id_mecanismo_falla = request.form.get('mecanismo_falla')
    id_detalle_falla = request.form.get('detalle_falla')
    id_codigo_modo_falla = request.form.get('codigo_modo_falla')
    id_consecutivo_modo_falla = request.form.get('id_consecutivo_modo_falla')
    id_metodo_deteccion_falla = request.form.get('metodo_detecion_falla')
    id_fallo_oculto = request.form.get('fallo_oculto')
    id_seguridad_fisica = request.form.get('seguridad_fisica')
    id_medio_ambiente = request.form.get('medio_ambiente')
    id_impacto_operacional = request.form.get('impacto_operacional')
    id_costos_reparacion = request.form.get('costos_reparacion')
    id_flexibilidad_operacional = request.form.get('flexibilidad_operacional')
    calculo_severidad = request.form.get('calculo_severidad')
    id_ocurrencia = request.form.get('ocurrencia')
    ocurrencia_mate= request.form.get('ocurrencia_matematica')
    rpn = request.form.get('rpn')
    id_probabilidad_deteccion = request.form.get('probabilidad_deteccion')
    id_riesgo = request.form.get('id_riesgo')
    

    # Insertar los datos relacionados en las tablas correspondientes y obtener los IDs
    id_falla_funcional = insertar_falla_funcional(falla_funcional)
    id_descripcion_modo_falla = insertar_descripcion_modo_falla(descripcion_modo_falla)
    id_causa = insertar_causa(causas)

    # Insertar todos estos IDs en la tabla FMEA junto con los nuevos campos
    id_fmea = insertar_fmea(
        id_equipo_info, id_sistema, id_falla_funcional, id_componente, id_codigo_modo_falla, 
        id_consecutivo_modo_falla, id_descripcion_modo_falla, id_causa, id_mecanismo_falla, 
        id_detalle_falla, mtbf, mttr,id_metodo_deteccion_falla, id_fallo_oculto, id_seguridad_fisica, 
        id_medio_ambiente, 
        id_impacto_operacional, id_costos_reparacion, id_flexibilidad_operacional,calculo_severidad, id_ocurrencia, 
        ocurrencia_mate,
        id_probabilidad_deteccion, rpn, id_riesgo

    )

    # Redireccionar o devolver respuesta exitosa
    return redirect(url_for('mostrar_FMEA'))  

#rutas para funcionesFMEA.js
@app.route('/LSA/obtener-detalles-falla/<int:mecanismo_id>', methods=['GET'])
def obtener_detalles_falla(mecanismo_id):
    cursor = db.connection.cursor()
    query = """
        SELECT id, nombre FROM detalle_falla
        WHERE id_mecanismo_falla = %s
    """
    cursor.execute(query, (mecanismo_id,))
    detalles_falla = cursor.fetchall()
    cursor.close()
    
    detalles_falla_lista = [{'id': detalle['id'], 'nombre': detalle['nombre']} for detalle in detalles_falla]
    return jsonify(detalles_falla_lista)
#Aqui estoy haciendo dos procesos a la vez tanto contando los consecutivos como mostrando el nombre
@app.route('/LSA/obtener-nombre-falla/<int:codigo_id>')
def obtener_nombre_falla(codigo_id):
    cursor = db.connection.cursor()

    # Obtener el nombre del modo de falla
    query_nombre = """
        SELECT nombre, codigo, id
        FROM codigo_modo_falla
        WHERE id = %s
    """
    cursor.execute(query_nombre, (codigo_id,))
    result = cursor.fetchone()

    if result:
        nombre_modo_falla = result['nombre']
        codigo_modo_falla = result['codigo']
        id_codigo_modo_falla = result['id']

        # Obtener el consecutivo de modo de falla
        query_consecutivo = """

            SELECT id

            FROM consecutivo_modo_falla 
            WHERE nombre = %s
        """
        cursor.execute(query_consecutivo, (codigo_modo_falla,))
        consecutivo_result = cursor.fetchone()

        if consecutivo_result:
            id_consecutivo_modo_falla = consecutivo_result['id']


            # Contar cuántas veces se usa el id_consecutivo_modo_falla en la tabla fmea
            count_query = """
                SELECT COUNT(*) as count
                FROM fmea
                WHERE id_consecutivo_modo_falla = %s
            """
            cursor.execute(count_query, (id_consecutivo_modo_falla,))
            count_result = cursor.fetchone()
            ocurrencias = count_result['count'] if count_result else 0

            # Calcular la nueva numeración
            nueva_numeracion = ocurrencias + 1

            # Actualizar la numeración en la tabla consecutivo_modo_falla

            query_update = """
                UPDATE consecutivo_modo_falla
                SET numeracion = %s
                WHERE id = %s
            """
            cursor.execute(query_update, (nueva_numeracion, id_consecutivo_modo_falla))
            db.connection.commit()

            cursor.close()

            return jsonify({
                'nombre': nombre_modo_falla,
                'consecutivo': f"{codigo_modo_falla}-{nueva_numeracion}",
                'id_consecutivo_modo_falla': id_consecutivo_modo_falla
            })
        else:
            cursor.close()
            return jsonify({'nombre': 'No encontrado', 'consecutivo': None}), 404
    else:
        cursor.close()
        return jsonify({'nombre': 'No encontrado', 'consecutivo': None}), 404


############################################################################################################





@app.route('/LSA/equipo/registro-LORA')
def registro_lora():
    return render_template('registro_lora.html')
"""
@app.route('/LSA/registro-analisis-funcional')
def registro_analisis_funcional():
    return render_template('registro_analisis_funcional.html')
"""



@app.route('/LSA/registro-repuesto')
def registro_repuesto():
    return render_template('registro_repuesto.html')

@app.route('/view_pdf_1')
def view_pdf_1():
    pdf_buffer = BytesIO()

    # Crear un PDF usando reportlab
    p = canvas.Canvas(pdf_buffer, pagesize=letter)
    p.drawString(100, 750, "Este es el PDF 1 generado desde Flask y visualizado en el navegador!")
    p.showPage()
    p.save()

    # Mover el puntero al principio del archivo
    pdf_buffer.seek(0)

    # Crear una respuesta personalizada para visualizar el PDF
    response = make_response(send_file(pdf_buffer, mimetype='application/pdf'))

    # Añadir encabezado para asegurar que no se descargue, solo se visualice
    response.headers['Content-Disposition'] = 'inline; filename="documento.pdf"'

    return response

# Ruta para descargar el primer PDF
@app.route('/download_pdf_1')
def download_pdf_1():
    pdf_buffer = BytesIO()

    # Crear un PDF usando reportlab
    p = canvas.Canvas(pdf_buffer, pagesize=letter)
    p.drawString(100, 750, "Este es el PDF 1 generado desde Flask!")
    p.showPage()
    p.save()

    # Mover el puntero al principio del archivo
    pdf_buffer.seek(0)

    # Enviar el PDF para su descarga
    return send_file(pdf_buffer, as_attachment=True, download_name="pdf_1.pdf", mimetype='application/pdf')





#new functions
@app.route('/LSA/crear_RCM/<int:fmea_id>')
def crear_RCM(fmea_id):
    fmea = obtener_fmea_por_id(fmea_id)
    acciones = obtener_lista_acciones_recomendadas()
    if fmea:
        print(fmea)
        return render_template('registro_RCM.html', fmea=fmea, acciones=acciones)
    else:
        return "FMEA no encontrado", 404


#funcion para guardar el RCM
@app.route('/LSA/guardar_RCM/<int:fmea_id>', methods=['POST'])
def guardar_RCM(fmea_id):
    rcm = {
        'id_fmea': fmea_id,
        'sistema': request.form.get('sistema'),
        'codigo_modo_falla': request.form.get('codigo_modo_falla'),
        'causas': request.form.get('causas'),
        'falla_funcional': request.form.get('falla_funcional'),
        'consecutivo_modo_falla': request.form.get('consecutivo_modo_falla'),
        'item_componente': request.form.get('item_componente'),
        'descripcion_modo_falla': request.form.get('descripcion_modo_falla'),
        'hidden_failures': request.form.get('hidden_failures'),
        'safety': request.form.get('safety'),
        'environment': request.form.get('environment'),
        'operation': request.form.get('operation'),
        'h1_s1_n1_o1': request.form.get('h1s1'),
        'h2_s2_n2_o2': request.form.get('h2s2'),
        'h3_s3_n3_o3': request.form.get('h3s3'),
        'h4_s4': request.form.get('h4s4'),
        'h5': request.form.get('h5'),
        'tarea': request.form.get('tarea'),
        'intervalo_inicial_horas': request.form.get('intervalo_inicial'),
        'id_accion_recomendada': request.form.get('accion_recomendada')
    }
    # Insertar los datos en la tabla RCM
    insertar_rcm(rcm)

    # Redireccionar después de guardar los cambios
    return redirect(url_for('editar_FMEA_lista'))




#actualizar rcm
@app.route('/LSA/equipos/actualizar_RCM/<int:fmea_id>', methods=['POST'])
def actualizar_RCM(fmea_id):
    # Obtener los datos del formulario
    rcm = {
        'id_fmea': fmea_id,
        'sistema': request.form.get('sistema'),
        'codigo_modo_falla': request.form.get('codigo_modo_falla'),
        'causas': request.form.get('causas'),
        'falla_funcional': request.form.get('falla_funcional'),
        'consecutivo_modo_falla': request.form.get('consecutivo_modo_falla'),
        'item_componente': request.form.get('item_componente'),
        'descripcion_modo_falla': request.form.get('descripcion_modo_falla'),
        'hidden_failures': request.form.get('hidden_failures'),
        'safety': request.form.get('safety'),
        'environment': request.form.get('environment'),
        'operation': request.form.get('operation'),
        'h1_s1_n1_o1': request.form.get('h1s1'),
        'h2_s2_n2_o2': request.form.get('h2s2'),
        'h3_s3_n3_o3': request.form.get('h3s3'),
        'h4_s4': request.form.get('h4s4'),
        'h5': request.form.get('h5'),
        'tarea': request.form.get('tarea'),
        'intervalo_inicial_horas': request.form.get('intervalo_inicial'),
        'id_accion_recomendada': request.form.get('accion_recomendada')
    }

    # Actualizar el registro RCM con los nuevos datos
    actualizar_rcm(rcm)

    # Redireccionar después de guardar los cambios
    return redirect(url_for('editar_RCM_lista'))

#eliminar rcm
@app.route('/LSA/eliminar_RCM/<int:fmea_id>')
def eliminar_RCM(fmea_id):
    eliminar_rcm(fmea_id)
    return redirect(url_for('editar_RCM_lista'))







#####analisis_funcional:


@app.route('/LSA/equipo/mostrar-analisis-funcional', methods=['GET'])
def mostrar_analisis_funcional():
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')
    id_equipo = user_data.get('id_equipo')
    
    if not id_equipo_info:
        flash('No se ha seleccionado un equipo.')
        return redirect(url_for('ruta_principal'))

    # Obtén el id_sistema desde la tabla equipo_info usando el id_equipo_info
    
    id_sistema = user_data.get('id_sistema')
    sistema_nombre = obtener_nombre_sistema_por_id(id_sistema)

    # Si no se proporciona id_sistema, el sistema es None
    if id_sistema is None:
        sistema = None
        subsistemas = []
    else:
        # Obtener el sistema usando el id_sistema
        sistema = obtener_sistema_por_id(id_sistema)
        """
        # Verificar si el sistema existe
        if sistema:
            # Obtener los subsistemas asociados al equipo
            subsistemas = obtener_subsistemas_por_equipo(id_equipo)
        else:
            # Si el sistema no existe, no hay subsistemas
            subsistemas = []
        """
    # Obtén los análisis funcionales relacionados con el equipo
    analisis_funcionales = obtener_analisis_funcionales_por_equipo_info(id_equipo_info)
    
    # Añadir el nombre del sistema a cada análisis funcional
    for analisis in analisis_funcionales:
        analisis['sistema_nombre'] = sistema_nombre

    return render_template('mostrar_analisis_funcional.html', analisis_funcionales=analisis_funcionales,sistema=sistema)

@app.route('/LSA/equipo/analisis_funcional/editar/<int:id>', methods=['GET', 'POST'])
def editar_analisis_funcional(id):

    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_sistema = user_data.get('id_sistema')
    id_equipo = user_data.get('id_equipo')
    id_equipo_info = user_data.get('id_equipo_info')


    print(f"Token: {token}")
    print(f"id_sistema: {id_sistema}")
    print(f"id_equipo: {id_equipo}")
    print(f"id_equipo_info: {id_equipo_info}")

    # Si no se proporciona id_sistema, el sistema es None
    if id_sistema is None:
        sistema = None
        subsistemas = []
    else:
        # Obtener el sistema usando el id_sistema
        sistema = obtener_sistema_por_id(id_sistema)
        
        # Verificar si el sistema existe
        if sistema:
            # Obtener los subsistemas asociados al equipo
            subsistemas = obtener_subsistemas_por_equipo(id_equipo)
        else:
            # Si el sistema no existe, no hay subsistemas
            subsistemas = []

    analisis_funcional = obtener_analisis_funcional_por_id(id)
    

    if request.method == 'POST':
        verbo = request.form['verbo']
        accion = request.form['accion']
        estandar_desempeño = request.form['estandar_desempeño']
        id_subsistema = request.form['subsistema']

        
        # Actualizar el análisis funcional
        actualizar_analisis_funcional(id, verbo, accion, estandar_desempeño, id_subsistema)
        flash('Análisis funcional actualizado correctamente')
        return redirect(url_for('mostrar_analisis_funcional'))
    
    return render_template('editar_analisis_funcional.html', 
                               analisis_funcional=analisis_funcional, 
                               sistema=sistema, 
                               subsistemas=subsistemas)

# Ruta para eliminar un análisis funcional
@app.route('/analisis_funcional/eliminar/<int:id>', methods=['POST'])
def eliminar_analisis_funcional_route(id):
    eliminar_analisis_funcional(id)
    flash('Análisis funcional eliminado correctamente')
    return redirect(url_for('mostrar_analisis_funcional'))

# Ruta API para insertar un nuevo análisis funcional (usado por JavaScript)
@app.route('/api/analisis-funcional', methods=['POST'])
def api_insertar_analisis_funcional():
    data = request.get_json()
    verbo = data.get('verbo')
    accion = data.get('accion')
    estandar_desempeño = data.get('estandar_desempeño')
    id_equipo_info = session.get('id_equipo_info')
    id_subsistema = data.get('subsistema')
    insertar_analisis_funcional(verbo, accion, estandar_desempeño, id_equipo_info, id_subsistema)
    return jsonify({'status': 'success'})




""""
ciber
# Ruta para registrar un nuevo análisis funcional
@app.route('/registro_analisis_funcional', methods=['GET'])
def registro_analisis_funcional():
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')
    sistema_nombre = obtener_nombre_sistema_por_id(id_equipo_info)
    subsistemas = obtener_subsistemas_por_equipo_mostrar(id_equipo_info)
    return render_template('registro_analisis_funcional.html', sistema_nombre=sistema_nombre, subsistemas=subsistemas)
    """





if __name__ == '__main__':
    app.run()
