
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal, registro_revista, listado_revistas,\
    ventana_list_widget_revistas, ventana_table_widget_revistas,\
    ventana_editar_revista
from modelo.clases import Revista

import sys
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QTableWidgetItem, QPushButton
from modelo.operaciones_bd import obtener_revistas
from _functools import partial

#variable global
revistas = None

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

def mostrar_listado_list_widget_revistas():
    global revistas
    ui_listado_revistas_list_widget.setupUi(MainWindow)
    revistas = obtener_revistas()
    for r in revistas:
        print(r)
        ui_listado_revistas_list_widget.list_widget_revistas.addItem( str(r[1]) + " precio: " + str(r[2]) )
    ui_listado_revistas_list_widget.list_widget_revistas.itemClicked.connect(ver_detalles_revista)    
    
def ver_detalles_revista():
    indice_seleccionado = ui_listado_revistas_list_widget.list_widget_revistas.currentRow()
    revista = revistas[indice_seleccionado]
    texto = ""
    texto += "titulo: " + str(revista[1]) + "\n"
    texto += "precio: " + str(revista[2]) + "\n"
    texto += "tema: " + str(revista[3]) + "\n"
    
    QMessageBox.about(MainWindow,"Info",texto)

def mostrar_table_widget_revistas():
    ui_listado_revistas_table_widget.setupUi(MainWindow)
    revistas = operaciones_bd.obtener_revistas()
    fila = 0    
    for r in revistas:
        ui_listado_revistas_table_widget.table_widget_revistas.insertRow(fila)
        
        indice_celda = 0
        for valor in r:
            celda = QTableWidgetItem(str(valor))
            ui_listado_revistas_table_widget.table_widget_revistas.setItem(fila,indice_celda,celda)
            indice_celda += 1
        #agregar el boton borrar a la fila
        boton_borrar = QPushButton("borrar")
        boton_borrar.clicked.connect(partial(borrar_revista,r[0]))#con partial se ejecutara borrar_revista con el id indicado por r[0]
        ui_listado_revistas_table_widget.table_widget_revistas.setCellWidget(fila,indice_celda,boton_borrar)
        #agregar boton editar a la fila
        boton_editar = QPushButton("editar")
        boton_editar.clicked.connect(partial(editar_revista,r[0]))
        ui_listado_revistas_table_widget.table_widget_revistas.setCellWidget(fila,indice_celda + 1,boton_editar)
        
        fila += 1
        
def borrar_revista(id_a_borrar):

    res = QMessageBox.question(MainWindow,"Alerta","Vas a borrar un registro de id: " + str(id_a_borrar))
    if res == QMessageBox.Yes:
        #necesito saber que revista ha seleccionado que se borre
        operaciones_bd.borrar_revista(id_a_borrar)
        mostrar_table_widget_revistas()

def editar_revista(id_a_editar):
    QMessageBox.about(MainWindow,"Info","vas a editar el id: " + str(id_a_editar))
    ui_editar_revista.setupUi(MainWindow)
    revista_a_editar = operaciones_bd.obtener_revista_por_id(id_a_editar)
    ui_editar_revista.entrada_titulo.setText(revista_a_editar.titulo)
    ui_editar_revista.entrada_precio.setText(str(revista_a_editar.precio))
    ui_editar_revista.entrada_tema.setText(revista_a_editar.tema)
    
    ui_editar_revista.boton_guardar_cambios_revista.clicked.connect(partial(guardar_cambios_revista,revista_a_editar.id))
    
def guardar_cambios_revista(id_a_guardarCambios):
    QMessageBox.about(MainWindow,"Info","guardando cambios sobre el registro id: " + str(id_a_guardarCambios))
    revista_a_guardar_Cambios = Revista()
    revista_a_guardar_Cambios.id = id_a_guardarCambios
    revista_a_guardar_Cambios.titulo = ui_editar_revista.entrada_titulo.text()
    revista_a_guardar_Cambios.precio = ui_editar_revista.entrada_precio.text()
    revista_a_guardar_Cambios.tema = ui_editar_revista.entrada_tema.text()
    operaciones_bd.guardar_cambios_revista(revista_a_guardar_Cambios)
    mostrar_table_widget_revistas()
    
#arranque de la aplicacion principal
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

#creo los interfaces
ui_principal = ventana_principal.Ui_MainWindow()
ui_registro_revista = registro_revista.Ui_MainWindow()
ui_listado_revistas = listado_revistas.Ui_MainWindow()
ui_listado_revistas_list_widget = ventana_list_widget_revistas.Ui_MainWindow()
ui_listado_revistas_table_widget = ventana_table_widget_revistas.Ui_MainWindow()
ui_editar_revista = ventana_editar_revista.Ui_MainWindow()
ui_principal.setupUi(MainWindow)

#preparar submenus
ui_principal.submenu_registrar_revista.triggered.connect(mostrar_registro_revista)
ui_principal.submenu_listar_revistas.triggered.connect(mostrar_listado_revistas)
ui_principal.submenu_list_widget_revistas.triggered.connect(mostrar_listado_list_widget_revistas)
ui_principal.submenu_table_widget_revistas.triggered.connect(mostrar_table_widget_revistas)

#mostrar ventana y cerrar aplicacion cuando se cierre
MainWindow.show()
sys.exit(app.exec_())