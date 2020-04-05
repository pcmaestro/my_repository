from PyQt5.QtWidgets import QDialog, QApplication
from ventanas import ventana
import sys


class AppHeladosyBebidas(QDialog):
    
    def __init__(self):
        super().__init__()
        self.ui = ventana.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.chk_chocolate.stateChanged.connect(self.calcular_total)
        self.ui.chk_vainilla.stateChanged.connect(self.calcular_total)
        self.ui.chk_oreo.stateChanged.connect(self.calcular_total)
        self.ui.chk_limon.stateChanged.connect(self.calcular_total)
        self.ui.chk_frambuesa.stateChanged.connect(self.calcular_total)
        self.ui.chk_coca_cola.stateChanged.connect(self.calcular_total)
        self.ui.chk_fanta_naranja.stateChanged.connect(self.calcular_total)
        self.ui.chk_fanta_limon.stateChanged.connect(self.calcular_total)
        self.show()
        
    def calcular_total(self):
        
        precio_final = 0.0
        
        if self.ui.chk_chocolate.isChecked():            
            precio_final += 1.5
        if self.ui.chk_vainilla.isChecked():
            precio_final += 1.5
        if self.ui.chk_oreo.isChecked():
            precio_final += 2
        if self.ui.chk_limon.isChecked():
            precio_final += 1
        if self.ui.chk_frambuesa.isChecked():
            precio_final += 1
        if self.ui.chk_coca_cola.isChecked():
            precio_final += 2
        if self.ui.chk_fanta_naranja.isChecked():
            precio_final += 2
        if self.ui.chk_fanta_limon.isChecked():
            precio_final += 2
        
        self.ui.txt_show.setText("El precio final es " + str(precio_final))


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    ventana_venta = AppHeladosyBebidas()
    
    ventana_venta.show()
    
    sys.exit(app.exec_())