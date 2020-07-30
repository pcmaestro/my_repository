# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_ejemplo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ejemplo_Uso_GUI(object):
    def setupUi(self, Ejemplo_Uso_GUI):
        Ejemplo_Uso_GUI.setObjectName("Ejemplo_Uso_GUI")
        Ejemplo_Uso_GUI.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Ejemplo_Uso_GUI)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_pulsar_boton = QtWidgets.QLabel(self.centralwidget)
        self.lbl_pulsar_boton.setGeometry(QtCore.QRect(160, 80, 361, 111))
        self.lbl_pulsar_boton.setText("")
        self.lbl_pulsar_boton.setObjectName("lbl_pulsar_boton")
        self.btn_pulsame = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pulsame.setGeometry(QtCore.QRect(260, 330, 191, 71))
        self.btn_pulsame.setObjectName("btn_pulsame")
        Ejemplo_Uso_GUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ejemplo_Uso_GUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Ejemplo_Uso_GUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ejemplo_Uso_GUI)
        self.statusbar.setObjectName("statusbar")
        Ejemplo_Uso_GUI.setStatusBar(self.statusbar)

        self.retranslateUi(Ejemplo_Uso_GUI)
        QtCore.QMetaObject.connectSlotsByName(Ejemplo_Uso_GUI)

    def retranslateUi(self, Ejemplo_Uso_GUI):
        _translate = QtCore.QCoreApplication.translate
        Ejemplo_Uso_GUI.setWindowTitle(_translate("Ejemplo_Uso_GUI", "MainWindow"))
        self.btn_pulsame.setText(_translate("Ejemplo_Uso_GUI", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ejemplo_Uso_GUI = QtWidgets.QMainWindow()
    ui = Ui_Ejemplo_Uso_GUI()
    ui.setupUi(Ejemplo_Uso_GUI)
    Ejemplo_Uso_GUI.show()
    sys.exit(app.exec_())
