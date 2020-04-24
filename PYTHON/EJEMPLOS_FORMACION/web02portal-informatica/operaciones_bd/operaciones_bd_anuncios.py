import mysql.connector
from operaciones_bd import constantes_sql

def conectar():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "bd_anuncios"
    )
    return conexion

def registrar_anuncio(anuncio):
    sql = constantes_sql.SQL_INSERCION_ANUNCIO
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        val = anuncio.nombre, anuncio.precio, anuncio.email
        cursor.execute(sql, val)
        conexion.commit()
    except Exception as e:
        print(e)
    finally:
        conexion.disconnect()
        
def obtener_anuncios():
    sql = constantes_sql.SQL_LISTADO_ANUNCIOS
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(sql)
        lista = cursor.fetchall()
        
    except Exception as e:
        print(e)
    finally:
        if conexion is not None:
            conexion.disconnect()
    return lista