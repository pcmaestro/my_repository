import mysql.connector
from modelo import constantes_sql

def conectar():
    
    mydb = mysql.connector.connect(
    
    host = "localhost",
    user = "root",
    database = "bd_revistas"    
    
    )
    
    return mydb

#Método que solicita un objeto de la clase Revista()
def registro_revista(revista):
    
    sql = constantes_sql.SQL_INSERCION_REVISTAS
    mydb = conectar()
    cursor = mydb.cursor()
    #La siguiente tupla se forma en el mismo orden que la SQL
    val = (revista.titulo, revista.precio, revista.tema)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.disconnect()