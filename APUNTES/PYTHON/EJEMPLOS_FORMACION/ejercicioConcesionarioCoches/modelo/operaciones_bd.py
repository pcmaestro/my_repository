import mysql.connector
from modelo import constantes_sql

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
    val = (coche.marca, coche.modelo, coche.color, coche.motor, coche.precio)
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