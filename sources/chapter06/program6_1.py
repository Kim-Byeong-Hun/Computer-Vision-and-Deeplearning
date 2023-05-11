# PyQt로 간단한 GUI만들기(버튼 클릭시 삑소리)
import os
os.chdir('C:/Users/qudgn/Computer-Vision-and-Deeplearning/sources/chapter06')

from PyQt5.QtWidgets import *
import sys
import winsound

class BeepSound(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('삑 소리 내기')
        self.setGeometry(200,200,500,100)

        shortBeepButton = QPushButton('짧게 삑', self)
        longBeepButton = QPushButton('길게 삑', self)
        quitButton = QPushButton('나가기', self)
        self.label = QLabel('환영합니다', self)  # 멤버변수로 설정(클래스 어느곳이든 호출 가능 및 생성객체도 접근 가능)

        shortBeepButton.setGeometry(10,10,100,30)
        longBeepButton.setGeometry(110,10,100,30)
        quitButton.setGeometry(210,10,100,30)
        self.label.setGeometry(10,40,500,70)

        shortBeepButton.clicked.connect(self.shortBeepFunction)
        longBeepButton.clicked.connect(self.longBeepFunction)
        quitButton.clicked.connect(self.quitFunction)

    def shortBeepFunction(self):
        self.label.setText('주파수 1000으로 0.5초 동안 삑 소리를 냅니다.')
        winsound.Beep(1000,500)

    def longBeepFunction(self):
        self.label.setText('주파수 1000으로 3초 동안 삑 소리를 냅니다.')
        winsound.Beep(1000,3000)

    def quitFunction(self):
        self.close()

app = QApplication(sys.argv)
win=BeepSound()
win.show()
app.exec_()