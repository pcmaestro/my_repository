# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventanaDialogo(object):
    def setupUi(self, ventanaDialogo):
        ventanaDialogo.setObjectName("ventanaDialogo")
        ventanaDialogo.resize(593, 560)
        ventanaDialogo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lbl_text_talla = QtWidgets.QLabel(ventanaDialogo)
        self.lbl_text_talla.setGeometry(QtCore.QRect(30, 20, 171, 41))
        self.lbl_text_talla.setObjectName("lbl_text_talla")
        self.verticalLayoutWidget = QtWidgets.QWidget(ventanaDialogo)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 70, 311, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vly_tallasCamisa = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vly_tallasCamisa.setContentsMargins(0, 0, 0, 0)
        self.vly_tallasCamisa.setObjectName("vly_tallasCamisa")
        self.btn_radio_M = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.btn_radio_M.setObjectName("btn_radio_M")
        self.vly_tallasCamisa.addWidget(self.btn_radio_M)
        self.btn_radio_L = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.btn_radio_L.setObjectName("btn_radio_L")
        self.vly_tallasCamisa.addWidget(self.btn_radio_L)
        self.btn_radio_XL = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.btn_radio_XL.setObjectName("btn_radio_XL")
        self.vly_tallasCamisa.addWidget(self.btn_radio_XL)
        self.btn_radio_XXL = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.btn_radio_XXL.setObjectName("btn_radio_XXL")
        self.vly_tallasCamisa.addWidget(self.btn_radio_XXL)
        self.lbl_text_formaPago = QtWidgets.QLabel(ventanaDialogo)
        self.lbl_text_formaPago.setGeometry(QtCore.QRect(30, 240, 171, 41))
        self.lbl_text_formaPago.setObjectName("lbl_text_formaPago")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(ventanaDialogo)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 290, 311, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.vly_formaPago = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vly_formaPago.setContentsMargins(0, 0, 0, 0)
        self.vly_formaPago.setObjectName("vly_formaPago")
        self.btn_pagoTarjeta = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.btn_pagoTarjeta.setObjectName("btn_pagoTarjeta")
        self.vly_formaPago.addWidget(self.btn_pagoTarjeta)
        self.btn_pagoContado = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.btn_pagoContado.setObjectName("btn_pagoContado")
        self.vly_formaPago.addWidget(self.btn_pagoContado)
        self.btn_pagoMovil = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.btn_pagoMovil.setObjectName("btn_pagoMovil")
        self.vly_formaPago.addWidget(self.btn_pagoMovil)
        self.lbl_textToShow = QtWidgets.QLabel(ventanaDialogo)
        self.lbl_textToShow.setGeometry(QtCore.QRect(30, 460, 441, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_textToShow.setFont(font)
        self.lbl_textToShow.setText("")
        self.lbl_textToShow.setObjectName("lbl_textToShow")

        self.retranslateUi(ventanaDialogo)
        QtCore.QMetaObject.connectSlotsByName(ventanaDialogo)

    def retranslateUi(self, ventanaDialogo):
        _translate = QtCore.QCoreApplication.translate
        ventanaDialogo.setWindowTitle(_translate("ventanaDialogo", "Dialog"))
        self.lbl_text_talla.setText(_translate("ventanaDialogo", "ELIJA UNA TALLA DE CAMISA"))
        self.btn_radio_M.setText(_translate("ventanaDialogo", " Talla M"))
        self.btn_radio_L.setText(_translate("ventanaDialogo", " Talla L"))
        self.btn_radio_XL.setText(_translate("ventanaDialogo", " Talla XL"))
        self.btn_radio_XXL.setText(_translate("ventanaDialogo", "Talla XXL"))
        self.lbl_text_formaPago.setText(_translate("ventanaDialogo", "ELIJA UNA FORMA DE PAGO"))
        self.btn_pagoTarjeta.setText(_translate("ventanaDialogo", " Pago con tarjeta"))
        self.btn_pagoContado.setText(_translate("ventanaDialogo", " Pago al contado"))
        self.btn_pagoMovil.setText(_translate("ventanaDialogo", " Pago móvil NFS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventanaDialogo = QtWidgets.QDialog()
    ui = Ui_ventanaDialogo()
    ui.setupUi(ventanaDialogo)
    ventanaDialogo.show()
    sys.exit(app.exec_())
