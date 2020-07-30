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
Actualiza los datos del libro:
<form action="ServletGuardarCambiosLibro" method="post">
titulo: <input type="text" value="${libro.titulo}" name="titulo"/> <span style="color: red">${errorTitulo}</span> <br/>
autor: <input type="text" value="${libro.autor}" name="autor"/><br/>
paginas: <input type="text" value="${libro.numeroPaginas}" name="paginas"/> <span style="color: red">${errorPaginas}</span> <br/>
precio: <input type="text" value="${libro.precio}" name="precio"/> <span style="color: red">${errorPaginas}</span> <br/>
<input type="hidden" name="id" value="${libro.id}"/>
<input type="submit" value="GUARDAR CAMBIOS"/>
</form>


</body>
</html>