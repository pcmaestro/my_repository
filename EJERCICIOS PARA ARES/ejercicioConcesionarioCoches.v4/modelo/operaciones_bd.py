import mysql.connector
from modelo import constantes_sql
from clases import clases


def conectar():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "bd_coches"
    )
    return mydb


#metodo que recive un objeto de la clase Revista para registrarla en 
#base de datos
def registro_coche(coche):
    sql = constantes_sql.SQL_INSERCION_COCHE
    mydb = conectar()
    cursor = mydb.cursor()
    #mirando el orden de insert de la sql formo la siguiente tupla con 
    #los valores a insertar en base de datos
    val = (coche.marca, coche.modelo, coche.color, coche.motor, coche.precio, coche.forma_pago)
    cursor.execute(sql,val)
    mydb.commit()
    mydb.disconnect()
    
def obtener_coches():
    sql = constantes_sql.SQL_LISTADO_COCHES
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute(sql)
    resultado_lista = cursor.fetchall()#esto obtiene el resultado de la select
    mydb.disconnect()
    return resultado_lista

def borrar_coche(id_registro):
     
    sql = constantes_sql.SQL_BORRAR_COCHE
    mydb  = conectar()
    cursor = mydb.cursor()
    val = (id_registro,)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.disconnect()
    
def obtener_coche_por_id(id_registro):    
    sql = constantes_sql.SQL_OBTENER_COCHE_POR_ID
    mydb = conectar()
    cursor = mydb.cursor()
    val = (id_registro,)
    print(sql)
    print(val)
    cursor.execute(sql, val)
    coche_obtenido = cursor.fetchone()
    mydb.commit()
    mydb.disconnect()
    objeto_coche = clases.Coche(marca = coche_obtenido[1], modelo = coche_obtenido[2], color = coche_obtenido[3], motor = coche_obtenido[4], precio = coche_obtenido[5], forma_pago = coche_obtenido[6])
                                
    return objeto_coche
                                    
def guardar_cambios_coche(cambios_ptes_guardar):    
    print("llego a operaciones_bd.guardar_cambios_coche()")    
    sql = constantes_sql.SQL_GUARDAR_CAMBIOS_COCHE
    print(sql)
    mydb = conectar()
    cursor = mydb.cursor()
    val = (cambios_ptes_guardar.marca, cambios_ptes_guardar.modelo, cambios_ptes_guardar.color, cambios_ptes_guardar.motor, cambios_ptes_guardar.precio, cambios_ptes_guardar.forma_pago ,cambios_ptes_guardar.id )
    cursor.execute(sql, val)
    mydb.commit()
    mydb.disconnect()
    
    