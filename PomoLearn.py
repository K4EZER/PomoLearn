import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PomoLearn")
        self.setGeometry(700, 300, 400, 400)
        self.setWindowIcon(QIcon("pomolearnlogo.png"))
        self.setStyleSheet("background-color: #ffe8e8;")
        self.initUI()
        self.label1 = QLabel("Pomo", self)
        self.label1.setFont(QFont("Serif",30))
        self.label1.setGeometry(90, 10, 120, 50)
        self.label1.setStyleSheet("color: #f27718;"
                             "background-color: #ffe8e8;"
                             "font-weight: bold;")
        self.label2 = QLabel("Learn", self)
        self.label2.setFont(QFont("Serif",30))
        self.label2.setGeometry(205, 10, 120, 50)
        self.label2.setStyleSheet("color: #009dff;"
                             "background-color: #ffe8e8;"
                             "font-weight: bold;")  
        
        
        
        
    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        question1 = QLabel("How many minutes would you like to focus on learning?", self.central_widget)
        question1.setFont(QFont("Serif",15))
        question1.setStyleSheet("color: #000000;"
                                "background-color: #ffe8e8;"
                                "font-weight: bold;"
                                "border: 1px solid #000000;")
        question1.move(20, 100)
        question1.setFixedSize(350, 50)
        question1.setWordWrap(True)
        
        min10button = QPushButton("10")
        min15button = QPushButton("15")
        min20button = QPushButton("20")
        min25button = QPushButton("25")
        min10button.clicked.connect(self.on_click)
        min15button.clicked.connect(self.on_click)
        min20button.clicked.connect(self.on_click)
        min25button.clicked.connect(self.on_click)
        
        #Minute Button Properties
        minbuttonsW = 80
        minbuttonsH = 80
        minbuttonBG = ""
        minbuttonFont = QFont("Serif", 20)
        minbuttonStyle = ("color: #ffffff;"
                            "background-color: #a37c7c;"
                            "font-weight: bold;")
        
        #Minute Button Settings
        min10button.setFont(minbuttonFont)
        min10button.setStyleSheet(minbuttonStyle)
        min15button.setFont(minbuttonFont)
        min15button.setStyleSheet(minbuttonStyle)
        min20button.setFont(minbuttonFont)
        min20button.setStyleSheet(minbuttonStyle)
        min25button.setFont(minbuttonFont)
        min25button.setStyleSheet(minbuttonStyle)
        
        min10button.setFixedSize(minbuttonsW, minbuttonsH)
        min15button.setFixedSize(minbuttonsW, minbuttonsH)
        min20button.setFixedSize(minbuttonsW, minbuttonsH)
        min25button.setFixedSize(minbuttonsW, minbuttonsH)
        buttonGrid = QGridLayout()
        buttonGrid.addWidget(min10button,0,0)
        buttonGrid.addWidget(min15button,0,1)
        buttonGrid.addWidget(min20button,0,2)
        buttonGrid.addWidget(min25button,0,3)
        self.central_widget.setLayout(buttonGrid)
        
        
    def on_click(self):
        button = self.sender()
        if button.text() == "10":
            print("10 minutes selected")
            self.central_widget.setVisible(False)
            self.showTimerUI()
            self.raiseLogo()
            
        elif button.text() == "15":
            print("15 minutes selected")
            self.central_widget.setVisible(False)
            self.showTimerUI()
            self.raiseLogo()
        elif button.text() == "20":
            print("20 minutes selected")
            self.central_widget.setVisible(False)
            self.showTimerUI()
            self.raiseLogo()
        elif button.text() == "25":
            print("25 minutes selected")
            self.central_widget.setVisible(False)
            self.showTimerUI()
            self.raiseLogo()
            
    def showTimerUI(self):
        self.timer_widget = QWidget()
        self.setCentralWidget(self.timer_widget)
        question2 = QLabel("How many repetitions till long break?", self.timer_widget)
        question2.setFont(QFont("Serif",15))
        question2.setStyleSheet("color: #000000;"
                                "background-color: #ffe8e8;"
                                "font-weight: bold;")
        question2.move(20, 100)
        question2.setFixedSize(350, 50)
        question2.setWordWrap(True)   
        
    def raiseLogo(self):
        self.label1.raise_()
        self.label2.raise_()
            
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()