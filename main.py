
#pip install PySide2
#pip install PySide6
#pip install Pycairo
#pip install pipwin
#pipwin install cairocffi
#pip install pyqt5

##Generamos el python con PySide2
#pyuic5 -x my_ui.ui -o my_ui.py
#lo mismo con resources
#pyrcc5 resources.qrc -o resoruces_rc.py



import os
import sys

from ui_interface import *

########################################################################
##   MAIN WINDOW CLASS
########################################################################
# class MainWindow(QMainWindow):
#     def __init__(self,parent=None):
#         QMainWindow.__init__(self)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         ########################################################################
#         # SHOW WINDOW
#         ########################################################################
#         self.show()

########################################################################
## EXECUTE  APP
########################################################################
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ########################################################################
#     ##
#     ########################################################################
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

########################################################################
## END
########################################################################