from PyQt5.QtWidgets import QApplication, QDialog

import sys

from ventanas import ventana

class Ventana_dialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ventana.Ui_dialogo()
        self.ui.setupUi(self)
        self.ui.btn.clicked.connect(self.boton_pulsado)
        self.show()
        
    def boton_pulsado(self):        
        input_usuario = self.ui.lbl_textbox.text()        
        self.ui.lbl_saludo.setText("HOLA, " + input_usuario)
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    window = Ventana_dialogo()
    
    sys.exit(app.exec_())