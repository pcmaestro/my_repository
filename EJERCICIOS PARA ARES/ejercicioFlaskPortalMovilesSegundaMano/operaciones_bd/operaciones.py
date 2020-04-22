import mysql.connector
from operaciones_bd import constantes_sql
from clases import modelo

def conectar():
    try:
        connect = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "bd_anuncios"
        )
    except Exception as e:
        print(e)
    return connect


def listar():
    sql = constantes_sql.SQL_LISTAR_ANUNCIOS
    try:
        conexion = conectar()    
        cursor = conexion.cursor()
        cursor.execute(sql)
        anuncios = cursor.fetchall()
        conexion.commit()
    except Exception as e:
        print(e)
    finally:
        conexion.disconnect()
    return anuncios

def registrar(anuncio):    
    sql = constantes_sql.SQL_INSERTAR_ANUNCIO    
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        val = (anuncio.marca, anuncio.modelo, anuncio.color, anuncio.pantalla, anuncio.memoria, anuncio.anyo, anuncio.precio, anuncio.nombre, anuncio.telefono, anuncio.email  )
        cursor.execute(sql, val)
        conexion.commit()
    except Exception as e:
        print(e)
    finally:
        conexion.disconnect()
    
    
    
    
    