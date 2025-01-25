import sys
import os

from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QIcon

from add_alarm_style import Ui_Dialog as AlarmUI

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class Alarm(QDialog):
    def __init__(self):
        super().__init__()

        self.init_visuals()
        self.init_connections()

        self.alarm_time = None

    def init_visuals(self):
        self.a = AlarmUI()
        self.a.setupUi(self)

        self.setWindowTitle("AddAlarm")
        self.setFixedSize(300, 300)

        self.play_icon_path = resource_path("../res/img/play.png")
        self.reset_icon_path = resource_path("../res/img/reset.png")
        self.clock_icon_path = resource_path("../res/img/clock.png")

        self.setWindowIcon(QIcon(self.clock_icon_path))
        self.a.confirmAlarm.setIcon(QIcon(self.play_icon_path))
        self.a.resetAlarm.setIcon(QIcon(self.reset_icon_path))

    def get_time(self):
        time_text = self.a.alarmValue.text()
        self.alarm_time = QTime.fromString(time_text, "HH:mm:ss")

    def add_alarm(self):
        self.get_time()
        if self.alarm_time.isValid():
            self.accept()
            QMessageBox.information(self, "Info", "Alarm added!")
        else:
            QMessageBox.warning(self, "Error", "Invalid time format! Please use HH:mm:ss.")

    def reset_alarm(self):
        self.a.alarmValue.clear()

    def init_connections(self):
        self.a.confirmAlarm.clicked.connect(self.add_alarm)
        self.a.resetAlarm.clicked.connect(self.reset_alarm)

    def get_alarm_time(self):
        return self.alarm_time