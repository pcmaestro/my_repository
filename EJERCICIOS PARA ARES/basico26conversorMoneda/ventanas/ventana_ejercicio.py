# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_ejercicio.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_texto = QtWidgets.QLabel(self.centralwidget)
        self.label_texto.setGeometry(QtCore.QRect(40, 110, 211, 31))
        self.label_texto.setObjectName("label_texto")
        self.entrada_euros = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_euros.setGeometry(QtCore.QRect(300, 120, 271, 20))
        self.entrada_euros.setObjectName("entrada_euros")
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setGeometry(QtCore.QRect(320, 220, 221, 51))
        self.label_resultado.setText("")
        self.label_resultado.setObjectName("label_resultado")
        self.boton_convertir_a_dolares = QtWidgets.QPushButton(self.centralwidget)
        self.boton_convertir_a_dolares.setGeometry(QtCore.QRect(30, 160, 211, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconos/usd_dollar_3313.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_convertir_a_dolares.setIcon(icon)
        self.boton_convertir_a_dolares.setObjectName("boton_convertir_a_dolares")
        self.boton_convertir_a_libras = QtWidgets.QPushButton(self.centralwidget)
        self.boton_convertir_a_libras.setGeometry(QtCore.QRect(30, 250, 211, 71))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("iconos/libra_esterlina.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_convertir_a_libras.setIcon(icon1)
        self.boton_convertir_a_libras.setObjectName("boton_convertir_a_libras")
        self.boton_convertir_a_yuanes = QtWidgets.QPushButton(self.centralwidget)
        self.boton_convertir_a_yuanes.setGeometry(QtCore.QRect(30, 340, 211, 71))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("iconos/yuan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_convertir_a_yuanes.setIcon(icon2)
        self.boton_convertir_a_yuanes.setObjectName("boton_convertir_a_yuanes")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_texto.setText(_translate("MainWindow", "INTRODUCE UNA CANTIDAD DE EUROS"))
        self.boton_convertir_a_dolares.setText(_translate("MainWindow", " CONVERTIR A DOLARES"))
        self.boton_convertir_a_libras.setText(_translate("MainWindow", " CONVERTIR A LIBRAS"))
        self.boton_convertir_a_yuanes.setText(_translate("MainWindow", " CONVERTIR A YUANES"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
