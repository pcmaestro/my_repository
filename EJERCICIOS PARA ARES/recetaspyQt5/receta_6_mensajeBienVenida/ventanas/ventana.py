# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialogo(object):
    def setupUi(self, dialogo):
        dialogo.setObjectName("dialogo")
        dialogo.resize(572, 416)
        dialogo.setStyleSheet("background-color: rgb(222, 251, 255);")
        self.lbl_text = QtWidgets.QLabel(dialogo)
        self.lbl_text.setGeometry(QtCore.QRect(20, 80, 131, 41))
        self.lbl_text.setObjectName("lbl_text")
        self.lbl_textbox = QtWidgets.QLineEdit(dialogo)
        self.lbl_textbox.setGeometry(QtCore.QRect(200, 90, 281, 20))
        self.lbl_textbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lbl_textbox.setObjectName("lbl_textbox")
        self.lbl_saludo = QtWidgets.QLabel(dialogo)
        self.lbl_saludo.setGeometry(QtCore.QRect(200, 160, 291, 131))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_saludo.setFont(font)
        self.lbl_saludo.setText("")
        self.lbl_saludo.setObjectName("lbl_saludo")
        self.btn = QtWidgets.QPushButton(dialogo)
        self.btn.setGeometry(QtCore.QRect(210, 320, 261, 51))
        self.btn.setStyleSheet("background-color: rgb(164, 227, 255);")
        self.btn.setObjectName("btn")

        self.retranslateUi(dialogo)
        QtCore.QMetaObject.connectSlotsByName(dialogo)

    def retranslateUi(self, dialogo):
        _translate = QtCore.QCoreApplication.translate
        dialogo.setWindowTitle(_translate("dialogo", "Dialog"))
        self.lbl_text.setText(_translate("dialogo", "ESCRIBE TU NOMBRE"))
        self.btn.setText(_translate("dialogo", "PULSAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogo = QtWidgets.QDialog()
    ui = Ui_dialogo()
    ui.setupUi(dialogo)
    dialogo.show()
    sys.exit(app.exec_())
