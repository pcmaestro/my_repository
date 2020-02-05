/* 2.- LO MISMO QUE ANTES, PERO TAMBIEN MOSTRAMOS LOS NOMBRES DE LOS 
    EMPLEADOS SIN HIJOS, INDICANDO " SIN HIJOS " EN EL NOMBRE DEL HIJO. */

SELECT   TEMPLA.NUEMPL, TEMPLA.NOMBRE, TEMPLA.APELLIDO, 
		 COALESCE(CONCAT(HIJOS.NOMBRE, " ", HIJOS.APELLIDO) , "SIN HIJOS") AS HIJOS

FROM TEMPLA LEFT JOIN HIJOS

ON TEMPLA.NUEMPL = HIJOS.NUEMPL

ORDER BY TEMPLA.NUEMPL

