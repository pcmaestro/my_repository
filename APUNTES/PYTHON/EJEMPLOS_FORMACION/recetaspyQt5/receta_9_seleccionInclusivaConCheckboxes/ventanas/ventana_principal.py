# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(688, 472)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 50, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.chk_queso = QtWidgets.QCheckBox(Dialog)
        self.chk_queso.setGeometry(QtCore.QRect(70, 110, 70, 17))
        self.chk_queso.setObjectName("chk_queso")
        self.chk_aceitunas = QtWidgets.QCheckBox(Dialog)
        self.chk_aceitunas.setGeometry(QtCore.QRect(70, 150, 70, 17))
        self.chk_aceitunas.setObjectName("chk_aceitunas")
        self.chk_salsa = QtWidgets.QCheckBox(Dialog)
        self.chk_salsa.setGeometry(QtCore.QRect(70, 200, 101, 17))
        self.chk_salsa.setObjectName("chk_salsa")
        self.text_show = QtWidgets.QLabel(Dialog)
        self.text_show.setGeometry(QtCore.QRect(80, 310, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_show.setFont(font)
        self.text_show.setText("")
        self.text_show.setObjectName("text_show")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "PRECIO PIZZA BASICA 15 €"))
        self.chk_queso.setText(_translate("Dialog", " Queso"))
        self.chk_aceitunas.setText(_translate("Dialog", " Aceitunas"))
        self.chk_salsa.setText(_translate("Dialog", " Salsa barbacoa"))
