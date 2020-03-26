# Las funciones pueden recibir información


def comprar(idProducto, idUsuario, cantidad=1):
    print("procesar la compra del usuario de id: " + str(idUsuario))
    print("para el producto de id: " + str(idProducto))
    print("cantidad " + str(cantidad))
    
# ....


comprar(5, 34, 7)

# Tambien se puede invocar la función así

comprar(idProducto=5, idUsuario=34, cantidad=7)
