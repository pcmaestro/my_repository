#Diferentes formas de validar un número

introducido = input("Introduce tu nombre : ")
print("Has introducido " + introducido)

edad = input("Introduce tu edad : ")
#Una vez rocogemos un input del usuario, antes de operar, hay que validar

#Ejemplo de validación usando el bloque try

try:
    edad_int = int(edad)
    print("Gracias por introducir un número")
    if edad_int >= 18:
        print("Bienvenido")
    else:
        print("No puedes entrar")
except:
    print("No has introducido un número")