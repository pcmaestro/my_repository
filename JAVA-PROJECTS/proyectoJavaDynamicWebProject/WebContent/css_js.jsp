<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>

<style>
.menuUsuario {
	margin: auto;
	padding: 2em;
	background-color: #F5EFEE;
	text-align: center;
	font-weight: bold;
	box-shadow: 1px 1px 1px;
}

.menuUsuario #inicio, #registro, #accesoAdmin {
	padding: 1.5em;
	text-decoration: none;
	font-size: 1.5em;
}

.menuUsuario a:link {
	text-decoration: none;
}

.menuUsuario a:hover {
	color: white;
}

.opcionMenu {
	margin: 2em;
	padding: 2em;
}

.formularios table {
	margin: auto;
	text-align: center;
}

.formularios table td {
	padding: 1em;
	padding-top: 2em;
}

.paginacion {
	padding-top: 1em;
	padding-bottom: 1em;
	text-align: center;
}

.paginacion a {
	padding-bottom: 1em;
}

.paginacion a:link {
	text-decoration: none;
}

.paginacion a:hover {
	color: red;
}

#contadorResultados {
	font-size: 1.5em;
}

.zonaListado .listado td {
	padding: 1.5em;
	font-size: 1.1em;
}

.zonaListado .listado th {
	padding: 1em;
	background-color: #F5EFEE;
}

.zonaListado .listado tr {
	box-shadow: 1px 1px 1px;
}

#loginBody {
	font-size: 2em;
}

#ventanaLogin {
	margin: auto;
	background-color: #F5EFEE;
	width: 50%;
	padding: 2em;
	text-align: center;
}

#ventanaLogin .label {
	color: black
}

#ventanaLogin td {
	padding: 0.5em;
}

#invisible {
	padding: 2em;
}

#botonRegistro {
	margin: auto;
}

#gracias {
	width: 70%;
	background-color: #F5EFEE;
	margin: auto;
	text-align: center;
	padding: 2em;
}

#textoGracias {
	font-size: 5em;
}

#gracias a:hover {
	text-decoration: none;
	color: red;
}

.menuAdministracion {
	margin: auto;
	padding: 0.5em;
	background-color: #F5EFEE;
	text-align: center;
	font-size: 1.5em;
	font-weight: bold;
	box-shadow: 1px 1px 1px;
}

.menuAdministracion a {
	padding-right: 2em;
	padding-left: 2em;
}

.menuAdministracion a:hover {
	text-decoration: none;
	color: white;
}

#tablaEdicion th, td {
	padding: 1.5em;
}

#tablaEdicion th {
	background-color: #F5EFEE;
}

#tablaEdicion tr {
	box-shadow: 1px 1px 1px;
}

#tablaEdicion a:hover {
	text-decoration: none;
	color: white;
}

img {
	height: 50px;
}

#error {
	width: 85%;
	margin: auto;
	color: red;
	display: none;
}

footer {
	height: 4em;
}
</style>


<link rel="stylesheet"
	href= <c:url value = "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" />
	integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
	crossorigin="anonymous" />

<script src= <c:url value =  "https://code.jquery.com/jquery-3.5.1.min.js" />
	integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
	crossorigin="anonymous"></script>