import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton('Добавить окружность', self)
        self.button.clicked.connect(self.add_circle)
        self.button.setGeometry(10, 10, 150, 50)

        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for circle in self.circles:
            painter.setBrush(Qt.yellow)
            painter.drawEllipse(circle['x'], circle['y'], circle['diameter'], circle['diameter'])

    def add_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)

        self.circles.append({'x': x, 'y': y, 'diameter': diameter})
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setGeometry(100, 100, 500, 500)
    mainWindow.show()
    sys.exit(app.exec_())
