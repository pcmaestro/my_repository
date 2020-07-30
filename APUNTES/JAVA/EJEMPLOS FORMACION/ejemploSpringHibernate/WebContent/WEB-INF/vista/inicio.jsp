<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="jstl" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>

Bienvenido a mi Portal de Anuncios<br/>
<a href="registroAnuncio">registrar mi anuncio</a><br/>
Listado de anuncios:<br/>

<jstl:forEach items="${anuncios}" var="anuncio">
	<div style="margin: 5px">
		${anuncio.titulo}<br/>
		precio: ${anuncio.precio}<br/>
		${anuncio.texto}
	</div>
</jstl:forEach>


</body>
</html>