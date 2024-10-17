from __init__ import db
import MySQLdb.cursors


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

    return [{'id': fila['id'],'nombre': fila['nombre'], 'valor': fila['valor']} for fila in fallos_ocultos]

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

    
    return [{'id': fila['id'], 'nombre': fila['nombre'], 'valor': fila['valor']} for fila in flexibilidad_operacional_datos]

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

    
    return [{'id': fila['id'], 'descripcion': fila['descripcion'], 'valor': fila['valor']} for fila in probabilidad_deteccion_datos]

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
        id_detalle_falla, MTBF, MTTR,id_metodo_deteccion_falla, id_fallo_oculto, id_seguridad_fisica, 
        id_medio_ambiente, 
        id_impacto_operacional, id_costos_reparacion, id_flexibilidad_operacional,calculo_severidad, 
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
        id_detalle_falla, MTBF, MTTR,id_metodo_deteccion_falla, id_fallo_oculto, id_seguridad_fisica, id_medio_ambiente, 
        id_impacto_operacional, id_costos_reparacion, id_flexibilidad_operacional,calculo_severidad, id_ocurrencia,
        ocurrencia_mate, id_probabilidad_deteccion, rpn, id_riesgo

    ))
    db.connection.commit()
    fmea_id = cursor.lastrowid  
    cursor.close()
    return fmea_id

########################################################################

#Funciones para mostrar fmea

#funcion para poder obtener los nombres que estan ligados al id resgistrados en una tabla
def obtener_nombre_por_id(tabla, id):
    cursor = db.connection.cursor()
    
    # Verificar si la tabla tiene la columna 'nombre'
    query_column_check = f"SHOW COLUMNS FROM {tabla} LIKE 'nombre'"
    cursor.execute(query_column_check)
    columna_existe = cursor.fetchone()

    if columna_existe:  # Si la columna 'nombre' existe
        query = f"SELECT nombre FROM {tabla} WHERE id = %s"
        cursor.execute(query, (id,))
        resultado = cursor.fetchone()
        cursor.close()

        if resultado:
            return resultado['nombre']
    else:  # Si no existe, devolver un valor por defecto
        cursor.close()
        return None

    return None

#No me acuerdo pa que sirve pero no la quiero eliminar por si acaso

# def obtener_valor_por_id(tabla, id):
#     cursor = db.connection.cursor()
#     query = f"SELECT valor FROM {tabla} WHERE id = %s"
#     cursor.execute(query, (id,))
#     resultado = cursor.fetchone()
#     cursor.close()

#     if resultado:
#         return resultado['valor']
#     return None


def obtener_fmeas():
    cursor = db.connection.cursor()
    
    # Realizamos la consulta
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
        f.id_riesgo
    FROM fmea f
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
        sistema_nombre = fmea['sistema'] if fmea['sistema'] else obtener_nombre_por_id('subsistemas', fmea['id_sistema'])

        falla_funcional_nombre = fmea['falla_funcional'] if fmea['falla_funcional'] else obtener_nombre_por_id('falla_funcional', fmea['id_falla_funcional'])

        componente_nombre = fmea['componente'] if fmea['componente'] else obtener_nombre_por_id('componentes', fmea['id_componente'])
        codigo_modo_falla_nombre = fmea['codigo_modo_falla'] if fmea['codigo_modo_falla'] else obtener_nombre_por_id('codigo_modo_falla', fmea['id_codigo_modo_falla'])
        consecutivo_modo_falla_nombre = fmea['consecutivo_modo_falla'] if fmea['consecutivo_modo_falla'] else obtener_nombre_por_id('consecutivo_modo_falla', fmea['id_consecutivo_modo_falla'])
        descripcion_modo_falla_nombre = fmea['descripcion_modo_falla'] if fmea['descripcion_modo_falla'] else obtener_nombre_por_id('descripcion_modo_falla', fmea['id_descripcion_modo_falla'])
        causa_nombre = fmea['causa'] if fmea['causa'] else obtener_nombre_por_id('causa', fmea['id_causa'])
        mecanismo_falla_nombre = fmea['mecanismo_falla'] if fmea['mecanismo_falla'] else obtener_nombre_por_id('mecanismo_falla', fmea['id_mecanismo_falla'])
        detalle_falla_nombre = fmea['detalle_falla'] if fmea['detalle_falla'] else obtener_nombre_por_id('detalle_falla', fmea['id_detalle_falla'])



        # Contar las ocurrencias de consecutivo_modo_falla
        if consecutivo_modo_falla_nombre not in consecutivo_modo_falla_counter:
            consecutivo_modo_falla_counter[consecutivo_modo_falla_nombre] = 0
        consecutivo_modo_falla_counter[consecutivo_modo_falla_nombre] += 1

        # Concatenar la numeración al consecutivo_modo_falla
        consecutivo_modo_falla_numerado = f"{consecutivo_modo_falla_nombre}-{consecutivo_modo_falla_counter[consecutivo_modo_falla_nombre]}"

        # Añadir el FMEA procesado a la lista
        fmeas_completos.append({
            'id': fmea['id'],
            'sistema': sistema_nombre,
            'falla_funcional': falla_funcional_nombre,
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
            'id_riesgo': fmea['id_riesgo']

        })

    return fmeas_completos


























