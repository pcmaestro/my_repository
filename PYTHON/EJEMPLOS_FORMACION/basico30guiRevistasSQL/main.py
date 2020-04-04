#Ejercicio con menú desplegable que da acceso a nuevas ventanas


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from clases import clases
from modelo import operaciones_bd

#Del paquete ventanas, traemos los 3 módulos de nuestras ventanas
from ventanas import ventana_principal, registro_revista, listado_revistas


def registrar_revista():
    revista = clases.Revista()
    revista.titulo = ui.registro_revista.entrada_titulo.text()
    revista.precio = ui.registro_revista.entrada_precio.text()
    revista.tema = ui.registro_revista.entrada_tema.text()

#Habiendo creado el objeto ui_registro_revista de la clase Ui_MainWindow()
#que hemos importado desde el módulo registro_revista , creamos una función
#que ejecute su método setupUI para mostrar la ventana al elegir la opción
#en el menú dev la ventana principal
def mostrar_registro_revista():
    ui_registro_revista.setupUi(MainWindow)
    ui.registro_revista.boton_registrar_revista.clicked.connect(registrar_revista)

#Igual que lo anterior,  con el objeto ui_listado_revistas de la clase
#Ui_MainWindow() del módulo listado_revistas
def mostrar_listado_revistas(): 
    ui_listado_revistas.setupUi(MainWindow)

#Arrancamos el proceso
app = QtWidgets.QApplication(sys.argv)

#Creamos el objeto con la ventana principal
MainWindow = QtWidgets.QMainWindow()

#Creamos los frame donde irán los contenidos de nuestras ventanas instanciando
#la clase Ui_MainWindow() de sus respectivos módulos
ui_principal = ventana_principal.Ui_MainWindow()
ui_registro_revista = registro_revista.Ui_MainWindow()
ui_listado_revistas = listado_revistas.Ui_MainWindow()
#Ejecutamos el método setupUI() de la ventana principal ( los de las otras se ejecutan
#al invocarlos seleccionandolas en el menú, el cual llama a sus funciones)
ui_principal.setupUi(MainWindow)

#Configuramos los eventos que ejecutan las funciones de las otras ventanas
ui_principal.submenu_registrar_revista.triggered.connect(mostrar_registro_revista)
ui_principal.submenu_listar_revistas.triggered.connect(mostrar_listado_revistas)

#Mostramos la ventana principal
MainWindow.show()
#La ventana no se cerrará mientras siga corriendo el proceso de PyQt5
sys.exit(app.exec_())