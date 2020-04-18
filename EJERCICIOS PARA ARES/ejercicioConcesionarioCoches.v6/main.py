from PyQt5 import QtWidgets  
from ventanas import ventana_tablewidget, ventana_principal, ventana_registro, ventana_listwidget, ventana_listado,\
    ventana_edicion, ventana_asistente
from clases.clases import Coche
import sys
from validadores import func_validacion
from modelo.operaciones_bd import obtener_coches, borrar_coche,\
    guardar_cambios_coche ,obtener_coche_por_id, registro_coche,\
    id_ultimo_registro
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton, QMessageBox,\
    QFileDialog, QLabel
from _functools import partial
from PyQt5.QtGui import QPixmap
import shutil
import os


#Variable global
coches = None

#metodos de la ventana de registro:
def registrar_coche():
    
    coche = Coche()    
    #Validación previa
    cocheOK = True
    coche.marca = ui_registro_coche.txt_marca.text()        
    if not func_validacion.validar_marca(coche.marca):
        ui_registro_coche.lbl_marca_ko.setText("Marca KO")   
        cocheOK = False
    else:
        ui_registro_coche.lbl_marca_ko.clear()         
        
    coche.modelo = ui_registro_coche.txt_modelo.text() 
    if not func_validacion.validar_modelo(coche.modelo):
        ui_registro_coche.lbl_modelo_ko.setText("Modelo KO")
        cocheOK = False
    else:
        ui_registro_coche.lbl_modelo_ko.clear()
        
    coche.color = ui_registro_coche.txt_color.text()    
    if not func_validacion.validar_color(coche.color):
        ui_registro_coche.lbl_color_ko.setText("Color KO")
        cocheOK = False
    else:
        ui_registro_coche.lbl_color_ko.clear()
    
    coche.motor = ui_registro_coche.txt_motor.text()    
    if not func_validacion.validar_motor(coche.motor):
        ui_registro_coche.lbl_motor_ko.setText("Motor KO")
        cocheOK = False
    else:
        ui_registro_coche.lbl_motor_ko.clear()
    
    coche.precio = str(ui_registro_coche.txt_precio.text())    
    if not func_validacion.validar_precio(coche.precio):
        ui_registro_coche.lbl_precio_ko.setText("Precio KO")
        cocheOK = False
    else:
        ui_registro_coche.lbl_precio_ko.clear()   
        
    coche.forma_pago = ui_registro_coche.txt_forma_pago.text()    
    if not func_validacion.validar_forma_pago(coche.forma_pago):
        ui_registro_coche.lbl_forma_pago_ko.setText("Forma pago KO")
        cocheOK = False
    else:
        ui_registro_coche.lbl_forma_pago_ko.clear()      
    
    if cocheOK == False:
        return
    
    #Envio a la base de datos
    registro_coche(coche)
    #limpio los controles
    ui_registro_coche.txt_marca.setText("")
    ui_registro_coche.txt_modelo.setText("")
    ui_registro_coche.txt_color.setText("")
    ui_registro_coche.txt_motor.setText("")
    ui_registro_coche.txt_precio.setText("")         
    ui_registro_coche.txt_forma_pago.setText("")
    #indicamos registro ok al usuario
    QMessageBox.about(MainWindow,"Info","Registro coche OK")
    
def registrar_asistente_coche():
    
    coche = Coche()    

    index_marca = ui_asistente.cbx_marca.currentIndex()
    coche.marca = ui_asistente.cbx_marca.itemText(index_marca)
    if coche.marca == "--------- elegir ---------":
        ui_asistente.lbl_marca_ko.setText("Debes elegir una marca")
    coche.modelo = ui_asistente.txt_modelo.text()
    if not func_validacion.validar_modelo(coche.modelo):
        ui_asistente.lbl_modelo_ko.setText("Modelo incorrecto")
        return
    else:
        ui_asistente.lbl_modelo_ko.clear()    
    index_color = ui_asistente.cbx_color.currentIndex()
    coche.color = ui_asistente.cbx_color.itemText(index_color)
    if coche.color == "--------- elegir ---------":
        ui_asistente.lbl_color_ko.setText("Debes elegir un color")
    if ui_asistente.radio_diesel.isChecked():
        coche.motor = "diesel"
    if ui_asistente.radio_gasolina.isChecked():
        coche.motor = "gasolina"    
    coche.precio = ui_asistente.spx_precio.value()    
    if ui_asistente.chx_cheque.isChecked():
        coche.forma_pago = "cheque"
    if ui_asistente.chx_contado.isChecked():
        coche.forma_pago = "contado"
    if ui_asistente.chx_financiado.isChecked():
        coche.forma_pago = "financiado"
    if ui_asistente.chx_tarjeta.isChecked():
        coche.forma_pago = "tarjeta"    
    
    registro_coche(coche)
    #Reseteo de valores
    ui_asistente.txt_modelo.clear()
    ui_asistente.spx_precio.setValue(90000)
    #indicamos registro ok al usuario
    QMessageBox.about(MainWindow,"Info","Registro coche OK")
    id_registrado = id_ultimo_registro()
    shutil.move("temp/imagen.jpg", "imagenes/" + str(id_registrado[0]) + ".jpg")
    
