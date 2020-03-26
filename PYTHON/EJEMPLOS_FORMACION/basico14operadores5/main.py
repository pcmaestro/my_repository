
a = 5
b = 5

#Usando operador de comparación
if a == b:
    print("a y b son iguales")

#Operador de identidad is ( usado por ejemplo para comprar objetos)
if a is b:
    print("a is b")

c = 8

if a != c:
    print("a y c son distintos")

#Operador de identidad is not
if a is not c:
    print("a y c son distintos")
    
#Operador de pertenencia in

frutas = ["naranja", "manzana", "pera"]

if "manzana" in frutas:
    print("manzana está dentro de frutas")

#Operador de pertenencia not in

frutas = ["naranja", "manzana", "pera"]

if "sandia" not in frutas:
    print("sandia no está dentro de frutas")

#Operadores de pertenencia con strings
email ="ana.maria@gmail.com"
#Hay que recordar que los string se pueden considerar como listas

if "@" in email:
    print("la direccion de correo es válida")

    