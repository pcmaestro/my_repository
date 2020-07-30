'''
sql de creacion de tabla:

CREATE TABLE `tabla_anuncios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `precio` DECIMAL(9,2) NULL,
  `email` VARCHAR(255) NULL,
  `email-valido` VARCHAR(2) NULL DEFAULT 'NO',
  PRIMARY KEY (`id`));

'''
#columnas en tabla_anuncios : id , nombre, precio, email, email-valido
SQL_INSERCION_ANUNCIO = "INSERT INTO `tabla_anuncios` (`id`, `nombre`, `precio`, `email`, `email-valido`, codigo) VALUES (NULL, %s, %s, %s, 'NO', %s);"

SQL_LISTADO_ANUNCIOS = "SELECT id, nombre, precio, email, `email-valido` from tabla_anuncios order by id desc;"

SQL_COMPROBAR_CODIGO_ANUNCIO = "SELECT nombre from tabla_anuncios where id = %s and codigo = %s ;"

SQL_VALIDAR_ANUNCIO = "UPDATE tabla_anuncios set `email-valido` = 'SI' where id = %s ;"

SQL_BORRAR_ANUNCIO = "DELETE from tabla_anuncios WHERE id = %s ;"

SQL_OBTENER_ANUNCIO_POR_ID = "SELECT * from tabla_anuncios WHERE id = %s;"

SQL_GUARDAR_CAMBIOS_ANUNCIO = "UPDATE tabla_anuncios set nombre = %s, precio = %s, email = %s, `email-valido` = %s WHERE id = %s ;"







