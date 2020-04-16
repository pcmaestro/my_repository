from ventanas import registro_revista
from PyQt5.Qt import QFileDialog, QPixmap
import shutil

class VentanaRegistrarRevista(registro_revista.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        #preparo los botones de la ventana
        self.boton_seleccionar_imagen.clicked.connect(self.seleccionar_imagen)
        self.MainWindow = MainWindow
        
    def seleccionar_imagen(self):
        archivo = QFileDialog.getOpenFileName(self.MainWindow)
        print(archivo)
        ruta_archivo = archivo[0]
        shutil.copy(ruta_archivo,"temporal/imagen.jpg")
        pixmap = QPixmap("temporal/imagen.jpg")
        alto_label = self.label_imagen.height()
        pixmap_redim = pixmap.scaledToHeight(alto_label)
        #redimensiono el pixmap no la imagen
        self.label_imagen.setPixmap(pixmap_redim)