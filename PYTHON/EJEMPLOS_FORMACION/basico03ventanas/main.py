'''
Created on 9 mar. 2020

@author: Hp 840 G2

'''
#Ejemplo introductorio de aplicaciones de escritorio con tkinter

import tkinter as tk

#Creamos una ventana de tkinter,  lo hacemos usando la clase Tk() ,  pero
#como esta clase no es propia de Python , indicamos que es de tkinter (al que
#más arriba hemos llamado tk)

win = tk.Tk()

#Invocamos el método mainloop para mostrar la ventana
#Aqui creamos un pequeño formulario , la etiqueta,
##el campo de entrada y sus posiciones en la ventana

texto = "Introduce una cantidad de euros"

etiqueta = tk.Label(win, text = texto)

etiqueta.grid(column = 0, row = 0)

entrada = tk.Entry(win, width = 12)

entrada.grid(column = 1, row = 0)

#Ahora añadimos un botón

boton = tk.Button(win, text = "Convertir")
boton.grid(column = 2, row = 0)

win.mainloop()

