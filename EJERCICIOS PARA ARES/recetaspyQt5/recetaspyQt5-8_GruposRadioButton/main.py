import sys

from PyQt5.QtWidgets import QApplication

from clases import clases

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    ventanaVentas = clases.ventanaDialogo()
    
    sys.exit(app.exec_())

