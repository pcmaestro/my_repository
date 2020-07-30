#El módulo QtWidgets lo necesitamos para crear los objetos de Qt,  los otros
#módulos son necesarios para convertir los archivos .ui en archivos .py
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_python
import sys


# OPCIONAL:
# +Sobre la actual aplicacion. Incorporar 1 boton para transformar los euros introducidos
# a otra moneda a elegir por el programador.
# + Incorporar un boton más para tranformar a otro tipo de moneda distinto
# + Mostrar un icono en el boton correspondiente de conversion

def transformar_a_dolares():
    introducido = ui.entrada_euros.text()
    introducido_float = float(introducido.replace(",","."))
    dolares = introducido_float * 1.1
    ui.label_resultado.setText("resultado en dolares: " + "{:.2f}".format(dolares).replace(".",",") )
    
#vamos a usar el archivo generado de la ventana directamente

#linea obligatoria para usar pyqt5
app = QtWidgets.QApplication(sys.argv)

#se prepara un MainWindow de pyqt5, esto seria parte del codigo recomendado de pyqt5
MainWindow = QtWidgets.QMainWindow()

#asi crea un objeto de la clase en el archivo generado y lo usa para preparar la ventana principal
#llamada MainWindow para que tenga todo lo que pusimos en el designer
ui = ventana_python.Ui_MainWindow()
ui.setupUi(MainWindow)

#todos los componentes puestos en la ventana por el designer estan en ui
ui.boton_convertir_a_dolares.clicked.connect(transformar_a_dolares)

#Muestra la ventana en pantalla
MainWindow.show()

#Mantiene la ventana abierta mientras se esté ejecutando nuestra apliación
sys.exit(app.exec_())




