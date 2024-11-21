from flask import jsonify
from __init__ import db
import MySQLdb.cursors
from functools import wraps





def insertar_componente_analisis_funcional(id_analisis_funcional, id_componente, verbo, accion):
    # Conexión a la base de datos
    cursor = db.connection.cursor()
    
    # Insertar los datos del componente relacionado con el análisis funcional
    query = """
    INSERT INTO `componente_analisis_funcional`(`id_componente`, `verbo`, `accion`, `id_analisis_funcional`)
    VALUES (%s, %s, %s, %s)
    """
    print(f"Query: {query}")
    print(f"Valores: id_componente={id_componente}, verbo={verbo}, accion={accion}, id_analisis_funcional={id_analisis_funcional}")
    
    cursor.execute(query, (id_componente, verbo, accion, id_analisis_funcional))
    db.connection.commit()

    cursor.close()


def obtener_componentes_por_subsistema(subsistema_id):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM componentes WHERE subsistema_id = %s"
    cursor.execute(query, (subsistema_id,))
    componentes = cursor.fetchall()
    cursor.close()
    return componentes

def insertar_componente_analisis_funcional(id_analisis_funcional, id_componente, verbo, accion):
    """
    Inserta un componente relacionado con un análisis funcional en la base de datos.
    Si `verbo` o `accion` están vacíos, se guardan como NULL en la base de datos.
    
    """
    # Conexión a la base de datos
    cursor = db.connection.cursor()

    # Convertir valores vacíos a None para que se guarden como NULL en la base de datos
    verbo = verbo if verbo else None
    accion = accion if accion else None

    # Insertar los datos del componente relacionado con el análisis funcional
    query = """
    INSERT INTO `componente_analisis_funcional`(`id_componente`, `verbo`, `accion`, `id_analisis_funcional`)
    VALUES (%s, %s, %s, %s)
    """
    print(f'\n\n\nInsertar componentes:')
    print(f"Query: {query}")
    print(f"Valores: id_componente={id_componente}, verbo={verbo}, accion={accion}, id_analisis_funcional={id_analisis_funcional}\n\n\n")

    # Ejecutar la consulta
    cursor.execute(query, (id_componente, verbo, accion, id_analisis_funcional))
    db.connection.commit()

    # Cerrar el cursor
    cursor.close()


def actualizar_componente_analisis_funcional(id_analisis_funcional, id_componente, verbo, accion):
    # Conexión a la base de datos
    cursor = db.connection.cursor()

    # Insertar los datos del componente relacionado con el análisis funcional
    query = """
    INSERT INTO `componente_analisis_funcional`(`id_componente`, `verbo`, `accion`, `id_analisis_funcional`)
    VALUES (%s, %s, %s, %s)
    """
    print(f'\n\n\n\nActualizar componentea:')
    print(f"Query: {query}")
    print(f"Valores: id_componente={id_componente}, verbo={verbo}, accion={accion}, id_analisis_funcional={id_analisis_funcional}\n\n\n")

    cursor.execute(query, (id_componente, verbo, accion, id_analisis_funcional))
    db.connection.commit()

    cursor.close()


def verificar_conexion():
    try:
        cursor = db.connection.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        return {"status": "success", "message": "Database connection successful"}, 200
    except db.connection.Error as e:
        return {"status": "error", "message": str(e)}, 500


def obtener_grupos_constructivos():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id, numeracion, nombre FROM grupo_constructivo ORDER BY numeracion"
    cursor.execute(query)
    grupos = cursor.fetchall()
    cursor.close()
    return grupos


