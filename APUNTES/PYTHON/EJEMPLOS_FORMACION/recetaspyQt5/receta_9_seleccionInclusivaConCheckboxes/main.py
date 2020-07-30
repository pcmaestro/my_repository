import sys

from PyQt5.QtWidgets import QApplication, QDialog

from ventanas import ventana_principal


class AplicacionPizza(QDialog):
    
    def __init__(self):
        super().__init__()
        self.ui = ventana_principal.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.chk_queso.stateChanged.connect(self.precio_pizza)
        self.ui.chk_aceitunas.stateChanged.connect(self.precio_pizza)
        self.ui.chk_salsa.stateChanged.connect(self.precio_pizza)
        
    def precio_pizza(self):
        
        precioPizza = 15
        
        if self.ui.chk_aceitunas.isChecked() == True:
            precioPizza += 2
        if self.ui.chk_queso.isCheckable() == True:
            precioPizza += 3
        if self.ui.chk_salsa.isChecked() == True:
            precioPizza += 2
            
        self.ui.text_show.setText("El precio final es {}".format(precioPizza))
            
        
        
        
if __name__ == "__main__" :

    app = QApplication(sys.argv)
    
    venta_pizza = AplicacionPizza()
    
    venta_pizza.show()
    
    sys.exit(app.exec_())