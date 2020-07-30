from PyQt5.QtWidgets import QDialog, QApplication

import sys

from ventanas.ventana import Ui_dialogWindow

class ElegirVuelo(QDialog):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_dialogWindow()
        self.ui.setupUi(self)
        self.ui.btn_radio_economica.toggled.connect(self.funcion_economica)
        self.ui.btn_radio_negocios.toggled.connect(self.funcion_negocios)
        self.ui.btn_radio_primera.toggled.connect(self.funcion_primera)       
        self.show()
        
    def funcion_economica(self):
        self.ui.lbl_textToShow.setText("Has seleccionado clase económica, 99 €")
        
    def funcion_negocios(self):
        self.ui.lbl_textToShow.setText("Has seleccionado clase negocios, 130 €")  
        
    def funcion_primera(self):
        self.ui.lbl_textToShow.setText("Has seleccionado clase primera, 190 €")

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    ventanaVuelos = ElegirVuelo()
    
    sys.exit(app.exec_())