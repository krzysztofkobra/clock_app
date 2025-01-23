import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QIcon
from stoper_widget import Ui_Form as StoperUI

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class StopwatchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.s = StoperUI()
        self.s.setupUi(self)

        self.play_icon_path = resource_path("res/img/play.png")
        self.pause_icon_path = resource_path("res/img/pause.png")
        self.reset_icon_path = resource_path("res/img/reset.png")
        self.clock_icon_path = resource_path("res/img/clock.png")

        self.setWindowIcon(QIcon(self.clock_icon_path))
        self.s.startButton.setIcon(QIcon(self.play_icon_path))
        self.s.resetButton.setIcon(QIcon(self.reset_icon_path))
        self.s.resetButton.setVisible(False)

        self.setWindowTitle("Stopwatch")
        self.setFixedSize(400, 500)

        self.timer = QTimer(self)
        self.elapsed_time = QTime(0, 0, 0)
        self.isRunning = False

        self.timer.timeout.connect(self.update_time)

        self.s.startButton.clicked.connect(self.toggle_start_pause)
        self.s.resetButton.clicked.connect(self.reset)

    def toggle_start_pause(self):
        if self.isRunning:
            self.pause()
        else:
            self.start()

    def start(self):
        if not self.timer.isActive():
            self.timer.start(1000)
        self.isRunning = True
        self.s.startButton.setIcon(QIcon(self.pause_icon_path))
        self.s.resetButton.setVisible(True)

    def pause(self):
        self.isRunning = False
        self.timer.stop()
        self.s.startButton.setIcon(QIcon(self.play_icon_path))

    def reset(self):
        self.pause()
        self.isRunning = False
        self.elapsed_time = QTime(0, 0, 0)
        self.update_labels()
        self.s.resetButton.setVisible(False)

    def update_time(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        self.update_labels()

    def update_labels(self):
        self.hours = self.elapsed_time.hour()
        self.minutes = self.elapsed_time.minute()
        self.seconds = self.elapsed_time.second()

        self.s.hour.setText(f"{self.hours:02}:")
        self.s.min.setText(f"{self.minutes:02}")
        self.s.sec.setText(f"{self.seconds:02}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StopwatchWindow()
    window.show()
    sys.exit(app.exec())