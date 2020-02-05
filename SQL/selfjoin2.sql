/* Listar el código, nombre y apellido de los clientes, junto con el código,
nombre y apellido del responsable del vendedor asignado a cliente. */

-- USE DBATENTO;

SELECT   C.CLIENTE, 
		 C.NOMBRE, 
		 C.APELLIDO1, 
		 R.VENDEDOR AS RESP_VENDEDOR, 
		 R.NOMBRE,
		 R.APELLIDO

FROM CLIENTES C JOIN VENDEDOR V 
ON C.VENDEDOR = V.VENDEDOR

	INNER JOIN VENDEDOR R 
	ON V.VENDEDOR = R.RESPONSABLE;