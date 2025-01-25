import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QDialog
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

    def init_visuals(self):
        self.a = AlarmUI()
        self.a.setupUi(self)

        self.setWindowTitle("AddAlarm")
        self.setFixedSize(300, 300)

        self.play_icon_path = resource_path("res/img/play.png")
        self.pause_icon_path = resource_path("res/img/pause.png")
        self.reset_icon_path = resource_path("res/img/reset.png")
        self.clock_icon_path = resource_path("res/img/clock.png")
        self.plus_icon_path = resource_path("res/img/plus.png")

        self.setWindowIcon(QIcon(self.clock_icon_path))
        self.a.confirmAlarm.setIcon(QIcon(self.play_icon_path))
        self.a.resetAlarm.setIcon(QIcon(self.reset_icon_path))

    def add_alarm(self):
        QMessageBox.information(self, "Info", "Alarm added!")

    def reset_alarm(self):
        pass

    def init_connections(self):
        self.a.confirmAlarm.clicked.connect(self.add_alarm)
        self.a.resetAlarm.clicked.connect(self.reset_alarm)