<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Registro de anuncios</title>
</head>
<body>
	<jsp:include page="menu.jsp"></jsp:include>
	
	Introduzca los datos de su anuncio
	
	</br>
	
	<form action="guardarNuevoCoche" method = "POST" enctype ="multipart/form-data">
	
	Marca <input type = "text" name = "marca"/></br>
	Modelo <input type = "text" name = "modelo"/></br>
	Color <input type = "text" name = "color"/></br>
	Motor <input type = "text" name = "motor"/></br>
	Cilindrada <input type = "text" name = "cilindrada"/></br>
	Precio <input type = "text" name = "precio"/></br>
	Telefono <input type = "text" name = "telefono"/></br>
	Email <input type = "text" name = "email"/></br>
	Antigüedad : <select name = "id_categoria" >		
						<c:forEach items = "${categorias}" var ="cat">
							<option value ="${cat.id}">${cat.categoria}</option>
						</c:forEach>
				</select></br>
	Imagen : <input type = "file" name = "imagen"/></br>
	<input type = "submit" value = "REGISTRAR"/>
	
	</form>
	
	
</body>
</html>