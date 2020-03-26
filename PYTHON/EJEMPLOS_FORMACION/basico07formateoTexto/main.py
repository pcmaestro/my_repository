class Producto():
    nombre =""
    precio = 0.0
    
producto1 = Producto()

producto1.nombre = "raton optico"
producto1.precio = 4.99

producto2 = Producto()

producto2.nombre = "alfombrilla raton"
producto2.precio = 3.99

productos = []
productos.append(producto1)
productos.append(producto2)

#Para mostrar información, es util definir un formato

formatoProducto = "nombre: {} precio: {}"

for p in productos:
    print( formatoProducto.format(p.nombre, p.precio) )
