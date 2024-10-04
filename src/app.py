from flask import Flask, render_template, request, jsonify, redirect, url_for, make_response, g, send_file
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
    obtener_repuesto_por_id
)
from __init__ import create_app


app = Flask(__name__)
app = create_app()
app.config.from_object(config['development'])
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = 'tu_clave_secreta'

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
        imagen = request.files.get('imagen_equipo')
        diagrama_flujo = request.files.get('diagrama_flujo')
        diagrama_caja_negra = request.files.get('diagrama_caja_negra')
        diagrama_caja_transparente = request.files.get('diagrama_caja_transparente')
        # Insertar en la tabla procedimientos
        id_procedimiento = insertar_procedimiento(procedimiento_arranque, procedimiento_parada)
        # Insertar en la tabla diagramas
        id_diagrama = insertar_diagrama(diagrama_flujo, diagrama_caja_negra, diagrama_caja_transparente)



        print(f"Nombre del tipo de equipo recibido: {id_equipo}")
       

        # Insertar en la tabla equipo_infos
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
    
    data = request.get_json()
    
    sistema_id = data.get('sistema')
    subsistema_id = data.get('subsistema')
    verbo = data.get('verbo')
    accion = data.get('accion')
    estandar_desempeño = data.get('estandar_desempeño')
    
    # Validar los datos recibidos (puedes agregar más validaciones)
    if not sistema_id or not subsistema_id or not verbo or not accion or not estandar_desempeño or not id_equipo_info:
        return jsonify({'error': 'Faltan datos obligatorios'}), 400
    
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

def guardar_info_usuario(token, id_sistema=None, id_equipo=None, id_equipo_info=None, usuario_id=None):
    
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
    else:

        usuario_info_temporal[token] = {
            'id_sistema': id_sistema,
            'id_equipo': id_equipo,
            'id_equipo_info': id_equipo_info,
            'usuario_id': usuario_id
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





@app.route('/LSA/mostrar-herramientas-especiales', methods=['GET'])
def mostrar_herramientas_especiales():
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')

    if id_equipo_info is None:
        return redirect(url_for('registro_generalidades'))

    herramientas = obtener_herramientas_especiales_por_equipo_info(id_equipo_info)
    return render_template('mostrar_herramientas_especiales.html', herramientas=herramientas)



@app.route('/api/herramientas-especiales', methods=['POST'])
def agregar_herramienta_especial():
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')

    if id_equipo_info is None:
        return jsonify({'error': 'Faltan datos obligatorios'}), 400

    # Obtener datos del formulario
    nombre_herramienta = request.form.get('nombre_herramienta')
    valor = request.form.get('valor')
    parte_numero = request.form.get('parte_numero')
    mtbf = request.form.get('mtbf')
    dibujo_seccion_transversal = request.files.get('dibujo_seccion_transversal')
    nota = request.form.get('nota')
    manual_referencia = request.form.get('manual_referencia')

    # Procesar imagen si existe
    dibujo_data = dibujo_seccion_transversal.read() if dibujo_seccion_transversal else None

    # Insertar en la base de datos
    herramienta_id = insertar_herramienta_especial(
        id_equipo_info, nombre_herramienta, valor, parte_numero,
        mtbf, dibujo_data, nota, manual_referencia
    )

    return jsonify({'message': 'Herramienta especial agregada', 'id': herramienta_id}), 200



@app.route('/LSA/editar-herramienta-especial/<int:id_herramienta>', methods=['GET'])
def editar_herramienta_especial(id_herramienta):
    token = g.user_token
    user_data = obtener_info_usuario(token)
    id_equipo_info = user_data.get('id_equipo_info')

    if id_equipo_info is None:
        return redirect(url_for('registro_generalidades'))

    herramienta = obtener_herramienta_especial_por_id(id_herramienta)

    if not herramienta:
        return 'Herramienta no encontrada', 404

    return render_template('editar_herramienta_especial.html', herramienta=herramienta)


@app.route('/api/herramientas-especiales/<int:id_herramienta>', methods=['POST'])
def actualizar_herramienta_especial(id_herramienta):
    # Obtener datos del formulario
    nombre_herramienta = request.form.get('nombre_herramienta')
    valor = request.form.get('valor')
    parte_numero = request.form.get('parte_numero')
    mtbf = request.form.get('mtbf')
    dibujo_seccion_transversal = request.files.get('dibujo_seccion_transversal')
    nota = request.form.get('nota')
    manual_referencia = request.form.get('manual_referencia')

    # Procesar imagen si existe
    dibujo_data = dibujo_seccion_transversal.read() if dibujo_seccion_transversal else None

    # Actualizar en la base de datos
    actualizar_herramienta_especial(
        id_herramienta, nombre_herramienta, valor, parte_numero,
        mtbf, dibujo_data, nota, manual_referencia
    )

    return jsonify({'message': 'Herramienta especial actualizada correctamente'}), 200



@app.route('/api/herramientas-especiales/<int:id_herramienta>', methods=['DELETE'])
def eliminar_herramienta_especial(id_herramienta):
    eliminar_herramienta_especial_db(id_herramienta)
    return jsonify({'message': 'Herramienta especial eliminada correctamente'}), 200























@app.route('/LSA/equipo/editar-analisis-funcional')
def editar_analisis_funcional():
    return render_template('editar_analisis_funcional.html')

@app.route('/LSA/equipo/editar-FMEA')
def editar_FMEA():
    return render_template('editar_FMEA.html')

@app.route('/LSA/equipo/editar-modulo-herramientas')
def editar_modulo_herramientas():
    return render_template('editar_herramientas-especiales.html')

@app.route('/LSA/equipo/editar-analisis-herramientas')
def editar_analisis_herramientas():
    return render_template('editar_analisis_herramientas.html')

@app.route('/LSA/equipo/editar-herramientas-especiales')
def editar_herramientas_especiales():
    return render_template('editar_herramientas_especiales2.html')



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

@app.route('/LSA/equipo/mostrar-informe')
def mostrar_informe():
    return render_template('mostrar_informe.html')

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
"""
@app.route('/LSA/registro-analisis-funcional')
def registro_analisis_funcional():
    return render_template('registro_analisis_funcional.html')
"""
@app.route('/LSA/registro-herramientas-especiales')
def registro_herramientas_especiales():
    return render_template('registro_herramientas_especiales.html')


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


if __name__ == '__main__':
    app.run()








