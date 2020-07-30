<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
INTRODUCE USUARIO Y CONTRASEÑA

<form action="ServletIdentificacionAdmin" method = "POST">

Usuario: <input type = "text" name = "usuario" />
</br>
Contraseña: <input type = "password" name = "password" />
</br>

<input type = "submit" value = "ENTRAR" />


</form>
</body>
</html>