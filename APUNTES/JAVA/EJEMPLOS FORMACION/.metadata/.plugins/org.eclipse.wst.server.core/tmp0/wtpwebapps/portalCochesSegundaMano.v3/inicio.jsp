<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!doctype html>
<html lang="es">
<head>
<meta charset="ISO-8859-1">
<title>Portal de coches de segunda mano</title>

</head>
<body>

	<jsp:include page="menu.jsp"></jsp:include>


	<div>
		Buscar por:
		<form action="inicio">
			Marca : <input type="text" value="${marcaAbuscar}" name="marca" /> </br>
			Modelo : <input type="text" value="${modeloAbuscar}" name="modelo" />
			</br> Color : <input type="text" value="${colorAbuscar}" name="color" /> </br>
			<input type="submit" value="BUSCAR" />
		</form>

		<a href="inicio">Resetear busqueda</a>

		<div>total de resultados: ${total}</div>

		<div>
			<c:if test="${ anterior >= 0 }">
				<a href="inicio?comienzo=${anterior}&marca=${marcaAbuscar}&modelo=${modeloAbuscar}&color=${colorAbuscar}">ANTERIOR</a>&nbsp;&nbsp;&nbsp;&nbsp;
			</c:if>

			<c:if test="${ siguiente < total }">
				<a href="inicio?comienzo=${siguiente}&marca=${marcaAbuscar}&modelo=${modeloAbuscar}&color=${colorAbuscar}">SIGUIENTE</a>
			</c:if>

		</div>

	</div>


	<div>
		AQUI VAN LOS ANUNCIOS
		
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
					<th>IMAGEN</th>
				</tr>
		<c:forEach items="${coches}" var="coche">
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
					<td><img src="imagenes/${coche.id}.jpg" style="height: 50px" alt = "No existe imagen"/> </td>
				</tr>

			</table>

		</c:forEach>

	</div>

</body>
</html>
