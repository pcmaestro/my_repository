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
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 451, 111))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.lbl_coche_fantastico = QtWidgets.QLabel(self.centralwidget)
        self.lbl_coche_fantastico.setGeometry(QtCore.QRect(80, 180, 601, 291))
        self.lbl_coche_fantastico.setText("")
        self.lbl_coche_fantastico.setObjectName("lbl_coche_fantastico")
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
        self.actionLista_con_list_widget = QtWidgets.QAction(MainWindow)
        self.actionLista_con_list_widget.setObjectName("actionLista_con_list_widget")
        self.actionlistar_con_table_widget = QtWidgets.QAction(MainWindow)
        self.actionlistar_con_table_widget.setObjectName("actionlistar_con_table_widget")
        self.actionAsistente_de_registro = QtWidgets.QAction(MainWindow)
        self.actionAsistente_de_registro.setObjectName("actionAsistente_de_registro")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuAcciones.addAction(self.actionRegistrar_coche)
        self.menuAcciones.addAction(self.actionListar_coches)
        self.menuAcciones.addAction(self.actionLista_con_list_widget)
        self.menuAcciones.addAction(self.actionlistar_con_table_widget)
        self.menuAcciones.addAction(self.actionAsistente_de_registro)
        self.menuAcciones.addAction(self.actionSalir)
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
        self.actionLista_con_list_widget.setText(_translate("MainWindow", "Lista con list widget"))
        self.actionlistar_con_table_widget.setText(_translate("MainWindow", "listar con table widget"))
        self.actionAsistente_de_registro.setText(_translate("MainWindow", "Asistente de registro"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
