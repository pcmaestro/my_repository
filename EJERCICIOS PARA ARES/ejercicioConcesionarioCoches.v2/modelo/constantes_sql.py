SQL_INSERCION_COCHE = "INSERT INTO tabla_coches(marca, modelo, color, motor, precio) VALUES (%s,%s,%s,%s,%s);"

SQL_LISTADO_COCHES = "SELECT * FROM tabla_coches;"

SQL_OBTENER_COCHE_POR_ID = "SELECT * FROM tabla_coches WHERE id_producto = %s ;"

SQL_BORRAR_COCHE = "DELETE FROM tabla_coches WHERE id_producto = %s ;"

SQL_GUARDAR_CAMBIOS_COCHE = "UPDATE tabla_coches SET marca = %s, modelo = %s, color = %s, motor = %s , precio = %s WHERE id_producto = %s ;"
