<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
INTRODUCE USUARIO Y CONTRASEŅA

<form action="ServletIdentificacionAdmin" method = "POST">

Usuario: <input type = "text" name = "usuario" />
</br>
Contraseņa: <input type = "password" name = "password" />
</br>

<input type = "submit" value = "ENTRAR" />


</form>
</body>
</html>