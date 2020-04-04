
from PyQt5 import QtWidgets
from ventanas import ventana_principal, ventana_registro, ventana_listado
from clases.clases import Coche
import sys
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox
from modelo.operaciones_bd import obtener_coches

#metodos de la ventana de registro:
def registrar_coche():
    
    coche = Coche("","","","",0)    
    coche.marca = ui_registro_coche.txt_marca.text()
    coche.modelo = ui_registro_coche.txt_modelo.text()
    coche.color = ui_registro_coche.txt_color.text()
    coche.motor = ui_registro_coche.txt_motor.text()
    coche.precio = float(ui_registro_coche.txt_precio.text())    
    
    #falta validarla y dar errores
    operaciones_bd.registro_coche(coche)
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
    
def listado():
    coches = obtener_coches()
    texto = "id\tMarca\t\Modelo\tColor\tMotor\tPrecio\n\n"
    for c in coches:
        texto += ( str(c[0]) + "\t" + c[1] + "\t" + str(c[2]) + "\t" + str(c[3]) + 
                  "\t" + str(c[4]) + "\t" + str(c[5]) +"\n")
    ui_listado_coches.text_show.setText(texto)

#arranque de la aplicacion principal
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    #creo los interfaces
    ui_principal = ventana_principal.Ui_MainWindow()
    ui_registro_coche = ventana_registro.Ui_MainWindow()
    ui_listado_coches = ventana_listado.Ui_MainWindow()
    ui_principal.setupUi(MainWindow)    
    
    #preparar submenus
    ui_principal.actionRegistrar_coche.triggered.connect(mostrar_registro_coche)
    ui_principal.actionListar_coches.triggered.connect(mostrar_listado_coches)
    
    #mostrar ventana y cerrar aplicacion cuando se cierre
    MainWindow.show()
    sys.exit(app.exec_())