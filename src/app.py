from flask import Flask, render_template, request, jsonify, redirect, url_for, make_response, g, send_file
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
    obtener_usuario_por_correo
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

@app.route('/LSA/registro-analisis-funcional')
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








