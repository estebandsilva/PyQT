import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer, Qt


class MovingRectangle(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Moving Rectangle')

        self.rect_label = QLabel(self)
        self.rect_label.setGeometry(50, 50, 50, 50)
        self.rect_label.setStyleSheet('background-color: red;')

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_rectangle)
        self.timer.start(50)  # Move the rectangle every 50 milliseconds

        self.step_x = 2
        self.step_y = 2

    def move_rectangle(self):
        rect_position = self.rect_label.pos()
        new_x = rect_position.x() + self.step_x
        new_y = rect_position.y() + self.step_y

        # Change direction when hitting boundaries
        if new_x + self.rect_label.width() > self.width() or new_x < 0:
            self.step_x = -self.step_x

        if new_y + self.rect_label.height() > self.height() or new_y < 0:
            self.step_y = -self.step_y

        self.rect_label.move(new_x, new_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MovingRectangle()
    window.show()
    sys.exit(app.exec_())
