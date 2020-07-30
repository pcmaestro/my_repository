
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">

<jsp:include page="../css_js.jsp"></jsp:include>

<title>Gestion de anuncios</title>
</head>
<body>

	<div class="menuAdministracion">
		<jsp:include page="menu.jsp"></jsp:include>
	</div>
	
	<div id = "invisible"></div>

	<table id = "tablaEdicion">
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
			<th>BORRAR</th>
			<th>EDITAR</th>
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
				<td><img src="imagenes/${coche.id}.jpg" style="height: 50px"
						alt="No existe imagen" /></td>
				<td>
					<button>
						<a onclick="return confirm('¿estas seguro?')"
							href="ServletBorrarCoche?id=${coche.id}">BORRAR </a>
					</button>
				</td>

				<td>
					<button>
						<a href="ServletEditarCoche?id=${coche.id}">EDITAR</a>
					</button>
				</td>
			</tr>
		</c:forEach>
	</table>



	

</body>
</html>