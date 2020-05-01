import mysql.connector
from operaciones_bd import constantes_sql
from clases.modelo import Anuncio

def conectar():
    conexion = mysql.connector.connect(
      host="AresPython.mysql.pythonanywhere-services.com",
      user="AresPython",
      passwd="curso1234",
      database="AresPython$bd_anuncios_informatica"
    )
    return conexion

def registrar_anuncio(anuncio, codigo):
    sql = constantes_sql.SQL_INSERCION_ANUNCIO
    conexion = conectar()
    id_generado = -1
    try:
        cursor = conexion.cursor()
        val = (anuncio.nombre, anuncio.precio, anuncio.email, codigo, anuncio.id_categoria)
        cursor.execute(sql,val)
        conexion.commit()
        id_generado = cursor.lastrowid
    except Exception as e:
        print(e)
    finally:
        if conexion is not None:
            conexion.disconnect()
    return id_generado

def obtener_anuncios():
    sql = constantes_sql.SQL_LISTADO_ANUNCIOS
    conexion = conectar()
    lista = None
    try:
        cursor = conexion.cursor()
        cursor.execute(sql)
        lista = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if conexion is not None:
            conexion.disconnect()

    print(lista)
    return lista

def comprobar_codigo_anuncio(id,codigo):
    sql = constantes_sql.SQL_COMPROBAR_CODIGO_ANUNCIO
    conexion = conectar()
    lista = None
    try:
        cursor = conexion.cursor()
        val = (id,codigo)
        cursor.execute(sql,val)
        lista = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if conexion is not None:
            conexion.disconnect()
    return len(lista) #da un cero, el id y el codigo no son valido y si da un 1 es que si

def validar_email_anuncio(id):
    sql = constantes_sql.SQL_VALIDAR_ANUNCIO
    conexion = conectar()
    cursor = conexion.cursor()
    val = (id,)
    cursor.execute(sql,val)
    conexion.commit()
    conexion.disconnect()

def borrar_anuncio(id):
    sql = constantes_sql.SQL_BORRAR_ANUNCIO
    conexion = conectar()
    cursor = conexion.cursor()
    val = (id,)
    cursor.execute(sql,val)
    conexion.commit()
    conexion.disconnect()

def obtener_anuncio_por_id(id):
    sql = constantes_sql.SQL_OBTENER_ANUNCIO_POR_ID
    conexion = conectar()
    cursor = conexion.cursor()
    val = (id,)
    cursor.execute(sql,val)
    res = cursor.fetchone()
    conexion.disconnect()

    anuncio = Anuncio()
    anuncio.id = res[0]
    anuncio.nombre = res[1]
    anuncio.precio = res[2]
    anuncio.email = res[3]
    anuncio.email_valido = res[4]

    return anuncio

def guardar_cambios_anuncio(anuncio):
    sql = constantes_sql.SQL_GUARDAR_CAMBIOS_ANUNCIO
    conexion = conectar()
    cursor = conexion.cursor()
    val = (anuncio.nombre, anuncio.precio, anuncio.email, anuncio.email_valido, anuncio.id)
    cursor.execute(sql,val)
    conexion.commit()
    conexion.disconnect()

def obtener_categorias():
    sql = constantes_sql.SQL_OBTENER_CATEGORIAS
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    conexion.disconnect()
    return res








