#Para usar otros módulos de Python

#Métodos de importación
import clases.Compra as moduloClaseCompra # Desde paquete clases,  archivo Compra

from Utilidades import validadores # Otro método, sin crear el alias

#....

compra = moduloClaseCompra.Compra()  # Del paquete clases, archivo Compra.py,  instanciamos la clase Compra()

compra.direccion = "Calle Real 45"

compra.productos = [3,5,14]

#...

email = "juan2@gmail.com"

Utilidades.validadores.validadorEmail(email) # Otro metodo

validadores.validadorEmail(email) # Este otro método requiere hacer un import from