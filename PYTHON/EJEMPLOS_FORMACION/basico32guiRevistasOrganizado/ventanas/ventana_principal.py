# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
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
        self.label.setGeometry(QtCore.QRect(200, 170, 461, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuRevistas = QtWidgets.QMenu(self.menubar)
        self.menuRevistas.setObjectName("menuRevistas")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.submenu_registrar_revista = QtWidgets.QAction(MainWindow)
        self.submenu_registrar_revista.setObjectName("submenu_registrar_revista")
        self.submenu_listar_revistas = QtWidgets.QAction(MainWindow)
        self.submenu_listar_revistas.setObjectName("submenu_listar_revistas")
        self.submenu_list_widget_revistas = QtWidgets.QAction(MainWindow)
        self.submenu_list_widget_revistas.setObjectName("submenu_list_widget_revistas")
        self.submenu_table_widget_revistas = QtWidgets.QAction(MainWindow)
        self.submenu_table_widget_revistas.setObjectName("submenu_table_widget_revistas")
        self.menuRevistas.addAction(self.submenu_registrar_revista)
        self.menuRevistas.addAction(self.submenu_listar_revistas)
        self.menuRevistas.addAction(self.submenu_list_widget_revistas)
        self.menuRevistas.addAction(self.submenu_table_widget_revistas)
        self.menubar.addAction(self.menuRevistas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "APLICACION GESTION REVISTAS"))
        self.label.setText(_translate("MainWindow", "Bienvenido a la aplicacion de getion de revistas\n"
" usando PyQt5"))
        self.menuRevistas.setTitle(_translate("MainWindow", "Revistas"))
        self.submenu_registrar_revista.setText(_translate("MainWindow", "Registrar Revista"))
        self.submenu_listar_revistas.setText(_translate("MainWindow", "Listar Revistas"))
        self.submenu_list_widget_revistas.setText(_translate("MainWindow", "Listar Revistas Usando List Widget"))
        self.submenu_table_widget_revistas.setText(_translate("MainWindow", "Listar Revistas Usando Table Widget"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

