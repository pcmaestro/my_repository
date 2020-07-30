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

Introduce los datos del coche </br>

<form action = "ServletGuardarCambiosCoche" method = "POST">

	Marca <input type = "text" value = "${coche.marca }" name = "marca"/></br>
	Modelo <input type = "text"value = "${coche.modelo}" name = "modelo"/></br>
	Color <input type = "text" value = "${coche.color}" name = "color"/></br>
	Motor <input type = "text" value = "${coche.motor}"  name = "motor"/></br>
	Cilindrada <input type = "text" value = "${coche.cilindrada}"  name = "cilindrada"/></br>
	Precio <input type = "text" value = "${coche.precio}"  name = "precio"/></br>
	Telefono <input type = "text" value = "${coche.telefono}"  name = "telefono"/></br>
	Email <input type = "text" value = "${coche.email}"  name = "email"/></br>	
	Antigüedad : <select name = "id_categoria" >					
					<option value ="1" ${nuevo} >nuevo</option>
					<option value ="2" ${seminuevo} >seminuevo</option>
					<option value ="3" ${viejo} > viejo </option>
	
				</select></br>
	<input type = "hidden" value = "${coche.id}" name = "id" />
	<input type = "submit" value = "MODIFICAR"/>

</form>



</body>
</html>