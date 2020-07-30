SQL_INSERCION_COCHE = "INSERT INTO tabla_coches(marca, modelo, color, motor, precio, forma_pago) VALUES (%s,%s,%s,%s,%s,%s);"

SQL_LISTADO_COCHES = "SELECT id_producto, marca, modelo, color, motor, REPLACE( FORMAT(precio, 0), ',' , '.'), forma_pago FROM tabla_coches;"

SQL_OBTENER_COCHE_POR_ID = "SELECT * FROM tabla_coches WHERE id_producto = %s ;"

SQL_BORRAR_COCHE = "DELETE FROM tabla_coches WHERE id_producto = %s ;"

SQL_GUARDAR_CAMBIOS_COCHE = "UPDATE tabla_coches SET marca = %s, modelo = %s, color = %s, motor = %s , precio = %s , forma_pago = %s WHERE id_producto = %s ;"

SQL_MAX_VALOR_ID = "SELECT MAX(id_producto) FROM tabla_coches"
