
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal, registro_revista, listado_revistas,\
    ventana_list_widget_revistas, ventana_table_widget_revistas,\
    ventana_editar_revista
from modelo.clases import Revista

import sys
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QTableWidgetItem, QPushButton, QFileDialog,\
    QPixmap, QLabel
from modelo.operaciones_bd import obtener_revistas
from _functools import partial
import shutil
import pathlib
from validadores import validacion_revista
from clases_ventanas import clase_ventana_principal

#variable global
revistas = None

#aqui no voy a poner ninguna funcion 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    objeto_ventana_principal = clase_ventana_principal.VentanaPrincipal()
    objeto_ventana_principal.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())