# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_listado.ui'
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
        self.label.setGeometry(QtCore.QRect(30, 20, 231, 41))
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.text_show = QtWidgets.QTextEdit(self.centralwidget)
        self.text_show.setGeometry(QtCore.QRect(30, 60, 621, 411))
        self.text_show.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text_show.setObjectName("text_show")
        self.btn_listar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_listar.setGeometry(QtCore.QRect(240, 490, 191, 61))
        self.btn_listar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(117, 117, 117, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btn_listar.setObjectName("btn_listar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "LISTADO DE COCHES"))
        self.btn_listar.setText(_translate("MainWindow", "LISTAR COCHES"))
