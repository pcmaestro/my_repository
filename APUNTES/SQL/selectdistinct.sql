SELECT DISTINCT
					CLI.CLIENTE, 
					CLI.NOMBRE, 
					CLI.APELLIDO1, 
					CLI.APELLIDO2

FROM CLIENTES CLI JOIN VALEDESC VAL 
ON CLI.CLIENTE = VAL.CLIENTE

WHERE CLI.SEXO = "F";
		