###############################funcion para mostrarPDF

#fmea editar y eliminar
def obtener_fmeas_por_usuario(id_equipo_info):
    cursor = db.connection.cursor()

    # Ajustar la consulta para filtrar por id_equipo_info
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
        f.id_riesgo
    FROM fmea f
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

    # Procesar los FMEAs como lo haces actualmente
    fmeas_completos = []
    consecutivo_modo_falla_counter = {}

    for fmea in fmeas:
        sistema_nombre = fmea['sistema'] if fmea['sistema'] else obtener_nombre_por_id('subsistemas', fmea['id_sistema'])
        falla_funcional_nombre = fmea['falla_funcional'] if fmea['falla_funcional'] else obtener_nombre_por_id('falla_funcional', fmea['id_falla_funcional'])
        componente_nombre = fmea['componente'] if fmea['componente'] else obtener_nombre_por_id('componentes', fmea['id_componente'])
        codigo_modo_falla_nombre = fmea['codigo_modo_falla'] if fmea['codigo_modo_falla'] else obtener_nombre_por_id('codigo_modo_falla', fmea['id_codigo_modo_falla'])
        consecutivo_modo_falla_nombre = fmea['consecutivo_modo_falla'] if fmea['consecutivo_modo_falla'] else obtener_nombre_por_id('consecutivo_modo_falla', fmea['id_consecutivo_modo_falla'])
        descripcion_modo_falla_nombre = fmea['descripcion_modo_falla'] if fmea['descripcion_modo_falla'] else obtener_nombre_por_id('descripcion_modo_falla', fmea['id_descripcion_modo_falla'])
        causa_nombre = fmea['causa'] if fmea['causa'] else obtener_nombre_por_id('causa', fmea['id_causa'])
        mecanismo_falla_nombre = fmea['mecanismo_falla'] if fmea['mecanismo_falla'] else obtener_nombre_por_id('mecanismo_falla', fmea['id_mecanismo_falla'])
        detalle_falla_nombre = fmea['detalle_falla'] if fmea['detalle_falla'] else obtener_nombre_por_id('detalle_falla', fmea['id_detalle_falla'])

        if consecutivo_modo_falla_nombre not in consecutivo_modo_falla_counter:
            consecutivo_modo_falla_counter[consecutivo_modo_falla_nombre] = 0
        consecutivo_modo_falla_counter[consecutivo_modo_falla_nombre] += 1

        consecutivo_modo_falla_numerado = f"{consecutivo_modo_falla_nombre}-{consecutivo_modo_falla_counter[consecutivo_modo_falla_nombre]}"

        fmeas_completos.append({
            'id': fmea['id'],
            'sistema': sistema_nombre,
            'falla_funcional': falla_funcional_nombre,
            'componente': componente_nombre,
            'codigo_modo_falla': codigo_modo_falla_nombre,
            'consecutivo_modo_falla': consecutivo_modo_falla_numerado,
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
            'id_riesgo': fmea['id_riesgo']
        })

    return fmeas_completos




###############################funcion para mostrarPDF
###############################funcion para mostrarPDF
###############################funcion para mostrarPDF



def obtener_analisis_funcional_por_usuario(id_equipo_info, sistema_nombre):
    cursor = db.connection.cursor()

    # Consulta SQL ajustada con el nombre correcto de la tabla 'subsistemas'
    query = """
    SELECT
        subsistemas.nombre as subsistema_nombre,
        analisis.verbo,
        analisis.accion,
        analisis.estandar_desempeño
    FROM analisis_funcional analisis
    JOIN subsistemas ON subsistemas.id = analisis.id_subsistema
    WHERE analisis.id_equipo_info = %s
    """
    
    # Ejecutar la consulta pasando el id_equipo_info como parámetro
    cursor.execute(query, (id_equipo_info,))
    analisis_funcionales = cursor.fetchall()
    
    cursor.close()

    # Agregar el sistema a cada registro de la consulta
    for analisis in analisis_funcionales:
        analisis['sistema_nombre'] = sistema_nombre
    
    # Devolver los resultados como una lista de diccionarios
    return analisis_funcionales










# database.py

