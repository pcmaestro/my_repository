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

<div style="text-align: center">
Listado de anuncios:
</div>

<c:forEach items="${libros}" var="libro">
	<div style="margin: 10px">
		autor: ${libro.autor}<br/>
		titulo: ${libro.titulo}<br/>
		precio: ${libro.precio}	
	</div>
</c:forEach>


</body>
</html>