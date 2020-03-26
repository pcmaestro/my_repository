class Jugador():
    nombre = ""
    puntos = 0
    
    #Esto es un constructor que no pide nada, de esta forma podemos crear objetos
    #de jugador sin tener que dar argumentos al constructor
    def __init__(self):
        #ESte código dentro del constructor se va a ejecutar cada vez que se cree
        #un objeto de esta clase
        print("Se ejecuta el constructor de jugador")
    
    
    #Vamos a definir un bloque de código que puedan ejecutar los objetos de Jugador()
    def borrar(self):
        print("Voy a borrar " + self.nombre)
    
    def mandar_email(self, email, urgente = False): ## El False hace el parametro urgente opcional
        print("mandar a : " + self.nombre)
        print("el siguiente email : " + email)
        print("urgente : " + str(urgente))
    
ana = Jugador() # Esto crea el objeto ana de la clase Jugador()

juan = Jugador()

ana.nombre = "Ana Maria"

juan.nombre = "Juan Gomez"

#Ahora mismo ana tiene su nombre y sus puntos y juan tiene su nombre y sus puntos

juan.borrar() # Self en el código borrar() es juan , o sea,  en los métodos
              #Representa al objeto . Self es obligatorio al definir un método

juan.mandar_email("juan@gmail.com") # No ponemos urgente, era parámetro opcional
