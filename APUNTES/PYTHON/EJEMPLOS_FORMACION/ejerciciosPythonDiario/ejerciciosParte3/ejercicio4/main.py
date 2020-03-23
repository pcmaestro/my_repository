'''
Ejercicio 4
Haz un programa que pida al usuario una cantidad de dolares, una tasa de interés
y un numero de años. Muestra por pantalla en cuanto se habrá convertido el capital
inicial transcurridos esos años si cada año se aplica la tasa de interés introducida.
Recordar que un capital C dolares a un interés del x por cien durante n años se convierte
en C * (1 + x/100)elevado a n (años). Probar el programa sabiendo que una cantidad de
10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.
'''

c1 = float(input("Indicame la cantidad de dinero : "))

i = float( input("indica la tasa de interés : ") )

t = float( input("Indica el número de años : ") )

c2 = ( c1 * ( 1 + i/100)**t)

#Formateo americano de moneda para el resultado

formateo = "El capital final serán {capital:,.2f} dolares"
formatoUSA = formateo.format(capital = c2)

#Y ahora hacemos reemplazos de la coma y el punto para pasar a formato europeo

formatoUE = formatoUSA.replace(".", "@").replace(",", ".").replace("@", ",")

print(formatoUE)

