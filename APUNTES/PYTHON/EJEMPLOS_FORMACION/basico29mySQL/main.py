import mysql.connector


mydb = mysql.connector.connect(
    
    host = "localhost",
    user = "root",
    database = "bd_revistas"
    
    
    )

print("Conexión OK")

cursor = mydb.cursor()

sql = "INSERT INTO `tabla_revistas` (`titulo`, `precio`, `tema`) VALUES ('Marca', '1.50', 'Deportes');"

cursor.execute(sql)

mydb.commit() # Lanza todos los cursor.execute() que hayamos creado previamente

print("Registro OK")
