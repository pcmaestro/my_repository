import mysql.connector
from operaciones_bd import constantes_sql
from clases import modelo
import operaciones_bd

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

def registrar(anuncio, codigo):    
    sql = constantes_sql.SQL_INSERTAR_ANUNCIO    
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        val = (anuncio.marca, anuncio.modelo, anuncio.color, anuncio.pantalla, anuncio.memoria, anuncio.anyo, anuncio.precio, anuncio.nombre, anuncio.telefono, anuncio.email, codigo  )
        cursor.execute(sql, val)
        conexion.commit()
        id_generado = cursor.lastrowid
    except Exception as e:
        print(e)
    finally:
        conexion.disconnect()    
    
    return id_generado
    
def comprobar_codigo_anuncio(id ,codigo):
    sql = constantes_sql.SQL_COMPROBAR_CODIGO_ANUNCIO
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        val = (id, codigo)
        cursor.execute(sql, val)
        list_from_bd = cursor.fetchall()
        conexion.commit()
    except Exception as e:
        print(e)
    finally:
        conexion.disconnect()
        
    return len(list_from_bd)
        
def validar_email(id):
    sql = constantes_sql.SQL_VALIDAR_CODIGO_ANUNCIO
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        val = (id,)
        cursor.execute(sql, val)
        conexion.commit()
    except Exception as e:
        print(e)
    finally:
        conexion.disconnect()
    
        
    
    
    