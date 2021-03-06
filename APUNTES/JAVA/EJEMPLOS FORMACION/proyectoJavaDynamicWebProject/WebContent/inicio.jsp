<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!doctype html>
<html lang="es">
<head>
<meta charset="ISO-8859-1">


<jsp:include page="css_js.jsp"></jsp:include>


<title>Portal de coches de segunda mano</title>

</head>
<body>

	<div class="menuUsuario">
		<jsp:include page="menu.jsp"></jsp:include>
	</div>


	<div class="formularios">

		<form action="inicio" >
			<table>
				<tr>
					<td>Marca</td>
					<td><input type="text" value="${marcaAbuscar}" name="marca" /></td>

					<td>Modelo</td>
					<td><input type="text" value="${colorAbuscar}" name="color" />
					</td>

					<td>Color</td>
					<td><input type="text" value="${modeloAbuscar}" name="modelo" />
					</td>

					<td><input type="submit" value="BUSCAR" /></td>

					<td>
						<button> <a href="inicio">Resetear busqueda<a></a></button>
					</td>

					<td id="contadorResultados">resultados totales : ${total}</td>
				</tr>

			</table>



		</form>


	</div>



	<div class="zonaListado">

		<table class="listado">

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
					<td><img src="imagenes/${coche.id}.jpg" style="height: 50px" alt="No existe imagen" />
						</td>
				</tr>
			</c:forEach>
		</table>
		

	</div>
	
	<footer>
	
	<div class = "paginacion">
	<c:if test="${ anterior >= 0 }">
		<a
			href="inicio?comienzo=${anterior}&marca=${marcaAbuscar}&modelo=${modeloAbuscar}&color=${colorAbuscar}">ANTERIORES</a>
		</c:if>

		<c:if test="${ siguiente < total }">
		<a
			href="inicio?comienzo=${siguiente}&marca=${marcaAbuscar}&modelo=${modeloAbuscar}&color=${colorAbuscar}">SIGUIENTES</a>
	</c:if>	
	</div>
	</footer>

</body>
</html>
