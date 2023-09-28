import sys

from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QLabel,QPushButton
from PyQt5.QtCore import QTimer
# from PyQt5.QtCore import QTimer

class Game(QWidget):
    def __init__(self,size):
        super().__init__()

        self.size = size

        self.setWindowTitle("Game Puzzle")
        self.setStyleSheet('font-size: 30px')
        self.__initUI()
        self.show()
        # self.showMaximized()

    def __initUI(self):
        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(100)

        self.label_time = QLabel('Time: 0 s')
        self.label_moves = QLabel('Moves: 0')

        self.btn_restart = QPushButton('Restart')
        self.btn_toggle = QPushButton('Pause')

        self.btn_toggle.clicked.connect(self.start_action)
        self.btn_restart.clicked.connect(self.show_restart)

        layout = QVBoxLayout()
        layout.addWidget(self.label_time)
        layout.addWidget(self.label_moves)
        layout.addWidget(self.btn_toggle)

app = QApplication(sys.argv)

win = Game(3)
app.exec_()