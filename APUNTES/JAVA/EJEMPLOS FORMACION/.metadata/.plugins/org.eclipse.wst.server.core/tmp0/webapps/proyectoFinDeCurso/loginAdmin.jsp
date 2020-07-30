<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">

<jsp:include page="css_js.jsp"></jsp:include>

<title>Acceso administradores</title>
</head>
<body id = "loginBody">

<div id ="invisible">
</div>
<div id = "ventanaLogin">

	INTRODUCE USUARIO Y CONTRASEÑA
	
	<br><br>
	
	<form action="ServletIdentificacionAdmin" method="POST">

		<table>
			<tr>
				<td class ="label">Usuario</td>
				<td><input type="text" name="usuario" /></td>
			</tr>

			<tr>
				<td class = "label">Contraseña</td>
				<td><input type="password" name="password" /></td>
			</tr>		

		</table>
		<br/>
		<input type="submit" value="ENTRAR" />
	</form>
	</div>
</body>
</html>