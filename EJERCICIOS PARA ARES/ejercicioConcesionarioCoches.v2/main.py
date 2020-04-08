from PyQt5 import QtWidgets  
from ventanas import ventana_tablewidget, ventana_principal, ventana_registro, ventana_listwidget, ventana_listado,\
    ventana_edicion
from clases.clases import Coche
import sys
from modelo.operaciones_bd import obtener_coches, borrar_coche,\
    guardar_cambios_coche ,obtener_coche_por_id, registro_coche
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton, QMessageBox
from _functools import partial

#Variable global
coches = None

#metodos de la ventana de registro:
def registrar_coche():
    
    coche = Coche()    
    coche.marca = ui_registro_coche.txt_marca.text()
    coche.modelo = ui_registro_coche.txt_modelo.text()
    coche.color = ui_registro_coche.txt_color.text()
    coche.motor = ui_registro_coche.txt_motor.text()
    coche.precio = float(ui_registro_coche.txt_precio.text())    
    
    #falta validarla y dar errores
    registro_coche(coche)
    #limpio los controles
    ui_registro_coche.txt_marca.setText("")
    ui_registro_coche.txt_modelo.setText("")
    ui_registro_coche.txt_color.setText("")
    ui_registro_coche.txt_motor.setText("")
    ui_registro_coche.txt_precio.setText("")   
    
    
    #indicamos registro ok al usuario
    QMessageBox.about(MainWindow,"Info","Registro coche OK")

#metodos del submenu
def mostrar_registro_coche():
    ui_registro_coche.setupUi(MainWindow)
    ui_registro_coche.btn_registrar.clicked.connect(registrar_coche)

def mostrar_listado_coches():
    ui_listado_coches.setupUi(MainWindow)
    ui_listado_coches.btn_listar.clicked.connect(listado)
    
def mostrar_list_widget():
    ui_listado_list_widget.setupUi(MainWindow)
    ui_listado_list_widget.btn_listar.clicked.connect(listado_list_widget)
    
def mostrar_table_widget():
    ui_listado_list_tablewidget.setupUi(MainWindow)
    ui_listado_list_tablewidget.btn_listar_tabla.clicked.connect(listado_table_widget)
    
def listado():
    coches = obtener_coches()
    texto = "id\tMarca\t\Modelo\tColor\tMotor\tPrecio\n\n"
    for c in coches:
        texto += ( str(c[0]) + "\t" + c[1] + "\t" + str(c[2]) + "\t" + str(c[3]) + 
                  "\t" + str(c[4]) + "\t" + str(c[5]) +"\n")
    ui_listado_coches.text_show.setText(texto)
    
def listado_list_widget():
    global coches    
    coches = obtener_coches()
    print(coches)
    for coche in coches:        
        ui_listado_list_widget.listWidget.addItem("Marca : " + str(coche[1]) +
                                                  "  Modelo : " + str(coche[2]) +
                                                  "  Color : " + str(coche[3]) +
                                                  "  Motor : " + str(coche[4]) +
                                                  "  Precio : " + str(coche[5]) ) 
        
def listado_table_widget():
    global coches
    coches = obtener_coches()
    fila = 0
    for coche in coches:        
        ui_listado_list_tablewidget.tableWidget.insertRow(fila)
        columna = 0        
        for propiedad in coche:
            celda = QTableWidgetItem(str(propiedad))
            ui_listado_list_tablewidget.tableWidget.setItem(fila, columna, celda)
            columna += 1
          
        btn_eliminar = QPushButton("Eliminar coche")
        btn_eliminar.clicked.connect( partial(eliminar_coche, coche[0]) )
        ui_listado_list_tablewidget.tableWidget.setCellWidget(fila, columna, btn_eliminar)
        
        btn_editar = QPushButton("Editar coche")
        btn_editar.clicked.connect( partial(editar_coche, coche[0]) )
        ui_listado_list_tablewidget.tableWidget.setCellWidget(fila, columna +1, btn_editar)
             
        fila += 1
                                                                                            
def eliminar_coche(id_coche):    
    aviso = QMessageBox.question(MainWindow,"Alerta", "Atención, vas eliminar el registro " + str(id_coche))
    if aviso == QMessageBox.Yes:        
        borrar_coche(id_coche)
        mostrar_table_widget()

def editar_coche(id_coche):
    print("LLego a editar_coche() y el id_coche es " + str(id_coche))
    QMessageBox.about(MainWindow, "Alerta" , "Vas a editar el registro " + str(id_coche))
    ui_editar_coche.setupUi(MainWindow)
    coche_modificado = obtener_coche_por_id(id_coche)
    ui_editar_coche.txt_marca.setText(str(coche_modificado.marca))
    ui_editar_coche.txt_modelo.setText(str(coche_modificado.modelo))
    ui_editar_coche.txt_color.setText(str(coche_modificado.color))
    ui_editar_coche.txt_motor.setText(str(coche_modificado.motor))
    ui_editar_coche.txt_precio.setText(str(coche_modificado.precio))
    ui_editar_coche.btn_modificar.clicked.connect( partial(guardar_coche_modificado, id_coche))

def guardar_coche_modificado(id_coche):
    QMessageBox.about(MainWindow, "Aviso", "Se va a modificar el coche con id " + str(id_coche))
    cambios_ptes_guardar = Coche()
    print("objeto cambios_ptes_guardar creado")
    cambios_ptes_guardar.__str__()
    cambios_ptes_guardar.id = id_coche
    print("Creada instancia cambios_ptes_guardar, el id es " + str(cambios_ptes_guardar.id))
    cambios_ptes_guardar.marca = ui_editar_coche.txt_marca.text()
    cambios_ptes_guardar.modelo = ui_editar_coche.txt_modelo.text()
    cambios_ptes_guardar.color = ui_editar_coche.txt_color.text()
    cambios_ptes_guardar.motor = ui_editar_coche.txt_motor.text()
    cambios_ptes_guardar.precio = ui_editar_coche.txt_precio.text()
    guardar_cambios_coche(cambios_ptes_guardar)
    mostrar_table_widget()
    
    
    
#arranque de la aplicacion principal
if __name__ == "__main__":    
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    #creo los interfaces
    ui_principal = ventana_principal.Ui_MainWindow()
    ui_registro_coche = ventana_registro.Ui_MainWindow()
    ui_listado_coches = ventana_listado.Ui_MainWindow()
    ui_listado_list_widget = ventana_listwidget.Ui_MainWindow()
    ui_listado_list_tablewidget = ventana_tablewidget.Ui_MainWindow()
    ui_editar_coche = ventana_edicion.Ui_MainWindow()
    ui_principal.setupUi(MainWindow)    
    
    #preparar submenus    
    ui_principal.actionRegistrar_coche.triggered.connect(mostrar_registro_coche)
    ui_principal.actionListar_coches.triggered.connect(mostrar_listado_coches)
    ui_principal.actionLista_con_list_widget.triggered.connect(mostrar_list_widget)
    ui_principal.actionlistar_con_table_widget.triggered.connect(mostrar_table_widget)
    
    #mostrar ventana y cerrar aplicacion cuando se cierre
    MainWindow.show()
    sys.exit(app.exec_())
