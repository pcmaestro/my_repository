import sys
from PyQt5.QtWidgets import QWidget, QApplication

import otro

#Variable global que indica, dependiendo de donde esté:
#Si está en el archivo python desde el que arrancamos, la variable
#__name__ equivale a __main___
#Si está en otro archivo que hayamos importado , la variable vale el nombre
#del módulo desde el que hacemos la importación
print(__name__)

#Al ejecutar el import de "otro" __name__ valdrá lo que traiga, y luego aparecerá
#el valor del archivo actual

