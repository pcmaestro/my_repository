
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>

	<jsp:include page="menu.jsp"></jsp:include>

	<c:forEach items="${coches}" var="coche">
		<div style="margin: 10px">

			<table>
				<tr>
					<th>MARCA</th>
					<th>MODELO</th>
					<th>COLOR</th>
					<th>MOTOR</th>
					<th>CILINDRADA</th>
					<th>PRECIO</th>
					<th>TF CONTACTO</th>
					<th>EMAIL CONTACTO</th>
					<th>CATEGORIA</th>	
					<th>BORRAR</th>
					<th>EDITAR</th>
				</tr>

				<tr>
					<td>${coche.marca}</td>
					<td>${coche.modelo}</td>
					<td>${coche.color}</td>
					<td>${coche.motor}</td>
					<td>${coche.cilindrada}</td>
					<td>${coche.precio}</td>
					<td>${coche.telefono}</td>
					<td>${coche.email}</td>
					<td>${coche.categoria.categoria}</td>	
					<td><a onclick="return confirm('¿estas seguro?')"
						href="ServletBorrarCoche?id=${coche.id}">BORRAR</a></td>
					<td><a href="ServletEditarCoche?id=${coche.id}">EDITAR</a></td>
				</tr>
			</table>
	
		</div>

	</c:forEach>

</body>
</html>