def obtener_informacion_equipo(id_equipo_info):
    cursor = db.connection.cursor()

    # Consulta SQL para obtener la información del equipo y sus relaciones
    query = """
    SELECT 
        equipo_info.*, 
        personal.nombre_completo AS responsable_nombre,
        sistema.nombre AS sistema_nombre,
        grupo_constructivo.nombre AS grupo_constructivo_nombre,
        subgrupo.nombre AS subgrupo_constructivo_nombre,
        datos_equipo.nombre AS datos_equipo_nombre,
        tipo_equipo.nombre AS tipo_equipo_nombre,
        procedimiento.arranque AS procedimiento_arranque,
        procedimiento.parada AS procedimiento_parada,
        diagrama.diagrama_fijo,
        diagrama.diagrama_caja_negra,
        diagrama.diagrama_caja_transparente
    FROM equipo_info
    LEFT JOIN personal ON equipo_info.id_personal = personal.id
    LEFT JOIN sistema ON equipo_info.id_sistema = sistema.id
    LEFT JOIN grupo_constructivo ON sistema.id_grupo_constructivo = grupo_constructivo.id
    LEFT JOIN subgrupo ON sistema.id_subgrupo_constructivo = subgrupo.id
    LEFT JOIN datos_equipo ON equipo_info.id_equipo = datos_equipo.id
    LEFT JOIN tipo_equipo ON equipo_info.id_tipo_equipo = tipo_equipo.id
    LEFT JOIN procedimiento ON equipo_info.id_procedimiento = procedimiento.id
    LEFT JOIN diagrama ON equipo_info.id_diagrama = diagrama.id
    WHERE equipo_info.id = %s
    """
    cursor.execute(query, (id_equipo_info,))
    equipo_info = cursor.fetchone()
    cursor.close()
    return equipo_info




###############################funciones para PDFFF




def obtener_analisis_herramientas_por_equipo(id_equipo_info):
    cursor = db.connection.cursor()
    query = """
    SELECT ah.*
    FROM analisis_herramientas ah
    WHERE ah.id_equipo_info = %s
    """
    cursor.execute(query, (id_equipo_info,))
    analisis = cursor.fetchall()
    cursor.close()
    return analisis





# database.py

def obtener_rcm_por_usuario(id_equipo_info):
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
        ar.nombre as accion_recomendada,
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
    LEFT JOIN accion_recomendada ar ON r.id_accion_recomendada = ar.id
    WHERE f.id_equipo_info = %s
    """
    cursor.execute(query, (id_equipo_info,))
    rcms = cursor.fetchall()
    cursor.close()
    return rcms
##################################funcionespdf











###################################################################Funcines para MTA#############################



#fmea editar y eliminar
def obtener_fmea_por_id(fmea_id):
    # Obtener la lista completa de FMEAs con nombres procesados
    fmeas_completos = obtener_fmeas()
    
    # Buscar el FMEA por el ID en la lista completa
    fmea_filtrado = next((fmea for fmea in fmeas_completos if fmea['id'] == fmea_id), None)
    
    # Si se encuentra el FMEA, lo devolvemos, si no, devolvemos None
    if fmea_filtrado:
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
    id_costos_reparacion, id_flexibilidad_operacional,calculo_severidad, id_ocurrencia, 
    ocurrencia_mate,id_probabilidad_deteccion, id_metodo_deteccion_falla, rpn, id_riesgo

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
        id_impacto_operacional, id_costos_reparacion, id_flexibilidad_operacional,calculo_severidad,
        id_ocurrencia, ocurrencia_mate,id_probabilidad_deteccion, id_metodo_deteccion_falla,rpn, id_riesgo,
        
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
    
    query = "INSERT INTO diagramas (diagrama_fijo, diagrama_caja_negra, diagrama_caja_transparente) VALUES (%s, %s, %s)"
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

def obtener_usuario_por_correo(correo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id, correo, password, nombre_completo FROM personal WHERE correo = %s"
    cursor.execute(query, (correo,))
    usuario = cursor.fetchone()
    cursor.close()
    return usuario

def insertar_analisis_funcional(verbo, accion, estandar_desempeño, id_equipo_info,subsistema_id):
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




def insertar_mta():
    pass
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

def insertar_analisis_herramienta(nombre, valor, id_equipo_info, parte_numero, id_herramienta_requerida, id_tipo_herramienta, id_clase_herramienta):
    cursor = db.connection.cursor()
    query = """
        INSERT INTO herramientas_generales (
            nombre, valor, id_equipo_info, parte_numero, id_herramienta_requerida, id_tipo_herramienta,id_clase_herramienta

        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (nombre, valor, id_equipo_info, parte_numero, id_herramienta_requerida, id_tipo_herramienta, id_clase_herramienta))

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



