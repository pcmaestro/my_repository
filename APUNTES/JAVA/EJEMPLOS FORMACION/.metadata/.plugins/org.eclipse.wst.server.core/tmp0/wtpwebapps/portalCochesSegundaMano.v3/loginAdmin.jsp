<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
INTRODUCE USUARIO Y CONTRASE�A

<form action="ServletIdentificacionAdmin" method = "POST">

Usuario: <input type = "text" name = "usuario" />
</br>
Contrase�a: <input type = "password" name = "password" />
</br>

<input type = "submit" value = "ENTRAR" />


</form>
</body>
</html>