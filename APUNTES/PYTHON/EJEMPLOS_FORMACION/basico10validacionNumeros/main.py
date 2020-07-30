#Diferentes formas de validar un número

introducido = input("Introduce tu nombre : ")
print("Has introducido " + introducido)

edad = input("Introduce tu edad : ")
#Una vez rocogemos un input del usuario, antes de operar, hay que validar

if edad.isnumeric():
    print("Introdujiste un número")
    edad_int = int(edad)    
    if edad_int >= 18:
        print("Bienvenido")
    else:
        print("No puedes entrar")
else:
    print("No has introducido un número")