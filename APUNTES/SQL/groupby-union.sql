-- Listar el vendedor y el total de ventas acumulado durante el año actual.

SELECT VENDEDOR, SUM(COMPRAS_ANUAL) "COMPRAS ANUALES"
FROM CLIENTES
WHERE VENDEDOR IS NOT NULL
GROUP BY VENDEDOR
HAVING SUM(COMPRAS_ANUAL) > 200
ORDER BY VENDEDOR;

-- Mostrar lv cantidad de clientes que existe por cada tipo

SELECT TIPO , COUNT(TIPO) AS CANTIDAD
FROM CLIENTES
GROUP BY TIPO
ORDER BY COUNT(TIPO) DESC;

-- Comprobar si algún cliente tiene más de una tarjeta

SELECT CLIENTE, COUNT(NUM_TARJETA) TARJETAS
FROM TARJETAS
GROUP BY CLIENTE
HAVING COUNT(NUM_TARJETA) > 1;

-- Listar los tipos de clientes que tengan más de dos clientes

SELECT TIPO, COUNT(*) CANTIDAD
FROM CLIENTES
GROUP BY TIPO
HAVING CANTIDAD > 2
ORDER BY COUNT(TIPO) DESC;

-- Mostar ahora la media de compras, la suma total por rango, la desviación típica y la varianza, para cada tipo de clientes

SELECT TIPO, 
		SUM(COMPRAS_ANUAL) "TOTAL COMPRAS", 
		ROUND(AVG(COMPRAS_ANUAL), 2) "MEIDA COMPRAS", 
		ROUND(STD(COMPRAS_ANUAL), 2) "DESV TIPICA", 
        ROUND(VARIANCE(COMPRAS_ANUAL), 2) "VARIANZA"
FROM CLIENTES
GROUP BY TIPO;

-- Para  cada responsable de vendedores, mostrar el salario máximo y el salario mínimo de los vendedores que están a su cargo.

SELECT RESPONSABLE, MIN(SALARIO) "MIN SAL", MAX(SALARIO) "MAX SAL"
FROM VENDEDOR
GROUP BY RESPONSABLE;

-- Mostar la misma información que antes, salario máximo y salario mínimo, pero esta vez agrupado por año de contratación de los vendedores

SELECT YEAR(FX_CONTRAT) "AÑO CONTRAT", MIN(SALARIO) "MIN SAL", MAX(SALARIO) "MAX SAL"
FROM VENDEDOR
GROUP BY YEAR(FX_CONTRAT)
ORDER BY YEAR(FX_CONTRAT);

-- De los responsables de Tipos de Cliente, mostrar aquellos que sean responsables de más de un tipo

SELECT RESPONSABLE, COUNT(*) "TIPOS"
FROM TIPOCLIE
WHERE RESPONSABLE IS NOT NULL
GROUP BY RESPONSABLE
HAVING TIPOS > 1;

-- Apellido mas repetido

SELECT DISTINCT APELLIDO1, COUNT(*)
FROM CLIENTES
GROUP BY APELLIDO1
ORDER BY COUNT(*);

-- Pareja de apellidos mas repetidos

SELECT CONCAT(APELLIDO1, " ", APELLIDO2) APELLIDOS , COUNT(*)
FROM CLIENTES
GROUP BY CONCAT(APELLIDO1, " ", APELLIDO2)
ORDER BY COUNT(*);

-- De aquellos clientes que hayan recibido más de un VALE DESCUENTO con\n
-- un importe medio superior a 10 euros, mostrar el importe medio de los vales,\n
-- la cantidad de vales recibidos así como las fechas del primer y el último vale.'

SELECT CLIENTE, COUNT(*), AVG(IMPORTE), MIN(FX_VALE), MAX(FX_VALE)
FROM VALEDESC;

-- Que meses hemos dado mas vales descuento , cuantos han sido y la media del importe

SELECT SUBSTR(FX_VALE, 1,7) MES , COUNT(*) CANTIDAD , ROUND(AVG(IMPORTE), 2) "IMPORTE MEDIO"
FROM VALEDESC
GROUP BY SUBSTR(FX_VALE, 1,7)
ORDER BY COUNT(*) DESC;

SELECT YEAR(FX_VALE) "AÑO", MONTH(FX_VALE) MES, COUNT(*) CANTIDAD, ROUND(AVG(IMPORTE), 2) "IMPORTE MEDIO"
FROM VALEDESC
GROUP BY YEAR(FX_VALE), MONTH(FX_VALE)
ORDER BY COUNT(*) DESC;

-- Acceder a la tabla de clientes y vendedores, y para cada cliente/vendedor, 
-- mostrar el nombre, el primer apellido, el código de clientevendedor, y por
-- último un campo con el literal ‘CLIENTE’ ó ‘VENDEDOR’. Ordenar la salida por
-- apellido y nombre.

SELECT NOMBRE, APELLIDO1 AS APELLIDO, CLIENTE AS CODIGO, "CLIENTE" AS TIPO
FROM CLIENTES
UNION
SELECT NOMBRE, APELLIDO, VENDEDOR AS CODIGO, "VENDEDOR"
FROM VENDEDOR
ORDER BY APELLIDO, NOMBRE

-- Acceder a la tabla de clientes y a la de tarjetas para mostrar una lista de los
-- clientes y los autorizados en las tarjetas de los clientes. Mostrar el código de
-- cliente, nombre, primer apellido, y al igual que en el ejercicio anterior, añadir al
-- final el literal ‘CLIENTE’ ó ‘AUTORIZADO’ en función de la información que estamos recuperando. 
-- Ordenar la salida por código de cliente.

SELECT CLIENTE, NOMBRE, APELLIDO1 AS APELLIDO, "CLIENTE" AS TIPO
FROM CLIENTES
UNION
SELECT CLIENTE, NOM_AUTORIZADO, APE_AUTORIZADO, "AUTORIZADO"
FROM TARJETAS



