def obtener_subgrupos(id_grupo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id, numeracion, nombre FROM subgrupo WHERE id_grupo_constructivo = %s ORDER BY numeracion"
    cursor.execute(query, (id_grupo,))
    subgrupos = cursor.fetchall()
    cursor.close()
    return subgrupos


def obtener_sistemas(id_subgrupo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id, numeracion, nombre FROM sistema WHERE id_subgrupo = %s ORDER BY numeracion"
    cursor.execute(query, (id_subgrupo,))
    sistemas = cursor.fetchall()
    cursor.close()
    return sistemas


def obtener_equipos(id_sistema):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id, nombre_equipo FROM equipo_info WHERE id_sistema = %s ORDER BY nombre_equipo"
    cursor.execute(query, (id_sistema,))
    equipos = cursor.fetchall()
    cursor.close()
    return equipos


def obtener_personal():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id, nombre_completo FROM personal ORDER BY nombre_completo"
    cursor.execute(query)
    personal = cursor.fetchall()
    cursor.close()
    return personal


def obtener_tipos_equipos():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id, nombre FROM tipo_equipos ORDER BY nombre"
    cursor.execute(query)
    tipos = cursor.fetchall()
    cursor.close()
    return tipos


def buscar_subgrupos(busqueda, id_grupo):
    cursor = db.connection.cursor()
    query = "SELECT id, numeracion, nombre FROM subgrupo WHERE id_grupo_constructivo = %s AND nombre LIKE %s ORDER BY numeracion"
    cursor.execute(query, (id_grupo, '%' + busqueda + '%'))
    subgrupos = cursor.fetchall()
    cursor.close()
    return subgrupos


def buscar_sistemas(busqueda, id_subgrupo):
    cursor = db.connection.cursor()
    query = "SELECT id, numeracion, nombre FROM sistema WHERE id_subgrupo = %s AND nombre LIKE %s ORDER BY numeracion"
    cursor.execute(query, (id_subgrupo, '%' + busqueda + '%'))
    sistemas = cursor.fetchall()
    cursor.close()
    return sistemas


def buscar_equipos(busqueda, id_sistema=None):
    cursor = db.connection.cursor()
    if id_sistema:
        query = "SELECT id, nombre_equipo FROM equipo_info WHERE id_sistema = %s AND nombre_equipo LIKE %s ORDER BY nombre_equipo"
        cursor.execute(query, (id_sistema, '%' + busqueda + '%'))
    else:
        query = "SELECT id, nombre_equipo FROM equipo_info WHERE nombre_equipo LIKE %s ORDER BY nombre_equipo"
        cursor.execute(query, ('%' + busqueda + '%',))
    equipos = cursor.fetchall()
    cursor.close()
    return equipos


def obtener_personal():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre_completo FROM personal ORDER BY nombre_completo"
    cursor.execute(query)
    personal = cursor.fetchall()
    cursor.close()
    return personal


def obtener_tipos_equipos():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre FROM tipo_equipos ORDER BY nombre"
    cursor.execute(query)
    tipos_equipos = cursor.fetchall()
    cursor.close()
    return tipos_equipos


#Funciones para FMEA

#Obtener datos desplegables

def obtener_fallos_ocultos():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre, valor FROM fallo_oculto"
    cursor.execute(query)
    fallos_ocultos = cursor.fetchall()

    cursor.close()

    return [{'id': fila['id'], 'nombre': fila['nombre'], 'valor': fila['valor']} for fila in fallos_ocultos]


def obtener_seguridad_fisica():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre, valor FROM seguridad_fisica"
    cursor.execute(query)
    seguridad_fisica = cursor.fetchall()
    cursor.close()

    return [{'id': fila['id'], 'nombre': fila['nombre'], 'valor': fila['valor']} for fila in seguridad_fisica]


def obtener_medio_ambiente():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre, valor FROM medio_ambiente"
    cursor.execute(query)
    medio_ambiente_datos = cursor.fetchall()
    cursor.close()

    return [{'id': fila['id'], 'nombre': fila['nombre'], 'valor': fila['valor']} for fila in medio_ambiente_datos]


def obtener_impacto_operacional():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre, valor FROM impacto_operacional"
    cursor.execute(query)
    impacto_operacional_datos = cursor.fetchall()
    cursor.close()

    return [{'id': fila['id'], 'nombre': fila['nombre'], 'valor': fila['valor']} for fila in impacto_operacional_datos]


def obtener_costos_reparacion():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre, valor FROM costos_reparacion"
    cursor.execute(query)
    costos_reparacion_datos = cursor.fetchall()
    cursor.close()

    return [{'id': fila['id'], 'nombre': fila['nombre'], 'valor': fila['valor']} for fila in costos_reparacion_datos]


def obtener_flexibilidad_operacional():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre, valor FROM flexibilidad_operacional"
    cursor.execute(query)
    flexibilidad_operacional_datos = cursor.fetchall()
    cursor.close()

    return [{'id': fila['id'], 'nombre': fila['nombre'], 'valor': fila['valor']} for fila in
            flexibilidad_operacional_datos]


def obtener_Ocurrencia():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre, valor FROM ocurrencia"
    cursor.execute(query)
    ocurrencia_datos = cursor.fetchall()
    cursor.close()

    return [{'id': fila['id'], 'nombre': fila['nombre'], 'valor': fila['valor']} for fila in ocurrencia_datos]


def obtener_probablilidad_deteccion():
    cursor = db.connection.cursor()
    query = "SELECT id, descripcion, valor FROM probabilidad_deteccion"
    cursor.execute(query)
    probabilidad_deteccion_datos = cursor.fetchall()
    cursor.close()

    return [{'id': fila['id'], 'descripcion': fila['descripcion'], 'valor': fila['valor']} for fila in
            probabilidad_deteccion_datos]


def obtener_componentes_por_subsistema(subsistema_id):
    cursor = db.connection.cursor()

    query = """
        SELECT id, nombre 
        FROM componentes 
        WHERE id_subsistemas = %s
    """
    cursor.execute(query, (subsistema_id,))
    componentes = cursor.fetchall()
    cursor.close()

    # Convertir los resultados en una lista de diccionarios

    return [{'id': c['id'], 'nombre': c['nombre']} for c in componentes]


def obtener_mecanismos_falla():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre FROM mecanismo_falla"
    cursor.execute(query)
    mecanismos_falla = cursor.fetchall()
    cursor.close()
    return [{'id': fila['id'], 'nombre': fila['nombre']} for fila in mecanismos_falla]


def obtener_detalles_falla_por_mecanismo(id_mecanismo_falla):
    cursor = db.connection.cursor()
    query = """
        SELECT id, nombre 
        FROM detalle_falla
        WHERE id_mecanismo_falla = %s
    """
    cursor.execute(query, (id_mecanismo_falla,))
    detalles_falla = cursor.fetchall()
    cursor.close()
    print(f"Detalles de falla para id_mecanismo_falla {id_mecanismo_falla}: {detalles_falla}")
    return [{'id': fila['id'], 'nombre': fila['nombre']} for fila in detalles_falla]


def obtener_codigos_modo_falla():
    cursor = db.connection.cursor()
    query = "SELECT id, codigo, nombre FROM codigo_modo_falla"
    cursor.execute(query)
    codigos = cursor.fetchall()
    cursor.close()
    return [{'id': fila['id'], 'codigo': fila['codigo'], 'nombre': fila['nombre']} for fila in codigos]


def obtener_metodos_deteccion_falla():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre FROM metodo_deteccion_falla"
    cursor.execute(query)
    metodos_deteccion_falla = cursor.fetchall()
    cursor.close()

    return [{'id': fila['id'], 'nombre': fila['nombre']} for fila in metodos_deteccion_falla]


#Esta no es para un desplegable pero retorna una lista de la misma manera
def obtener_lista_riesgos():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre FROM riesgo ORDER BY id"
    cursor.execute(query)
    riesgos = cursor.fetchall()
    cursor.close()

    # Verificar la lista obtenida antes de retornarla
    print("Lista de riesgos obtenida:", riesgos)

    return [{'id': riesgo['id'], 'nombre': riesgo['nombre']} for riesgo in riesgos]


#Obtener id para FMEA
def obtener_id_equipo_info_por_fmea(fmea_id):
    cursor = db.connection.cursor()
    query = """
    SELECT id_equipo_info 
    FROM fmea 
    WHERE id = %s
    """

    cursor.execute(query, (fmea_id,))
    resultado = cursor.fetchone()
    cursor.close()

    if resultado:
        return resultado['id_equipo_info']  # Retorna el id_equipo_info si lo encuentra
    else:
        return None  # Si no encuentra el fmea_id, retorna None


def obtener_id_sistema_por_fmea_id(fmea_id):
    cursor = db.connection.cursor()
    query = """
    SELECT id_sistema 
    FROM fmea 
    WHERE id = %s
    """

    cursor.execute(query, (fmea_id,))
    resultado = cursor.fetchone()
    cursor.close()

    if resultado:
        return resultado['id_sistema']
    else:
        return None


def obtener_id_componente_por_fmea_id(fmea_id):
    cursor = db.connection.cursor()
    query = """
    SELECT id_componente
    FROM fmea
    WHERE id = %s
    """
    cursor.execute(query, (fmea_id,))
    componente = cursor.fetchone()
    cursor.close()

    return componente['id_componente'] if componente else None


def obtener_id_subsistema_por_componente_id(id_componente):
    cursor = db.connection.cursor()
    query = """
    SELECT id_subsistemas
    FROM componentes
    WHERE id = %s
    """
    cursor.execute(query, (id_componente,))
    subsistema_id = cursor.fetchone()
    cursor.close()

    return subsistema_id['id_subsistemas'] if subsistema_id else None


##Insertar en sus respectivas tablas los datos que devuelven el id para la tabla de fmea

#funcion con la queverificamos en cada uno que los datos no existan para incertarlos y si ya estan simplemente se referencian esos
def obtener_id_si_existe(query, params):
    cursor = db.connection.cursor()
    cursor.execute(query, params)
    resultado = cursor.fetchone()
    cursor.close()
    return resultado['id'] if resultado else None


def insertar_falla_funcional(falla_funcional_nombre):
    query_existencia = "SELECT id FROM falla_funcional WHERE nombre = %s"
    falla_funcional_id = obtener_id_si_existe(query_existencia, (falla_funcional_nombre,))

    if falla_funcional_id:
        return falla_funcional_id

    cursor = db.connection.cursor()
    query = "INSERT INTO falla_funcional (nombre) VALUES (%s)"
    cursor.execute(query, (falla_funcional_nombre,))
    db.connection.commit()
    falla_funcional_id = cursor.lastrowid
    cursor.close()
    return falla_funcional_id


def insertar_descripcion_modo_falla(descripcion_modo_falla):
    query_existencia = "SELECT id FROM descripcion_modo_falla WHERE nombre = %s"
    descripcion_modo_falla_id = obtener_id_si_existe(query_existencia, (descripcion_modo_falla,))

    if descripcion_modo_falla_id:
        return descripcion_modo_falla_id

    cursor = db.connection.cursor()
    query = "INSERT INTO descripcion_modo_falla (nombre) VALUES (%s)"
    cursor.execute(query, (descripcion_modo_falla,))
    db.connection.commit()
    descripcion_modo_falla_id = cursor.lastrowid
    cursor.close()
    return descripcion_modo_falla_id


def insertar_causa(nombre_causa):
    query_existencia = "SELECT id FROM causa WHERE nombre = %s"
    causa_id = obtener_id_si_existe(query_existencia, (nombre_causa,))

    if causa_id:
        return causa_id

    cursor = db.connection.cursor()
    query = "INSERT INTO causa (nombre) VALUES (%s)"
    cursor.execute(query, (nombre_causa,))
    db.connection.commit()
    causa_id = cursor.lastrowid
    cursor.close()
    return causa_id


################################################################################################################

#Fmea Registro
def insertar_fmea(id_equipo_info, id_sistema, id_falla_funcional, id_componente, id_codigo_modo_falla,
                  id_consecutivo_modo_falla, id_descripcion_modo_falla, id_causa, id_mecanismo_falla,
                  id_detalle_falla, MTBF, MTTR, id_metodo_deteccion_falla, id_fallo_oculto, id_seguridad_fisica,
                  id_medio_ambiente,
                  id_impacto_operacional, id_costos_reparacion, id_flexibilidad_operacional, calculo_severidad,
                  id_ocurrencia, ocurrencia_mate,
                  id_probabilidad_deteccion, rpn, id_riesgo):
    cursor = db.connection.cursor()
    query = """
        INSERT INTO fmea (
            id_equipo_info, id_sistema, id_falla_funcional, id_componente, id_codigo_modo_falla, 
            id_consecutivo_modo_falla, id_descripcion_modo_falla, id_causa, id_mecanismo_falla, 
            id_detalle_falla, MTBF, MTTR,id_metodo_deteccion_falla, id_fallo_oculto, id_seguridad_fisica, id_medio_ambiente, 
            id_impacto_operacional, id_costos_reparacion, id_flexibilidad_operacional,calculo_severidad, id_ocurrencia, ocurrencia_mate,
            id_probabilidad_deteccion, RPN, id_riesgo
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)

    """
    cursor.execute(query, (
        id_equipo_info, id_sistema, id_falla_funcional, id_componente, id_codigo_modo_falla,
        id_consecutivo_modo_falla, id_descripcion_modo_falla, id_causa, id_mecanismo_falla,
        id_detalle_falla, MTBF, MTTR, id_metodo_deteccion_falla, id_fallo_oculto, id_seguridad_fisica,
        id_medio_ambiente,
        id_impacto_operacional, id_costos_reparacion, id_flexibilidad_operacional, calculo_severidad, id_ocurrencia,


        ocurrencia_mate, id_probabilidad_deteccion, rpn, id_riesgo

    ))
    db.connection.commit()
    fmea_id = cursor.lastrowid
    cursor.close()
    return fmea_id


########################################################################

#Funciones para mostrar fmea

#funcion para poder obtener los nombres que estan ligados al id resgistrados en una tabla


def obtener_nombre_por_id(tabla, id, columna_id='id'):

    cursor = db.connection.cursor()

    # Verificar si la tabla tiene la columna 'nombre'
    query_column_check = f"SHOW COLUMNS FROM {tabla} LIKE 'nombre'"
    cursor.execute(query_column_check)
    columna_existe = cursor.fetchone()

    if columna_existe:  # Si la columna 'nombre' existe


        # Usar el nombre de columna dinámico en el WHERE
        query = f"SELECT nombre FROM {tabla} WHERE {columna_id} = %s"

        cursor.execute(query, (id,))
        resultado = cursor.fetchone()
        cursor.close()

        if resultado:
            return resultado['nombre']

    else:

        cursor.close()
        return None

    return None



def obtener_fmeas(id_equipo_info):
    print(f"Llamada a obtener_fmeas con id_equipo_info={id_equipo_info}")


    cursor = db.connection.cursor()

    # Realizamos la consulta
    query = """
    SELECT 
        f.id, 
        f.id_equipo_info, 
        f.id_sistema, 
        s.nombre AS sistema, 
        f.id_falla_funcional, 
        ff.nombre AS falla_funcional, 
        f.id_componente, 
        c.nombre AS componente, 
        f.id_codigo_modo_falla, 
        cmf.nombre AS codigo_modo_falla, 
        f.id_consecutivo_modo_falla, 
        cf.nombre AS consecutivo_modo_falla, 
        f.id_descripcion_modo_falla, 
        dmf.nombre AS descripcion_modo_falla, 
        f.id_causa, 
        causa.nombre AS causa, 
        f.id_mecanismo_falla, 
        mf.nombre AS mecanismo_falla, 
        f.id_detalle_falla, 
        df.nombre AS detalle_falla, 
        f.MTBF, 
        f.MTTR, 
        f.id_metodo_deteccion_falla,
        f.id_fallo_oculto,
        fo.valor AS fallo_oculto_valor, 
        fo.nombre AS fallo_oculto_descripcion, 
        f.id_seguridad_fisica, 
        sf.valor AS seguridad_fisica_valor, 
        sf.nombre AS seguridad_fisica_descripcion, 
        f.id_medio_ambiente, 
        ma.valor AS medio_ambiente_valor, 
        ma.nombre AS medio_ambiente_descripcion, 
        f.id_impacto_operacional, 
        io.valor AS impacto_operacional_valor, 
        io.nombre AS impacto_operacional_descripcion, 
        f.id_costos_reparacion, 
        cr.valor AS costos_reparacion_valor, 
        cr.nombre AS costos_reparacion_descripcion, 
        f.id_flexibilidad_operacional, 
        flex.valor AS flexibilidad_operacional_valor, 
        flex.nombre AS flexibilidad_operacional_descripcion, 
        f.calculo_severidad,
        f.id_ocurrencia, 
        o.valor AS ocurrencia_valor, 
        o.nombre AS ocurrencia_descripcion, 
        f.ocurrencia_mate, 
        f.id_probabilidad_deteccion, 
        pd.valor AS probabilidad_deteccion_valor, 
        pd.descripcion AS probabilidad_deteccion_descripcion,
        f.RPN,
        f.id_riesgo,

        r.nombre AS nombre_riesgo,
        p.nombre_completo AS nombre_completo,
        p.id AS id_personal
      FROM fmea f
    LEFT JOIN equipo_info ei ON f.id_equipo_info = ei.id
    LEFT JOIN personal p ON ei.id_personal = p.id
    LEFT JOIN subsistemas s ON f.id_sistema = s.id
    LEFT JOIN falla_funcional ff ON f.id_falla_funcional = ff.id
    LEFT JOIN componentes c ON f.id_componente = c.id
    LEFT JOIN codigo_modo_falla cmf ON f.id_codigo_modo_falla = cmf.id
    LEFT JOIN consecutivo_modo_falla cf ON f.id_consecutivo_modo_falla = cf.id
    LEFT JOIN descripcion_modo_falla dmf ON f.id_descripcion_modo_falla = dmf.id
    LEFT JOIN causa ON f.id_causa = causa.id
    LEFT JOIN mecanismo_falla mf ON f.id_mecanismo_falla = mf.id
    LEFT JOIN detalle_falla df ON f.id_detalle_falla = df.id
    LEFT JOIN fallo_oculto fo ON f.id_fallo_oculto = fo.id
    LEFT JOIN seguridad_fisica sf ON f.id_seguridad_fisica = sf.id
    LEFT JOIN medio_ambiente ma ON f.id_medio_ambiente = ma.id
    LEFT JOIN impacto_operacional io ON f.id_impacto_operacional = io.id
    LEFT JOIN costos_reparacion cr ON f.id_costos_reparacion = cr.id
    LEFT JOIN flexibilidad_operacional flex ON f.id_flexibilidad_operacional = flex.id
    LEFT JOIN ocurrencia o ON f.id_ocurrencia = o.id
    LEFT JOIN probabilidad_deteccion pd ON f.id_probabilidad_deteccion = pd.id
    LEFT JOIN riesgo r ON f.id_riesgo = r.id
    WHERE f.id_equipo_info = %s AND f.estado = 'activo'
    """

    cursor.execute(query, (id_equipo_info,))
    fmeas = cursor.fetchall()
    cursor.close()

    print("Resultados de la consulta FMEAs:", fmeas)


    # Lista para almacenar los FMEAs procesados
    fmeas_completos = []

    # Diccionario para contar las ocurrencias de cada consecutivo_modo_falla
    consecutivo_modo_falla_counter = {}

    # Procesar cada fila de la consulta
    for fmea in fmeas:
        # Verificar si alguna columna no tiene nombre o descripción
        # Y buscar el nombre/valor por ID si es necesario

        #verificaría cada campo:
        sistema_nombre = fmea['sistema'] if fmea['sistema'] else obtener_nombre_por_id('subsistemas',
                                                                                       fmea['id_sistema'])

        falla_funcional_nombre = fmea['falla_funcional'] if fmea['falla_funcional'] else obtener_nombre_por_id(
            'falla_funcional', fmea['id_falla_funcional'])

        componente_nombre = fmea['componente'] if fmea['componente'] else obtener_nombre_por_id('componentes',
                                                                                                fmea['id_componente'])
        codigo_modo_falla_nombre = fmea['codigo_modo_falla'] if fmea['codigo_modo_falla'] else obtener_nombre_por_id(
            'codigo_modo_falla', fmea['id_codigo_modo_falla'])
        consecutivo_modo_falla_nombre = fmea['consecutivo_modo_falla'] if fmea[
            'consecutivo_modo_falla'] else obtener_nombre_por_id('consecutivo_modo_falla',
                                                                 fmea['id_consecutivo_modo_falla'])
        descripcion_modo_falla_nombre = fmea['descripcion_modo_falla'] if fmea[
            'descripcion_modo_falla'] else obtener_nombre_por_id('descripcion_modo_falla',
                                                                 fmea['id_descripcion_modo_falla'])
        causa_nombre = fmea['causa'] if fmea['causa'] else obtener_nombre_por_id('causa', fmea['id_causa'])
        mecanismo_falla_nombre = fmea['mecanismo_falla'] if fmea['mecanismo_falla'] else obtener_nombre_por_id(
            'mecanismo_falla', fmea['id_mecanismo_falla'])
        detalle_falla_nombre = fmea['detalle_falla'] if fmea['detalle_falla'] else obtener_nombre_por_id(
            'detalle_falla', fmea['id_detalle_falla'])

        
        nombre_riesgo = fmea['nombre_riesgo'] or obtener_nombre_por_id('riesgo', fmea['id_riesgo'])


        # Contar las ocurrencias de consecutivo_modo_falla
        if consecutivo_modo_falla_nombre not in consecutivo_modo_falla_counter:
            consecutivo_modo_falla_counter[consecutivo_modo_falla_nombre] = 0
        consecutivo_modo_falla_counter[consecutivo_modo_falla_nombre] += 1

        # Concatenar la numeración al consecutivo_modo_falla
        consecutivo_modo_falla_numerado = f"{consecutivo_modo_falla_nombre}-{consecutivo_modo_falla_counter[consecutivo_modo_falla_nombre]}"

        # Añadir el FMEA procesado a la lista
        fmeas_completos.append({
            'id': fmea['id'],
            'id_equipo_info': fmea['id_equipo_info'],
            'id_sistema': fmea['id_sistema'],
            'sistema': sistema_nombre,
            'id_falla_funcional': fmea['id_falla_funcional'],
            'falla_funcional': falla_funcional_nombre,
            'id_descripcion_modo_falla': fmea['id_descripcion_modo_falla'],
            'componente': componente_nombre,
            'codigo_modo_falla': codigo_modo_falla_nombre,
            'consecutivo_modo_falla': consecutivo_modo_falla_nombre,
            'descripcion_modo_falla': descripcion_modo_falla_nombre,
            'causa': causa_nombre,
            'mecanismo_falla': mecanismo_falla_nombre,
            'detalle_falla': detalle_falla_nombre,
            'MTBF': fmea['MTBF'],
            'MTTR': fmea['MTTR'],
            'fallo_oculto_valor': fmea['fallo_oculto_valor'],
            'fallo_oculto_descripcion': fmea['fallo_oculto_descripcion'],
            'seguridad_fisica_valor': fmea['seguridad_fisica_valor'],
            'seguridad_fisica_descripcion': fmea['seguridad_fisica_descripcion'],
            'medio_ambiente_valor': fmea['medio_ambiente_valor'],
            'medio_ambiente_descripcion': fmea['medio_ambiente_descripcion'],
            'impacto_operacional_valor': fmea['impacto_operacional_valor'],
            'impacto_operacional_descripcion': fmea['impacto_operacional_descripcion'],
            'costos_reparacion_valor': fmea['costos_reparacion_valor'],
            'costos_reparacion_descripcion': fmea['costos_reparacion_descripcion'],
            'flexibilidad_operacional_valor': fmea['flexibilidad_operacional_valor'],
            'flexibilidad_operacional_descripcion': fmea['flexibilidad_operacional_descripcion'],
            'ocurrencia_valor': fmea['ocurrencia_valor'],
            'ocurrencia_descripcion': fmea['ocurrencia_descripcion'],
            'ocurrencia_mate': fmea['ocurrencia_mate'],  # Añadir este campo
            'calculo_severidad': fmea['calculo_severidad'],
            'probabilidad_deteccion_valor': fmea['probabilidad_deteccion_valor'],
            'probabilidad_deteccion_descripcion': fmea['probabilidad_deteccion_descripcion'],
            'RPN': fmea['RPN'],
            'id_riesgo': fmea['id_riesgo'],
            'nombre_riesgo': nombre_riesgo,
            'nombre_completo': fmea['nombre_completo'],
            'id_personal': fmea['id_personal']

        })
    print("FMEAs completos procesados:", fmeas_completos)

    return fmeas_completos


#########################

#fmea editar y eliminar
def obtener_fmea_por_id(fmea_id, id_equipo_info):
    # Obtener la lista completa de FMEAs con nombres procesados
    fmeas_completos = obtener_fmeas(id_equipo_info)

    # Buscar el FMEA por el ID en la lista completa
    fmea_filtrado = next((fmea for fmea in fmeas_completos if fmea['id'] == fmea_id), None)

    # Si se encuentra el FMEA, lo devolvemos, si no, devolvemos None
    if fmea_filtrado:
        print(fmea_filtrado)
        return fmea_filtrado
    else:
        return None


def obtener_ID_FMEA(fmea_id):
    cursor = db.connection.cursor()

    query = "SELECT * FROM fmea WHERE id = %s AND estado = 'activo'"

    cursor.execute(query, (fmea_id,))
    fmea = cursor.fetchone()
    cursor.close()

    return fmea


def actualizar_fmea(
        fmea_id, id_equipo_info, sistema_id, id_falla_funcional, id_componente,
        id_codigo_modo_falla, id_consecutivo_modo_falla, id_descripcion_modo_falla,
        id_causa, id_mecanismo_falla, id_detalle_falla, mtbf, mttr, id_fallo_oculto,
        id_seguridad_fisica, id_medio_ambiente, id_impacto_operacional,
        id_costos_reparacion, id_flexibilidad_operacional, calculo_severidad, id_ocurrencia,
        ocurrencia_mate, id_probabilidad_deteccion, id_metodo_deteccion_falla, rpn, id_riesgo

):
    cursor = db.connection.cursor()
    query = """
        UPDATE fmea SET
            id_equipo_info = %s, id_sistema = %s, id_falla_funcional = %s, 
            id_componente = %s, id_codigo_modo_falla = %s, id_consecutivo_modo_falla = %s, 
            id_descripcion_modo_falla = %s, id_causa = %s, id_mecanismo_falla = %s, 
            id_detalle_falla = %s, MTBF = %s, MTTR = %s, id_fallo_oculto = %s, 
            id_seguridad_fisica = %s, id_medio_ambiente = %s, id_impacto_operacional = %s, 
            id_costos_reparacion = %s, id_flexibilidad_operacional = %s, calculo_severidad = %s, id_ocurrencia = %s, 
            ocurrencia_mate = %s, id_probabilidad_deteccion = %s, id_metodo_deteccion_falla = %s, RPN = %s, id_riesgo = %s

        WHERE id = %s
    """
    cursor.execute(query, (
        id_equipo_info, sistema_id, id_falla_funcional, id_componente, id_codigo_modo_falla,
        id_consecutivo_modo_falla, id_descripcion_modo_falla, id_causa, id_mecanismo_falla,
        id_detalle_falla, mtbf, mttr, id_fallo_oculto, id_seguridad_fisica, id_medio_ambiente,
        id_impacto_operacional, id_costos_reparacion, id_flexibilidad_operacional, calculo_severidad,
        id_ocurrencia, ocurrencia_mate, id_probabilidad_deteccion, id_metodo_deteccion_falla, rpn, id_riesgo,

        fmea_id

    ))
    db.connection.commit()
    cursor.close()


##################################################################################################################

def obtener_aor_por_id_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT AOR FROM equipo_info WHERE id = %s"
    cursor.execute(query, (id_equipo_info,))
    resultado = cursor.fetchone()
    cursor.close()
    if resultado:
        return resultado['AOR']
    else:
        return None

def insertar_procedimiento(arranque, parada):
    cursor = db.connection.cursor()
    query = "INSERT INTO procedimientos (arranque, parada) VALUES (%s, %s)"
    cursor.execute(query, (arranque, parada))
    db.connection.commit()
    procedimiento_id = cursor.lastrowid
    cursor.close()
    return procedimiento_id


def insertar_diagrama(diagrama_flujo, diagrama_caja_negra, diagrama_caja_transparente):
    cursor = db.connection.cursor()

    query = "INSERT INTO diagramas (diagrama_flujo, diagrama_caja_negra, diagrama_caja_transparente) VALUES (%s, %s, %s)"
    cursor.execute(query, (diagrama_flujo, diagrama_caja_negra, diagrama_caja_transparente))
    db.connection.commit()
    diagrama_id = cursor.lastrowid
    cursor.close()
    return diagrama_id


def insertar_equipo_info(nombre_equipo, AOR, fecha, fiabilidad_equipo, MTBF, GRES, criticidad_equipo,
                         marca, modelo, peso_seco, dimensiones, descripcion, imagen_equipo_file,
                         id_personal, id_diagrama, id_procedimiento, id_sistema, id_equipo
                         ):
    cursor = db.connection.cursor()

    query = """
        INSERT INTO equipo_info (
            nombre_equipo, AOR, fecha, fiabilidad_equipo, MTBF, GRES, criticidad_equipo,
            marca, modelo, peso_seco, dimensiones, descripcion, imagen,
            id_personal, id_diagrama, id_procedimiento, id_sistema, id_equipo
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        nombre_equipo, AOR, fecha, fiabilidad_equipo, MTBF, GRES, criticidad_equipo,
        marca, modelo, peso_seco, dimensiones, descripcion, imagen_equipo_file,
        id_personal, id_diagrama, id_procedimiento, id_sistema, id_equipo
    ))
    db.connection.commit()
    equipo_info_id = cursor.lastrowid
    cursor.close()
    return equipo_info_id


def obtener_equipos_por_tipo(id_tipo_equipo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id, nombre FROM equipos WHERE id_tipos_equipos = %s ORDER BY nombre"
    cursor.execute(query, (id_tipo_equipo,))
    equipospro = cursor.fetchall()
    cursor.close()
    return equipospro


def obtener_id_equipo_por_id_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id_equipo FROM equipo_info WHERE id=%s;"
    cursor.execute(query, (id_equipo_info,))
    resultado = cursor.fetchone()
    cursor.close()
    return resultado['id_equipo'] if resultado else None


def obtener_sistema_por_id(id_sistema):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM sistema WHERE id = %s"
    cursor.execute(query, (id_sistema,))
    sistema = cursor.fetchone()
    cursor.close()
    return sistema


def obtener_subsistema_por_id(id_subsistema):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM subsistemas WHERE id = %s"
    cursor.execute(query, (id_subsistema,))
    sistema = cursor.fetchone()
    cursor.close()
    return sistema


def obtener_subsistemas_por_equipo(id_equipo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM subsistemas WHERE id_equipo = %s"
    cursor.execute(query, (id_equipo,))
    subsistemas = cursor.fetchall()
    cursor.close()
    return subsistemas


# ... otras funciones ...

def obtener_usuario_por_correo(correo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id, correo, password, nombre_completo FROM personal WHERE correo = %s"
    cursor.execute(query, (correo,))
    usuario = cursor.fetchone()
    cursor.close()
    return usuario


def insertar_analisis_funcional(verbo, accion, estandar_desempeño, id_equipo_info, subsistema_id):
    cursor = db.connection.cursor()
    query = """
            INSERT INTO analisis_funcional (verbo, accion, estandar_desempeño, id_equipo_info,id_subsistema)
            VALUES (%s, %s, %s, %s, %s)
        """
    cursor.execute(query, (verbo, accion, estandar_desempeño, id_equipo_info, subsistema_id,))
    db.connection.commit()
    analisis_funcional_id = cursor.lastrowid
    cursor.close()
    return analisis_funcional_id


###################################################################Funcines para MTA#############################


#insertar_mta(fmea['id_equipo_info'], id_sistema, id_componente, fmea['id_falla_funcional'], fmea['id_descripcion_modo_falla'], id_tipo_mantenimiento, id_tarea_mantenimiento, cantidad_personal, consumibles_requeridos ,requeridos_tarea,condiciones_ambientales, condiciones_estado_equipo, condiciones_especiales,  horas, minutos, detalle_tarea)
def insertar_mta(id_rcm, id_equipo_info, id_sistema, id_componente, id_falla_funcional, id_descripcion_modo_falla,
                 id_tipo_mantenimiento, id_tarea_mantenimiento, cantidad_personal, consumibles_requeridos,
                 requeridos_tarea, condiciones_ambientales, condiciones_estado_equipo, condiciones_especiales, horas,
                 minutos, detalle_tarea):
    cursor = db.connection.cursor()
    query = """
        INSERT INTO mta (
            id_rcm, id_equipo_info, id_sistema, id_componente, id_falla_funcional, id_descripcion_modo_falla, id_tipo_mantenimiento, id_tarea_mantenimiento, cantidad_personal, consumibles_requeridos, requeridos_tarea, condiciones_ambientales, condiciones_estado_equipo, condiciones_especiales, horas, minutos, detalle_tarea
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        id_rcm, id_equipo_info, id_sistema, id_componente, id_falla_funcional, id_descripcion_modo_falla,
        id_tipo_mantenimiento, id_tarea_mantenimiento, cantidad_personal, consumibles_requeridos, requeridos_tarea,
        condiciones_ambientales, condiciones_estado_equipo, condiciones_especiales, horas, minutos, detalle_tarea
    ))
    db.connection.commit()
    mta_id = cursor.lastrowid
    cursor.close()
    return mta_id


def actualizar_mta(id_mta, id_tipo_mantenimiento, id_tarea_mantenimiento, cantidad_personal, consumibles_requeridos,
                   requeridos_tarea, condiciones_ambientales, condiciones_estado_equipo, condiciones_especiales, horas,
                   minutos, detalle_tarea):
    cursor = db.connection.cursor()
    query = """
        UPDATE mta
        SET id_tipo_mantenimiento = %s, id_tarea_mantenimiento = %s, cantidad_personal = %s, consumibles_requeridos = %s, requeridos_tarea = %s, condiciones_ambientales = %s, condiciones_estado_equipo = %s, condiciones_especiales = %s, horas = %s, minutos = %s, detalle_tarea = %s
        WHERE id = %s
    """
    cursor.execute(query, (
        id_tipo_mantenimiento, id_tarea_mantenimiento, cantidad_personal, consumibles_requeridos, requeridos_tarea,
        condiciones_ambientales, condiciones_estado_equipo, condiciones_especiales, horas, minutos, detalle_tarea,
        id_mta
    ))
    db.connection.commit()
    cursor.close()


def eliminar_mta(id_mta):
    cursor = db.connection.cursor()
    # Cambiar el estado a 'inactivo' en lugar de eliminar
    update_query = "UPDATE mta SET estado = 'inactivo' WHERE id = %s"
    cursor.execute(update_query, (id_mta,))
    db.connection.commit()
    cursor.close()


def obtener_mtas_completos():
    cursor = db.connection.cursor()
    query = """
    SELECT 
        m.id, 
        m.id_rcm, 
        m.id_equipo_info, 
        m.id_sistema, 
        m.id_componente, 
        m.id_falla_funcional, 
        m.id_descripcion_modo_falla, 
        m.id_tipo_mantenimiento, 
        m.id_tarea_mantenimiento, 
        m.cantidad_personal, 
        m.consumibles_requeridos, 
        m.requeridos_tarea, 
        m.condiciones_ambientales, 
        m.condiciones_estado_equipo, 
        m.condiciones_especiales, 
        m.horas, 
        m.minutos, 
        m.detalle_tarea,
        ei.nombre_equipo as equipo, 
        s.nombre as sistema, 
        c.nombre as componente, 
        ff.nombre as falla_funcional, 
        dmf.nombre as descripcion_modo_falla, 
        tm.nombre as tipo_mantenimiento, 
        tmr.nombre as tarea_mantenimiento,
        l.nivel,
        l.actividades,
        l.operario        
    FROM mta m
    LEFT JOIN rcm r ON m.id_rcm = r.id
    LEFT JOIN equipo_info ei ON m.id_equipo_info = ei.id
    LEFT JOIN sistema s ON m.id_sistema = s.id
    LEFT JOIN componentes c ON m.id_componente = c.id
    LEFT JOIN falla_funcional ff ON m.id_falla_funcional = ff.id
    LEFT JOIN descripcion_modo_falla dmf ON m.id_descripcion_modo_falla = dmf.id
    LEFT JOIN tipo_mantenimiento tm ON m.id_tipo_mantenimiento = tm.id
    LEFT JOIN tarea_mantenimiento tmr ON m.id_tarea_mantenimiento = tmr.id
    LEFT JOIN lora_mta l ON m.id = l.id_mta
    WHERE m.estado = 'activo'
    """
    cursor.execute(query)
    mtas = cursor.fetchall()
    cursor.close()
    return mtas


def obtener_mta_por_id_rcm(id_rcm):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM mta AS m WHERE m.estado = 'activo' AND m.id_rcm = %s"
    cursor.execute(query, (id_rcm,))
    mta = cursor.fetchone()
    cursor.close()
    return mta



"""
1RO para la funcion de mostrar herramientas necesito que haga una peticion a la base de datos de herramientas
relaciones y que me devuelva todas las herramientas que tienen el id_equipo_info y me va a devolver los datos en la columna id_herramienta y en la id_clase_herramienta
luego un print para ver que me devolivo, despues de eso, voy a hacer otra peticion para mostrar donde en la variable analisis se va a hacer una funcion
que busque en la base de datos de herramientas_generales las que tengan el id_clase_herramienta 1 donde por cada dato que obtuve en el filtrado de herramientas relaciones
voy a hacer una peticion para que se me devulva toda la fila que contiene ese id_herramienta, y la misma logica con herramientas especiales que se guarda en la variable herramientas
"""
#######################
def obtener_herramientas_relacionadas_por_equipo(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT id_herramienta, id_clase_herramienta
        FROM herramientas_relacion
        WHERE id_equipo_info = %s
    """
    cursor.execute(query, (id_equipo_info,))
    herramientas_relacionadas = cursor.fetchall()
    cursor.close()
    return herramientas_relacionadas

def obtener_detalle_herramienta_general(id_herramienta):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT * FROM herramientas_generales
        WHERE id = %s
    """
    cursor.execute(query, (id_herramienta,))
    herramienta_general = cursor.fetchone()
    cursor.close()
    return herramienta_general

def obtener_detalle_herramienta_especial(id_herramienta):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT * FROM herramientas_especiales
        WHERE id = %s
    """
    cursor.execute(query, (id_herramienta,))
    herramienta_especial = cursor.fetchone()
    cursor.close()
    return herramienta_especial

#######################
def obtener_datos_herramienta(nombre_herramienta):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)  # Usar un cursor de diccionario para acceder por nombre de columna

    # Buscar el id_clase_herramienta en la tabla herramientas_requeridas usando el nombre de la herramienta
    query = "SELECT id_clase_herramienta FROM herramientas_requeridas WHERE nombre = %s"
    cursor.execute(query, (nombre_herramienta,))
    resultado = cursor.fetchone()
    
    # Si no se encuentra la herramienta, devolver None para ambos valores
    if not resultado:
        cursor.close()
        return None, None

    # Extraer id_clase_herramienta del resultado
    id_clase_herramienta = resultado.get('id_clase_herramienta')

    # Determinar en cuál tabla buscar según el valor de id_clase_herramienta
    if id_clase_herramienta == 1:
        tabla_busqueda = 'herramientas_generales'
        columna_nombre = 'nombre'
    elif id_clase_herramienta == 2:
        tabla_busqueda = 'herramientas_especiales'
        columna_nombre = 'nombre_herramienta'
    else:
        cursor.close()
        return None, id_clase_herramienta

    # Ejecutar la consulta para obtener el ID de la herramienta en la tabla correspondiente
    query = f"SELECT id FROM {tabla_busqueda} WHERE {columna_nombre} = %s"
    cursor.execute(query, (nombre_herramienta,))
    resultado = cursor.fetchone()
    cursor.close()

    # Si se encuentra un ID en la tabla específica, devolver el ID y el id_clase_herramienta
    if resultado:
        return resultado.get('id'), id_clase_herramienta
    else:
        return None, id_clase_herramienta

def insertar_herramienta_relacion(id_herramienta, id_clase_herramienta, id_equipo_info):
    cursor = db.connection.cursor()

    # Inserta la relación en la tabla herramientas_relacion
    query = """
        INSERT INTO herramientas_relacion (id_herramienta, id_clase_herramienta, id_equipo_info)
        VALUES (%s, %s, %s)
    """
    try:
        cursor.execute(query, (id_herramienta, id_clase_herramienta, id_equipo_info))
        db.connection.commit()  # Confirma los cambios en la base de datos
        print(f"Relación insertada: Herramienta ID {id_herramienta}, Clase {id_clase_herramienta}, Equipo {id_equipo_info}")
    except Exception as e:
        db.connection.rollback()  # Revertir cambios si ocurre un error
        print("Error al insertar la relación:", e)
    finally:
        cursor.close()
    
    
def obtener_herramientas_generales_por_equipo(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM `herramientas_relacion` WHERE id_equipo_info = %s;"
    cursor.execute(query, (id_equipo_info,))
    herramientas_relacion = cursor.fetchall()
    query = "SELECT * FROM `herramientas_generales` WHERE id_tipo_herramienta = 1;"
    cursor.execute(query)
    herramientas_generales = cursor.fetchall()
    cursor.close()
    print("herramientas_relacion:", herramientas_relacion)
    print("herramientas_generales:", herramientas_generales)
    return herramientas_generales

def obtener_herramientas_especiales_por_equipo(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT he.*, hr.id_equipo_info 
        FROM herramientas_especiales he
        JOIN herramientas_relacion hr ON he.id = hr.id_herramienta
        WHERE hr.id_clase_herramienta = 2 AND hr.id_equipo_info = %s
    """
    cursor.execute(query, (id_equipo_info,))
    herramientas_especiales = cursor.fetchall()
    cursor.close()
    return herramientas_especiales



def obtener_nombre_componente_por_id(componente_id):
    cursor = db.connection.cursor()
    query = "SELECT nombre FROM componentes WHERE id = %s"
    cursor.execute(query, (componente_id,))
    result = cursor.fetchone()  # Obtener el primer resultado

    cursor.close()

    if result:
        return result['nombre']  # Devolver el nombre del componente si se encuentra
    else:
        return None  # Si no se encuentra el componente, devuelve None


def obtener_tipos_mantenimiento():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre FROM tipo_mantenimiento"
    cursor.execute(query)
    tipos_mantenimiento = cursor.fetchall()
    cursor.close()

    # Devuelve una lista de diccionarios con los id y nombres de los tipos de mantenimiento
    return [{'id': fila['id'], 'nombre': fila['nombre']} for fila in tipos_mantenimiento]


def obtener_tareas_mantenimiento():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre FROM tarea_mantenimiento"
    cursor.execute(query)
    tareas_mantenimiento = cursor.fetchall()
    cursor.close()

    return [{'id': fila['id'], 'nombre': fila['nombre']} for fila in tareas_mantenimiento]


#########################################################################################


#crud repuesto

def insertar_repuesto(
        id_equipo_info, nombre_herramienta, valor,
        dibujo_seccion, notas, mtbf, codigo_otan
):
    cursor = db.connection.cursor()
    query = """
        INSERT INTO repuesto (
            id_equipo_info, nombre_repuesto, valor,
            dibujo_transversal, notas, mtbf, codigo_otan
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        id_equipo_info, nombre_herramienta, valor,
        dibujo_seccion, notas, mtbf, codigo_otan
    ))
    db.connection.commit()
    repuesto_id = cursor.lastrowid
    cursor.close()
    return repuesto_id


def obtener_repuestos_por_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM repuesto WHERE id_equipo_info = %s"
    cursor.execute(query, (id_equipo_info,))
    repuestos = cursor.fetchall()
    cursor.close()
    return repuestos


def actualizar_repuesto(id_repuesto, nombre_repuesto, valor, dibujo_transversal, notas, mtbf, codigo_otan):
    cursor = db.connection.cursor()

    # Construimos la consulta SQL dinámicamente
    query = """
        UPDATE repuesto
        SET nombre_repuesto = %s, valor = %s, notas = %s, mtbf = %s, codigo_otan = %s
    """
    params = [nombre_repuesto, valor, notas, mtbf, codigo_otan]

    if dibujo_transversal is not None:
        query += ", dibujo_transversal = %s"
        params.append(dibujo_transversal)

    query += " WHERE id = %s"
    params.append(id_repuesto)

    cursor.execute(query, params)
    db.connection.commit()
    cursor.close()


# database.py
def eliminar_repuesto(id_repuesto):
    cursor = db.connection.cursor()
    query = "DELETE FROM repuesto WHERE id = %s"
    cursor.execute(query, (id_repuesto,))
    db.connection.commit()
    cursor.close()


def obtener_repuesto_por_id(id_repuesto):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM repuesto WHERE id = %s"
    cursor.execute(query, (id_repuesto,))
    repuesto = cursor.fetchone()
    cursor.close()
    return repuesto


# database.py

def insertar_analisis_herramienta(nombre, valor, id_equipo_info, parte_numero, id_herramienta_requerida,
                                  id_tipo_herramienta, id_clase_herramienta,dibujo_seccion_transversal,cantidad):
    cursor = db.connection.cursor()
    query = """
        INSERT INTO herramientas_generales (
            nombre, valor, id_equipo_info, parte_numero, id_herramienta_requerida, id_tipo_herramienta,id_clase_herramienta,dibujo_seccion_transversal,cantidad

        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)
    """

    cursor.execute(query, (
    nombre, valor, id_equipo_info, parte_numero, id_herramienta_requerida, id_tipo_herramienta, id_clase_herramienta,dibujo_seccion_transversal,cantidad))


    db.connection.commit()
    analisis_id = cursor.lastrowid
    cursor.close()
    return analisis_id


def obtener_analisis_herramienta_por_id(id_analisis):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM herramientas_generales WHERE id = %s"
    cursor.execute(query, (id_analisis,))
    analisis = cursor.fetchone()
    cursor.close()
    return analisis


def obtener_analisis_herramientas_por_equipo(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM herramientas_generales WHERE id_equipo_info = %s"
    cursor.execute(query, (id_equipo_info,))
    analisis = cursor.fetchall()
    cursor.close()
    return analisis



def actualizar_analisis_herramienta(id_analisis, nombre, valor, parte_numero,dibujo_seccion_transversal,cantidad):
    cursor = db.connection.cursor()
    query = """
        UPDATE herramientas_generales
        SET nombre = %s, valor = %s, parte_numero = %s, dibujo_seccion_transversal = %s,cantidad = %s
        WHERE id = %s
    """
    cursor.execute(query, (nombre, valor, parte_numero,dibujo_seccion_transversal,cantidad, id_analisis))



    db.connection.commit()
    cursor.close()


def eliminar_analisis_herramienta(id_analisis):
    cursor = db.connection.cursor()
    query = "DELETE FROM herramientas_generales WHERE id = %s"
    cursor.execute(query, (id_analisis,))
    db.connection.commit()
    cursor.close()


def obtener_herramientas_por_equipo(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    
    # Obtener herramientas relacionadas con el equipo
    query = """
        SELECT hr.id_clase_herramienta, hr.id_herramienta 
        FROM herramientas_relacion hr 
        WHERE hr.id_equipo_info = %s
    """
    cursor.execute(query, (id_equipo_info,))
    relaciones = cursor.fetchall()
    
    herramientas = []
    
    for relacion in relaciones:
        id_clase_herramienta = relacion['id_clase_herramienta']
        id_herramienta = relacion['id_herramienta']
        
        if id_clase_herramienta == 1:
            # Buscar en herramientas_generales
            query_general = "SELECT * FROM herramientas_generales WHERE id = %s"
            cursor.execute(query_general, (id_herramienta,))
            herramienta = cursor.fetchone()
            if herramienta:
                herramienta['tipo'] = 'general'
                herramientas.append(herramienta)
        
        elif id_clase_herramienta == 2:
            # Buscar en herramientas_especiales
            query_especial = "SELECT * FROM herramientas_especiales WHERE id = %s"
            cursor.execute(query_especial, (id_herramienta,))
            herramienta = cursor.fetchone()
            if herramienta:
                herramienta['tipo'] = 'especial'
                herramientas.append(herramienta)
    
    cursor.close()
    return herramientas




#Herramientas especiales:


def insertar_herramienta_especial(
        parte_numero, nombre_herramienta, valor,
        dibujo_seccion_transversal, nota, id_equipo_info,
        manual_referencia, id_tipo_herramienta, cantidad,
        id_herramienta_requerida, id_clase_herramienta  # Aseguramos que se recibe este parámetro

):
    cursor = db.connection.cursor()
    query = """
        INSERT INTO herramientas_especiales (
            parte_numero, nombre_herramienta, valor,
            dibujo_seccion_transversal, nota, id_equipo_info,
            manual_referencia, id_tipo_herramienta, cantidad, id_herramienta_requerida,id_clase_herramienta
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
    """
    cursor.execute(query, (
        parte_numero, nombre_herramienta, valor,
        dibujo_seccion_transversal, nota, id_equipo_info,
        manual_referencia, id_tipo_herramienta, cantidad, id_herramienta_requerida, id_clase_herramienta
    ))
    db.connection.commit()
    herramienta_id = cursor.lastrowid
    cursor.close()
    return herramienta_id


def obtener_herramienta_especial_por_id(id_herramienta):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM herramientas_especiales WHERE id = %s"
    cursor.execute(query, (id_herramienta,))
    herramienta = cursor.fetchone()
    cursor.close()
    return herramienta


def obtener_herramientas_especiales_por_equipo(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM herramientas_especiales WHERE id_equipo_info = %s"
    cursor.execute(query, (id_equipo_info,))
    herramientas = cursor.fetchall()
    cursor.close()
    return herramientas


def actualizar_herramienta_especial(
        id_herramienta, parte_numero, nombre_herramienta, valor,
        dibujo_seccion_transversal, nota, manual_referencia, id_tipo_herramienta, cantidad
):
    cursor = db.connection.cursor()
    query = """
        UPDATE herramientas_especiales
        SET parte_numero = %s, nombre_herramienta = %s, valor = %s,
            dibujo_seccion_transversal = %s, nota = %s,
            manual_referencia = %s, id_tipo_herramienta = %s, cantidad = %s
        WHERE id = %s
    """
    cursor.execute(query, (
        parte_numero, nombre_herramienta, valor,
        dibujo_seccion_transversal, nota, manual_referencia,
        id_tipo_herramienta, cantidad, id_herramienta
    ))
    db.connection.commit()
    cursor.close()


def eliminar_herramienta_especial(id_herramienta):
    cursor = db.connection.cursor()
    query = "DELETE FROM herramientas_especiales WHERE id = %s"
    cursor.execute(query, (id_herramienta,))
    db.connection.commit()
    cursor.close()


def insertar_herramienta_requerida(nombre, id_tipo_herramienta, id_clase_herramienta):
    cursor = db.connection.cursor()
    query = """
        INSERT INTO herramientas_requeridas (nombre, id_tipo_herramienta,id_clase_herramienta)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (nombre, id_tipo_herramienta, id_clase_herramienta))
    db.connection.commit()
    herramienta_requerida_id = cursor.lastrowid
    cursor.close()
    return herramienta_requerida_id


def obtener_tipos_herramientas():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id_tipo_herramienta, nombre_tipo FROM tipo_herramientas ORDER BY nombre_tipo"
    cursor.execute(query)
    tipos = cursor.fetchall()
    cursor.close()
    return tipos


############################RCMMMMM
def obtener_rcm_por_fmea(id_fmea):
    print("id_fmea")
    print(id_fmea)
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT
            r.id,
            r.id_fmea,
            s.nombre as sistema, 
            ff.nombre as falla_funcional, 
            c.nombre as componente, 
            cmf.nombre as codigo_modo_falla, 
            cf.nombre as consecutivo_modo_falla, 
            dmf.nombre as descripcion_modo_falla, 
            causa.nombre as causa, 
            r.hidden_failures,
            r.safety,
            r.environment,
            r.operation,
            r.h1_s1_n1_o1,
            r.h2_s2_n2_o2,
            r.h3_s3_n3_o3,
            r.h4_s4,
            r.h5,
            r.tarea,
            r.id_accion_recomendada,
            r.intervalo_inicial_horas
        FROM rcm r
        LEFT JOIN fmea f ON r.id_fmea = f.id
        LEFT JOIN sistema s ON f.id_sistema = s.id
        LEFT JOIN falla_funcional ff ON f.id_falla_funcional = ff.id
        LEFT JOIN componentes c ON f.id_componente = c.id
        LEFT JOIN codigo_modo_falla cmf ON f.id_codigo_modo_falla = cmf.id
        LEFT JOIN consecutivo_modo_falla cf ON f.id_consecutivo_modo_falla = cf.id
        LEFT JOIN descripcion_modo_falla dmf ON f.id_descripcion_modo_falla = dmf.id
        LEFT JOIN causa ON f.id_causa = causa.id
        WHERE r.id_fmea = %s AND r.estado = 'activo'
    """
    cursor.execute(query, (id_fmea,))
    rcm = cursor.fetchone()
    # rcm = context[0]
    print(rcm)
    cursor.close()
    return rcm


def obtener_rcm_por_id(id_rcm):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT
            r.id,
            r.id_fmea,
            s.nombre as sistema, 
            ff.nombre as falla_funcional, 
            c.nombre as componente, 
            cmf.nombre as codigo_modo_falla, 
            cf.nombre as consecutivo_modo_falla, 
            dmf.nombre as descripcion_modo_falla, 
            causa.nombre as causa, 
            r.hidden_failures,
            r.safety,
            r.environment,
            r.operation,
            r.h1_s1_n1_o1,
            r.h2_s2_n2_o2,
            r.h3_s3_n3_o3,
            r.h4_s4,
            r.h5,
            r.tarea,
            r.id_accion_recomendada,
            r.intervalo_inicial_horas
        FROM rcm r
        LEFT JOIN fmea f ON r.id_fmea = f.id
        LEFT JOIN sistema s ON f.id_sistema = s.id
        LEFT JOIN falla_funcional ff ON f.id_falla_funcional = ff.id
        LEFT JOIN componentes c ON f.id_componente = c.id
        LEFT JOIN codigo_modo_falla cmf ON f.id_codigo_modo_falla = cmf.id
        LEFT JOIN consecutivo_modo_falla cf ON f.id_consecutivo_modo_falla = cf.id
        LEFT JOIN descripcion_modo_falla dmf ON f.id_descripcion_modo_falla = dmf.id
        LEFT JOIN causa ON f.id_causa = causa.id
        WHERE r.id = %s AND r.estado = 'activo'
    """
    cursor.execute(query, (id_rcm,))
    rcm = cursor.fetchone()
    cursor.close()
    return rcm


def obtener_rcms_completos():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT
            r.id,
            r.id_fmea,
            f.id_equipo_info,
            s.nombre as sistema, 
            ff.nombre as falla_funcional, 
            c.nombre as componente, 
            cmf.nombre as codigo_modo_falla, 
            cf.nombre as consecutivo_modo_falla, 
            dmf.nombre as descripcion_modo_falla, 
            causa.nombre as causa, 
            r.hidden_failures,
            r.safety,
            r.environment,
            r.operation,
            r.h1_s1_n1_o1,
            r.h2_s2_n2_o2,
            r.h3_s3_n3_o3,
            r.h4_s4,
            r.h5,
            r.tarea,
            r.id_accion_recomendada,
            r.intervalo_inicial_horas
        FROM rcm r
        LEFT JOIN fmea f ON r.id_fmea = f.id
        LEFT JOIN sistema s ON f.id_sistema = s.id
        LEFT JOIN falla_funcional ff ON f.id_falla_funcional = ff.id
        LEFT JOIN componentes c ON f.id_componente = c.id
        LEFT JOIN codigo_modo_falla cmf ON f.id_codigo_modo_falla = cmf.id
        LEFT JOIN consecutivo_modo_falla cf ON f.id_consecutivo_modo_falla = cf.id
        LEFT JOIN descripcion_modo_falla dmf ON f.id_descripcion_modo_falla = dmf.id
        LEFT JOIN causa ON f.id_causa = causa.id
        WHERE r.estado = 'activo'
    """
    cursor.execute(query)
    rcms_completos = cursor.fetchall()
    cursor.close()
    return rcms_completos


def obtener_fmeas_con_rcm():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id_fmea FROM rcm WHERE estado = 'activo'"
    cursor.execute(query)
    fmeas_con_rcm = cursor.fetchall()
    cursor.close()

    # Extraer solo los id_fmea de los resultados
    id_fmeas = [fmea['id_fmea'] for fmea in fmeas_con_rcm]
    return id_fmeas


def eliminar_rcm(id_fmea,id_rcm):
    cursor = db.connection.cursor()
    # Cambiar el estado a 'inactivo' en lugar de eliminar
    query = "UPDATE rcm SET estado = 'inactivo' WHERE id_fmea = %s AND id = %s"
    cursor.execute(query, (id_fmea,id_rcm))
    db.connection.commit()
    cursor.close()
"""
cursor = db.connection.cursor()
    # Cambiar el estado a 'inactivo' en lugar de eliminar
    update_query = "UPDATE rcm SET estado = 'inactivo' WHERE id = %s"
    cursor.execute(update_query, (id_rcm,))
    db.connection.commit()
    cursor.close()

"""

def actualizar_rcm(rcm):
    cursor = db.connection.cursor()
    query = """
        UPDATE rcm
        SET hidden_failures = %s, safety = %s, environment = %s, operation = %s, h1_s1_n1_o1 = %s, h2_s2_n2_o2 = %s, h3_s3_n3_o3 = %s, h4_s4 = %s, h5 = %s, tarea = %s, intervalo_inicial_horas = %s, id_accion_recomendada = %s
        WHERE id_fmea = %s
    """
    cursor.execute(query, (
        rcm['hidden_failures'], rcm['safety'], rcm['environment'], rcm['operation'], rcm['h1_s1_n1_o1'],
        rcm['h2_s2_n2_o2'], rcm['h3_s3_n3_o3'], rcm['h4_s4'], rcm['h5'], rcm['tarea'], rcm['intervalo_inicial_horas'],
        rcm['id_accion_recomendada'], rcm['id_fmea']
    ))
    db.connection.commit()
    cursor.close()


def obtener_lista_acciones_recomendadas():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM accion_recomendada"
    cursor.execute(query)
    accion_recomendada = cursor.fetchall()
    cursor.close()
    print("acciones")
    print(accion_recomendada)
    return accion_recomendada


def insertar_rcm(rcm):
    cursor = db.connection.cursor()
    query = """
        INSERT INTO rcm (
            id_fmea, hidden_failures, safety, environment, operation, h1_s1_n1_o1, h2_s2_n2_o2, h3_s3_n3_o3, h4_s4, h5, tarea, intervalo_inicial_horas, id_accion_recomendada
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        rcm['id_fmea'], rcm['hidden_failures'], rcm['safety'], rcm['environment'], rcm['operation'], rcm['h1_s1_n1_o1'],
        rcm['h2_s2_n2_o2'], rcm['h3_s3_n3_o3'], rcm['h4_s4'], rcm['h5'], rcm['tarea'], rcm['intervalo_inicial_horas'],
        rcm['id_accion_recomendada']
    ))
    db.connection.commit()
    cursor.close()


#generalidades


# database.py

def obtener_equipo_info_por_id(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM equipo_info WHERE id = %s"
    cursor.execute(query, (id_equipo_info,))
    equipo = cursor.fetchone()
    cursor.close()
    return equipo


def actualizar_equipo_info(id_equipo_info, data):
    cursor = db.connection.cursor()

    # Inicializamos los campos que siempre se actualizarán
    fields = [
        "nombre_equipo = %s",
        "AOR = %s",
        "fecha = %s",
        "fiabilidad_equipo = %s",
        "MTBF = %s",
        "GRES = %s",
        "criticidad_equipo = %s",
        "marca = %s",
        "peso_seco = %s",
        "modelo = %s",
        "dimensiones = %s",
        "descripcion = %s",
        "id_personal = %s",
        "id_diagrama = %s",
        "id_procedimiento = %s",
        "id_sistema = %s",
        "id_equipo = %s"
    ]

    params = [
        data['nombre_equipo'], data['aor'], data['fecha'], data['fiabilidad_equipo'], data['mtbf'],
        data['gres_sistema'],
        data['criticidad_equipo'], data['marca'], data['peso_seco'], data['modelo'], data['dimensiones'],
        data['descripcion_equipo'], data['responsable'], data['id_diagrama'], data['id_procedimiento'],
        data['sistema'], data['equipo']
    ]

    # Si hay una nueva imagen, agregamos la actualización del campo 'imagen'
    if data['imagen_equipo'] is not None:
        fields.append("imagen = %s")
        params.append(data['imagen_equipo'])

    # Añadimos el ID del equipo a los parámetros
    params.append(id_equipo_info)

    # Construimos la consulta SQL dinámicamente
    query = f"""
        UPDATE equipo_info
        SET {', '.join(fields)}
        WHERE id = %s
    """

    cursor.execute(query, params)
    db.connection.commit()
    cursor.close()


def eliminar_equipo_info(id_equipo_info):
    cursor = db.connection.cursor()
    query = "DELETE FROM equipo_info WHERE id = %s"
    cursor.execute(query, (id_equipo_info,))
    db.connection.commit()
    cursor.close()


def obtener_diagramas_por_id(id_diagrama):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM diagramas WHERE id = %s"
    cursor.execute(query, (id_diagrama,))
    diagrama = cursor.fetchone()
    cursor.close()
    return diagrama


def obtener_responsables():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id, nombre_completo FROM personal"
    cursor.execute(query)
    responsables = cursor.fetchall()
    cursor.close()
    return responsables




def obtener_personal_por_id(id_personal):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM personal WHERE id = %s"
    cursor.execute(query, (id_personal,))
    responsable = cursor.fetchone()
    cursor.close()
    return responsable


def obtener_grupo_constructivo_por_id(id_grupo_constructivo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM grupo_constructivo WHERE id = %s"
    cursor.execute(query, (id_grupo_constructivo,))
    grupo_constructivo = cursor.fetchone()
    cursor.close()
    return grupo_constructivo




def obtener_equipo_por_id(id_equipo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM equipo_info WHERE id = %s"
    cursor.execute(query, (id_equipo,))
    equipo = cursor.fetchone()
    cursor.close()
    return equipo


def obtener_subgrupo_constructivo_por_sistema_id(id_sistema):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    # Obtener id_subgrupo de la tabla sistema
    query_sistema = "SELECT id_subgrupo FROM sistema WHERE id = %s"
    cursor.execute(query_sistema, (id_sistema,))
    sistema = cursor.fetchone()

    if not sistema:
        cursor.close()
        return None  # Si no se encuentra el sistema, retornamos None

    id_subgrupo = sistema['id_subgrupo']

    # Obtener el subgrupo_constructivo de la tabla subgrupo
    query_subgrupo = "SELECT * FROM subgrupo WHERE id = %s"
    cursor.execute(query_subgrupo, (id_subgrupo,))
    subgrupo_constructivo = cursor.fetchone()

    cursor.close()
    return subgrupo_constructivo  # Retornamos el subgrupo constructivo obtenido


def obtener_datos_equipo_por_id(id_equipo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM equipos WHERE id = %s"
    cursor.execute(query, (id_equipo,))
    equipo = cursor.fetchone()
    cursor.close()
    return equipo




# Función para actualizar un análisis funcional existente
def actualizar_analisis_funcional(id_analisis_funcional, verbo, accion, estandar_desempeño, id_subsistema):
    cursor = db.connection.cursor()
    query = """
        UPDATE analisis_funcional
        SET verbo = %s, accion = %s, estandar_desempeño = %s, id_subsistema = %s
        WHERE id = %s
    """
    cursor.execute(query, (verbo, accion, estandar_desempeño, id_subsistema, id_analisis_funcional))
    db.connection.commit()
    cursor.close()


# Función para eliminar un análisis funcional
def eliminar_analisis_funcional(id_analisis_funcional):
    cursor = db.connection.cursor()
    # Cambiar el estado a 'inactivo' en lugar de eliminar
    query = "UPDATE analisis_funcional SET estado = 'inactivo' WHERE id = %s"
    cursor.execute(query, (id_analisis_funcional,))
    db.connection.commit()
    cursor.close()



def obtener_subsistemas_por_equipo_mostrar(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    # Obtener el id_equipo desde equipo_info
    query_equipo = "SELECT id_equipo FROM equipo_info WHERE id = %s"
    cursor.execute(query_equipo, (id_equipo_info,))
    equipo_info = cursor.fetchone()
    if not equipo_info:
        cursor.close()
        return []

    id_equipo = equipo_info['id_equipo']

    # Obtener los subsistemas que pertenecen al id_equipo
    query_subsistemas = "SELECT id, nombre FROM subsistemas WHERE id_equipo = %s"
    cursor.execute(query_subsistemas, (id_equipo,))
    subsistemas = cursor.fetchall()
    cursor.close()
    return subsistemas


def obtener_nombre_sistema_por_id(subsistema_id):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    # Si subsistema_id se refiere directamente al sistema
    query = """
    SELECT s.nombre 
    FROM subsistemas s
    WHERE s.id = %s
    """

    cursor.execute(query, (subsistema_id,))
    resultado = cursor.fetchone()
    cursor.close()

    if resultado:
        return resultado['nombre']
    else:
        return None


def obtener_herramientas_requeridas_por_tipo():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    dict_herramientas = {}
    tipos = obtener_tipos_herramientas()
    for tipo in tipos:
        query = '''SELECT * FROM herramientas_requeridas hr 
                join tipo_herramientas th on hr.id_tipo_herramienta = th.id_tipo_herramienta 
                WHERE nombre_tipo = %s'''
        cursor.execute(query, (tipo['nombre_tipo'],))
        herramientas = cursor.fetchall()
        dict_herramientas[tipo['nombre_tipo']] = herramientas
    cursor.close()

    return dict_herramientas


def insertar_herramientas_requeridas_mta(herramientas_requeridas, id_mta):
    cursor = db.connection.cursor()
    #recorrer la tupla de herramientas requeridas e insertarlas junto al id_mta en la tabla herramientas_mta
    if herramientas_requeridas:
        for herramienta in herramientas_requeridas:
            query = '''INSERT INTO herramientas_mta (id_mta, id_herramienta_requerida) VALUES (%s, %s)'''
            cursor.execute(query, (id_mta, herramienta))
        db.connection.commit()
    cursor.close()


def eliminar_herramientas_requeridas_mta(id_mta):
    cursor = db.connection.cursor()
    query = "DELETE FROM herramientas_mta WHERE id_mta = %s"
    cursor.execute(query, (id_mta,))
    db.connection.commit()
    cursor.close()


# obtener_herramientas_mta,
def obtener_herramientas_mta():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = '''SELECT * FROM herramientas_mta hm
            JOIN herramientas_requeridas hr on hm.id_herramienta_requerida = hr.id_herramienta_requerida'''
    cursor.execute(query)
    herramientas_mta = cursor.fetchall()
    cursor.close()
    return herramientas_mta


def insertar_repuestos_requeridos_mta(repuestos_requeridos, id_mta):
    cursor = db.connection.cursor()
    #recorrer la tupla de herramientas requeridas e insertarlas junto al id_mta en la tabla herramientas_mta
    if repuestos_requeridos:
        for repuesto in repuestos_requeridos:
            query = '''INSERT INTO repuestos_mta (id_mta, id_repuesto) VALUES (%s, %s)'''
            cursor.execute(query, (id_mta, repuesto))
        db.connection.commit()
    cursor.close()


def eliminar_repuestos_requeridos_mta(id_mta):
    cursor = db.connection.cursor()
    query = "DELETE FROM repuestos_mta WHERE id_mta = %s"
    cursor.execute(query, (id_mta,))
    db.connection.commit()
    cursor.close()


#     obtener_repuestos_mta
def obtener_repuestos_mta():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = '''SELECT * FROM repuestos_mta rm
            JOIN repuesto r on rm.id_repuesto = r.id'''
    cursor.execute(query)
    repuestos_mta = cursor.fetchall()
    cursor.close()
    return repuestos_mta


def insertar_mta_lora(nivel, actividades, operario, id_mta):
    cursor = db.connection.cursor()
    query = '''INSERT INTO lora_mta (nivel, actividades, operario, id_mta) VALUES (%s, %s, %s, %s)'''
    cursor.execute(query, (nivel, actividades, operario, id_mta))
    db.connection.commit()
    cursor.close()


def actualizar_mta_lora(nivel, actividades, operario, id_mta):
    cursor = db.connection.cursor()
    query = '''UPDATE lora_mta SET nivel = %s, actividades = %s, operario = %s WHERE id_mta = %s'''
    cursor.execute(query, (nivel, actividades, operario, id_mta))
    db.connection.commit()
    cursor.close()


def eliminar_mta_lora(id_mta):
    cursor = db.connection.cursor()
    query = "DELETE FROM lora_mta WHERE id_mta = %s"
    cursor.execute(query, (id_mta,))
    db.connection.commit()
    cursor.close()


def obtener_mta_lora():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM lora_mta"
    cursor.execute(query)
    lora_mta = cursor.fetchall()
    cursor.close()
    return lora_mta


def obtener_max_id_mta():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT MAX(id) as max_id FROM mta WHERE estado = 'activo'"
    cursor.execute(query)
    max_id = cursor.fetchone()
    cursor.close()
    print(max_id['max_id'])
    return max_id['max_id']


def obtener_rcms_con_mta():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id_rcm FROM mta WHERE estado = 'activo'"
    cursor.execute(query)
    rcms_con_mta = cursor.fetchall()
    cursor.close()

    # Extraer solo los id_fmea de los resultados
    id_rcms = [mta['id_rcm'] for mta in rcms_con_mta]
    return id_rcms


def obtener_lora_mta_por_id_mta(id_mta):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM lora_mta WHERE id_mta = %s"
    cursor.execute(query, (id_mta,))
    lora_mta = cursor.fetchone()
    cursor.close()
    return lora_mta


def obtener_herramientas_mta_por_id_mta(id_mta):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = '''SELECT * FROM herramientas_mta hm
            JOIN herramientas_requeridas hr on hm.id_herramienta_requerida = hr.id_herramienta_requerida
            WHERE id_mta = %s'''
    cursor.execute(query, (id_mta,))
    herramientas_mta = cursor.fetchall()
    cursor.close()
    return herramientas_mta


def obtener_repuestos_mta_por_id_mta(id_mta):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = '''SELECT * FROM repuestos_mta rm
            JOIN repuesto r on rm.id_repuesto = r.id
            WHERE id_mta = %s'''
    cursor.execute(query, (id_mta,))
    repuestos_mta = cursor.fetchall()
    cursor.close()
    return repuestos_mta


# Función para obtener el id_equipo_info basado en nombre_equipo en MySQL
def obtener_id_equipo_info_por_nombre(nombre_equipo):
    # Conectar a la base de datos MySQL
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    # Consulta SQL para obtener id_equipo_info basado en nombre_equipo
    query = "SELECT id FROM equipo_info WHERE nombre_equipo = %s"
    cursor.execute(query, (nombre_equipo,))

    # Obtener el primer resultado
    result = cursor.fetchone()

    # Cerrar la conexión
    cursor.close()
    if result:
        return result['id']  # Devuelve el id del equipo
    else:
        return None


# obtener_informacion_equipo_info,
def obtener_informacion_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM equipo_info WHERE id = %s"
    cursor.execute(query, (id_equipo_info,))
    equipo_info = cursor.fetchone()
    cursor.close()
    return equipo_info


# obtener_fmeas_por_equipo_info,
def obtener_fmeas_por_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
    SELECT 
        f.id, 
        f.id_equipo_info, 
        f.id_sistema, 

        s.nombre as sistema, 
        f.id_falla_funcional, 
        ff.nombre as falla_funcional, 
        f.id_componente, 
        c.nombre as componente, 
        f.id_codigo_modo_falla, 
        cmf.nombre as codigo_modo_falla, 

        f.id_consecutivo_modo_falla, 
        cf.nombre as consecutivo_modo_falla, 
        f.id_descripcion_modo_falla, 
        dmf.nombre as descripcion_modo_falla, 
        f.id_causa, 
        causa.nombre as causa, 
        f.id_mecanismo_falla, 
        mf.nombre as mecanismo_falla, 
        f.id_detalle_falla, 
        df.nombre as detalle_falla, 

        f.MTBF, 
        f.MTTR, 
        f.id_metodo_deteccion_falla,
        f.id_fallo_oculto,
        fo.valor as fallo_oculto_valor, 
        fo.nombre as fallo_oculto_descripcion, 
        f.id_seguridad_fisica, 
        sf.valor as seguridad_fisica_valor, 
        sf.nombre as seguridad_fisica_descripcion, 
        f.id_medio_ambiente, 
        ma.valor as medio_ambiente_valor, 
        ma.nombre as medio_ambiente_descripcion, 
        f.id_impacto_operacional, 
        io.valor as impacto_operacional_valor, 
        io.nombre as impacto_operacional_descripcion, 
        f.id_costos_reparacion, 
        cr.valor as costos_reparacion_valor, 
        cr.nombre as costos_reparacion_descripcion, 
        f.id_flexibilidad_operacional, 
        flex.valor as flexibilidad_operacional_valor, 
        flex.nombre as flexibilidad_operacional_descripcion, 
        f.calculo_severidad,
        f.id_ocurrencia, 
        o.valor as ocurrencia_valor, 
        o.nombre as ocurrencia_descripcion, 
        f.ocurrencia_mate, 
        f.id_probabilidad_deteccion, 
        pd.valor as probabilidad_deteccion_valor, 
        pd.descripcion as probabilidad_deteccion_descripcion,
        f.RPN,
        f.id_riesgo,
        p.nombre_completo as nombre_completo,
        p.id as id_personal
    FROM fmea f
    LEFT JOIN equipo_info ei ON f.id_equipo_info = ei.id
    LEFT JOIN personal p ON ei.id_personal = p.id
    LEFT JOIN sistema s ON f.id_sistema = s.id
    LEFT JOIN falla_funcional ff ON f.id_falla_funcional = ff.id
    LEFT JOIN componentes c ON f.id_componente = c.id
    LEFT JOIN codigo_modo_falla cmf ON f.id_codigo_modo_falla = cmf.id
    LEFT JOIN consecutivo_modo_falla cf ON f.id_consecutivo_modo_falla = cf.id
    LEFT JOIN descripcion_modo_falla dmf ON f.id_descripcion_modo_falla = dmf.id
    LEFT JOIN causa ON f.id_causa = causa.id
    LEFT JOIN mecanismo_falla mf ON f.id_mecanismo_falla = mf.id
    LEFT JOIN detalle_falla df ON f.id_detalle_falla = df.id
    LEFT JOIN fallo_oculto fo ON f.id_fallo_oculto = fo.id
    LEFT JOIN seguridad_fisica sf ON f.id_seguridad_fisica = sf.id
    LEFT JOIN medio_ambiente ma ON f.id_medio_ambiente = ma.id
    LEFT JOIN impacto_operacional io ON f.id_impacto_operacional = io.id
    LEFT JOIN costos_reparacion cr ON f.id_costos_reparacion = cr.id
    LEFT JOIN flexibilidad_operacional flex ON f.id_flexibilidad_operacional = flex.id
    LEFT JOIN ocurrencia o ON f.id_ocurrencia = o.id
    LEFT JOIN probabilidad_deteccion pd ON f.id_probabilidad_deteccion = pd.id
    """

    cursor.execute(query)
    fmeas = cursor.fetchall()
    cursor.close()

    # Lista para almacenar los FMEAs procesados
    fmeas_completos = []

    # Diccionario para contar las ocurrencias de cada consecutivo_modo_falla
    consecutivo_modo_falla_counter = {}

    # Procesar cada fila de la consulta
    for fmea in fmeas:
        # Verificar si alguna columna no tiene nombre o descripción
        # Y buscar el nombre/valor por ID si es necesario

        #verificaría cada campo:
        sistema_nombre = fmea['sistema'] if fmea['sistema'] else obtener_nombre_por_id('subsistemas',
                                                                                       fmea['id_sistema'])

        falla_funcional_nombre = fmea['falla_funcional'] if fmea['falla_funcional'] else obtener_nombre_por_id(
            'falla_funcional', fmea['id_falla_funcional'])

        componente_nombre = fmea['componente'] if fmea['componente'] else obtener_nombre_por_id('componentes',
                                                                                                fmea['id_componente'])
        codigo_modo_falla_nombre = fmea['codigo_modo_falla'] if fmea['codigo_modo_falla'] else obtener_nombre_por_id(
            'codigo_modo_falla', fmea['id_codigo_modo_falla'])
        consecutivo_modo_falla_nombre = fmea['consecutivo_modo_falla'] if fmea[
            'consecutivo_modo_falla'] else obtener_nombre_por_id('consecutivo_modo_falla',
                                                                 fmea['id_consecutivo_modo_falla'])
        descripcion_modo_falla_nombre = fmea['descripcion_modo_falla'] if fmea[
            'descripcion_modo_falla'] else obtener_nombre_por_id('descripcion_modo_falla',
                                                                 fmea['id_descripcion_modo_falla'])
        causa_nombre = fmea['causa'] if fmea['causa'] else obtener_nombre_por_id('causa', fmea['id_causa'])
        mecanismo_falla_nombre = fmea['mecanismo_falla'] if fmea['mecanismo_falla'] else obtener_nombre_por_id(
            'mecanismo_falla', fmea['id_mecanismo_falla'])
        detalle_falla_nombre = fmea['detalle_falla'] if fmea['detalle_falla'] else obtener_nombre_por_id(
            'detalle_falla', fmea['id_detalle_falla'])

        # Contar las ocurrencias de consecutivo_modo_falla
        if consecutivo_modo_falla_nombre not in consecutivo_modo_falla_counter:
            consecutivo_modo_falla_counter[consecutivo_modo_falla_nombre] = 0
        consecutivo_modo_falla_counter[consecutivo_modo_falla_nombre] += 1

        # Concatenar la numeración al consecutivo_modo_falla
        consecutivo_modo_falla_numerado = f"{consecutivo_modo_falla_nombre}-{consecutivo_modo_falla_counter[consecutivo_modo_falla_nombre]}"

        # Añadir el FMEA procesado a la lista
        fmeas_completos.append({
            'id': fmea['id'],
            'id_equipo_info': fmea['id_equipo_info'],
            'id_sistema': fmea['id_sistema'],
            'sistema': sistema_nombre,
            'id_falla_funcional': fmea['id_falla_funcional'],
            'falla_funcional': falla_funcional_nombre,
            'id_descripcion_modo_falla': fmea['id_descripcion_modo_falla'],
            'componente': componente_nombre,
            'codigo_modo_falla': codigo_modo_falla_nombre,
            'consecutivo_modo_falla': consecutivo_modo_falla_nombre,
            'descripcion_modo_falla': descripcion_modo_falla_nombre,
            'causa': causa_nombre,
            'mecanismo_falla': mecanismo_falla_nombre,
            'detalle_falla': detalle_falla_nombre,
            'MTBF': fmea['MTBF'],
            'MTTR': fmea['MTTR'],
            'fallo_oculto_valor': fmea['fallo_oculto_valor'],
            'fallo_oculto_descripcion': fmea['fallo_oculto_descripcion'],
            'seguridad_fisica_valor': fmea['seguridad_fisica_valor'],
            'seguridad_fisica_descripcion': fmea['seguridad_fisica_descripcion'],
            'medio_ambiente_valor': fmea['medio_ambiente_valor'],
            'medio_ambiente_descripcion': fmea['medio_ambiente_descripcion'],
            'impacto_operacional_valor': fmea['impacto_operacional_valor'],
            'impacto_operacional_descripcion': fmea['impacto_operacional_descripcion'],
            'costos_reparacion_valor': fmea['costos_reparacion_valor'],
            'costos_reparacion_descripcion': fmea['costos_reparacion_descripcion'],
            'flexibilidad_operacional_valor': fmea['flexibilidad_operacional_valor'],
            'flexibilidad_operacional_descripcion': fmea['flexibilidad_operacional_descripcion'],
            'ocurrencia_valor': fmea['ocurrencia_valor'],
            'ocurrencia_descripcion': fmea['ocurrencia_descripcion'],
            'probabilidad_deteccion_valor': fmea['probabilidad_deteccion_valor'],
            'probabilidad_deteccion_descripcion': fmea['probabilidad_deteccion_descripcion'],
            'RPN': fmea['RPN'],
            'id_riesgo': fmea['id_riesgo'],
            'nombre_completo': fmea['nombre_completo'],
            'id_personal': fmea['id_personal']

        })

    return fmeas_completos


#########################

#fmea editar y eliminar
def obtener_fmea_por_id(fmea_id, id_equipo_info):
    # Obtener la lista completa de FMEAs con nombres procesados
    fmeas_completos = obtener_fmeas(id_equipo_info)

    # Buscar el FMEA por el ID en la lista completa
    fmea_filtrado = next((fmea for fmea in fmeas_completos if fmea['id'] == fmea_id), None)

    # Si se encuentra el FMEA, lo devolvemos, si no, devolvemos None
    if fmea_filtrado:
        print(fmea_filtrado)
        return fmea_filtrado
    else:
        return None


def obtener_ID_FMEA(fmea_id):
    cursor = db.connection.cursor()

    query = "SELECT * FROM fmea WHERE id = %s"

    cursor.execute(query, (fmea_id,))
    fmea = cursor.fetchone()
    cursor.close()

    return fmea


def actualizar_fmea(
        fmea_id, id_equipo_info, sistema_id, id_falla_funcional, id_componente,
        id_codigo_modo_falla, id_consecutivo_modo_falla, id_descripcion_modo_falla,
        id_causa, id_mecanismo_falla, id_detalle_falla, mtbf, mttr, id_fallo_oculto,
        id_seguridad_fisica, id_medio_ambiente, id_impacto_operacional,
        id_costos_reparacion, id_flexibilidad_operacional, calculo_severidad, id_ocurrencia,
        ocurrencia_mate, id_probabilidad_deteccion, id_metodo_deteccion_falla, rpn, id_riesgo

):
    cursor = db.connection.cursor()
    query = """
        UPDATE fmea SET
            id_equipo_info = %s, id_sistema = %s, id_falla_funcional = %s, 
            id_componente = %s, id_codigo_modo_falla = %s, id_consecutivo_modo_falla = %s, 
            id_descripcion_modo_falla = %s, id_causa = %s, id_mecanismo_falla = %s, 
            id_detalle_falla = %s, MTBF = %s, MTTR = %s, id_fallo_oculto = %s, 
            id_seguridad_fisica = %s, id_medio_ambiente = %s, id_impacto_operacional = %s, 
            id_costos_reparacion = %s, id_flexibilidad_operacional = %s, calculo_severidad = %s, id_ocurrencia = %s, 
            ocurrencia_mate = %s, id_probabilidad_deteccion = %s, id_metodo_deteccion_falla = %s, RPN = %s, id_riesgo = %s

        WHERE id = %s
    """
    cursor.execute(query, (
        id_equipo_info, sistema_id, id_falla_funcional, id_componente, id_codigo_modo_falla,
        id_consecutivo_modo_falla, id_descripcion_modo_falla, id_causa, id_mecanismo_falla,
        id_detalle_falla, mtbf, mttr, id_fallo_oculto, id_seguridad_fisica, id_medio_ambiente,
        id_impacto_operacional, id_costos_reparacion, id_flexibilidad_operacional, calculo_severidad,
        id_ocurrencia, ocurrencia_mate, id_probabilidad_deteccion, id_metodo_deteccion_falla, rpn, id_riesgo,

        fmea_id

    ))
    db.connection.commit()
    cursor.close()


##################################################################################################################


def insertar_procedimiento(arranque, parada):
    cursor = db.connection.cursor()
    query = "INSERT INTO procedimientos (arranque, parada) VALUES (%s, %s)"
    cursor.execute(query, (arranque, parada))
    db.connection.commit()
    procedimiento_id = cursor.lastrowid
    cursor.close()
    return procedimiento_id


def insertar_diagrama(diagrama_flujo, diagrama_caja_negra, diagrama_caja_transparente):
    cursor = db.connection.cursor()

    query = "INSERT INTO diagramas (diagrama_flujo, diagrama_caja_negra, diagrama_caja_transparente) VALUES (%s, %s, %s)"
    cursor.execute(query, (diagrama_flujo, diagrama_caja_negra, diagrama_caja_transparente))
    db.connection.commit()
    diagrama_id = cursor.lastrowid
    cursor.close()
    return diagrama_id


def insertar_equipo_info(nombre_equipo, AOR, fecha, fiabilidad_equipo, MTBF, GRES, criticidad_equipo,
                         marca, modelo, peso_seco, dimensiones, descripcion, imagen_equipo_file,
                         id_personal, id_diagrama, id_procedimiento, id_sistema, id_equipo
                         ):
    cursor = db.connection.cursor()

    query = """
        INSERT INTO equipo_info (
            nombre_equipo, AOR, fecha, fiabilidad_equipo, MTBF, GRES, criticidad_equipo,
            marca, modelo, peso_seco, dimensiones, descripcion, imagen,
            id_personal, id_diagrama, id_procedimiento, id_sistema, id_equipo
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        nombre_equipo, AOR, fecha, fiabilidad_equipo, MTBF, GRES, criticidad_equipo,
        marca, modelo, peso_seco, dimensiones, descripcion, imagen_equipo_file,
        id_personal, id_diagrama, id_procedimiento, id_sistema, id_equipo
    ))
    db.connection.commit()
    equipo_info_id = cursor.lastrowid
    cursor.close()
    return equipo_info_id


def obtener_equipos_por_tipo(id_tipo_equipo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id, nombre FROM equipos WHERE id_tipos_equipos = %s ORDER BY nombre"
    cursor.execute(query, (id_tipo_equipo,))
    equipospro = cursor.fetchall()
    cursor.close()
    return equipospro


def obtener_sistema_por_id(id_sistema):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM sistema WHERE id = %s"
    cursor.execute(query, (id_sistema,))
    sistema = cursor.fetchone()
    cursor.close()
    return sistema


def obtener_subsistema_por_id(id_subsistema):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM subsistemas WHERE id = %s"
    cursor.execute(query, (id_subsistema,))
    sistema = cursor.fetchone()
    cursor.close()
    return sistema


def obtener_subsistemas_por_equipo(id_equipo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM subsistemas WHERE id_equipo = %s"
    cursor.execute(query, (id_equipo,))
    subsistemas = cursor.fetchall()
    cursor.close()
    return subsistemas


# ... otras funciones ...


def insertar_analisis_funcional(verbo, accion, estandar_desempeño, id_equipo_info, subsistema_id):
    cursor = db.connection.cursor()
    query = """
            INSERT INTO analisis_funcional (verbo, accion, estandar_desempeño, id_equipo_info,id_subsistema)
            VALUES (%s, %s, %s, %s, %s)
        """
    cursor.execute(query, (verbo, accion, estandar_desempeño, id_equipo_info, subsistema_id,))
    db.connection.commit()
    analisis_funcional_id = cursor.lastrowid
    cursor.close()
    return analisis_funcional_id


###################################################################Funcines para MTA#############################


#insertar_mta(fmea['id_equipo_info'], id_sistema, id_componente, fmea['id_falla_funcional'], fmea['id_descripcion_modo_falla'], id_tipo_mantenimiento, id_tarea_mantenimiento, cantidad_personal, consumibles_requeridos ,requeridos_tarea,condiciones_ambientales, condiciones_estado_equipo, condiciones_especiales,  horas, minutos, detalle_tarea)
def insertar_mta(id_rcm, id_equipo_info, id_sistema, id_componente, id_falla_funcional, id_descripcion_modo_falla,
                 id_tipo_mantenimiento, id_tarea_mantenimiento, cantidad_personal, consumibles_requeridos,
                 requeridos_tarea, condiciones_ambientales, condiciones_estado_equipo, condiciones_especiales, horas,
                 minutos, detalle_tarea):
    cursor = db.connection.cursor()
    query = """
        INSERT INTO mta (
            id_rcm, id_equipo_info, id_sistema, id_componente, id_falla_funcional, id_descripcion_modo_falla, id_tipo_mantenimiento, id_tarea_mantenimiento, cantidad_personal, consumibles_requeridos, requeridos_tarea, condiciones_ambientales, condiciones_estado_equipo, condiciones_especiales, horas, minutos, detalle_tarea
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        id_rcm, id_equipo_info, id_sistema, id_componente, id_falla_funcional, id_descripcion_modo_falla,
        id_tipo_mantenimiento, id_tarea_mantenimiento, cantidad_personal, consumibles_requeridos, requeridos_tarea,
        condiciones_ambientales, condiciones_estado_equipo, condiciones_especiales, horas, minutos, detalle_tarea
    ))
    db.connection.commit()
    mta_id = cursor.lastrowid
    cursor.close()
    return mta_id


def actualizar_mta(id_mta, id_tipo_mantenimiento, id_tarea_mantenimiento, cantidad_personal, consumibles_requeridos,
                   requeridos_tarea, condiciones_ambientales, condiciones_estado_equipo, condiciones_especiales, horas,
                   minutos, detalle_tarea):
    cursor = db.connection.cursor()
    query = """
        UPDATE mta
        SET id_tipo_mantenimiento = %s, id_tarea_mantenimiento = %s, cantidad_personal = %s, consumibles_requeridos = %s, requeridos_tarea = %s, condiciones_ambientales = %s, condiciones_estado_equipo = %s, condiciones_especiales = %s, horas = %s, minutos = %s, detalle_tarea = %s
        WHERE id = %s
    """
    cursor.execute(query, (
        id_tipo_mantenimiento, id_tarea_mantenimiento, cantidad_personal, consumibles_requeridos, requeridos_tarea,
        condiciones_ambientales, condiciones_estado_equipo, condiciones_especiales, horas, minutos, detalle_tarea,
        id_mta
    ))
    db.connection.commit()
    cursor.close()


def eliminar_mta(id_mta):
    cursor = db.connection.cursor()
    query = "DELETE FROM mta WHERE id = %s"
    cursor.execute(query, (id_mta,))
    db.connection.commit()
    cursor.close()



def obtener_nombre_componente_por_id(componente_id):
    cursor = db.connection.cursor()
    query = "SELECT nombre FROM componentes WHERE id = %s"
    cursor.execute(query, (componente_id,))
    result = cursor.fetchone()  # Obtener el primer resultado

    cursor.close()

    if result:
        return result['nombre']  # Devolver el nombre del componente si se encuentra
    else:
        return None  # Si no se encuentra el componente, devuelve None


def obtener_tipos_mantenimiento():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre FROM tipo_mantenimiento"
    cursor.execute(query)
    tipos_mantenimiento = cursor.fetchall()
    cursor.close()

    # Devuelve una lista de diccionarios con los id y nombres de los tipos de mantenimiento
    return [{'id': fila['id'], 'nombre': fila['nombre']} for fila in tipos_mantenimiento]


def obtener_tareas_mantenimiento():
    cursor = db.connection.cursor()
    query = "SELECT id, nombre FROM tarea_mantenimiento"
    cursor.execute(query)
    tareas_mantenimiento = cursor.fetchall()
    cursor.close()

    return [{'id': fila['id'], 'nombre': fila['nombre']} for fila in tareas_mantenimiento]


#########################################################################################


#crud repuesto

def insertar_repuesto(
        id_equipo_info, nombre_herramienta, valor,
        dibujo_seccion, notas, mtbf, codigo_otan
):
    cursor = db.connection.cursor()
    query = """
        INSERT INTO repuesto (
            id_equipo_info, nombre_repuesto, valor,
            dibujo_transversal, notas, mtbf, codigo_otan
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        id_equipo_info, nombre_herramienta, valor,
        dibujo_seccion, notas, mtbf, codigo_otan
    ))
    db.connection.commit()
    repuesto_id = cursor.lastrowid
    cursor.close()
    return repuesto_id


def obtener_repuestos_por_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM repuesto WHERE id_equipo_info = %s"
    cursor.execute(query, (id_equipo_info,))
    repuestos = cursor.fetchall()
    cursor.close()
    return repuestos


def actualizar_repuesto(id_repuesto, nombre_repuesto, valor, dibujo_transversal, notas, mtbf, codigo_otan):
    cursor = db.connection.cursor()

    # Construimos la consulta SQL dinámicamente
    query = """
        UPDATE repuesto
        SET nombre_repuesto = %s, valor = %s, notas = %s, mtbf = %s, codigo_otan = %s
    """
    params = [nombre_repuesto, valor, notas, mtbf, codigo_otan]

    if dibujo_transversal is not None:
        query += ", dibujo_transversal = %s"
        params.append(dibujo_transversal)

    query += " WHERE id = %s"
    params.append(id_repuesto)

    cursor.execute(query, params)
    db.connection.commit()
    cursor.close()


# database.py
def eliminar_repuesto(id_repuesto):
    cursor = db.connection.cursor()
    query = "DELETE FROM repuesto WHERE id = %s"
    cursor.execute(query, (id_repuesto,))
    db.connection.commit()
    cursor.close()


def obtener_repuesto_por_id(id_repuesto):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM repuesto WHERE id = %s"
    cursor.execute(query, (id_repuesto,))
    repuesto = cursor.fetchone()
    cursor.close()
    return repuesto


# database.py









def eliminar_analisis_herramienta(id_analisis):
    cursor = db.connection.cursor()
    query = "DELETE FROM herramientas_generales WHERE id = %s"
    cursor.execute(query, (id_analisis,))
    db.connection.commit()
    cursor.close()


#Herramientas especiales:


def insertar_herramienta_especial(
        parte_numero, nombre_herramienta, valor,
        dibujo_seccion_transversal, nota, id_equipo_info,
        manual_referencia, id_tipo_herramienta, cantidad,
        id_herramienta_requerida, id_clase_herramienta  # Aseguramos que se recibe este parámetro

):
    cursor = db.connection.cursor()
    query = """
        INSERT INTO herramientas_especiales (
            parte_numero, nombre_herramienta, valor,
            dibujo_seccion_transversal, nota, id_equipo_info,
            manual_referencia, id_tipo_herramienta, cantidad, id_herramienta_requerida,id_clase_herramienta
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
    """
    cursor.execute(query, (
        parte_numero, nombre_herramienta, valor,
        dibujo_seccion_transversal, nota, id_equipo_info,
        manual_referencia, id_tipo_herramienta, cantidad, id_herramienta_requerida, id_clase_herramienta
    ))
    db.connection.commit()
    herramienta_id = cursor.lastrowid
    cursor.close()
    return herramienta_id


def obtener_herramienta_especial_por_id(id_herramienta):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM herramientas_especiales WHERE id = %s"
    cursor.execute(query, (id_herramienta,))
    herramienta = cursor.fetchone()
    cursor.close()
    return herramienta


def obtener_herramientas_especiales_por_equipo(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM herramientas_especiales WHERE id_equipo_info = %s"
    cursor.execute(query, (id_equipo_info,))
    herramientas = cursor.fetchall()
    cursor.close()
    return herramientas



########################################
def obtener_ids_herramientas_relacionadas(id_equipo_info, clase_herramienta):
    cursor = db.connection.cursor()
    query = """
        SELECT id_herramienta
        FROM herramientas_equipo_info
        WHERE id_equipo_info = %s AND id_clase_herramienta = %s
    """
    cursor.execute(query, (id_equipo_info, clase_herramienta))
    resultados = cursor.fetchall()
    cursor.close()
    # Extraemos solo los IDs en una lista
    ids_herramientas = [row[0] for row in resultados]
    return ids_herramientas

########################################


def actualizar_herramienta_especial(
        id_herramienta, parte_numero, nombre_herramienta, valor,
        dibujo_seccion_transversal, nota, manual_referencia, id_tipo_herramienta, cantidad
):
    cursor = db.connection.cursor()
    query = """
        UPDATE herramientas_especiales
        SET parte_numero = %s, nombre_herramienta = %s, valor = %s,
            dibujo_seccion_transversal = %s, nota = %s,
            manual_referencia = %s, id_tipo_herramienta = %s, cantidad = %s
        WHERE id = %s
    """
    cursor.execute(query, (
        parte_numero, nombre_herramienta, valor,
        dibujo_seccion_transversal, nota, manual_referencia,
        id_tipo_herramienta, cantidad, id_herramienta
    ))
    db.connection.commit()
    cursor.close()


def eliminar_herramienta_especial(id_herramienta):
    cursor = db.connection.cursor()
    query = "DELETE FROM herramientas_especiales WHERE id = %s"
    cursor.execute(query, (id_herramienta,))
    db.connection.commit()
    cursor.close()


def insertar_herramienta_requerida(nombre, id_tipo_herramienta, id_clase_herramienta):
    cursor = db.connection.cursor()
    query = """
        INSERT INTO herramientas_requeridas (nombre, id_tipo_herramienta,id_clase_herramienta)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (nombre, id_tipo_herramienta, id_clase_herramienta))
    db.connection.commit()
    herramienta_requerida_id = cursor.lastrowid
    cursor.close()
    return herramienta_requerida_id


def obtener_tipos_herramientas():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id_tipo_herramienta, nombre_tipo FROM tipo_herramientas ORDER BY nombre_tipo"
    cursor.execute(query)
    tipos = cursor.fetchall()
    cursor.close()
    return tipos


############################RCMMMMM
def obtener_rcm_por_fmea(id_fmea):
    print("id_fmea")
    print(id_fmea)
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT
            r.id,
            r.id_fmea,
            s.nombre as sistema, 
            ff.nombre as falla_funcional, 
            c.nombre as componente, 
            cmf.nombre as codigo_modo_falla, 
            cf.nombre as consecutivo_modo_falla, 
            dmf.nombre as descripcion_modo_falla, 
            causa.nombre as causa, 
            r.hidden_failures,
            r.safety,
            r.environment,
            r.operation,
            r.h1_s1_n1_o1,
            r.h2_s2_n2_o2,
            r.h3_s3_n3_o3,
            r.h4_s4,
            r.h5,
            r.tarea,
            r.id_accion_recomendada,
            r.intervalo_inicial_horas
        FROM rcm r
        LEFT JOIN fmea f ON r.id_fmea = f.id
        LEFT JOIN subsistemas s ON f.id_sistema = s.id
        LEFT JOIN falla_funcional ff ON f.id_falla_funcional = ff.id
        LEFT JOIN componentes c ON f.id_componente = c.id
        LEFT JOIN codigo_modo_falla cmf ON f.id_codigo_modo_falla = cmf.id
        LEFT JOIN consecutivo_modo_falla cf ON f.id_consecutivo_modo_falla = cf.id
        LEFT JOIN descripcion_modo_falla dmf ON f.id_descripcion_modo_falla = dmf.id
        LEFT JOIN causa ON f.id_causa = causa.id
        WHERE r.id_fmea = %s
    """
    cursor.execute(query, (id_fmea,))
    context = cursor.fetchall()
    rcm = context[0]
    print(rcm)
    cursor.close()
    return rcm


def obtener_rcm_por_id(id_rcm):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT
            r.id,
            r.id_fmea,
            s.nombre as sistema, 
            ff.nombre as falla_funcional, 
            c.nombre as componente, 
            cmf.nombre as codigo_modo_falla, 
            cf.nombre as consecutivo_modo_falla, 
            dmf.nombre as descripcion_modo_falla, 
            causa.nombre as causa, 
            r.hidden_failures,
            r.safety,
            r.environment,
            r.operation,
            r.h1_s1_n1_o1,
            r.h2_s2_n2_o2,
            r.h3_s3_n3_o3,
            r.h4_s4,
            r.h5,
            r.tarea,
            r.id_accion_recomendada,
            r.intervalo_inicial_horas
        FROM rcm r
        LEFT JOIN fmea f ON r.id_fmea = f.id
        LEFT JOIN subsistemas s ON f.id_sistema = s.id
        LEFT JOIN falla_funcional ff ON f.id_falla_funcional = ff.id
        LEFT JOIN componentes c ON f.id_componente = c.id
        LEFT JOIN codigo_modo_falla cmf ON f.id_codigo_modo_falla = cmf.id
        LEFT JOIN consecutivo_modo_falla cf ON f.id_consecutivo_modo_falla = cf.id
        LEFT JOIN descripcion_modo_falla dmf ON f.id_descripcion_modo_falla = dmf.id
        LEFT JOIN causa ON f.id_causa = causa.id
        WHERE r.id = %s
    """
    cursor.execute(query, (id_rcm,))
    rcm = cursor.fetchone()
    cursor.close()
    return rcm



def obtener_fmeas_con_rcm():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id_fmea FROM rcm"
    cursor.execute(query)
    fmeas_con_rcm = cursor.fetchall()
    cursor.close()

    # Extraer solo los id_fmea de los resultados
    id_fmeas = [fmea['id_fmea'] for fmea in fmeas_con_rcm]
    return id_fmeas




def actualizar_rcm(rcm):
    cursor = db.connection.cursor()
    query = """
        UPDATE rcm
        SET hidden_failures = %s, safety = %s, environment = %s, operation = %s, h1_s1_n1_o1 = %s, h2_s2_n2_o2 = %s, h3_s3_n3_o3 = %s, h4_s4 = %s, h5 = %s, tarea = %s, intervalo_inicial_horas = %s, id_accion_recomendada = %s
        WHERE id_fmea = %s
    """
    cursor.execute(query, (
        rcm['hidden_failures'], rcm['safety'], rcm['environment'], rcm['operation'], rcm['h1_s1_n1_o1'],
        rcm['h2_s2_n2_o2'], rcm['h3_s3_n3_o3'], rcm['h4_s4'], rcm['h5'], rcm['tarea'], rcm['intervalo_inicial_horas'],
        rcm['id_accion_recomendada'], rcm['id_fmea']
    ))
    db.connection.commit()
    cursor.close()


def obtener_lista_acciones_recomendadas():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM accion_recomendada"
    cursor.execute(query)
    accion_recomendada = cursor.fetchall()
    cursor.close()
    print("acciones")
    print(accion_recomendada)
    return accion_recomendada


def insertar_rcm(rcm):
    cursor = db.connection.cursor()
    query = """
        INSERT INTO rcm (
            id_fmea, hidden_failures, safety, environment, operation, h1_s1_n1_o1, h2_s2_n2_o2, h3_s3_n3_o3, h4_s4, h5, tarea, intervalo_inicial_horas, id_accion_recomendada
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        rcm['id_fmea'], rcm['hidden_failures'], rcm['safety'], rcm['environment'], rcm['operation'], rcm['h1_s1_n1_o1'],
        rcm['h2_s2_n2_o2'], rcm['h3_s3_n3_o3'], rcm['h4_s4'], rcm['h5'], rcm['tarea'], rcm['intervalo_inicial_horas'],
        rcm['id_accion_recomendada']
    ))
    db.connection.commit()
    cursor.close()


#generalidades


# database.py

def obtener_equipo_info_por_id(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM equipo_info WHERE id = %s"
    cursor.execute(query, (id_equipo_info,))
    equipo = cursor.fetchone()
    cursor.close()
    return equipo


def actualizar_equipo_info(id_equipo_info, data):
    cursor = db.connection.cursor()

    # Inicializamos los campos que siempre se actualizarán
    fields = [
        "nombre_equipo = %s",
        "AOR = %s",
        "fecha = %s",
        "fiabilidad_equipo = %s",
        "MTBF = %s",
        "GRES = %s",
        "criticidad_equipo = %s",
        "marca = %s",
        "peso_seco = %s",
        "modelo = %s",
        "dimensiones = %s",
        "descripcion = %s",
        "id_personal = %s",
        "id_diagrama = %s",
        "id_procedimiento = %s",
        "id_sistema = %s",
        "id_equipo = %s"
    ]

    params = [
        data['nombre_equipo'], data['aor'], data['fecha'], data['fiabilidad_equipo'], data['mtbf'],
        data['gres_sistema'],
        data['criticidad_equipo'], data['marca'], data['peso_seco'], data['modelo'], data['dimensiones'],
        data['descripcion_equipo'], data['responsable'], data['id_diagrama'], data['id_procedimiento'],
        data['sistema'], data['equipo']
    ]

    # Si hay una nueva imagen, agregamos la actualización del campo 'imagen'
    if data['imagen_equipo'] is not None:
        fields.append("imagen = %s")
        params.append(data['imagen_equipo'])

    # Añadimos el ID del equipo a los parámetros
    params.append(id_equipo_info)

    # Construimos la consulta SQL dinámicamente
    query = f"""
        UPDATE equipo_info
        SET {', '.join(fields)}
        WHERE id = %s
    """

    cursor.execute(query, params)
    db.connection.commit()
    cursor.close()


def eliminar_equipo_info(id_equipo_info):
    cursor = db.connection.cursor()
    query = "DELETE FROM equipo_info WHERE id = %s"
    cursor.execute(query, (id_equipo_info,))
    db.connection.commit()
    cursor.close()


def obtener_diagramas_por_id(id_diagrama):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM diagramas WHERE id = %s"
    cursor.execute(query, (id_diagrama,))
    diagrama = cursor.fetchone()
    cursor.close()
    return diagrama


def obtener_responsables():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id, nombre_completo FROM personal"
    cursor.execute(query)
    responsables = cursor.fetchall()
    cursor.close()
    return responsables


def obtener_procedimiento_por_id(id_procedimiento):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM procedimientos WHERE id = %s"
    cursor.execute(query, (id_procedimiento,))
    procedimiento = cursor.fetchone()
    cursor.close()
    return procedimiento


def obtener_personal_por_id(id_personal):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM personal WHERE id = %s"
    cursor.execute(query, (id_personal,))
    responsable = cursor.fetchone()
    cursor.close()
    return responsable


def obtener_grupo_constructivo_por_id(id_grupo_constructivo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM grupo_constructivo WHERE id = %s"
    cursor.execute(query, (id_grupo_constructivo,))
    grupo_constructivo = cursor.fetchone()
    cursor.close()
    return grupo_constructivo


def obtener_grupo_constructivo_por_sistema_id(id_sistema):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    # Obtener id_subgrupo de la tabla sistema
    query_sistema = "SELECT id_subgrupo FROM sistema WHERE id = %s"
    cursor.execute(query_sistema, (id_sistema,))
    sistema = cursor.fetchone()

    if not sistema:
        cursor.close()
        return None  # Si no se encuentra el sistema, retornamos None

    id_subgrupo = sistema['id_subgrupo']

    # Obtener id_grupo_constructivo de la tabla subgrupo
    query_subgrupo = "SELECT id_grupo_constructivo FROM subgrupo WHERE id = %s"
    cursor.execute(query_subgrupo, (id_subgrupo,))
    subgrupo = cursor.fetchone()

    if not subgrupo:
        cursor.close()
        return None  # Si no se encuentra el subgrupo, retornamos None

    id_grupo_constructivo = subgrupo['id_grupo_constructivo']

    # Obtener el grupo_constructivo de la tabla grupo_constructivo
    query_grupo = "SELECT * FROM grupo_constructivo WHERE id = %s"
    cursor.execute(query_grupo, (id_grupo_constructivo,))
    grupo_constructivo = cursor.fetchone()

    cursor.close()
    return grupo_constructivo  # Retornamos el grupo constructivo obtenido


def obtener_equipo_por_id(id_equipo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM equipo_info WHERE id = %s"
    cursor.execute(query, (id_equipo,))
    equipo = cursor.fetchone()
    cursor.close()
    return equipo


def obtener_subgrupo_constructivo_por_sistema_id(id_sistema):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    # Obtener id_subgrupo de la tabla sistema
    query_sistema = "SELECT id_subgrupo FROM sistema WHERE id = %s"
    cursor.execute(query_sistema, (id_sistema,))
    sistema = cursor.fetchone()

    if not sistema:
        cursor.close()
        return None  # Si no se encuentra el sistema, retornamos None

    id_subgrupo = sistema['id_subgrupo']

    # Obtener el subgrupo_constructivo de la tabla subgrupo
    query_subgrupo = "SELECT * FROM subgrupo WHERE id = %s"
    cursor.execute(query_subgrupo, (id_subgrupo,))
    subgrupo_constructivo = cursor.fetchone()

    cursor.close()
    return subgrupo_constructivo  # Retornamos el subgrupo constructivo obtenido


def obtener_datos_equipo_por_id(id_equipo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM equipos WHERE id = %s"
    cursor.execute(query, (id_equipo,))
    equipo = cursor.fetchone()
    cursor.close()
    return equipo


def obtener_tipo_equipo_por_id(id_tipos_equipos):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM tipo_equipos WHERE id = %s"
    cursor.execute(query, (id_tipos_equipos,))
    tipo_equipo = cursor.fetchone()
    cursor.close()
    return tipo_equipo



# Función para obtener todos los análisis funcionales de un equipo específico
def obtener_analisis_funcionales_por_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    query = """
    SELECT af.id, af.verbo, af.accion, af.estandar_desempeño, ss.nombre AS subsistema_nombre
    FROM analisis_funcional af
    JOIN subsistemas ss ON af.id_subsistema = ss.id
    WHERE af.id_equipo_info = %s AND af.estado = 'activo'
    """

    query2 = """
        SELECT cf.id, cf.id_componente, c.nombre, cf.verbo, cf.accion, cf.id_analisis_funcional 
        FROM componente_analisis_funcional cf
        JOIN analisis_funcional af ON af.id = cf.id_analisis_funcional
        JOIN componentes c ON c.id = cf.id_componente
        WHERE af.id_equipo_info = %s AND af.estado = 'activo';
    """


    cursor.execute(query, (id_equipo_info,))
    analisis_funcionales = cursor.fetchall()
    
    cursor.execute(query2, (id_equipo_info,))
    componentes_analisis_funcionales = cursor.fetchall()

    cursor.close()

    return analisis_funcionales, componentes_analisis_funcionales


# Función para obtener un análisis funcional por su ID
def obtener_analisis_funcional_por_id(id_analisis_funcional):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT af.*
        FROM analisis_funcional af
        WHERE af.id = %s AND af.estado = 'activo'
    """

    query2="""SELECT cf.id, cf.id_componente, c.nombre, cf.verbo, cf.accion, cf.id_analisis_funcional
        FROM componente_analisis_funcional cf
        JOIN analisis_funcional af ON cf.id_analisis_funcional = af.id
        JOIN componentes c ON c.id = cf.id_componente
        WHERE af.id = %s AND af.estado = 'activo';
    """

    cursor.execute(query, (id_analisis_funcional,))
    analisis_funcional = cursor.fetchone()

    cursor.execute(query2, (id_analisis_funcional,))
    componentes_analisis_funcionales = cursor.fetchall()

    cursor.close()
    return analisis_funcional, componentes_analisis_funcionales


# Función para actualizar un análisis funcional existente
def actualizar_analisis_funcional(id_analisis_funcional, verbo, accion, estandar_desempeño, id_subsistema, componentes):
    cursor = db.connection.cursor()
    
    # Actualizar el análisis funcional principal
    query = """
        UPDATE analisis_funcional
        SET verbo = %s, accion = %s, estandar_desempeño = %s, id_subsistema = %s
        WHERE id = %s
    """
    cursor.execute(query, (verbo, accion, estandar_desempeño, id_subsistema, id_analisis_funcional))

    # Eliminar los componentes existentes
    query_delete = "DELETE FROM componente_analisis_funcional WHERE id_analisis_funcional = %s"
    cursor.execute(query_delete, (id_analisis_funcional,))

    # Insertar componentes actualizados
    for componente in componentes:
        id_componente = componente['id_']
        verbo_componente = componente['verbo'] if componente['verbo'] else None
        accion_componente = componente['accion'] if componente['accion'] else None

        # Insertar solo si el ID del componente es válido
        if id_componente:
            query_componente = """
                INSERT INTO componente_analisis_funcional (id_componente, verbo, accion, id_analisis_funcional)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query_componente, (id_componente, verbo_componente, accion_componente, id_analisis_funcional))

    # Confirmar cambios en la base de datos
    db.connection.commit()
    cursor.close()




def obtener_subsistemas_por_equipo_mostrar(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    # Obtener el id_equipo desde equipo_info
    query_equipo = "SELECT id_equipo FROM equipo_info WHERE id = %s"
    cursor.execute(query_equipo, (id_equipo_info,))
    equipo_info = cursor.fetchone()
    if not equipo_info:
        cursor.close()
        return []

    id_equipo = equipo_info['id_equipo']

    # Obtener los subsistemas que pertenecen al id_equipo
    query_subsistemas = "SELECT id, nombre FROM subsistemas WHERE id_equipo = %s"
    cursor.execute(query_subsistemas, (id_equipo,))
    subsistemas = cursor.fetchall()
    cursor.close()
    return subsistemas


def obtener_nombre_sistema_por_id(subsistema_id):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    # Si subsistema_id se refiere directamente al sistema
    query = """
    SELECT s.nombre 
    FROM subsistemas s
    WHERE s.id = %s
    """

    cursor.execute(query, (subsistema_id,))
    resultado = cursor.fetchone()
    cursor.close()

    if resultado:
        return resultado['nombre']
    else:
        return None


def obtener_herramientas_requeridas_por_tipo():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    dict_herramientas = {}
    tipos = obtener_tipos_herramientas()
    for tipo in tipos:
        query = '''SELECT * FROM herramientas_requeridas hr 
                join tipo_herramientas th on hr.id_tipo_herramienta = th.id_tipo_herramienta 
                WHERE nombre_tipo = %s'''
        cursor.execute(query, (tipo['nombre_tipo'],))
        herramientas = cursor.fetchall()
        dict_herramientas[tipo['nombre_tipo']] = herramientas
    cursor.close()

    return dict_herramientas


def insertar_herramientas_requeridas_mta(herramientas_requeridas, id_mta):
    cursor = db.connection.cursor()
    #recorrer la tupla de herramientas requeridas e insertarlas junto al id_mta en la tabla herramientas_mta
    if herramientas_requeridas:
        for herramienta in herramientas_requeridas:
            query = '''INSERT INTO herramientas_mta (id_mta, id_herramienta_requerida) VALUES (%s, %s)'''
            cursor.execute(query, (id_mta, herramienta))
        db.connection.commit()
    cursor.close()


def eliminar_herramientas_requeridas_mta(id_mta):
    cursor = db.connection.cursor()
    query = "DELETE FROM herramientas_mta WHERE id_mta = %s"
    cursor.execute(query, (id_mta,))
    db.connection.commit()
    cursor.close()


# obtener_herramientas_mta,
def obtener_herramientas_mta():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = '''SELECT * FROM herramientas_mta hm
            JOIN herramientas_requeridas hr on hm.id_herramienta_requerida = hr.id_herramienta_requerida'''
    cursor.execute(query)
    herramientas_mta = cursor.fetchall()
    cursor.close()
    return herramientas_mta


def insertar_repuestos_requeridos_mta(repuestos_requeridos, id_mta):
    cursor = db.connection.cursor()
    #recorrer la tupla de herramientas requeridas e insertarlas junto al id_mta en la tabla herramientas_mta
    if repuestos_requeridos:
        for repuesto in repuestos_requeridos:
            query = '''INSERT INTO repuestos_mta (id_mta, id_repuesto) VALUES (%s, %s)'''
            cursor.execute(query, (id_mta, repuesto))
        db.connection.commit()
    cursor.close()


def eliminar_repuestos_requeridos_mta(id_mta):
    cursor = db.connection.cursor()
    query = "DELETE FROM repuestos_mta WHERE id_mta = %s"
    cursor.execute(query, (id_mta,))
    db.connection.commit()
    cursor.close()


#     obtener_repuestos_mta
def obtener_repuestos_mta():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = '''SELECT * FROM repuestos_mta rm
            JOIN repuesto r on rm.id_repuesto = r.id'''
    cursor.execute(query)
    repuestos_mta = cursor.fetchall()
    cursor.close()
    return repuestos_mta


def insertar_mta_lora(nivel, actividades, operario, id_mta):
    cursor = db.connection.cursor()
    query = '''INSERT INTO lora_mta (nivel, actividades, operario, id_mta) VALUES (%s, %s, %s, %s)'''
    cursor.execute(query, (nivel, actividades, operario, id_mta))
    db.connection.commit()
    cursor.close()


def actualizar_mta_lora(nivel, actividades, operario, id_mta):
    cursor = db.connection.cursor()
    query = '''UPDATE lora_mta SET nivel = %s, actividades = %s, operario = %s WHERE id_mta = %s'''
    cursor.execute(query, (nivel, actividades, operario, id_mta))
    db.connection.commit()
    cursor.close()


def eliminar_mta_lora(id_mta):
    cursor = db.connection.cursor()
    query = "DELETE FROM lora_mta WHERE id_mta = %s"
    cursor.execute(query, (id_mta,))
    db.connection.commit()
    cursor.close()


def obtener_mta_lora():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM lora_mta"
    cursor.execute(query)
    lora_mta = cursor.fetchall()
    cursor.close()
    return lora_mta


def obtener_max_id_mta():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT MAX(id) as max_id FROM mta"
    cursor.execute(query)
    max_id = cursor.fetchone()
    cursor.close()
    print(max_id['max_id'])
    return max_id['max_id']


def obtener_rcms_con_mta():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id_rcm FROM mta"
    cursor.execute(query)
    rcms_con_mta = cursor.fetchall()
    cursor.close()

    # Extraer solo los id_fmea de los resultados
    id_rcms = [mta['id_rcm'] for mta in rcms_con_mta]
    return id_rcms


def obtener_lora_mta_por_id_mta(id_mta):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM lora_mta WHERE id_mta = %s"
    cursor.execute(query, (id_mta,))
    lora_mta = cursor.fetchone()
    cursor.close()
    return lora_mta


def obtener_herramientas_mta_por_id_mta(id_mta):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = '''SELECT * FROM herramientas_mta hm
            JOIN herramientas_requeridas hr on hm.id_herramienta_requerida = hr.id_herramienta_requerida
            WHERE id_mta = %s'''
    cursor.execute(query, (id_mta,))
    herramientas_mta = cursor.fetchall()
    cursor.close()
    return herramientas_mta


def obtener_repuestos_mta_por_id_mta(id_mta):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = '''SELECT * FROM repuestos_mta rm
            JOIN repuesto r on rm.id_repuesto = r.id
            WHERE id_mta = %s'''
    cursor.execute(query, (id_mta,))
    repuestos_mta = cursor.fetchall()
    cursor.close()
    return repuestos_mta


# Función para obtener el id_equipo_info basado en nombre_equipo en MySQL
def obtener_id_equipo_info_por_nombre(nombre_equipo):
    # Conectar a la base de datos MySQL
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    # Consulta SQL para obtener id_equipo_info basado en nombre_equipo
    query = "SELECT id FROM equipo_info WHERE nombre_equipo = %s"
    cursor.execute(query, (nombre_equipo,))

    # Obtener el primer resultado
    result = cursor.fetchone()

    # Cerrar la conexión
    cursor.close()
    if result:
        return result['id']  # Devuelve el id del equipo
    else:
        return None


# obtener_informacion_equipo_info,
def obtener_informacion_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM equipo_info WHERE id = %s"
    cursor.execute(query, (id_equipo_info,))
    equipo_info = cursor.fetchone()
    cursor.close()
    return equipo_info


# obtener_fmeas_por_equipo_info,
def obtener_fmeas_por_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
    SELECT 
        f.id, 
        f.id_equipo_info, 
        f.id_sistema, 

        s.nombre as sistema, 
        f.id_falla_funcional, 
        ff.nombre as falla_funcional, 
        f.id_componente, 
        c.nombre as componente, 
        f.id_codigo_modo_falla, 
        cmf.nombre as codigo_modo_falla, 

        f.id_consecutivo_modo_falla, 
        cf.nombre as consecutivo_modo_falla, 
        f.id_descripcion_modo_falla, 
        dmf.nombre as descripcion_modo_falla, 
        f.id_causa, 
        causa.nombre as causa, 
        f.id_mecanismo_falla, 
        mf.nombre as mecanismo_falla, 
        f.id_detalle_falla, 
        df.nombre as detalle_falla, 

        f.MTBF, 
        f.MTTR, 
        f.id_metodo_deteccion_falla,
        f.id_fallo_oculto,
        fo.valor as fallo_oculto_valor, 
        fo.nombre as fallo_oculto_descripcion, 
        f.id_seguridad_fisica, 
        sf.valor as seguridad_fisica_valor, 
        sf.nombre as seguridad_fisica_descripcion, 
        f.id_medio_ambiente, 
        ma.valor as medio_ambiente_valor, 
        ma.nombre as medio_ambiente_descripcion, 
        f.id_impacto_operacional, 
        io.valor as impacto_operacional_valor, 
        io.nombre as impacto_operacional_descripcion, 
        f.id_costos_reparacion, 
        cr.valor as costos_reparacion_valor, 
        cr.nombre as costos_reparacion_descripcion, 
        f.id_flexibilidad_operacional, 
        flex.valor as flexibilidad_operacional_valor, 
        flex.nombre as flexibilidad_operacional_descripcion, 
        f.calculo_severidad,
        f.id_ocurrencia, 
        o.valor as ocurrencia_valor, 
        o.nombre as ocurrencia_descripcion, 
        f.ocurrencia_mate, 
        f.id_probabilidad_deteccion, 
        pd.valor as probabilidad_deteccion_valor, 
        pd.descripcion as probabilidad_deteccion_descripcion,
        f.RPN,
        f.id_riesgo,
        p.nombre_completo as nombre_completo,
        p.id as id_personal
    FROM fmea f
    LEFT JOIN equipo_info ei ON f.id_equipo_info = ei.id
    LEFT JOIN personal p ON ei.id_personal = p.id
    LEFT JOIN sistema s ON f.id_sistema = s.id
    LEFT JOIN falla_funcional ff ON f.id_falla_funcional = ff.id
    LEFT JOIN componentes c ON f.id_componente = c.id
    LEFT JOIN codigo_modo_falla cmf ON f.id_codigo_modo_falla = cmf.id
    LEFT JOIN consecutivo_modo_falla cf ON f.id_consecutivo_modo_falla = cf.id
    LEFT JOIN descripcion_modo_falla dmf ON f.id_descripcion_modo_falla = dmf.id
    LEFT JOIN causa ON f.id_causa = causa.id
    LEFT JOIN mecanismo_falla mf ON f.id_mecanismo_falla = mf.id
    LEFT JOIN detalle_falla df ON f.id_detalle_falla = df.id
    LEFT JOIN fallo_oculto fo ON f.id_fallo_oculto = fo.id
    LEFT JOIN seguridad_fisica sf ON f.id_seguridad_fisica = sf.id
    LEFT JOIN medio_ambiente ma ON f.id_medio_ambiente = ma.id
    LEFT JOIN impacto_operacional io ON f.id_impacto_operacional = io.id
    LEFT JOIN costos_reparacion cr ON f.id_costos_reparacion = cr.id
    LEFT JOIN flexibilidad_operacional flex ON f.id_flexibilidad_operacional = flex.id
    LEFT JOIN ocurrencia o ON f.id_ocurrencia = o.id
    LEFT JOIN probabilidad_deteccion pd ON f.id_probabilidad_deteccion = pd.id
    WHERE f.id_equipo_info = %s
    """
    cursor.execute(query, (id_equipo_info,))
    fmeas = cursor.fetchall()
    cursor.close()
    return fmeas



def obtener_rcm_por_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    query = """
            SELECT
                r.id,
                r.id_fmea,
                f.id_equipo_info,
                s.nombre AS sistema, 
                ff.nombre AS falla_funcional, 
                c.nombre AS componente, 
                cmf.nombre AS codigo_modo_falla, 
                cf.nombre AS consecutivo_modo_falla, 
                dmf.nombre AS descripcion_modo_falla, 
                causa.nombre AS causa, 
                r.hidden_failures,
                r.safety,
                r.environment,
                r.operation,
                r.h1_s1_n1_o1,
                r.h2_s2_n2_o2,
                r.h3_s3_n3_o3,
                r.h4_s4,
                r.h5,
                r.tarea,
                ar.nombre AS accion_recomendada, -- Se agrega el nombre de la acción recomendada
                r.intervalo_inicial_horas
            FROM rcm r
            LEFT JOIN fmea f ON r.id_fmea = f.id
            LEFT JOIN subsistemas s ON f.id_sistema = s.id
            LEFT JOIN falla_funcional ff ON f.id_falla_funcional = ff.id
            LEFT JOIN componentes c ON f.id_componente = c.id
            LEFT JOIN codigo_modo_falla cmf ON f.id_codigo_modo_falla = cmf.id
            LEFT JOIN consecutivo_modo_falla cf ON f.id_consecutivo_modo_falla = cf.id
            LEFT JOIN descripcion_modo_falla dmf ON f.id_descripcion_modo_falla = dmf.id
            LEFT JOIN causa ON f.id_causa = causa.id
            LEFT JOIN accion_recomendada ar ON r.id_accion_recomendada = ar.id 
            WHERE f.id_equipo_info = %s AND r.estado = 'activo'

        """

    cursor.execute(query, (id_equipo_info,))
    rcms = cursor.fetchall()
    cursor.close()
    return rcms

# obtener_mta_por_equipo_info
def obtener_mta_por_equipo_info(id_equipo_info):

    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT 
            m.id, 
            m.id_rcm, 
            m.id_equipo_info, 
            m.id_sistema, 
            m.id_componente, 
            m.id_falla_funcional, 
            m.id_descripcion_modo_falla, 
            m.id_tipo_mantenimiento, 
            m.id_tarea_mantenimiento, 
            m.cantidad_personal, 
            m.consumibles_requeridos, 
            m.requeridos_tarea, 
            m.condiciones_ambientales, 
            m.condiciones_estado_equipo, 
            m.condiciones_especiales, 
            m.horas, 
            m.minutos, 
            m.detalle_tarea,
            ei.nombre_equipo as equipo, 
            s.nombre as sistema, 
            c.nombre as componente, 
            ff.nombre as falla_funcional, 
            dmf.nombre as descripcion_modo_falla, 
            tm.nombre as tipo_mantenimiento, 
            tmr.nombre as tarea_mantenimiento,
            l.nivel,
            l.actividades,
            l.operario        
        FROM mta m
        LEFT JOIN rcm r ON m.id_rcm = r.id
        LEFT JOIN equipo_info ei ON m.id_equipo_info = ei.id
        LEFT JOIN sistema s ON m.id_sistema = s.id
        LEFT JOIN componentes c ON m.id_componente = c.id
        LEFT JOIN falla_funcional ff ON m.id_falla_funcional = ff.id
        LEFT JOIN descripcion_modo_falla dmf ON m.id_descripcion_modo_falla = dmf.id
        LEFT JOIN tipo_mantenimiento tm ON m.id_tipo_mantenimiento = tm.id
        LEFT JOIN tarea_mantenimiento tmr ON m.id_tarea_mantenimiento = tmr.id
        LEFT JOIN lora_mta l ON m.id = l.id_mta
        WHERE m.id_equipo_info = %s AND m.estado = 'activo'
        """
    cursor.execute(query, (id_equipo_info,))
    mta = cursor.fetchall()
    cursor.close()

    return mta



def crear_personal(nombre_completo):
    correo = 'correo1@example.com'
    password = 'password1'
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = "INSERT INTO personal (correo, password, nombre_completo) VALUES (%s, %s, %s)"
    cursor.execute(sql, (correo, password, nombre_completo))
    db.connection.commit()
    new_id = cursor.lastrowid
    cursor.close()
    return new_id

def obtener_fmeas_con_rcm_por_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT f.id
        FROM rcm r
        LEFT JOIN fmea f ON r.id_fmea = f.id
        WHERE f.id_equipo_info = %s AND r.estado = 'activo'
    """
    cursor.execute(query, (id_equipo_info,))

    fmeas_con_rcm = cursor.fetchall()
    cursor.close()

    # Extraer solo los id_fmea de los resultados
    id_fmeas = [fmea['id_fmea'] for fmea in fmeas_con_rcm]
    return id_fmeas

def obtener_rcms_con_mta_por_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    query = """
        SELECT m.id_rcm
        FROM mta m
        WHERE m.id_equipo_info = %s AND m.estado = 'activo'
    """

    cursor.execute(query, (id_equipo_info,))
    rcms_con_mta = cursor.fetchall()
    cursor.close()

    # Extraer solo los id_rcm de los resultados
    id_rcms = [rcm['id_rcm'] for rcm in rcms_con_mta]
    return id_rcms





###funciones desactivar
def desactivar_mta(id_mta):

    cursor = db.connection.cursor()
    # Cambiar el estado a 'inactivo' en lugar de eliminar
    update_query = "UPDATE mta SET estado = 'inactivo' WHERE id = %s"
    cursor.execute(update_query, (id_mta,))
    db.connection.commit()
    cursor.close()

def desactivar_rcm(id_fmea,id_rcm):
    cursor = db.connection.cursor()
    # Cambiar el estado a 'inactivo' en lugar de eliminar
    update_query = "UPDATE rcm SET estado = 'inactivo' WHERE id_fmea = %s AND id = %s"
    cursor.execute(update_query, (id_fmea,id_rcm))
    db.connection.commit()
    cursor.close()
"""
def eliminar_FMEA(fmea_id):
    cursor = db.connection.cursor()
    # Cambiar el estado a 'inactivo' en lugar de eliminar
    update_query = "UPDATE fmea SET estado = 'inactivo' WHERE id = %s"
    cursor.execute(update_query, (fmea_id,))
    db.connection.commit()
    cursor.close()
"""
def desactivar_equipo_info(id_equipo_in):
    cursor = db.connection.cursor()
    # Cambiar el estado a 'inactivo' en lugar de eliminar
    update_query = "UPDATE equipo_info SET estado = 'inactivo' WHERE id = %s"
    cursor.execute(update_query, (id_equipo_in,))

    db.connection.commit()
    cursor.close()


########################################






def obtener_subgrupos_por_sistema(id_sistema):

    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    # Obtener el id_subgrupo relacionado con el sistema

    query_sistema = "SELECT id_subgrupo FROM sistema WHERE id = %s"
    cursor.execute(query_sistema, (id_sistema,))
    sistema = cursor.fetchone()

    if not sistema:
        cursor.close()
        return None  # Si el sistema no existe, retornamos None

    id_subgrupo = sistema['id_subgrupo']

    # Obtener información del subgrupo asociado
    query_subgrupo = "SELECT * FROM subgrupo WHERE id = %s"
    cursor.execute(query_subgrupo, (id_subgrupo,))
    subgrupo_constructivo = cursor.fetchall()  # Retornará una lista de subgrupos

    cursor.close()
    return subgrupo_constructivo


def obtener_sistemas_por_grupo(grupo_id):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    # Obtener todos los subgrupos que pertenecen al grupo constructivo
    query_subgrupos = "SELECT id FROM subgrupo WHERE id_grupo_constructivo = %s"
    cursor.execute(query_subgrupos, (grupo_id,))
    subgrupos = cursor.fetchall()

    # Extraer los IDs de subgrupo para buscar sistemas asociados
    subgrupo_ids = [subgrupo['id'] for subgrupo in subgrupos]

    if not subgrupo_ids:
        cursor.close()
        return []  # Si no hay subgrupos, retornar lista vacía

    # Obtener sistemas que pertenecen a estos subgrupos
    query_sistemas = "SELECT * FROM sistema WHERE id_subgrupo IN %s"
    cursor.execute(query_sistemas, (tuple(subgrupo_ids),))
    sistemas = cursor.fetchall()

    cursor.close()
    return sistemas


def obtener_equipos_por_sistema(sistema_id):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    
    # Consultar equipos relacionados al sistema específico en la tabla equipo_info
    query = """
        SELECT *
        FROM equipo_info
        WHERE id_sistema = %s
    """
    cursor.execute(query, (sistema_id,))
    equipos = cursor.fetchall()
    

    cursor.close()
    return equipos



def actualizar_procedimiento(id_procedimiento, arranque, parada):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = '''
        UPDATE procedimientos
        SET arranque = %s,
            parada = %s
        WHERE id = %s
    '''
    cursor.execute(query, (arranque, parada, id_procedimiento))
    db.connection.commit()
    cursor.close()



def actualizar_diagrama(id_diagrama, diagrama_flujo_file, diagrama_caja_negra_file, diagrama_caja_transparente_file):

    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    # Leer los archivos si existen
    diagrama_flujo = diagrama_flujo_file.read() if diagrama_flujo_file else None
    diagrama_caja_negra = diagrama_caja_negra_file.read() if diagrama_caja_negra_file else None
    diagrama_caja_transparente = diagrama_caja_transparente_file.read() if diagrama_caja_transparente_file else None

    # Preparar los campos y valores para la consulta de actualización
    campos = []
    valores = []

    if diagrama_flujo is not None:
        campos.append('diagrama_flujo = %s')
        valores.append(diagrama_flujo)
    if diagrama_caja_negra is not None:
        campos.append('diagrama_caja_negra = %s')
        valores.append(diagrama_caja_negra)
    if diagrama_caja_transparente is not None:
        campos.append('diagrama_caja_transparente = %s')
        valores.append(diagrama_caja_transparente)

    # Solo ejecutamos la consulta si hay campos para actualizar
    if campos:
        valores.append(id_diagrama)
        query = 'UPDATE diagramas SET ' + ', '.join(campos) + ' WHERE id = %s'
        cursor.execute(query, valores)
        db.connection.commit()

    cursor.close()



def obtener_id_sistema_por_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT id_sistema 
        FROM equipo_info 
        WHERE id = %s
    """
    cursor.execute(query, (id_equipo_info,))
    fila = cursor.fetchone()
    cursor.close()
    return fila['id_sistema'] if fila else None



def obtener_id_equipo_por_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    query = """
        SELECT id_equipo 
        FROM equipo_info 
        WHERE id = %s
    """
    cursor.execute(query, (id_equipo_info,))
    fila = cursor.fetchone()

    cursor.close()
    return fila['id_equipo'] if fila else None





def check_nombre_equipo_exists(nombre_equipo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT COUNT(*) AS count FROM equipo_info WHERE nombre_equipo = %s AND estado = 'activo'"
    cursor.execute(query, (nombre_equipo,))
    result = cursor.fetchone()
    cursor.close()
    return result['count'] > 0





def obtener_herramientas_requeridas_por_tipo():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    dict_herramientas = {}
    tipos = obtener_tipos_herramientas()
    for tipo in tipos:
        query = '''SELECT * FROM herramientas_requeridas hr 
                join tipo_herramientas th on hr.id_tipo_herramienta = th.id_tipo_herramienta 
                WHERE nombre_tipo = %s'''
        cursor.execute(query, (tipo['nombre_tipo'],))
        herramientas = cursor.fetchall()
        dict_herramientas[tipo['nombre_tipo']] = herramientas
    cursor.close()

    return dict_herramientas


def insertar_herramientas_requeridas_mta(herramientas_requeridas, id_mta):
    cursor = db.connection.cursor()
    #recorrer la tupla de herramientas requeridas e insertarlas junto al id_mta en la tabla herramientas_mta
    if herramientas_requeridas:
        for herramienta in herramientas_requeridas:
            query = '''INSERT INTO herramientas_mta (id_mta, id_herramienta_requerida) VALUES (%s, %s)'''
            cursor.execute(query, (id_mta, herramienta))
        db.connection.commit()
    cursor.close()


def eliminar_herramientas_requeridas_mta(id_mta):
    cursor = db.connection.cursor()
    query = "DELETE FROM herramientas_mta WHERE id_mta = %s"
    cursor.execute(query, (id_mta,))
    db.connection.commit()
    cursor.close()


# obtener_herramientas_mta,
def obtener_herramientas_mta():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = '''SELECT * FROM herramientas_mta hm
            JOIN herramientas_requeridas hr on hm.id_herramienta_requerida = hr.id_herramienta_requerida'''
    cursor.execute(query)
    herramientas_mta = cursor.fetchall()
    cursor.close()
    return herramientas_mta


def insertar_repuestos_requeridos_mta(repuestos_requeridos, id_mta):
    cursor = db.connection.cursor()
    #recorrer la tupla de herramientas requeridas e insertarlas junto al id_mta en la tabla herramientas_mta
    if repuestos_requeridos:
        for repuesto in repuestos_requeridos:
            query = '''INSERT INTO repuestos_mta (id_mta, id_repuesto) VALUES (%s, %s)'''
            cursor.execute(query, (id_mta, repuesto))
        db.connection.commit()
    cursor.close()


def eliminar_repuestos_requeridos_mta(id_mta):
    cursor = db.connection.cursor()
    query = "DELETE FROM repuestos_mta WHERE id_mta = %s"
    cursor.execute(query, (id_mta,))
    db.connection.commit()
    cursor.close()


#     obtener_repuestos_mta
def obtener_repuestos_mta():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = '''SELECT * FROM repuestos_mta rm
            JOIN repuesto r on rm.id_repuesto = r.id'''
    cursor.execute(query)
    repuestos_mta = cursor.fetchall()
    cursor.close()
    return repuestos_mta


def insertar_mta_lora(nivel, actividades, operario, id_mta):
    cursor = db.connection.cursor()
    query = '''INSERT INTO lora_mta (nivel, actividades, operario, id_mta) VALUES (%s, %s, %s, %s)'''
    cursor.execute(query, (nivel, actividades, operario, id_mta))
    db.connection.commit()
    cursor.close()


def actualizar_mta_lora(nivel, actividades, operario, id_mta):
    cursor = db.connection.cursor()
    query = '''UPDATE lora_mta SET nivel = %s, actividades = %s, operario = %s WHERE id_mta = %s'''
    cursor.execute(query, (nivel, actividades, operario, id_mta))
    db.connection.commit()
    cursor.close()


def eliminar_mta_lora(id_mta):
    cursor = db.connection.cursor()
    query = "DELETE FROM lora_mta WHERE id_mta = %s"
    cursor.execute(query, (id_mta,))
    db.connection.commit()
    cursor.close()


def obtener_mta_lora():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM lora_mta"
    cursor.execute(query)
    lora_mta = cursor.fetchall()
    cursor.close()
    return lora_mta


def obtener_max_id_mta():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT MAX(id) as max_id FROM mta"
    cursor.execute(query)
    max_id = cursor.fetchone()
    cursor.close()
    print(max_id['max_id'])
    return max_id['max_id']


def obtener_rcms_con_mta():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id_rcm FROM mta"
    cursor.execute(query)
    rcms_con_mta = cursor.fetchall()
    cursor.close()

    # Extraer solo los id_fmea de los resultados
    id_rcms = [mta['id_rcm'] for mta in rcms_con_mta]
    return id_rcms


def obtener_lora_mta_por_id_mta(id_mta):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM lora_mta WHERE id_mta = %s"
    cursor.execute(query, (id_mta,))
    lora_mta = cursor.fetchone()
    cursor.close()
    return lora_mta


def obtener_herramientas_mta_por_id_mta(id_mta):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = '''SELECT * FROM herramientas_mta hm
            JOIN herramientas_requeridas hr on hm.id_herramienta_requerida = hr.id_herramienta_requerida
            WHERE id_mta = %s'''
    cursor.execute(query, (id_mta,))
    herramientas_mta = cursor.fetchall()
    cursor.close()
    return herramientas_mta


def obtener_repuestos_mta_por_id_mta(id_mta):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = '''SELECT * FROM repuestos_mta rm
            JOIN repuesto r on rm.id_repuesto = r.id
            WHERE id_mta = %s'''
    cursor.execute(query, (id_mta,))
    repuestos_mta = cursor.fetchall()
    cursor.close()
    return repuestos_mta


# Función para obtener el id_equipo_info basado en nombre_equipo en MySQL
def obtener_id_equipo_info_por_nombre(nombre_equipo):
    # Conectar a la base de datos MySQL
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    # Consulta SQL para obtener id_equipo_info basado en nombre_equipo
    query = "SELECT id FROM equipo_info WHERE nombre_equipo = %s"
    cursor.execute(query, (nombre_equipo,))

    # Obtener el primer resultado
    result = cursor.fetchone()

    # Cerrar la conexión
    cursor.close()
    if result:
        return result['id']  # Devuelve el id del equipo
    else:
        return None


# obtener_informacion_equipo_info,
def obtener_informacion_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM equipo_info WHERE id = %s"
    cursor.execute(query, (id_equipo_info,))
    equipo_info = cursor.fetchone()
    cursor.close()
    return equipo_info


# obtener_fmeas_por_equipo_info,
def obtener_fmeas_por_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
    SELECT 
            f.id, 
            f.id_equipo_info, 
            f.id_sistema, 
            s.nombre AS sistema, 
            f.id_falla_funcional, 
            ff.nombre AS falla_funcional, 
            f.id_componente, 
            c.nombre AS componente, 
            f.id_codigo_modo_falla, 
            cmf.nombre AS codigo_modo_falla, 
            f.id_consecutivo_modo_falla, 
            cf.nombre AS consecutivo_modo_falla, 
            f.id_descripcion_modo_falla, 
            dmf.nombre AS descripcion_modo_falla, 
            f.id_causa, 
            causa.nombre AS causa, 
            f.id_mecanismo_falla, 
            mf.nombre AS mecanismo_falla, 
            f.id_detalle_falla, 
            df.nombre AS detalle_falla, 
            f.MTBF, 
            f.MTTR, 
            f.id_metodo_deteccion_falla,
            f.id_fallo_oculto,
            fo.valor AS fallo_oculto_valor, 
            fo.nombre AS fallo_oculto_descripcion, 
            f.id_seguridad_fisica, 
            sf.valor AS seguridad_fisica_valor, 
            sf.nombre AS seguridad_fisica_descripcion, 
            f.id_medio_ambiente, 
            ma.valor AS medio_ambiente_valor, 
            ma.nombre AS medio_ambiente_descripcion, 
            f.id_impacto_operacional, 
            io.valor AS impacto_operacional_valor, 
            io.nombre AS impacto_operacional_descripcion, 
            f.id_costos_reparacion, 
            cr.valor AS costos_reparacion_valor, 
            cr.nombre AS costos_reparacion_descripcion, 
            f.id_flexibilidad_operacional, 
            flex.valor AS flexibilidad_operacional_valor, 
            flex.nombre AS flexibilidad_operacional_descripcion, 
            f.calculo_severidad,
            f.id_ocurrencia, 
            o.valor AS ocurrencia_valor, 
            o.nombre AS ocurrencia_descripcion, 
            f.ocurrencia_mate, 
            f.id_probabilidad_deteccion, 
            pd.valor AS probabilidad_deteccion_valor, 
            pd.descripcion AS probabilidad_deteccion_descripcion,
            f.RPN,
            f.id_riesgo,
            r.nombre AS nombre_riesgo,
            p.nombre_completo AS nombre_completo,
            p.id AS id_personal
          FROM fmea f
        LEFT JOIN equipo_info ei ON f.id_equipo_info = ei.id
        LEFT JOIN personal p ON ei.id_personal = p.id
        LEFT JOIN subsistemas s ON f.id_sistema = s.id
        LEFT JOIN falla_funcional ff ON f.id_falla_funcional = ff.id
        LEFT JOIN componentes c ON f.id_componente = c.id
        LEFT JOIN codigo_modo_falla cmf ON f.id_codigo_modo_falla = cmf.id
        LEFT JOIN consecutivo_modo_falla cf ON f.id_consecutivo_modo_falla = cf.id
        LEFT JOIN descripcion_modo_falla dmf ON f.id_descripcion_modo_falla = dmf.id
        LEFT JOIN causa ON f.id_causa = causa.id
        LEFT JOIN mecanismo_falla mf ON f.id_mecanismo_falla = mf.id
        LEFT JOIN detalle_falla df ON f.id_detalle_falla = df.id
        LEFT JOIN fallo_oculto fo ON f.id_fallo_oculto = fo.id
        LEFT JOIN seguridad_fisica sf ON f.id_seguridad_fisica = sf.id
        LEFT JOIN medio_ambiente ma ON f.id_medio_ambiente = ma.id
        LEFT JOIN impacto_operacional io ON f.id_impacto_operacional = io.id
        LEFT JOIN costos_reparacion cr ON f.id_costos_reparacion = cr.id
        LEFT JOIN flexibilidad_operacional flex ON f.id_flexibilidad_operacional = flex.id
        LEFT JOIN ocurrencia o ON f.id_ocurrencia = o.id
        LEFT JOIN probabilidad_deteccion pd ON f.id_probabilidad_deteccion = pd.id
        LEFT JOIN riesgo r ON f.id_riesgo = r.id
        WHERE f.id_equipo_info = %s
    """
    cursor.execute(query, (id_equipo_info,))
    fmeas = cursor.fetchall()
    cursor.close()
    return fmeas




# obtener_mta_por_equipo_info
def obtener_mta_por_equipo_info(id_equipo_info):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT 
            m.id, 
            m.id_rcm, 
            m.id_equipo_info, 
            m.id_sistema, 
            m.id_componente, 
            m.id_falla_funcional, 
            m.id_descripcion_modo_falla, 
            m.id_tipo_mantenimiento, 
            m.id_tarea_mantenimiento, 
            m.cantidad_personal, 
            m.consumibles_requeridos, 
            m.requeridos_tarea, 
            m.condiciones_ambientales, 
            m.condiciones_estado_equipo, 
            m.condiciones_especiales, 
            m.horas, 
            m.minutos, 
            m.detalle_tarea,
            ei.nombre_equipo as equipo, 
            s.nombre as sistema, 
            c.nombre as componente, 
            ff.nombre as falla_funcional, 
            dmf.nombre as descripcion_modo_falla, 
            tm.nombre as tipo_mantenimiento, 
            tmr.nombre as tarea_mantenimiento,
            l.nivel,
            l.actividades,
            l.operario        
        FROM mta m
        LEFT JOIN rcm r ON m.id_rcm = r.id
        LEFT JOIN equipo_info ei ON m.id_equipo_info = ei.id
        LEFT JOIN subsistemas s ON m.id_sistema = s.id
        LEFT JOIN componentes c ON m.id_componente = c.id
        LEFT JOIN falla_funcional ff ON m.id_falla_funcional = ff.id
        LEFT JOIN descripcion_modo_falla dmf ON m.id_descripcion_modo_falla = dmf.id
        LEFT JOIN tipo_mantenimiento tm ON m.id_tipo_mantenimiento = tm.id
        LEFT JOIN tarea_mantenimiento tmr ON m.id_tarea_mantenimiento = tmr.id
        LEFT JOIN lora_mta l ON m.id = l.id_mta
        WHERE m.id_equipo_info = %s
        """
    cursor.execute(query, (id_equipo_info,))
    mta = cursor.fetchall()
    cursor.close()

    return mta

def eliminar_personal(id_personal):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        # Primero, eliminar registros en equipo_info que referencian al personal
        sql_equipo_info = "UPDATE equipo_info SET id_personal = NULL WHERE id_personal = %s"
        cursor.execute(sql_equipo_info, (id_personal,))

        # Ahora, eliminar el registro en personal
        sql = "DELETE FROM personal WHERE id = %s"
        cursor.execute(sql, (id_personal,))

        db.connection.commit()
    except MySQLdb.IntegrityError as e:
        print(f"Error al eliminar personal: {e}")
        # Opcionalmente, puedes manejar la excepción según tus necesidades
        # Por ejemplo, devolver un mensaje de error o lanzar una excepción personalizada
        raise
    finally:
        cursor.close()




def crear_personal(nombre_completo):
    correo = 'correo1@example.com'
    password = 'password1'
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = "INSERT INTO personal (correo, password, nombre_completo) VALUES (%s, %s, %s)"
    cursor.execute(sql, (correo, password, nombre_completo))
    db.connection.commit()
    new_id = cursor.lastrowid
    cursor.close()
    return new_id