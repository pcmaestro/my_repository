
SQL_INSERCION_REVISTA = "INSERT INTO `tabla_revistas` (`titulo`, `precio`, `tema`, digital, frecuencia, tipo ) VALUES (%s, %s, %s, %s, %s, %s);"
SQL_LISTADO_REVISTAS = "SELECT id,titulo, precio ,tema FROM tabla_revistas;"
SQL_BORRAR_REVISTA = "DELETE FROM tabla_revistas WHERE id = %s ;"
SQL_OBTENER_REVISTA_POR_ID = "SELECT * FROM tabla_revistas WHERE id = %s ;"
SQL_GUARDAR_CAMBIOS_REVISTA = "UPDATE tabla_revistas SET titulo = %s , precio = %s , tema = %s WHERE id = %s ;"