from ventanas import ventana_principal
from clases_ventanas.clase_registrar_revista import VentanaRegistrarRevista
from clases_ventanas.clase_listado_table_widget import VentanaListadoTableWidget

class VentanaPrincipal(ventana_principal.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        #y ahora yo preparo todo lo que quiera
        #programaria las opciones de menu, los botones etc..
        self.submenu_registrar_revista.triggered.connect(self.mostrar_registro_revista)
        self.submenu_table_widget_revistas.triggered.connect(self.mostrar_listado_con_table_widget)
        self.MainWindow = MainWindow
        
    def mostrar_registro_revista(self):
        self.ventanaRegistro = VentanaRegistrarRevista()
        self.ventanaRegistro.setupUi(self.MainWindow)
    
    def mostrar_listado_con_table_widget(self):
        self.ventanaListado = VentanaListadoTableWidget()
        self.ventanaListado.setupUi(self.MainWindow)
        
        
        
        