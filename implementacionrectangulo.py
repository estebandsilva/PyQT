import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow
from PyQt5.QtCore import QTimer

# Importa el archivo generado por pyuic5
from ui_interface import *


class MovingRectangleApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.rect_label.setStyleSheet('background-color: red;')

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_rectangle)
        self.timer.start(50)  # Mover el rectángulo cada 50 milisegundos

        self.step_x = 2
        self.step_y = 2

    def move_rectangle(self):
        rect_position = self.rect_label.pos()
        new_x = rect_position.x() + self.step_x
        new_y = rect_position.y() + self.step_y

        # Cambiar la dirección cuando golpea los límites
        if new_x + self.rect_label.width() > self.width() or new_x < 0:
            self.step_x = -self.step_x

        if new_y + self.rect_label.height() > self.height() or new_y < 0:
            self.step_y = -self.step_y

        self.rect_label.move(new_x, new_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MovingRectangleApp()
    window.show()
    sys.exit(app.exec_())
