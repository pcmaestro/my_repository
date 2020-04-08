import mysql.connector
from modelo import constantes_sql, clases

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

def borrar_revista(id):
    sql = constantes_sql.SQL_BORRAR_REVISTA
    mydb = conectar()
    cursor = mydb.cursor()
    val = (id,)
    cursor.execute(sql,val)
    mydb.commit()
    mydb.disconnect()
    
def obtener_revista_por_id(id):
    sql = constantes_sql.SQL_OBTENER_REVISTA_POR_ID
    mydb = conectar()
    cursor = mydb.cursor()
    val = (id,)
    cursor.execute(sql,val)
    revista_obtenida = cursor.fetchone()
    print(revista_obtenida)
    mydb.disconnect()
    objeto_revista = clases.Revista( id= revista_obtenida[0] , \
        titulo = revista_obtenida[1], precio = revista_obtenida[2], \
        tema = revista_obtenida[3])
    return objeto_revista    
    
def guardar_cambios_revista(revista):
    sql = constantes_sql.SQL_GUARDAR_CAMBIOS_REVISTA
    mydb = conectar()
    cursor = mydb.cursor()
    val = (revista.titulo, revista.precio, revista.tema, revista.id)
    cursor.execute(sql,val)
    mydb.commit()
    mydb.disconnect()
    
    
    