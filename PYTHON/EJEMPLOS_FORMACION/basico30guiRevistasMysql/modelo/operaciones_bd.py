import mysql.connector
from modelo import constantes_sql

def conectar():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "bd_revistas"
    )
    return mydb

#metodo que recive un objeto de la clase Revista para registrarla en 
#base de datos
def registro_revista(revista):
    sql = constantes_sql.SQL_INSERCION_REVISTA
    mydb = conectar()
    cursor = mydb.cursor()
    #mirando el orden de insert de la sql formo la siguiente tupla con 
    #los valores a insertar en base de datos
    val = (revista.titulo,revista.precio, revista.tema)
    cursor.execute(sql,val)
    mydb.commit()
    mydb.disconnect()
    
def obtener_revistas():
    sql = constantes_sql.SQL_LISTADO_REVISTAS
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute(sql)
    resultado_lista = cursor.fetchall()#esto obtiene el resultado de la select
    mydb.disconnect()
    return resultado_lista
    
    


    
    
    