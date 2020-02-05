-- Mstrar el nombre, la fecha de alta y el límite de compras de los clientes que son mujeres
USE DBATENTO;

SELECT C.TIPO, C.NOMBRE, C.APELLIDO1, C.FX_ALTA, T.LIM_MES
FROM CLIENTES C INNER JOIN TARJETAS T
ON C.CLIENTE = T.CLIENTE
WHERE C.SEXO = "F";