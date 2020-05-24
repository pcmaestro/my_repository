# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(545, 444)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 70, 141, 16))
        self.label.setObjectName("label")
        self.num1 = QtWidgets.QLineEdit(Dialog)
        self.num1.setGeometry(QtCore.QRect(250, 70, 251, 20))
        self.num1.setObjectName("num1")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 141, 16))
        self.label_2.setObjectName("label_2")
        self.num2 = QtWidgets.QLineEdit(Dialog)
        self.num2.setGeometry(QtCore.QRect(250, 140, 251, 20))
        self.num2.setObjectName("num2")
        self.btn_sumar = QtWidgets.QPushButton(Dialog)
        self.btn_sumar.setGeometry(QtCore.QRect(30, 210, 91, 31))
        self.btn_sumar.setObjectName("btn_sumar")
        self.btn_restar = QtWidgets.QPushButton(Dialog)
        self.btn_restar.setGeometry(QtCore.QRect(150, 210, 91, 31))
        self.btn_restar.setObjectName("btn_restar")
        self.btn_multiplicar = QtWidgets.QPushButton(Dialog)
        self.btn_multiplicar.setGeometry(QtCore.QRect(270, 210, 91, 31))
        self.btn_multiplicar.setObjectName("btn_multiplicar")
        self.btn_dividir = QtWidgets.QPushButton(Dialog)
        self.btn_dividir.setGeometry(QtCore.QRect(390, 210, 91, 31))
        self.btn_dividir.setObjectName("btn_dividir")
        self.resultado = QtWidgets.QLabel(Dialog)
        self.resultado.setGeometry(QtCore.QRect(40, 280, 441, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.resultado.setFont(font)
        self.resultado.setText("")
        self.resultado.setObjectName("resultado")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "PRIMER NUMERO"))
        self.label_2.setText(_translate("Dialog", "SEGUNDO NUMERO"))
        self.btn_sumar.setText(_translate("Dialog", "SUMAR"))
        self.btn_restar.setText(_translate("Dialog", "RESTAR"))
        self.btn_multiplicar.setText(_translate("Dialog", "MULTIPLICAR"))
        self.btn_dividir.setText(_translate("Dialog", "DIVIDIR"))
