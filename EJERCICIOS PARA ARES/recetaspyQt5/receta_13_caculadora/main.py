from PyQt5.QtWidgets import QDialog, QApplication
import sys
from ventanas import ventana

class Calculadora(QDialog):
    
    def __init__(self):
        super().__init__()
        self.ui = ventana.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn_sumar.clicked.connect(self.func_sumar)
        self.ui.btn_restar.clicked.connect(self.func_restar)
        self.ui.btn_multiplicar.clicked.connect(self.func_multiplicar)
        self.ui.btn_dividir.clicked.connect(self.func_dividir)
        self.show()
    
    def func_sumar(self):
        primer_numero = 0
        segundo_numero = 0
        resultado_suma = 0
        
        if len(self.ui.num1.text()) > 0 and len(self.ui.num2.text()) > 0:
            primer_numero = int(self.ui.num1.text())
            segundo_numero = int(self.ui.num2.text())
            resultado_suma = primer_numero + segundo_numero
            self.ui.resultado.setText("El resultado es " + str(resultado_suma))        
        

    def func_restar(self):
        primer_numero = 0
        segundo_numero = 0
        resultado_resta = 0
        
        if len(self.ui.num1.text()) > 0 and len(self.ui.num2.text()) > 0:
            primer_numero = int(self.ui.num1.text())
            segundo_numero = int(self.ui.num2.text())
            resultado_resta = primer_numero - segundo_numero
            self.ui.resultado.setText("El resultado es " + str(resultado_resta)) 
    
    def func_multiplicar(self):
        primer_numero = 0
        segundo_numero = 0
        resultado_multiplicar = 0
        
        if len(self.ui.num1.text()) > 0 and len(self.ui.num2.text()) > 0:
            primer_numero = int(self.ui.num1.text())
            segundo_numero = int(self.ui.num2.text())
            resultado_multiplicar = primer_numero * segundo_numero
            self.ui.resultado.setText("El resultado es " + str(resultado_multiplicar)) 
    
    def func_dividir(self):
        primer_numero = 0
        segundo_numero = 0
        resultado_division = 0
        
        if len(self.ui.num1.text()) > 0 and len(self.ui.num2.text()) > 0:
            primer_numero = float(self.ui.num1.text())
            segundo_numero = float(self.ui.num2.text())
            resultado_division = primer_numero / segundo_numero
            self.ui.resultado.setText("El resultado es " + str(resultado_division)) 
    
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    calculadora = Calculadora()
    
    calculadora.show()
    
    sys.exit(app.exec_())
        