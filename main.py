
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



from Custom_Widgets.ProgressIndicator import test
test.main()