import sys
import os

from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QIcon

from add_timer_style import Ui_Dialog as TimerUI

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class Timer(QDialog):
    def __init__(self):
        super().__init__()

        self.init_visuals()
        self.init_connections()

        self.timer_time = None

    def init_visuals(self):
        self.t = TimerUI()
        self.t.setupUi(self)

        self.setWindowTitle("AddTimer")
        self.setFixedSize(300, 300)

        self.play_icon_path = resource_path("res/img/play.png")
        self.reset_icon_path = resource_path("res/img/reset.png")
        self.clock_icon_path = resource_path("res/img/clock.png")

        self.setWindowIcon(QIcon(self.clock_icon_path))
        self.t.confirmTimer.setIcon(QIcon(self.play_icon_path))
        self.t.resetTimer.setIcon(QIcon(self.reset_icon_path))

    def init_connections(self):
        self.t.confirmTimer.clicked.connect(self.add_timer)
        self.t.resetTimer.clicked.connect(self.reset_timer)
        self.t.plusHalf.clicked.connect(lambda: self.update_timer(30))
        self.t.plusOne.clicked.connect(lambda: self.update_timer(60))
        self.t.plusFive.clicked.connect(lambda: self.update_timer(300))

    def add_timer(self):
        self.get_time()
        if self.timer_time.isValid():
            self.accept()
            if self.timer_time != QTime(0, 0, 0):
                QMessageBox.information(self, "Info", "Timer set!")
        else:
            QMessageBox.warning(self, "Error", "Invalid time format! Please use HH:mm:ss.")

    def update_timer(self, seconds):
        self.get_time()
        new_time = self.timer_time.addSecs(seconds)
        self.t.time.setText(new_time.toString("HH:mm:ss"))

    def get_time(self):
        time_text = self.t.time.text()
        self.timer_time = QTime.fromString(time_text, "HH:mm:ss")

    def get_timer_time(self):
        return self.timer_time

    def reset_timer(self):
        self.t.time.setText("00:00:00")