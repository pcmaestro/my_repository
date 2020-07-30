<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">

<jsp:include page="css_js.jsp"></jsp:include>

<title>Registro de anuncios</title>
</head>
<body id = "body" onload = "cargando()">
	
	<div class="menuUsuario">
	<jsp:include page="menu.jsp"></jsp:include>
	</div>

	<div id = "invisible"></div>
	
	<div id = "error">
		Revisa el contenido de los formularios, no pueden estar vacios y los números
		no pueden tener puntos ni comas, los campos de texto no pueden contener acentos.
		El campo telefono debe ser numérico de 9 cifras empezando por 6/7/8/9, el campo
		cilindrada debe ser numérico de 4 cifras , el precio debe ser numérico y el email
		debe tener un formato válido
	
	</div>
	
	
	<div class ="formularios">
	<form action="guardarNuevoCoche" method="POST" enctype="multipart/form-data" id = "formularioRegistro" onsubmit="return validar(e)">
		<table>

			<tr>
				<td>Marca</td>
				<td><input type="text" name="marca" id = "marca"/></td>
				<td>Modelo</td>
				<td><input type="text" name="modelo" id = "modelo" /></td>
				<td>Color</td>
				<td><input type="text" name="color" id = "color" /></td>
				<td>Motor</td>
					<td><input type="text" name="motor" id = "motor" /></td>
			</tr>	
				
			<tr id = "lastRowForm">	
				<td>Cilindrada</td>
				<td><input type="text" name="cilindrada" id = "cilindrada" /></td>
				<td>Precio</td>
				<td><input type="text" name="precio" id = "precio" /></td>
				<td>Telefono</td>
				<td><input type="text" name="telefono" id = "telefono"/></td>
				<td>Email</td>
				<td><input type="text" name="email" id = "email" /></td>
			</tr>	
			
			</table>
			
			<hr/>
			
			<table>
			<tr>	
				<td>Antigüedad</td>
				<td>
				<select name="id_categoria">
						<c:forEach items="${categorias}" var="cat">
							<option value="${cat.id}">${cat.categoria}</option>
						</c:forEach>
				</select>
				</td>

				<td>Imagen</td>					
				<td><input type="file" name="imagen" /></td>

				<td><input type="submit" value="REGISTRAR"  /></td>
			</tr>

		</table>
		
	</form>
	</div>
	
	<jsp:include page="scripts.jsp"></jsp:include>

</body>
</html>