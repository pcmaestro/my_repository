a = "Hola"
print(a)

b = """String en 
varias lineas"""
print(b)

c = '''String en 
varias lieas de nuevo'''
print(c)

#Los string se consideran como Arrays

array = ["uno", "dos"]
frase = "Hola"
print(array[0])
print(frase[0])

#Tanto los arrays como string se les puede acceder por indices negativos

print(array[-1])
print(frase[-1])

#Los indices negativos hacen referencia al elemento correspondiente
#contando desde el final del Array

#La función len nos devuelve la cantidad de elementos de un array y
#la cantidad de caracteres de un string

print(len(array))
print(len(frase))

#Podemos obtener sólo parte del Array o del string

parte = frase[1:3]
print(parte)

#Pasar los string a mayusculas y minusculas

print(frase.upper())
print(frase.lower())

#El método strip elimina espacios en blanco al principio y al final
nombre = "   Mario Del Real   "
print(nombre)
print(nombre.strip())

#El método replace reemplaza caracteres, en este caso lo cambiamos por una entidad
texto = "año"
texto_entidad = texto.replace("ñ", "&ntilde;")
print("Texto seguro para html y bases de datos : " + texto_entidad)

#El método split trocea un string y lo combierte en elementos de una lista

csv = "raton optico 23.56, alfombrilla raton 4.7;portatil soy 399"

lineas = csv.split(";")

print(lineas)
print(type(lineas))

#Para recorrer la lista creada,  lo hacemos con un bucle for

for l in lineas:
    print(l)
    
#Ahora hacemos otra separación por las comas

for l in lineas:
    compras = l.split(",")
    for c in compras:
        print(c)
