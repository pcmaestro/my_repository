#Las funciones pueden devolver información

def validarNombre(nombre):
    if nombre == "":
        return "El nombre está vacío"
    else:
        return "Nombre OK"

resultado = validarNombre("Pedro")

#Si le damos un nombre, la función devuelve None , porque sólo hemos definido que
#devuelva un valor si nombre no está vacío
print("resultado " + str(resultado) )

#Pero ahora si devuelve "Nombre OK"
def validarNombre(nombre):
    if nombre == "":
        return "El nombre está vacío"
    else:
        return "Nombre OK"

resultado = validarNombre("Pedro")