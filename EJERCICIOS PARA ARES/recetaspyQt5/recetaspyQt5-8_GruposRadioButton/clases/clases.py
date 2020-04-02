from PyQt5.QtWidgets import QDialog

from ventanas.ventana import Ui_ventanaDialogo

class ventanaDialogo(QDialog):
    
    def __init__(self):
        
        super().__init__()
        self.ui = Ui_ventanaDialogo()
        self.ui.setupUi(self)
        self.ui.btn_radio_M.toggled.connect(self.func_mostrar)
        self.ui.btn_radio_L.toggled.connect(self.func_mostrar)
        self.ui.btn_radio_XL.toggled.connect(self.func_mostrar)
        self.ui.btn_radio_XXL.toggled.connect(self.func_mostrar)
        self.ui.btn_pagoTarjeta.toggled.connect(self.func_mostrar)
        self.ui.btn_pagoContado.toggled.connect(self.func_mostrar)
        self.ui.btn_pagoMovil.toggled.connect(self.func_mostrar)        
        self.show()
        
    def func_mostrar(self):
        
        self.talla = ""
        
        if self.ui.btn_radio_M.isChecked():
            self.talla = "M"
        elif self.ui.btn_radio_L.isChecked():
            self.talla = "L"
        elif self.ui.btn_radio_XL.isChecked():
            self.talla = "XL"
        elif self.ui.btn_radio_XXL.isChecked():
            self.talla = "XXL"

        self.pago = ""
        
        if self.ui.btn_pagoTarjeta.isChecked():
            self.pago = "Tarjeta"
        elif self.ui.btn_pagoContado.isChecked():
            self.pago = "Contado"
        elif self.ui.btn_pagoMovil.isChecked():
            self.pago = "Móvil NFS"
            
        self.mostrar = "Talla : {}\nForma de Pago : {}".format(self.talla, self.pago)
        
        self.ui.lbl_textToShow.setText(self.mostrar)
        
    
        
#End class ventanaDialogo        
        