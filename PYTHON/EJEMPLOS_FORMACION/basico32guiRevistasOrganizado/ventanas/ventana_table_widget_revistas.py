# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_table_widget_revistas.ui'
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
        self.table_widget_revistas = QtWidgets.QTableWidget(self.centralwidget)
        self.table_widget_revistas.setGeometry(QtCore.QRect(40, 70, 731, 481))
        self.table_widget_revistas.setObjectName("table_widget_revistas")
        self.table_widget_revistas.setColumnCount(7)
        self.table_widget_revistas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_revistas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_revistas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_revistas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_revistas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_revistas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_revistas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_revistas.setHorizontalHeaderItem(6, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 30, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table_widget_revistas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.table_widget_revistas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "titulo"))
        item = self.table_widget_revistas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "precio"))
        item = self.table_widget_revistas.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "tema"))
        item = self.table_widget_revistas.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "borrar"))
        item = self.table_widget_revistas.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "editar"))
        item = self.table_widget_revistas.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "imagen"))
        self.label.setText(_translate("MainWindow", "LISTADO USANDO TABLE WIDGET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

