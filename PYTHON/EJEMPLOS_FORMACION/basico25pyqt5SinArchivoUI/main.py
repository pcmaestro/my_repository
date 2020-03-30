import sys
from PyQt5.QtWidgets import QWidget, QApplication

#import otro
#print(__name__) # variable global que indica dependiendo de donde esté
                # 1) si está en el archivo de python desde el que arrancamos
                #    la variable _name_ vale "__main__"
                
                # 2) si está en otro archivo que hayamos importado 
                #    la variable _name_ vale el nombre de dicho archivo o modulo de pyhton
                
if __name__ == "__main__":
    app = QApplication([])#creo la aplicacion de pyqt5
    
    w = QWidget() #objeto de la clase Qwidget que representa una ventana
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle("Ventana creada sin designer")
    w.show()
    
    sys.exit(app.exec_())


