import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QDialog
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QIcon
from clock_style import Ui_Form as ClockUI
from add_alarm_style import Ui_Dialog as AlarmUI
from add_timer_style import Ui_Dialog as TimerUI

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class addAlarm(QDialog):
    def __init__(self):
        super().__init__()

        self.init_visuals()
        self.init_connections()

    def init_visuals(self):
        self.a = AlarmUI()
        self.a.setupUi(self)

        self.windowTitle("addAlarm")
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

class addTimer(QDialog):
    def __init__(self):
        super().__init__()

        self.init_visuals()
        self.init_connections()

    def init_visuals(self):
        self.t = TimerUI()
        self.t.setupUi(self)

        self.windowTitle("addTimer")
        self.setFixedSize(300, 300)

        self.play_icon_path = resource_path("res/img/play.png")
        self.pause_icon_path = resource_path("res/img/pause.png")
        self.reset_icon_path = resource_path("res/img/reset.png")
        self.clock_icon_path = resource_path("res/img/clock.png")
        self.plus_icon_path = resource_path("res/img/plus.png")

        self.setWindowIcon(QIcon(self.clock_icon_path))
        self.t.confirmTimer.setIcon(QIcon(self.play_icon_path))
        self.t.resetTimer.setIcon(QIcon(self.reset_icon_path))

    def add_timer(self):
        QMessageBox.information(self, "Info", "Timer set!")

    def reset_timer(self):
        pass

    def init_connections(self):
        self.t.confirmTimer.clicked.connect(self.add_timer)
        self.t.resetTimer.clicked.connect(self.reset_timer)

class ClockApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_visuals()
        self.init_clocks()
        self.init_connections()

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
    window = ClockApp()
    window.show()
    sys.exit(app.exec())