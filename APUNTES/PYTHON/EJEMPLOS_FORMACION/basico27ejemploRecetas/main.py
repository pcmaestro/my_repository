from PyQt5.Qt import QDialog, QApplication
import sys
import ventana_ejemplo

class EjemploAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        print("se ejecuja el constructor de la clase EjemploAplicacion")
        self.ejemplo = ventana_ejemplo.Ui_Ejemplo_Uso_GUI()
        self.ejemplo.setupUi(self)        
        self.ejemplo.btn_pulsame.clicked.connect(self.boton_pulsado)
        self.show()
    
    def boton_pulsado(self):
        self.ejemplo.lbl_pulsar_boton.setText("gracias")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    aplicacion = EjemploAplicacion()
    sys.exit(app.exec_())
