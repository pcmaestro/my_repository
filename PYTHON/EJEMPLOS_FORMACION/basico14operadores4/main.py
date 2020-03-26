
usuarioBaneado = True

conexion = True

resultado = usuarioBaneado and conexion

#Aqui seria True and True = True
print("resultado de operador and :" + str(resultado) )

conexion = False

resultado = usuarioBaneado and conexion

#Aqui seria True and False = False
print("resultado de operador and :" + str(resultado) )

#Ejemplo validación de concesión de préstamo
prestamo = 40000
historialOk = True
fondos = 12000

#La condicion es que el cliente no tenga concedido ya un préstamo superior a
#50.000 eur, que su historial no tenga incidencias y que tenga fondos
#de más de 10.000 eur

nuevoPrestamo = prestamo < 50000 and historialOk and fondos > 10000

print("prestamo concedido : " + str(nuevoPrestamo))

#Operador or

a = 4
b = -3

resultado_or = a > 0 or b > 0  # b no es mayor que cero , pero a si lo es

print("resultado_or : " + str(resultado_or))

#Operador not

saldo = 0
historial = "ok"
credito = -1000

#Bloquearemos la tarjeta si el historial no es OK , como en este caso historial = Ok, el
#resultado será que no hay que bloquear la tarjeta

bloquear_tarjeta = not (historial == "ok") and saldo <= 0 and credito <= 0
print("bloqueo de tarjeta : " + str(bloquear_tarjeta))