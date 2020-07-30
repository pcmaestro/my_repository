import re
expresion_titulo = "^[0-9a-zA-Z áéíóúÁÉÍÓÚñÑ]{5,30}$"
expresion_precio = "^[0-9,\.]{1,9}$"
expresion_tema= "^[0-9a-zA-Z áéíóúÁÉÍÓÚñÑ]{5,40}$"


def validar_titulo(titulo):
    validador_titulo = re.compile(expresion_titulo)
    return validador_titulo.match(titulo)

def validar_precio(precio):
    validador_precio = re.compile(expresion_precio)
    return validador_precio.match(precio)

def validar_tema(tema):
    validador_tema = re.compile(expresion_tema)
    return validador_tema.match(tema)


    
    