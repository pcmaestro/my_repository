from ventanas import ventana_table_widget_revistas
from modelo import operaciones_bd
from PyQt5.Qt import QTableWidgetItem, QPushButton, QLabel, QPixmap, QMessageBox
from _functools import partial
import pathlib



class VentanaListadoTableWidget(ventana_table_widget_revistas.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
    
    def borrar_revista(self,id):
        pass

    def editar_revista(self,id):
        pass
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        revistas = operaciones_bd.obtener_revistas()
        fila = 0
        for r in revistas:
            self.table_widget_revistas.insertRow(fila)
            indice_celda = 0
            for valor in r:
                celda = QTableWidgetItem(str(valor))
                self.table_widget_revistas.setItem(fila,indice_celda,celda)
                indice_celda += 1
            #agregar el boton borrar a la fila
            boton_borrar = QPushButton("borrar")
            boton_borrar.clicked.connect(partial(self.borrar_revista,r[0]))#con partial se ejecutara borrar_revista con el id indicado por r[0]
            self.table_widget_revistas.setCellWidget(fila,indice_celda,boton_borrar)
            #agregar boton editar a la fila
            boton_editar = QPushButton("editar")
            boton_editar.clicked.connect(partial(self.editar_revista,r[0]))
            self.table_widget_revistas.setCellWidget(fila,indice_celda + 1,boton_editar)
            
            #icono de la imagen
            icono = QLabel()
            ruta_imagen = "imagenes/"+str(r[0])+".jpg"
            objeto_path = pathlib.Path(ruta_imagen)
            existe = objeto_path.is_file()
            if existe:           
                pixmap = QPixmap(ruta_imagen)
                pixmap_redim = pixmap.scaledToHeight(50)
                icono.setPixmap(pixmap_redim)
                self.table_widget_revistas.setCellWidget(fila,indice_celda + 2,icono)
            
            fila += 1