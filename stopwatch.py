from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stopwatch')
        self.setGeometry(100, 100, 400, 500)
        self.UiComponent()
        self.show()

    def UiComponent(self):
        self.count = 0
        self.flag = False
        self.label = QLabel(self)
        self.label.setGeometry(75, 100, 250, 70)
        self.label.setStyleSheet('border: 4px solid black')
        self.label.setText(str(self.count))
        self.label.setFont(QFont('Arial', 25))
        self.label.setAlignment(Qt.AlignCenter)
        start = QPushButton('Start', self)
        start.setGeometry(125, 250, 150, 40)
        start.pressed.connect(self.start)

        stop = QPushButton('Stop', self)
        stop.setGeometry(125, 300, 150, 40)
        stop.pressed.connect(self.stop)

        reset = QPushButton('Reset', self)
        reset.setGeometry(125, 350, 150, 40)
        reset.pressed.connect(self.reset)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

    def start(self):
        self.flag = True

    def stop(self):
        self.flag = False

    def reset(self):
        self.flag = False
        self.count = 0
        self.label.setText(str(self.count))

    def showTime(self):
        if self.flag:
            self.count += 1
            self.label.setText(str(self.count))




app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
