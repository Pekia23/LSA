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

def insertar_procedimiento(arranque, parada):
    cursor = db.connection.cursor()
    query = "INSERT INTO procedimientos (arranque, parada) VALUES (%s, %s)"
    cursor.execute(query, (arranque, parada))
    db.connection.commit()
    procedimiento_id = cursor.lastrowid
    cursor.close()
    return procedimiento_id

def insertar_diagrama(diagrama_flujo_file, diagrama_caja_negra_file, diagrama_caja_transparente_file):
    cursor = db.connection.cursor()
    diagrama_flujo = diagrama_flujo_file.read() if diagrama_flujo_file else None
    diagrama_caja_negra = diagrama_caja_negra_file.read() if diagrama_caja_negra_file else None
    diagrama_caja_transparente = diagrama_caja_transparente_file.read() if diagrama_caja_transparente_file else None
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
    imagen = imagen_equipo_file.read() if imagen_equipo_file else None
    query = """
        INSERT INTO equipo_info (
            nombre_equipo, AOR, fecha, fiabilidad_equipo, MTBF, GRES, criticidad_equipo,
            marca, modelo, peso_seco, dimensiones, descripcion, imagen,
            id_personal, id_diagrama, id_procedimiento, id_sistema, id_equipo
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        nombre_equipo, AOR, fecha, fiabilidad_equipo, MTBF, GRES, criticidad_equipo,
        marca, modelo, peso_seco, dimensiones, descripcion, imagen,
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