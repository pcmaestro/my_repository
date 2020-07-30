<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib uri="http://www.springframework.org/tags/form" 
prefix="springform" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>

Introduce los datos de tu anuncio:<br/>
<springform:form commandName="objetoForm" action="guardarAnuncio">

	titulo: <springform:input path="titulo"/><br/>
	
	precio: <springform:input path="precio"/><br/>
	
	texto:  <br/>
			<springform:textarea path="texto" cols="15" rows="3"/>
			<br/>
	
	<input type="submit" value="REGISTRAR ANUNCIO"/>
	
</springform:form>

</body>
</html>