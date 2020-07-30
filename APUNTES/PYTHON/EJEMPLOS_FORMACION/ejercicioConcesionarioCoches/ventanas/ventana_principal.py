# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(233, 255, 252);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 110, 451, 251))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuAcciones = QtWidgets.QMenu(self.menubar)
        self.menuAcciones.setObjectName("menuAcciones")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRegistrar_coche = QtWidgets.QAction(MainWindow)
        self.actionRegistrar_coche.setObjectName("actionRegistrar_coche")
        self.actionListar_coches = QtWidgets.QAction(MainWindow)
        self.actionListar_coches.setObjectName("actionListar_coches")
        self.menuAcciones.addAction(self.actionRegistrar_coche)
        self.menuAcciones.addAction(self.actionListar_coches)
        self.menubar.addAction(self.menuAcciones.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">GESTION COMERCIAL DE COCHES</p></body></html>"))
        self.menuAcciones.setTitle(_translate("MainWindow", "Acciones"))
        self.actionRegistrar_coche.setText(_translate("MainWindow", "Registrar coche"))
        self.actionListar_coches.setText(_translate("MainWindow", "Listar coches"))
