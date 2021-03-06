#Formateo de fecha y hora


from time import time
from datetime import datetime


#Este método nos devuelve el tiempo transcurrido desde 01/01/1970
ahora = time()
print(str(ahora))

#Este método nos devuelve fecha y hora en formato ISO
ahora = datetime.now()
print(ahora)

#Esta propiedad de time() nos devuelve el año actual
print("Año actual " + str(ahora.year))


#Este es el método que nos permite formatear y convertir a string las fechas y las horas
string_fecha = ahora.strftime("%m/%d/%Y, %H:%M:%S")
print(string_fecha)