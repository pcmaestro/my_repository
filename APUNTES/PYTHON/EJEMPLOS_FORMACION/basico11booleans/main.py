#Ejemplo de uso de booleanos

variable = True

if variable == True:
    print("Variable igual a True")
    
    
if variable:
    print("Variable vale True en if sin ==")
    
a = 4
b = 10

if b > a:
    print("b es mayor que a")

resultado = b > a

print("Resultado: " + str(resultado))

if resultado:
    print("b es mayor que a")
    
resultado2 = b=10 # resultado2 vale True si b es 10

if resultado == True and resultado2 == True:
    print("Ambos resultados se cumplen")

#Esta es la forma recomendada por la documentación oficial
if resultado and resultado2:
    print("Ambos resultados se cumplen sin == en el if")

#Muchos valores pueden ser considerados como booleanos

# El numero 0 siempre es False , cualquier otro numero devuelve True

variable = 123

if variable:
    print("variable " + str(variable) + " vale True")


variable = 0

if variable:
    print("variable vale True")
else:
    print("variable vale False")
    
booleano = bool(variable)

print("booleano vale " + str(booleano))


booleano = bool(44)

print("booleano vale " + str(booleano))

#Los Array con datos son True y los vacios son False
booleano = bool( ["plantano", "manzana"])

print("booleano vale " + str(booleano))

booleano = bool([])

print("booleano vale " + str(booleano))

#Los string vacios valen False, y con caracteres valen True
booleano = bool("")

print("booleano vale " + str(booleano) )

booleano = bool("Hola")

print("booleano vale " + str(booleano) )

#Una variable a None vale False

nueva_variable = None #Algo no vale nada, no hay valor inicial

booleano = bool(nueva_variable)
print("booleano vale " + str(booleano))


