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
        Dialog.resize(730, 504)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 30, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 110, 271, 221))
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName("groupBox")
        self.chk_vainilla = QtWidgets.QCheckBox(self.groupBox)
        self.chk_vainilla.setGeometry(QtCore.QRect(20, 70, 70, 17))
        self.chk_vainilla.setObjectName("chk_vainilla")
        self.chk_oreo = QtWidgets.QCheckBox(self.groupBox)
        self.chk_oreo.setGeometry(QtCore.QRect(20, 110, 70, 17))
        self.chk_oreo.setObjectName("chk_oreo")
        self.chk_limon = QtWidgets.QCheckBox(self.groupBox)
        self.chk_limon.setGeometry(QtCore.QRect(20, 150, 70, 17))
        self.chk_limon.setObjectName("chk_limon")
        self.chk_chocolate = QtWidgets.QCheckBox(self.groupBox)
        self.chk_chocolate.setGeometry(QtCore.QRect(20, 30, 70, 17))
        self.chk_chocolate.setObjectName("chk_chocolate")
        self.chk_frambuesa = QtWidgets.QCheckBox(self.groupBox)
        self.chk_frambuesa.setGeometry(QtCore.QRect(20, 190, 91, 17))
        self.chk_frambuesa.setObjectName("chk_frambuesa")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(410, 110, 251, 221))
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.chk_coca_cola = QtWidgets.QCheckBox(self.groupBox_2)
        self.chk_coca_cola.setGeometry(QtCore.QRect(40, 60, 70, 17))
        self.chk_coca_cola.setObjectName("chk_coca_cola")
        self.chk_fanta_naranja = QtWidgets.QCheckBox(self.groupBox_2)
        self.chk_fanta_naranja.setGeometry(QtCore.QRect(40, 110, 101, 17))
        self.chk_fanta_naranja.setObjectName("chk_fanta_naranja")
        self.chk_fanta_limon = QtWidgets.QCheckBox(self.groupBox_2)
        self.chk_fanta_limon.setGeometry(QtCore.QRect(40, 160, 91, 17))
        self.chk_fanta_limon.setObjectName("chk_fanta_limon")
        self.txt_show = QtWidgets.QLabel(Dialog)
        self.txt_show.setGeometry(QtCore.QRect(130, 350, 451, 81))
        self.txt_show.setText("")
        self.txt_show.setObjectName("txt_show")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Menu de helados y bebidas"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">MENU</p></body></html>"))
        self.groupBox.setTitle(_translate("Dialog", "Seleccionar un helado:"))
        self.chk_vainilla.setText(_translate("Dialog", " Vainilla"))
        self.chk_oreo.setText(_translate("Dialog", " Oreo"))
        self.chk_limon.setText(_translate("Dialog", " Limon"))
        self.chk_chocolate.setText(_translate("Dialog", " Chocolate"))
        self.chk_frambuesa.setText(_translate("Dialog", " Frambuesa"))
        self.groupBox_2.setTitle(_translate("Dialog", "Seleccionar una bebida:"))
        self.chk_coca_cola.setText(_translate("Dialog", " Coca Cola"))
        self.chk_fanta_naranja.setText(_translate("Dialog", " Fanta Naranja"))
        self.chk_fanta_limon.setText(_translate("Dialog", " Fanta Limon"))
