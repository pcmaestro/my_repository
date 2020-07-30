'''

tabla mensajes:

CREATE TABLE `bd_chat`.`tabla_mensajes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `mensaje` VARCHAR(2000) NULL,
  PRIMARY KEY (`id`));
  
  
'''
import mysql.connector
from operaciones_bd import constantes_sql

def conectar():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd="root1234",#solo para el ordenador de ares
        database = "bd_chat"
        )
    return conexion

def registrar_mensaje(nombre, mensaje):
    sql = constantes_sql.SQL_INSERTAR_MENSAJE
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        val = (nombre, mensaje)
        cursor.execute(sql,val)
        conexion.commit()
    except Exception as e:
        print(e)
    finally:
        if conexion != None:
            conexion.disconnect()
    
def obtener_mensajes():
    sql = constantes_sql.SQL_OBTENER_MENSAJES
    conexion = conectar()
    lista_mensajes = None
    try:
        cursor = conexion.cursor()
        cursor.execute(sql)
        lista_mensajes = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        conexion.disconnect()
    return lista_mensajes
    
