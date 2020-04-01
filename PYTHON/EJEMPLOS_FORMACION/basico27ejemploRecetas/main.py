#Creación de ventanas mediante la creación de una clase

from PyQt5.Qt import QDialog, QApplication 
import sys

#Aqui importamos el módulo donde está el archivo creado en pyqt5
from ventana_ejemplo import *

#Creamos la clase en cuestión
class EjemploAplicacion(QDialog):     
    def __init__(self):    
        #Aqui traemos el constructor de la clase padre QDialog()     
        super().__init__()         
        print("se ejecuja el constructor de la clase EjemploAplicacion")   
        #Instanciamos un objeto de la clase Ui_Ejemplo_Uso_GUI() creada en ventana_ejemplo    
        self.ejemplo = Ui_Ejemplo_Uso_GUI()
        #Y a dicho objeto le ejecutamos el método setupUI() de la clase Ui_Ejemplo_Uso_GUI() para dar formato
        self.ejemplo.setupUi(self)      
        #Y ahota idicamos el método que se ejecutará en el evento de clickar el botón de la ventana    
        self.ejemplo.btn_pulsame.clicked.connect(self.boton_pulsado)      
        #Finalmente, mostramos la ventana   
        self.show()          
        
    def boton_pulsado(self):   
        #Acción al pulsar en el botón, en este caso mostrar un texto en el label lbl_pulsar_boton
        self.ejemplo.lbl_pulsar_boton.setText("gracias")          

#Comprobamos que estamos arrancando en el módulo principal de la ventana    
if __name__ == "__main__":     
    
    #Arrancamos el proceos de PyQt5, le pasamos como argumentos el array que guarda lo que vamos
    #tecleando en el interprete de Python
    app = QApplication(sys.argv)
    #Instanciamos un objeto de la clase que hemos creado para ejecutar la ventana
    aplicacion = EjemploAplicacion()   
    #Indicamos al sistema que mantenga abierta la ventana mientras se ejecuta el proceso de PyQt5
    sys.exit(app.exec_()) 