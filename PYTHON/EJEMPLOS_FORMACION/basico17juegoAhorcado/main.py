'''
    MAIN

'''

frase_a_adivinar = "Luke, yo soy tu padre"

frase_a_mostrar = ""

for letra in frase_a_adivinar:
    if letra != " ":
        frase_a_mostrar += "_"
    else:
        frase_a_mostrar += " "
        
print("Adivina la siguiente frase : ")
print(frase_a_mostrar)

#Agregar un menú de opciones para resolver frase o desvelar letra

fin_juego = False

while not fin_juego:
    print("1- Resolver frase")
    print("2- Desvelar letra")
    introducido = input("Introduce una opción : ")
    if introducido == "1":
        frase_introducida = input("Introduce la frase : ")
        if frase_introducida == frase_a_adivinar :
            print("Felicidades, has adivinado la frase")
            fin_juego = True
        else:
            print("Fallaste !!")
    elif introducido == "2":
        letra = input("Introduce la letra a desvelar : ")
        indice = 0
        for l in frase_a_adivinar:
            if l == letra:
                print("Encontré la letra en el indice : " + str(indice))
                #Del indice sacado,  hay que cambiar el guion_bajo por la letra
                #Python no permite modificar caracteres de un string por su posición
                #en el índice .  Debido a esto,  vamos a transformar el string a lista
                #para cambiar el guion por la letra, y luego volveremos a convertir a string
                frase_guiones_lista = list(frase_a_mostrar)
                frase_guiones_lista[indice] = letra
                frase_a_mostrar = "".join(frase_guiones_lista)
            indice += 1
        print(frase_a_mostrar)
        