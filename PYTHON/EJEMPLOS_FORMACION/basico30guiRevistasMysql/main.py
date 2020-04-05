
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal, registro_revista, listado_revistas
from modelo.clases import Revista

import sys
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox
from modelo.operaciones_bd import obtener_revistas

#metodos de la ventana de registro:
def registrar_revista():
    revista = Revista()
    revista.titulo = ui_registro_revista.entrada_titulo.text()
    revista.precio = float(ui_registro_revista.entrada_precio.text())
    revista.tema = ui_registro_revista.entrada_tema.text()
    #falta validarla y dar errores
    operaciones_bd.registro_revista(revista)
    #limpio los controles
    ui_registro_revista.entrada_titulo.setText("")
    ui_registro_revista.entrada_precio.setText("")
    ui_registro_revista.entrada_tema.setText("")
    #indicamos registro ok al usuario
    QMessageBox.about(MainWindow,"Info","Registro revista OK")

#metodos del submenu
def mostrar_registro_revista():
    ui_registro_revista.setupUi(MainWindow)
    ui_registro_revista.boton_registrar_revista.clicked.connect(registrar_revista)

def mostrar_listado_revistas():
    ui_listado_revistas.setupUi(MainWindow)
    revistas = obtener_revistas()
    texto = ""
    for r in revistas:
        texto += "id: " + str(r[0]) + " datos: " + r[1] + " " + str(r[2]) + " " + r[3] + "\n"
    ui_listado_revistas.listado_revistas.setText(texto)

#arranque de la aplicacion principal
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

#creo los interfaces
ui_principal = ventana_principal.Ui_MainWindow()
ui_registro_revista = registro_revista.Ui_MainWindow()
ui_listado_revistas = listado_revistas.Ui_MainWindow()
ui_principal.setupUi(MainWindow)

#preparar submenus
ui_principal.submenu_registrar_revista.triggered.connect(mostrar_registro_revista)
ui_principal.submenu_listar_revistas.triggered.connect(mostrar_listado_revistas)

#mostrar ventana y cerrar aplicacion cuando se cierre
MainWindow.show()
sys.exit(app.exec_())