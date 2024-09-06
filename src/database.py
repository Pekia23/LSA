# database.py

# Importa la conexión a la base de datos
from __init__ import db

# Función para buscar equipos en la base de datos
def buscar_equipos(searchbox):
    cursor = db.connection.cursor()
    query = "SELECT nombre_equipo FROM equipo_info WHERE nombre_equipo LIKE %s ORDER BY nombre_equipo"
    cursor.execute(query, (searchbox + '%',))
    result = cursor.fetchall()
    cursor.close()
    return result

def verificar_conexion():
    try:
        # Crear un cursor para realizar una consulta simple
        cursor = db.connection.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        return {"status": "success", "message": "Database connection successful"}, 200
    except db.connection.Error as e:
        return {"status": "error", "message": str(e)}, 500