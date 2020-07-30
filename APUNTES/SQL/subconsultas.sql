/* los clientes que tengan una media de compras de este año superior a la
media . Ordenar la salida por código de vendedor */


SELECT 		CLIENTE, 
			NOMBRE,
			APELLIDO1,
			ROUND((COMPRAS_ANUAL)/4, 2) AS MEDIA_CLIENTE, 
			VENDEDOR		

			
	FROM CLIENTES
		WHERE COMPRAS_ANUAL/4 > (SELECT AVG(COMPRAS_ANUAL)														
	ORDER BY VENDEDOR	

	

/* Listar los tipos de cliente que tengan una media de compras del año actual,
superior a la media de compras para el año actual de todos los clientes*/

SELECT 	 TIPO,
		 AVG(COMPRAS_ANUAL) AS "MEDIA/CLIENTE"
		 
	FROM CLIENTES 
	GROUP BY TIPO
		HAVING AVG(COMPRAS_ANUAL) > (SELECT AVG(COMPRAS_ANUAL)
																

		
																
/* Mostrar el código de cliente, el nombre y la edad del cliente que más ha gastado este año.*/

SELECT   	CLIENTE,
			NOMBRE,
			APELLIDO1,
			TIMESTAMPDIFF(YEAR, FX_NACIMIENTO, CURDATE()) AS EDAD,
			COMPRAS_ANUAL
	FROM CLIENTES
		WHERE COMPRAS_ANUAL = (SELECT MAX(COMPRAS_ANUAL)
							  	FROM CLIENTES)


/* Mostrar qué clientes varones han comprado más que alguna de las clientes mujeres */

SELECT		NOMBRE,
			APELLIDO1,
			COMPRAS_ANUAL

	FROM CLIENTES
		WHERE SEXO = "M" 
			AND COMPRAS_ANUAL > ANY(SELECT COMPRAS_ANUAL
									 FROM CLIENTES
										WHERE SEXO = "F")
																


		
		
		
	

																












