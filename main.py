import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QIcon
from clock_style import Ui_Form as ClockUI

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class StopwatchWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.c = ClockUI()
        self.c.setupUi(self)

        self.init_visuals()
        self.init_clocks()
        self.init_connections()

    def stopwatch_toggle_start_pause(self):
        if self.isStopwatchRunning:
            self.stopwatch_pause()
        else:
            self.stopwatch_start()

    def stopwatch_start(self):
        if not self.timer.isActive():
            self.timer.start(1000)
        self.isStopwatchRunning = True
        self.c.startButton.setIcon(QIcon(self.pause_icon_path))
        self.c.resetButton.setVisible(True)

    def stopwatch_pause(self):
        self.isStopwatchRunning = False
        self.timer.stop()
        self.c.startButton.setIcon(QIcon(self.play_icon_path))

    def stopwatch_reset(self):
        self.pause()
        self.isStopwatchRunning = False
        self.elapsed_time = QTime(0, 0, 0)
        self.update_labels()
        self.c.resetButton.setVisible(False)

    def stopwatch_update_time(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        self.update_labels()

    def stopwatch_update_labels(self):
        hours = self.elapsed_time.hour()
        minutes = self.elapsed_time.minute()
        seconds = self.elapsed_time.second()

        self.c.hour.setText(f"{hours:02}:")
        self.c.min.setText(f"{minutes:02}")
        self.c.sec.setText(f"{seconds:02}")

    def init_visuals(self):
        self.setWindowTitle("ClockApp")
        self.setFixedSize(400, 500)

        self.play_icon_path = resource_path("res/img/play.png")
        self.pause_icon_path = resource_path("res/img/pause.png")
        self.reset_icon_path = resource_path("res/img/reset.png")
        self.clock_icon_path = resource_path("res/img/clock.png")
        self.plus_icon_path = resource_path("res/img/plus.png")

        self.setWindowIcon(QIcon(self.clock_icon_path))
        self.c.startButton.setIcon(QIcon(self.play_icon_path))
        self.c.resetButton.setIcon(QIcon(self.reset_icon_path))
        self.c.resetButton.setVisible(False)

    def init_connections(self):
        self.stopwatch.timeout.connect(self.stopwatch_update_time)
        self.c.startButton.clicked.connect(self.stopwatch_toggle_start_pause)
        self.c.resetButton.clicked.connect(self.stopwatch_reset)

    def init_clocks(self):
        self.stopwatch = QTimer(self)
        self.elapsed_time = QTime(0, 0, 0)
        self.isStopwatchRunning = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StopwatchWindow()
    window.show()
    sys.exit(app.exec())