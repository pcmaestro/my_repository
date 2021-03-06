#Las variables globales no se pueden modificar directamente en las funciones
#Esto es debido a que se encuentran en ambitos (scopes) distintos
#El método básico es informar variables globales dentro de las funciones con global
#Pero este método no es recomendable, ya que en programas muy grandes
#puede provocar compartamientos no deseados.

#En este caso la variable local está dentro de la función, al invocar dicha función
#se ejecuta correctamente

def mi_funcion():
    x = 300
    print("X vale " + str(x))
 
mi_funcion()

#Pero en este otro caso la variable es global y no podemos modificarla directamente
#en la función,  para esta última ,  x sería una variable propia

x = 300

def mi_funcion2():
    x = 400
    print("X ahora vale " + str(x))
    

mi_funcion2()

    
