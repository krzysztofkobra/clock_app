import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QDialog
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QIcon

from clock_style import Ui_Form as ClockUI

from timer import Timer
from alarm import Alarm

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class ClockApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_visuals()
        self.init_clocks()
        self.init_connections()

    def init_visuals(self):
        self.c = ClockUI()
        self.c.setupUi(self)

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

        self.c.startTimer.setIcon(QIcon(self.play_icon_path))
        self.c.resetTimer.setIcon(QIcon(self.reset_icon_path))
        self.c.addTimer.setIcon(QIcon(self.plus_icon_path))

        self.c.addAlarm.setIcon(QIcon(self.plus_icon_path))

        self.c.resetButton.setVisible(False)
        self.c.deleteAlarm.setVisible(False)
        self.c.alarmSwitch.setVisible(False)
        self.c.resetTimer.setVisible(False)

    def init_connections(self):
        self.stopwatch.timeout.connect(self.stopwatch_update_time)
        self.timer.timeout.connect(self.timer_tick)

        self.c.startButton.clicked.connect(self.stopwatch_toggle_start_pause)
        self.c.resetButton.clicked.connect(self.stopwatch_reset)

        self.c.addTimer.clicked.connect(self.open_timer_dialog)
        self.c.startTimer.clicked.connect(self.timer_toggle_start_pause)
        self.c.plusButton.clicked.connect(self.add_30)
        self.c.resetTimer.clicked.connect(self.timer_reset)

    def init_clocks(self):
        self.stopwatch = QTimer(self)
        self.timer = QTimer(self)

        self.elapsed_time = QTime(0, 0, 0)
        self.timer_time = QTime(0, 0, 0)

        self.isStopwatchRunning = False
        self.isAlarmOn = False
        self.isTimerRunning = False

    def stopwatch_toggle_start_pause(self):
        if self.isStopwatchRunning:
            self.stopwatch_pause()
        else:
            self.stopwatch_start()

    def stopwatch_start(self):
        if not self.stopwatch.isActive():
            self.stopwatch.start(1000)
        self.isStopwatchRunning = True
        self.c.startButton.setIcon(QIcon(self.pause_icon_path))
        self.c.resetButton.setVisible(True)

    def stopwatch_pause(self):
        self.isStopwatchRunning = False
        self.stopwatch.stop()
        self.c.startButton.setIcon(QIcon(self.play_icon_path))

    def stopwatch_reset(self):
        self.stopwatch_pause()
        self.isStopwatchRunning = False
        self.elapsed_time = QTime(0, 0, 0)
        self.stopwatch_update_labels()
        self.c.resetButton.setVisible(False)

    def stopwatch_update_time(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        self.stopwatch_update_labels()

    def stopwatch_update_labels(self):
        hours = self.elapsed_time.hour()
        minutes = self.elapsed_time.minute()
        seconds = self.elapsed_time.second()

        self.c.hour.setText(f"{hours:02}:")
        self.c.min.setText(f"{minutes:02}")
        self.c.sec.setText(f"{seconds:02}")

    def open_timer_dialog(self):
        dialog = Timer()
        if dialog.exec() == QDialog.Accepted:
            self.timer_time = dialog.get_timer_time()
            if self.timer_time.isValid():
                self.timer_update_labels()
                self.c.resetTimer.setVisible(True)

    def timer_update_labels(self):
        self.timer_h = self.timer_time.hour()
        self.timer_m = self.timer_time.minute()
        self.timer_s = self.timer_time.second()

        self.c.hour_2.setText(f"{self.timer_h:02}:")
        self.c.min_2.setText(f"{self.timer_m:02}")
        self.c.sec_2.setText(f"{self.timer_s:02}")

    def timer_toggle_start_pause(self):
        if self.isTimerRunning:
            self.timer_pause()
        else:
            self.timer_start()

    def timer_pause(self):
        self.isTimerRunning = False
        self.c.startTimer.setIcon(QIcon(self.play_icon_path))

    def timer_start(self):
        if not self.timer.isActive():
            self.timer.start(1000)
            self.isTimerRunning = True
            self.c.startTimer.setIcon(QIcon(self.pause_icon_path))

    def timer_reset(self):
        self.timer_pause()
        self.timer_time = QTime(0, 0, 0)
        self.timer_update_labels()
        self.c.resetTimer.setVisible(False)

    def timer_stop(self):
        print("a loud sound boom")
        self.timer.stop()
        self.c.startTimer.setIcon(QIcon(self.play_icon_path))
        self.c.resetTimer.setVisible(False)
        QMessageBox.information(self, "Timer", "Time's up!")

    def timer_tick(self):
        if self.timer_time == QTime(0, 0, 0):
            self.timer_stop()
            return

        self.timer_time = self.timer_time.addSecs(-1)
        self.timer_update_labels()

    def add_30(self):
        self.timer_time = self.timer_time.addSecs(30)
        self.timer_update_labels()
        self.c.resetTimer.setVisible(True)