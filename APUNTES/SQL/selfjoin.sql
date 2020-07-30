/*Listar el nombre y apellido de cada vendedor junto con el nombre y apellido de
su responsable.*/

SELECT V.VENDEDOR, V.NOMBRE, V.APELLIDO, V.RESPONSABLE, R.NOMBRE, R.APELLIDO
FROM VENDEDOR V INNER JOIN VENDEDOR R
ON V.RESPONSABLE = R.VENDEDOR
WHERE V.VENDEDOR != R.RESPONSABLE


