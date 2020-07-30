<!DOCTYPE html>
<%@page import="java.util.List"%>
<%@page import="servlets.Anuncio"%>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

Ultimos anuncios: <br/>

<% 
//esto es codigo java que se ejecuta en el servidor
String saludo = "hola";
out.print(saludo);

List<Anuncio> listado = (List<Anuncio>)request.getAttribute("anuncios");
for( Anuncio a : listado){
	out.print("<div>");
	out.print("titulo: " + a.getTitulo() +"<br/>");
	out.print("texto: " + a.getTexto());		
	out.print("</div>");
}
%>

</body>
</html>