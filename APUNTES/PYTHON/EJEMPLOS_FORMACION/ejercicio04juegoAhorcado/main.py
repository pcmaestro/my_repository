'''
    MAIN

'''
frases = [
    "Luke, yo soy tu padre",
    "En un lugar de la mancha",    
    "Houston , tenemos un problema",
    "Alguien volo sobre el nido del cuco",
    "Vienes a pedirme un favor, y ni siquiera me llamas padrino",    
]

frase_introducida = ""

for i in frases:   
    frase_a_adivinar = i
    while not frase_introducida == frase_a_adivinar:
        frase_a_mostrar = ""        
        puntos = 100        
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
            print("Actualmente tienes " + str(puntos) + " puntos")
            print("1- Resolver frase")
            print("2- Desvelar letra")
            introducido = input("Introduce una opción : ")    
            if introducido == "1":
                frase_introducida = input("Introduce la frase : ")
                if (frase_introducida.lower() == frase_a_adivinar.lower()):
                    print("Felicidades, has adivinado la frase")
                    print("Te han quedado " + str(puntos) + " puntos")
                    fin_juego = True
                else:
                    print("Fallaste !!")
                    puntos -= 20
            elif introducido == "2":
                letra = input("Introduce la letra a desvelar : ")
                vocales ="aeiou"
                if vocales.find(letra) != -1:
                    puntos -= 10
                else:
                    puntos -= 5
                indice = 0
                puntos -= 10
                frase_a_adivinar_min = frase_a_adivinar.lower()
                if frase_a_adivinar_min.find(letra) != -1:    
                    for l in frase_a_adivinar_min:            
                        if l == letra:                
                            print("Encontré la letra en el indice : " + str(indice))
                            #Del indice sacado,  hay que cambiar el guion_bajo por la letra
                            #Python no permite modificar caracteres de un string por su posición
                            #en el índice .  Debido a esto,  vamos a transformar el string a lista
                            #para cambiar el guion por la letra, y luego volveremos a convertir a string
                            frase_guiones_lista = list(frase_a_mostrar)
                            frase_guiones_lista[indice] = frase_a_adivinar[indice] ## También valdría solo l
                            frase_a_mostrar = "".join(frase_guiones_lista)                
                        indice += 1
                    print(frase_a_mostrar)
                else:
                    print("la letra " + letra + " no está incluida en la frase")
print("FIN DEL JUEGO")

        