#Este método es le mejor para manipular archivos,  abre y cierra directamente
#el archivo, pero requiere de indentación, en este ejemplo copiamos el contenido
#de un fichero a otro

with open("c:/Users/hipercor/Desktop/pruebaOutput.txt", "a") as output:
    with open("c:/Users/hipercor/Desktop/pruebaInput.txt", "r") as file:
        for linea in file:
            output.write(linea)   

print("Programa finalizado")