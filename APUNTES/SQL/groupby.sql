-- Masa salarial por departamento + depatamentos sin gente , EMPLYEE- SALARY ,WORKDEPT // DEPARTMENT- DEPTNO, DEPTNAME

SELECT DEPT.DEPTNO, DEPT.DEPTNAME, (SUM(EMPL.SALARY)) AS MASA_SALARIAL

FROM DEPARTMENT AS DEPT LEFT JOIN EMPLOYEE AS EMPL

ON DEPT.DEPTNO = EMPL.WORKDEPT

GROUP BY DEPT.DEPTNO, DEPT.DEPTNAME

ORDER BY MASA_SALARIAL DESC

