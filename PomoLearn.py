import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PomoLearn")
        self.setGeometry(700, 300, 400, 400)
        self.setWindowIcon(QIcon("pomolearnlogo.png"))
        self.setStyleSheet("background-color: #363c40")
        
        label1 = QLabel("Pomo", self)
        label1.setFont(QFont("Serif",30))
        label1.setGeometry(90, 10, 120, 50)
        label1.setStyleSheet("color: #f27718;"
                             "background-color: #272b2e;"
                             "font-weight: bold;")
        
        label2 = QLabel("Learn", self)
        label2.setFont(QFont("Serif",30))
        label2.setGeometry(205, 10, 120, 50)
        label2.setStyleSheet("color: #009dff;"
                             "background-color: #272b2e;"
                             "font-weight: bold;")
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()