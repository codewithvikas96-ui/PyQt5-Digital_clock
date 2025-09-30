import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.setGeometry(600,400,300,100)
        self.digital_clock_UI()

    def digital_clock_UI(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        self.time_label = QLabel()
        self.time_label.setStyleSheet("font-size: 50px; font-family:  Helvetica; color: hsl(111, 100%, 50%);")
        self.setStyleSheet("background-color: black;")
        main_layout.addWidget(self.time_label)

        central_widget.setLayout(main_layout)  
        self.setCentralWidget(central_widget)

        self.timer = QTimer()
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        self.show_time()

    def show_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")  
        self.time_label.setText(current_time)

def main():
    app = QApplication(sys.argv)
    my_window = Window()
    my_window.show()
    sys.exit(app.exec_())

main()