def actualizar_analisis_herramienta(id_analisis, nombre, valor, parte_numero):
    cursor = db.connection.cursor()
    query = """
        UPDATE herramientas_generales
        SET nombre = %s, valor = %s, parte_numero = %s
        WHERE id = %s
    """
    cursor.execute(query, (nombre, valor, parte_numero, id_analisis))

    db.connection.commit()
    cursor.close()


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
        manual_referencia, id_tipo_herramienta, cantidad, id_herramienta_requerida,id_clase_herramienta
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







def insertar_herramienta_requerida(nombre, id_tipo_herramienta,id_clase_herramienta):
    cursor = db.connection.cursor()
    query = """
        INSERT INTO herramientas_requeridas (nombre, id_tipo_herramienta,id_clase_herramienta)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (nombre, id_tipo_herramienta,id_clase_herramienta))
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
        WHERE r.id_fmea = %s
    """
    cursor.execute(query, (id_fmea,))
    context = cursor.fetchall()
    rcm = context[0]
    print(rcm)
    cursor.close()
    return rcm

def obtener_rcms_completos():
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
    """
    cursor.execute(query)
    rcms_completos = cursor.fetchall()
    cursor.close()
    return rcms_completos

def obtener_fmeas_con_rcm():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT id_fmea FROM rcm"
    cursor.execute(query)
    fmeas_con_rcm = cursor.fetchall()
    cursor.close()

    # Extraer solo los id_fmea de los resultados
    id_fmeas = [fmea['id_fmea'] for fmea in fmeas_con_rcm]
    return id_fmeas

def eliminar_rcm(id_fmea):
    cursor = db.connection.cursor()
    query = "DELETE FROM rcm WHERE id_fmea = %s"
    cursor.execute(query, (id_fmea,))
    db.connection.commit()
    cursor.close()


def actualizar_rcm(rcm):
    cursor = db.connection.cursor()
    query = """
        UPDATE rcm
        SET hidden_failures = %s, safety = %s, environment = %s, operation = %s, h1_s1_n1_o1 = %s, h2_s2_n2_o2 = %s, h3_s3_n3_o3 = %s, h4_s4 = %s, h5 = %s, tarea = %s, intervalo_inicial_horas = %s, id_accion_recomendada = %s
        WHERE id_fmea = %s
    """
    cursor.execute(query, (
        rcm['hidden_failures'], rcm['safety'], rcm['environment'], rcm['operation'], rcm['h1_s1_n1_o1'], rcm['h2_s2_n2_o2'], rcm['h3_s3_n3_o3'], rcm['h4_s4'], rcm['h5'], rcm['tarea'], rcm['intervalo_inicial_horas'], rcm['id_accion_recomendada'], rcm['id_fmea']
    ))
    db.connection.commit()
    cursor.close()


def obtener_lista_acciones_recomendadas():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM accion_recomendada"
    cursor.execute(query)
    accion_recomendada = cursor.fetchall()
    cursor.close()
    return accion_recomendada



def insertar_rcm(rcm):
    cursor = db.connection.cursor()
    query = """
        INSERT INTO rcm (
            id_fmea, hidden_failures, safety, environment, operation, h1_s1_n1_o1, h2_s2_n2_o2, h3_s3_n3_o3, h4_s4, h5, tarea, intervalo_inicial_horas, id_accion_recomendada
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        rcm['id_fmea'], rcm['hidden_failures'], rcm['safety'], rcm['environment'], rcm['operation'], rcm['h1_s1_n1_o1'], rcm['h2_s2_n2_o2'], rcm['h3_s3_n3_o3'], rcm['h4_s4'], rcm['h5'], rcm['tarea'], rcm['intervalo_inicial_horas'], rcm['id_accion_recomendada']
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
        data['nombre_equipo'], data['aor'], data['fecha'], data['fiabilidad_equipo'], data['mtbf'], data['gres_sistema'],
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


def obtener_tipo_equipo_por_id(id_tipo_equipo):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM tipo_equipos WHERE id = %s"
    cursor.execute(query, (id_tipo_equipo,))
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
    WHERE af.id_equipo_info = %s
    """

    cursor.execute(query, (id_equipo_info,))
    analisis_funcionales = cursor.fetchall()
    cursor.close()
    
    return analisis_funcionales


# Función para obtener un análisis funcional por su ID
def obtener_analisis_funcional_por_id(id_analisis_funcional):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT af.*
        FROM analisis_funcional af
        WHERE af.id = %s
    """
    cursor.execute(query, (id_analisis_funcional,))
    analisis_funcional = cursor.fetchone()
    cursor.close()
    return analisis_funcional


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
    query = "DELETE FROM analisis_funcional WHERE id = %s"
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





def eliminar_personal(id_personal):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = "DELETE FROM personal WHERE id = %s"
    cursor.execute(sql, (id_personal,))
    db.connection.commit()
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
    print(dict_herramientas)
    return dict_herramientas