# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_edicion.ui'
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 581, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 47, 13))
        self.label_2.setObjectName("label_2")
        self.txt_marca = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_marca.setGeometry(QtCore.QRect(140, 130, 401, 20))
        self.txt_marca.setObjectName("txt_marca")
        self.txt_modelo = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_modelo.setGeometry(QtCore.QRect(140, 200, 401, 20))
        self.txt_modelo.setObjectName("txt_modelo")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 200, 47, 13))
        self.label_3.setObjectName("label_3")
        self.txt_color = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_color.setGeometry(QtCore.QRect(140, 270, 401, 20))
        self.txt_color.setObjectName("txt_color")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 270, 47, 13))
        self.label_4.setObjectName("label_4")
        self.txt_motor = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_motor.setGeometry(QtCore.QRect(140, 340, 401, 20))
        self.txt_motor.setObjectName("txt_motor")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 340, 47, 13))
        self.label_5.setObjectName("label_5")
        self.txt_precio = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_precio.setGeometry(QtCore.QRect(140, 420, 401, 20))
        self.txt_precio.setObjectName("txt_precio")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 420, 47, 13))
        self.label_6.setObjectName("label_6")
        self.btn_modificar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_modificar.setGeometry(QtCore.QRect(220, 480, 181, 41))
        self.btn_modificar.setObjectName("btn_modificar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modificar registro"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">MODIFICAR COCHE</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "MARCA"))
        self.label_3.setText(_translate("MainWindow", "MODELO"))
        self.label_4.setText(_translate("MainWindow", "COLOR"))
        self.label_5.setText(_translate("MainWindow", "MOTOR"))
        self.label_6.setText(_translate("MainWindow", "PRECIO"))
        self.btn_modificar.setText(_translate("MainWindow", "MODIFICAR"))
