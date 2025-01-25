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
        self.pause_icon_path = resource_path("res/img/pause.png")
        self.reset_icon_path = resource_path("res/img/reset.png")
        self.clock_icon_path = resource_path("res/img/clock.png")
        self.plus_icon_path = resource_path("res/img/plus.png")

        self.setWindowIcon(QIcon(self.clock_icon_path))
        self.t.confirmTimer.setIcon(QIcon(self.play_icon_path))
        self.t.resetTimer.setIcon(QIcon(self.reset_icon_path))

    def init_connections(self):
        self.t.confirmTimer.clicked.connect(self.add_timer)
        self.t.resetTimer.clicked.connect(self.reset_timer)
        self.t.plusHalf.clicked.connect(self.add_30)
        self.t.plusOne.clicked.connect(self.add_1)
        self.t.plusFive.clicked.connect(self.add_5)

    def add_timer(self):
        self.get_time()
        if self.timer_time.isValid():
            self.accept()
            QMessageBox.information(self, "Info", "Timer set!")
        else:
            QMessageBox.warning(self, "Error", "Invalid time format! Please use HH:mm:ss.")

    def add_30(self):
        self.get_time()
        new_time = self.timer_time.addSecs(30)
        self.t.time.setText(new_time.toString("HH:mm:ss"))

    def add_1(self):
        self.get_time()
        new_time = self.timer_time.addSecs(60)
        self.t.time.setText(new_time.toString("HH:mm:ss"))

    def add_5(self):
        self.get_time()
        new_time = self.timer_time.addSecs(300)
        self.t.time.setText(new_time.toString("HH:mm:ss"))

    def get_time(self):
        time_text = self.t.time.text()
        self.timer_time = QTime.fromString(time_text, "HH:mm:ss")

    def get_timer_time(self):
        return self.timer_time

    def reset_timer(self):
        self.t.time.setText("00:00:00")

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

    def init_connections(self):
        self.stopwatch.timeout.connect(self.stopwatch_update_time)
        self.c.startButton.clicked.connect(self.stopwatch_toggle_start_pause)
        self.c.resetButton.clicked.connect(self.stopwatch_reset)

        self.c.addTimer.clicked.connect(self.open_timer_dialog)
        self.c.startTimer.clicked.connect(self.timer_toggle_start_pause)

    def init_clocks(self):
        self.stopwatch = QTimer(self)
        self.elapsed_time = QTime(0, 0, 0)

        self.isStopwatchRunning = False
        self.isAlarmSet = False
        self.isTimerRunning = False

    def timer_toggle_start_pause(self):
        pass

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
            time_text = dialog.get_timer_time()
            if time_text.isValid():
                self.timer_h = time_text.hour()
                self.timer_m = time_text.minute()
                self.timer_s = time_text.second()
                self.timer_update_labels()

    def timer_update_labels(self):
        self.c.hour_2.setText(f"{self.timer_h:02}:")
        self.c.min_2.setText(f"{self.timer_m:02}")
        self.c.sec_2.setText(f"{self.timer_s:02}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClockApp()
    window.show()
    sys.exit(app.exec())