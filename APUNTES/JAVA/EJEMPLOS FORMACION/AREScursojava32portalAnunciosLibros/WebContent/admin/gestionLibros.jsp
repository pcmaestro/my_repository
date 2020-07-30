<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<jsp:include page="menu.jsp"></jsp:include>

<c:forEach items="${libros}" var="libro">
	<div style="margin: 10px">
		autor: ${libro.autor}<br/>
		titulo: ${libro.titulo}<br/>
		precio: ${libro.precio}	
		<a onclick="return confirm('¿estas seguro?')" href="ServletBorrarLibro?id=${libro.id}">BORRAR</a>
		<a href="ServletEditarLibro?id=${libro.id}">EDITAR</a>
	</div>
</c:forEach>

</body>
</html>