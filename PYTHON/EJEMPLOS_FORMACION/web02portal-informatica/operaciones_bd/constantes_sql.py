
SQL_INSERCION_ANUNCIO = "INSERT INTO tabla_anuncios (id , nombre, precio, email, `email-valido`) VALUES (NULL,%s,%s,%s,'NO');"

SQL_LISTADO_ANUNCIOS = "SELECT id, nombre, precio, email from tabla_anuncios order by id desc;"
