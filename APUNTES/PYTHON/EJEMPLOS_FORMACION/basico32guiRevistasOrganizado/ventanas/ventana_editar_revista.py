# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_editar_revista.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 60, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 120, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.entrada_titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_titulo.setGeometry(QtCore.QRect(350, 120, 113, 20))
        self.entrada_titulo.setObjectName("entrada_titulo")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 160, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.entrada_precio = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_precio.setGeometry(QtCore.QRect(350, 160, 113, 20))
        self.entrada_precio.setObjectName("entrada_precio")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 200, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.entrada_tema = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_tema.setGeometry(QtCore.QRect(350, 200, 113, 20))
        self.entrada_tema.setObjectName("entrada_tema")
        self.boton_guardar_cambios_revista = QtWidgets.QPushButton(self.centralwidget)
        self.boton_guardar_cambios_revista.setGeometry(QtCore.QRect(290, 340, 171, 41))
        self.boton_guardar_cambios_revista.setObjectName("boton_guardar_cambios_revista")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Actualiza los datos de la revista"))
        self.label_2.setText(_translate("MainWindow", "titulo:"))
        self.label_3.setText(_translate("MainWindow", "precio:"))
        self.label_4.setText(_translate("MainWindow", "tema:"))
        self.boton_guardar_cambios_revista.setText(_translate("MainWindow", "GUARDAR CAMBIOS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

