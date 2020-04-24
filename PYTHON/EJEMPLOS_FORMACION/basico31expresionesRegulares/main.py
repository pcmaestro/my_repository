import re

#Validamos 0-9, a-z en mayusculas, minusculas, con acentos y con espacios
#Mínimo 2 caracteres y máximo 30 caracteres
patron = "^[0-9a-zA-Z áéíóúÁÉÍÓÚñÑ]{2,30}$"
patron_email = "^[a-zA-Z0-9\.]{2,30}@[a-zA-Z0-9]{2,30}\.[a-zA-Z]{2,3}$"
validador = re.compile(patron)

texto ="hola buenas Calle Del sol 12 "

resultado_validacion = validador.match(texto)

if resultado_validacion:
    print("texto introducido OK")
else:
    print("texto incorrecto")
    
    
email = "quie.ton@hotmail.com"
validador_email = re.compile(patron_email)
resultado_validacion = validador_email.match(email)
if resultado_validacion :
    print("EMAIL OK")
else :
    print("EMAIL NO VALIDO")
    


    

