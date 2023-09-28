import sys

from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QLabel,QPushButton,QLineEdit
from PyQt5.QtCore import QTimer
# from PyQt5.QtCore import QTimer

class Game(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Game Tic Tac Toe")
        self.setStyleSheet('font-size: 30px')
        self.__initUI()
        self.show()
        # self.showMaximized()

    def __initUI(self):
        self.v_box = QVBoxLayout()
        self.h_box_bottom = QVBoxLayout()
        self.h_box_top = QHBoxLayout()
        self.grid = QGridLayout()
        self.edit_name_win = QLineEdit("Winner")

        self.btn_restart = QPushButton("Restart")
        self.btn_quit = QPushButton("Quit")

        self.btn_restart.clicked.connect(self.def_restart)
        # self.btn_quit.clicked.connect(self.def_quit)

        self.h_box_top.addWidget(self.btn_restart)
        self.h_box_top.addStretch()
        self.h_box_top.addWidget(self.btn_quit)
        
        self.h_box_bottom.addWidget(self.edit_name_win)

        self.v_box.addLayout(self.h_box_top)
        self.v_box.addLayout(self.grid)
        self.v_box.addLayout(self.h_box_bottom)

        self.setLayout(self.v_box)

        self.def_restart()

    def def_restart(self):
        self.matrix = list()
        i = 0

        for x in range(3):
            for y in range(3):
                self.grid.addWidget(QPushButton(" "),x,y)


app = QApplication(sys.argv)

win = Game()
win.show()
sys.exit(app.exec_())