/*Para los clientes que tengan tarjeta, listar los clientes junto con el límite de
compras correspondiente a su tipo y el límite mensual de la
tarjeta.*/

SELECT  CLIENTES.CLIENTE, CLIENTES.TIPO, CLIENTES.NOMBRE, 
		TIPOCLIE.LIMITE_COMPRAS, TARJETAS.LIM_MES
FROM TARJETAS INNER JOIN CLIENTES
ON TARJETAS.CLIENTE = CLIENTES.CLIENTE
	INNER JOIN TIPOCLIE
		ON TIPOCLIE.TIPO = CLIENTES.TIPO