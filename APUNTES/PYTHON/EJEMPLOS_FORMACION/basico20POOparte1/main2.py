class Jugador():
    nombre = ""
    puntos = 0
    
    #Vamos a definir un bloque de código que puedan ejecutar los objetos de Jugador()
    def borrar(self):
        print("Voy a borrar " + self.nombre)
    
ana = Jugador() # Esto crea el objeto ana de la clase Jugador()

juan = Jugador()

ana.nombre = "Ana Maria"

juan.nombre = "Juan Gomez"

#Ahora mismo ana tiene su nombre y sus puntos y juan tiene su nombre y sus puntos

juan.borrar() # Self en el código borrar() es juan , o sea,  en los métodos
              #Representa al objeto . Self es obligatorio al definir un método
