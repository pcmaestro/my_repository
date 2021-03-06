'''
    EJEMPLO DE JUEGO DE VENTANAS CON TKINTER. EVENTOS Y DIFERENTES
    COMPONENTES VISUALES
'''

from tkinter import *
from tkinter import messagebox
from time import time

#contador de aciertos
contador = 0

#contador de oportunidades
oportunidades = 1 

#Indicadores de acierto
img1 = 0 
img2 = 0
img3 = 0
img4 = 0
img5 = 0

#Contador de clicks
clicks = 0

#Iniciar variable para almacenar nombre de usuario
nombre =""

#Iniciar variable para almacenar tiempo de resolución
tiempo_ejecucion = -1

#Iniciar variable para almacenar jugadores
listado = ""

#Iniciar contador de tiempo de juego
tiempo_inicial = time()

#Guardamos nombre del usuario y creamos archivo de jugadores en caso de
#no existir
def caja_texto():
    global nombre
    nombre = entrada_usuario.get()
    file = open(
        "D:/WORKSPACE/LICLIPSE/ejercicio05ventanaDiferencias/archivo.txt", "a+"
        )
    file.close()
    alert.destroy()

#end caja_texto    

#Eventos desencadenados por el click del raton
def click_raton(evento):
    global x, y, nombre, contador, oportunidades, img1, img2, img3, img4, img5 
    global clicks, tiempo_ejecucion
    x = evento.x
    y = evento.y
    print("x : " + str(x))
    print("y : " + str(y))
    clicks +=1
    print("Van " + str(clicks) + " clicks")
    
         
    if oportunidades < 11:
        
        if x >= 12 and x <= 568 and y >= 161 and y <= 215:
            if img1 == 0:
                contador += 1
                img1 = 1
                messagebox.showinfo(
                    "Mensaje", "Felicidades, acertaste !, te faltan " 
                    + str(5 - contador) + " diferencias por adivinar"
                    )
            else:
                messagebox.showinfo(
                "Mensaje", "Esta diferencia ya la habias acertado"
                )
            
            
        elif x >= 832  and x <= 901  and y >= 236  and y <= 276:
            if img2 == 0:
                contador += 1
                img2 = 1
                messagebox.showinfo(
                    "Mensaje", "Felicidades, acertaste !, te faltan " 
                    + str(5 - contador) + " diferencias por adivinar"
                    )
            else:
                messagebox.showinfo(
                "Mensaje", "Esta diferencia ya la habias acertado"
                )
            
            
        elif x >= 896  and x <= 945  and y >= 170  and y <= 213 :
            if img3 == 0:
                contador += 1
                img3 = 1
                messagebox.showinfo(
                    "Mensaje", "Felicidades, acertaste !, te faltan " 
                    + str(5 - contador) + " diferencias por adivinar"
                    )
            else:
                messagebox.showinfo(
                "Mensaje", "Esta diferencia ya la habias acertado"
                )
            
            
        elif x >= 866  and x <= 937  and y >= 29  and y <= 74 :
            if img4 == 0:
                contador += 1
                img4 = 1
                messagebox.showinfo(
                    "Mensaje", "Felicidades, acertaste !, te faltan " 
                    + str(5 - contador) + " diferencias por adivinar"
                    )
            else:
                messagebox.showinfo(
                "Mensaje", "Esta diferencia ya la habias acertado"
                )
            
            
        elif x >= 694  and x <= 788  and y >= 156  and y <= 205 :
            if img5 == 0:
                contador += 1
                img5 = 1
                messagebox.showinfo(
                    "Mensaje", "Felicidades, acertaste !, te faltan " 
                    + str(5 - contador) + " diferencias por adivinar"
                    )
            else:
                messagebox.showinfo(
                "Mensaje", "Esta diferencia ya la habias acertado"
                )
            
            
        else:
            if oportunidades != 10:
                messagebox.showinfo(
                    "Mensaje", "No has acertado, te quedan " + 
                    str(10 - oportunidades) + " oportunidades")
        '''       
            else:          
                messagebox.showinfo(
                    "Mensaje", "OOOOH !! , agotaste tus oportunidades"
                    )
        '''        
        
        if clicks == 10:
                messagebox.showinfo(
                    "Mensaje", "OOOOH !! , agotaste tus oportunidades"
                    )
                ventana.destroy()
            
        
        if contador == 5:        
            tiempo_final = time() 
            tiempo_ejecucion = tiempo_final - tiempo_inicial        
            messagebox.showinfo(
                "Mensaje", "Acertaste todas las diferencias, has tardado " + 
                                str( round(tiempo_ejecucion, 2) ) + " segundos" 
                                )
            ventana.destroy()
            tiempo_usuario()
        
            
        oportunidades += 1

        
#end click_raton

#Escribimos en el archivo el nombre y el tiempo del jugador
def tiempo_usuario():
    global nombre
    file = open(
        "D:/WORKSPACE/LICLIPSE/ejercicio05ventanaDiferencias/archivo.txt", "a"
        )     
    file.write(
        nombre + " , tiempo : " + str( round(tiempo_ejecucion, 2) ) 
        + " segundos\n"
        )
    file.close()

#end tiempo_usuario

#Mostramos en la ventana de juego los tiempos de los jugadores
def mostrar_tiempo_usuario():
    global listado
    file = open(
        "D:/WORKSPACE/LICLIPSE/ejercicio05ventanaDiferencias/archivo.txt", "r"
        )
    listado = file.read()
    file.close()

#Ventana para recoger el nombre del usuario
alert = Tk()
alert.title("Mensaje")
etiqueta1 = Label(
    alert, text = "Averigua las 5 diferencias entre ambas imagenes." 
                + " Indica tu nombre :").place(x = 10, y = 50
    )
entrada_usuario = StringVar()
campo =Entry(alert, textvariable = entrada_usuario).place(x = 400 ,y = 50)
Button(alert, text = "Enviar", command = caja_texto).place(x = 10, y = 80)
alert.geometry("700x150")
alert.mainloop()

#Ventana de juego
ventana = Tk()
canvas = Canvas(ventana, width = 800, height = 600)
canvas.pack(expand = YES , fill = BOTH)
imagen = PhotoImage(file = "paisaje2.png")
canvas.create_image(0,0,image= imagen, anchor = NW)
mostrar_tiempo_usuario()
etiqueta2 = Label(ventana, text = listado).place(x = 10, y = 300)
ventana.geometry("1050x600")
ventana.title("Pincha para adivinar las diferencias")
ventana.bind("<Button 1>", click_raton)
ventana.mainloop()



