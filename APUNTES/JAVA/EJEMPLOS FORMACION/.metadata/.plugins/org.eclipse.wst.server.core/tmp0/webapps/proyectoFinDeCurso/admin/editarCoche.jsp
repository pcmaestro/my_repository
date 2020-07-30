<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">

<jsp:include page="../css_js.jsp"></jsp:include>

<title>Editar anuncio</title>
</head>
<body>

	<div class="menuAdministracion">
		<jsp:include page="menu.jsp"></jsp:include>
	</div>

	<div id="invisible"></div>



	<form action="ServletGuardarCambiosCoche" method="POST">
		<div class="formularios">
			<table>

				<tr>
					<td>Marca</td>
					<td><input type="text" value="${coche.marca }" name="marca" /></td>
					<td>Modelo</td>
					<td><input type="text" value="${coche.modelo}" name="modelo" /></td>
					<td>Color</td>
					<td><input type="text" value="${coche.color}" name="color" /></td>
					<td>Motor</td>
					<td><input type="text" value="${coche.motor}" name="motor" /></td>
				</tr>

				<tr>
					<td>Cilindrada</td>
					<td><input type="text" value="${coche.cilindrada}"
						name="cilindrada" /></td>
					<td>Precio</td>
					<td><input type="text" value="${coche.precio}" name="precio" /></td>
					<td>Telefono</td>
					<td><input type="text" value="${coche.telefono}"
						name="telefono" /></td>
					<td>Email</td>
					<td><input type="text" value="${coche.email}" name="email" /></td>
				</tr>

			</table>
		</div>

		<hr>
		<div class="formularios">
			<table>

				<tr>
					<td>Antigüedad : <select name="id_categoria">
							<option value="1" ${nuevo}>nuevo</option>
							<option value="2" ${seminuevo}>seminuevo</option>
							<option value="3" ${viejo}>viejo</option>

					</select></br>
					</td>
					<td><input type="hidden" value="${coche.id}" name="id" /> <input
						type="submit" value="MODIFICAR" /></td>
				</tr>
			</table>
		</div>
	</form>



</body>
</html>