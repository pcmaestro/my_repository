'''
Este método askstring crea una pequeña ventana similar al window.prompt de
javascript para introducir un dato en una caja de texto 
La ventanita que se cre no se puede dimensionar con geometry()
'''
from tkinter import *
from tkinter.simpledialog    import askstring
from tkinter.messagebox import showinfo

ventana = Tk()
ventana.geometry("700x150")
nombre = askstring("Nombre", "Introduce tu nombre")
showinfo("Mensaje", "Hola " + nombre)
ventana.mainloop()

'''

En esta función incluimos una subventana que se crea a partir de la principal. 
El problema con esto es que parar la producción de múltiples ventanas
El contador de clicks es simplemente para que sólo se abra una
'''
from tkinter import *


click = 0

def click_raton(evento):
    global click
    if click < 1:
        ventanita = Tk()
        ventanita.geometry("200x150")
    click +=1
    
#end click_raton

ventana = Tk()
ventana.geometry("400x300")
ventana.bind("<Button 1>", click_raton)
ventana.mainloop()