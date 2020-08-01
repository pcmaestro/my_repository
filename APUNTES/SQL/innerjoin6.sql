/*  4.0- MOSTRAR DE CADA DEPARTAMENTO, SU NOMBRE, SU CODIGO Y EL NOMBRE Y APELLIDO 
     DEL DIRECTOR. */

SELECT   TDEPTA.NOMDEP, 
		 TDEPTA.NUMDEP, 
		 CONCAT(TEMPLA.NOMBRE, " ", TEMPLA.APELLIDO) AS "DIRECTOR DEPARTAMENTO"

FROM TDEPTA INNER JOIN TEMPLA ON TEMPLA.NUEMPL = TDEPTA.NUMDIREC;