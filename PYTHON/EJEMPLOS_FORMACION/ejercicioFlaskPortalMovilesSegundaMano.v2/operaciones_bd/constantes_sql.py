SQL_LISTAR_ANUNCIOS = "SELECT marca, modelo, color, pantalla, memoria, anyo, precio,nombre, telefono, email, email_validado FROM tabla_terminales ORDER BY id DESC;"

SQL_INSERTAR_ANUNCIO = "INSERT INTO tabla_terminales (marca, modelo, color, pantalla, memoria, anyo, precio, nombre, telefono, email, email_validado, codigo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'NO',%s);"

SQL_COMPROBAR_CODIGO_ANUNCIO = "SELECT nombre FROM tabla_terminales WHERE id = %s AND codigo = %s;"

SQL_VALIDAR_CODIGO_ANUNCIO = "UPDATE tabla_terminales SET email_validado = 'SI'  WHERE id = %s;"