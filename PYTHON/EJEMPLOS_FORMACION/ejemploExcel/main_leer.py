import pandas as pd

#Leyendo la primera hoja
peliculas = pd.read_excel("movies.xls")
'''
#Leyendo el resto de hojas
pagina_del_excel = 2 # Cuenta las hojas desde cero
peliculas = pd.read_excel("movies.xls", sheet_name = pagina_del_excel)
print(peliculas)
'''
#Para listar todas las columnas
columnas = peliculas.columns


print("columnas leidas")
for c in columnas:
    print(c)

#Tamaño del excel en formato (filas, columnas)
print(peliculas.shape)

#Para leer de una fila hasta otra ( no cuenta el encabezado y empieza de cero)
fila = 3
while fila < 10:
    for c in columnas:
        print(peliculas[c][fila], end = ' -- ')
    print("")
    fila += 1

        