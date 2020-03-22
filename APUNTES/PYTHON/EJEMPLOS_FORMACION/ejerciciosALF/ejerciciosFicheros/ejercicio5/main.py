'''
Ejercicio 5
Escribir un programa que abra el fichero con información sobre el PIB per cápita 
de los países de la Unión Europea 
(url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true), 
pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de 
todos los años disponibles
'''
from urllib.request import urlopen


web = urlopen("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true")
contenido = web.read().decode("utf-8")

x = input("Indicame las iniciales del pais que deseaess consultar : ")

pais = x.upper()

y = contenido.find(pais)

z = y + 118

print("El pais está en la posición " + str(y) )

print("\t" + contenido[22:140])
print(contenido[y:z])
