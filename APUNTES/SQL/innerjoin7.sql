-- USE db_empl


SELECT   E.NUEMPL,
		 E.NOMBRE,
		 E.DEPT,
		 D.NOMDEP,
		 D.NUMDIREC,
		 DR.NOMBRE,
		 DR.APELLIDO,
		 COALESCE(AU.AUMENTO, "NO TIENE") AS IMP_AUMENTO
		 
	FROM TEMPLA E JOIN TDEPTA D 
		ON D.NUMDEP = E.DEPT
			JOIN TEMPLA DR ON DR.NUEMPL = D.NUMDIREC
				LEFT JOIN AUMSAL AU
					ON AU.nuempl = E.NUEMPL
						WHERE COALESCE(AU.AUMENTO, "NO TIENE") > 3000 
						  AND COALESCE(AU.AUMENTO, "NO TIENE") < 7000
						  ORDER BY IMP_AUMENTO DESC