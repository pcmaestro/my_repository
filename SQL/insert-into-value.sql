/* 10.1.  -  Insertar un cliente con nombre y apellidos -a tu gusto-, que se ha dado de alta
 hoy (no puedes poner la fecha como valor fijo), que naci� en el 1990, los campos
 VENDEDOR, EMPRESA son nulos. Vive en tu barrio. El tipo cliente es A1. */


INSERT INTO CLIENTES (CLIENTE, NOMBRE, APELLIDO1 , APELLIDO2, TIPO, 
			TELEFONO, FX_ALTA, VENDEDOR, CODPOSTAL, SEXO, 
			FX_NACIMIENTO, COMPRAS_ANUAL, EMPRESA)

VALUES ('100004', 'CURRO', 'ROMERO', 'DE TORRES', 'A1', NULL, 
		CURRENT TIMESTAMP, NULL, '28921', 'M', '1990-07-01', NULL, NULL);

SELECT *
FROM CLIENTES WHERE CLIENTE = '100004';



-- Insertar otro cliente que sea la pareja del anterior. 

INSERT INTO CLIENTES (CLIENTE, NOMBRE, APELLIDO1 , APELLIDO2, TIPO, 
			TELEFONO, FX_ALTA, VENDEDOR, CODPOSTAL, SEXO, 
			FX_NACIMIENTO, COMPRAS_ANUAL, EMPRESA)

VALUES ('100008', 'CRISTINA', 'GARCIA', 'MALAJE', 'A1', NULL, 
		CURRENT TIMESTAMP, NULL, '28921', 'M', '1990-07-01', NULL, NULL);

SELECT *
FROM CLIENTES WHERE CLIENTE = '100008';


/*Insertar un cliente con nombre y apellidos -a tu gusto-, que se ha dado de alta
 hoy (no puedes poner la fecha como valor fijo), que naci� en el 1970, los campos
 VENDEDOR, EMPRESA son nulos. Vive en tu barrio. El tipo cliente es C1. */

INSERT INTO CLIENTES (CLIENTE, NOMBRE, APELLIDO1 , APELLIDO2, TIPO, 
			TELEFONO, FX_ALTA, VENDEDOR, CODPOSTAL, SEXO, 
			FX_NACIMIENTO, COMPRAS_ANUAL, EMPRESA)

VALUES ('100012', 'MANUEL', 'BENITEZ', 'CORDOBES', 'C1', NULL, 
		CURRENT TIMESTAMP, NULL, '28921', 'M', '1970-07-01', NULL, NULL);


SELECT *

FROM CLIENTES c WHERE CLIENTE = '100012';

UPDATE CLIENTES 

SET SEXO = 'F'

WHERE CLIENTE = '100008';


