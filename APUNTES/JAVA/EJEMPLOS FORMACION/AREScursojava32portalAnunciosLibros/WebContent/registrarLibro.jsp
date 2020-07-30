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

Introduce los datos de tu libro:<br/>

<form action="guardarNuevoLibro" method="post">
titulo: <input type="text" name="titulo"/> <span style="color: red">${errorTitulo}</span> <br/>
autor: <input type="text" name="autor"/><br/>
paginas: <input type="text" name="paginas"/> <span style="color: red">${errorPaginas}</span> <br/>
precio: <input type="text" name="precio"/> <span style="color: red">${errorPaginas}</span> <br/>
<input type="submit" value="REGISTRAR"/>

</form>

</body>
</html>