def insertar_imagen():
        
        archivo = QFileDialog.getOpenFileName(MainWindow)
        shutil.copy(archivo[0], "temp/imagen.jpg")    
        
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
    
def mostrar_asistente():
    ui_asistente.setupUi(MainWindow)
    ui_asistente.btn_insertar.clicked.connect(insertar_imagen)    
    ui_asistente.btn_registrar.clicked.connect(registrar_asistente_coche)
    
def listado():
    coches = obtener_coches()
    texto = "id\tMarca\tModelo\tColor\tMotor\tPrecio\tForma de pago\n\n"
    for c in coches:
        texto += ( str(c[0]) + "\t" + c[1] + "\t" + str(c[2]) + "\t" + str(c[3]) + 
                  "\t" + str(c[4]) + "\t" + str(round(c[5])) + "\t" + str(c[6]) + "\n")
    ui_listado_coches.text_show.setText(texto)
    
def listado_list_widget():
    global coches    
    ui_listado_list_widget.listWidget.clear()
    coches = obtener_coches()
    ui_listado_list_widget.listWidget.addItem("Marca\t\tModelo\t\tColor\t\tMotor\t\tPrecio\t\tForma de pago")
    ui_listado_list_widget.listWidget.addItem("___________________________________________________________________________________________________________________________________\n")
    for coche in coches:        
        ui_listado_list_widget.listWidget.addItem(str(coche[1]) + "\t\t" +
                                                  str(coche[2]) + "\t\t" +
                                                  str(coche[3]) + "\t\t" +
                                                  str(coche[4]) + "\t\t" +
                                                  str(round(coche[5])) + "\t\t" +
                                                  str(coche[6])          ) 
        
def listado_table_widget():
    global coches    
    ui_listado_list_tablewidget.tableWidget.setRowCount(0)
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
        #icono de la imagen
        icono = QLabel()
        ruta_imagen = "imagenes/"+str(coche[0])+".jpg"
        print(ruta_imagen)
        objeto_path = os.path.isfile(ruta_imagen)    
        print(objeto_path)    
        if objeto_path:           
            pixmap = QPixmap(ruta_imagen)            
            icono.setPixmap(pixmap)
            ui_listado_list_tablewidget.tableWidget.setCellWidget(fila, columna + 2, icono)
        fila += 1
                                                                                            
def eliminar_coche(id_coche):    
    aviso = QMessageBox.question(MainWindow,"Alerta", "Atención, vas eliminar el registro " + str(id_coche))
    if aviso == QMessageBox.Yes:        
        borrar_coche(id_coche)
        mostrar_table_widget()
        listado_table_widget()

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
    ui_editar_coche.txt_forma_pago.setText(str(coche_modificado.forma_pago))
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
    cambios_ptes_guardar.forma_pago = ui_editar_coche.txt_forma_pago.text()
    guardar_cambios_coche(cambios_ptes_guardar)
    mostrar_table_widget()  

def cerrar_aplicacion():
    sys.exit(0)
    
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
    ui_asistente = ventana_asistente.Ui_MainWindow()      
    ui_principal.setupUi(MainWindow)    
    
    #preparar submenus    
    ui_principal.actionRegistrar_coche.triggered.connect(mostrar_registro_coche)
    ui_principal.actionListar_coches.triggered.connect(mostrar_listado_coches)
    ui_principal.actionLista_con_list_widget.triggered.connect(mostrar_list_widget)
    ui_principal.actionlistar_con_table_widget.triggered.connect(mostrar_table_widget)
    ui_principal.actionAsistente_de_registro.triggered.connect(mostrar_asistente)
    ui_principal.actionSalir.triggered.connect(cerrar_aplicacion)
    
    pixmap = QPixmap("imagenes/coche_fantastico.jpg")
    ui_principal.lbl_coche_fantastico.setPixmap(pixmap)   
    
    
    #mostrar ventana y cerrar aplicacion cuando se cierre
    MainWindow.show()

    sys.exit(app.exec_())
