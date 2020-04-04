# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialogWindow(object):
    def setupUi(self, dialogWindow):
        dialogWindow.setObjectName("dialogWindow")
        dialogWindow.resize(599, 452)
        dialogWindow.setStyleSheet("background-color: rgb(225, 255, 216);")
        self.lbl_plainText1 = QtWidgets.QLabel(dialogWindow)
        self.lbl_plainText1.setGeometry(QtCore.QRect(60, 40, 341, 16))
        self.lbl_plainText1.setObjectName("lbl_plainText1")
        self.btn_radio_primera = QtWidgets.QRadioButton(dialogWindow)
        self.btn_radio_primera.setGeometry(QtCore.QRect(70, 80, 281, 17))
        self.btn_radio_primera.setObjectName("btn_radio_primera")
        self.btn_radio_negocios = QtWidgets.QRadioButton(dialogWindow)
        self.btn_radio_negocios.setGeometry(QtCore.QRect(70, 120, 281, 17))
        self.btn_radio_negocios.setObjectName("btn_radio_negocios")
        self.btn_radio_economica = QtWidgets.QRadioButton(dialogWindow)
        self.btn_radio_economica.setGeometry(QtCore.QRect(70, 160, 281, 17))
        self.btn_radio_economica.setObjectName("btn_radio_economica")
        self.lbl_plainText2 = QtWidgets.QLabel(dialogWindow)
        self.lbl_plainText2.setGeometry(QtCore.QRect(70, 220, 391, 21))
        self.lbl_plainText2.setObjectName("lbl_plainText2")
        self.lbl_textToShow = QtWidgets.QLabel(dialogWindow)
        self.lbl_textToShow.setGeometry(QtCore.QRect(70, 300, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_textToShow.setFont(font)
        self.lbl_textToShow.setText("")
        self.lbl_textToShow.setObjectName("lbl_textToShow")

        self.retranslateUi(dialogWindow)
        QtCore.QMetaObject.connectSlotsByName(dialogWindow)

    def retranslateUi(self, dialogWindow):
        _translate = QtCore.QCoreApplication.translate
        dialogWindow.setWindowTitle(_translate("dialogWindow", "Clase de vuelo"))
        self.lbl_plainText1.setText(_translate("dialogWindow", "ESCOJA LA CLASE DEL VUELO:"))
        self.btn_radio_primera.setText(_translate("dialogWindow", " Primera clase 190 €"))
        self.btn_radio_negocios.setText(_translate("dialogWindow", " Clase negocios 130 €"))
        self.btn_radio_economica.setText(_translate("dialogWindow", " Clase económica 99 €"))
        self.lbl_plainText2.setText(_translate("dialogWindow", "CLASE SELECCIONADA Y VALOR ASOCIADO:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogWindow = QtWidgets.QDialog()
    ui = Ui_dialogWindow()
    ui.setupUi(dialogWindow)
    dialogWindow.show()
    sys.exit(app.exec_())
