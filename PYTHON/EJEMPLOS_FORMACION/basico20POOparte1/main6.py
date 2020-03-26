class Jugador():
    nombre = ""
    puntos = 0    

    def __init__(self, nombre, puntos):
        #ESte código dentro del constructor se va a ejecutar cada vez que se cree
        #un objeto de esta clase
        print("Se ejecuta el constructor de jugador")
        self.nombre = nombre
        self.puntos = puntos    
    
    #Vamos a definir un bloque de código que puedan ejecutar los objetos de Jugador()
    def borrar(self):
        print("Voy a borrar " + self.nombre)
    
    def mandar_email(self, email, urgente = False): ## El False hace el parametro urgente opcional
        print("mandar a : " + self.nombre)
        print("el siguiente email : " + email)
        print("urgente : " + str(urgente))
#end class

#Si queremos crear una clase que sea igual que Jugador(), pero con algo más (nunca algo menos)
#o algún método cambiado , lo suyo es usar herencia

class JugadorVip(Jugador): # Ahora mismo JugadorVip() , esta clase tiene tódo el código de Jugador()
    dinero = 10
    
    #Yo puedo agregar nuevos métodos para JugadorVip(), o pisar los que llegan por herencia
    #a esto último se le llama polimorfismo o sobreescritura de métodos
    def mandar_email(self, email, urgente=False):
        print("mandar e-mail a jugador vip " + self.nombre)
    
#end class

ana = Jugador("Ana Maria", 499)

sofia = JugadorVip("Sofia", 500)

ana.mandar_email("ana@gmail.com", urgente = True)

sofia.mandar_email("sofia@gmail.com")

print("dinero de Sofia : " + str(sofia.dinero))
print("dinero de Ana : " + str(ana.dinero))
