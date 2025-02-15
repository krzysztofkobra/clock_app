import sys
import os

from PyQt5.QtWidgets import QWidget, QMessageBox, QDialog, QFileDialog
from PyQt5.QtCore import QTimer, QTime, QUrl, QSettings, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

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
        self.setFixedSize(400, 550)

        self.play_icon_path = resource_path("res/img/play.png")
        self.pause_icon_path = resource_path("res/img/pause.png")
        self.reset_icon_path = resource_path("res/img/reset.png")
        self.clock_icon_path = resource_path("res/img/clock.png")
        self.plus_icon_path = resource_path("res/img/plus.png")
        self.circle_icon_path = resource_path("res/img/circle.png")
        self.cross_icon_path = resource_path("res/img/cross.png")
        settings_icon_path = resource_path("res/img/settings.png")

        self.setWindowIcon(QIcon(self.clock_icon_path))
        self.c.startButton.setIcon(QIcon(self.play_icon_path))
        self.c.resetButton.setIcon(QIcon(self.reset_icon_path))

        self.c.startTimer.setIcon(QIcon(self.play_icon_path))
        self.c.resetTimer.setIcon(QIcon(self.reset_icon_path))
        self.c.addTimer.setIcon(QIcon(self.plus_icon_path))

        self.c.addAlarm.setIcon(QIcon(self.plus_icon_path))
        self.c.deleteAlarm.setIcon(QIcon(self.cross_icon_path))

        self.c.resetButton.setVisible(False)
        self.c.resetTimer.setVisible(False)

        self.c.deleteAlarm.setVisible(False)
        self.c.alarmSwitch.setVisible(False)

        self.c.setRingPhoneButton.setIcon(QIcon(settings_icon_path))

    def init_connections(self):
        self.stopwatch.timeout.connect(self.stopwatch_update_time)
        self.timer.timeout.connect(self.timer_tick)
        self.alarm_timer.timeout.connect(self.alarm)

        self.c.startButton.clicked.connect(self.stopwatch_toggle_start_pause)
        self.c.resetButton.clicked.connect(self.stopwatch_reset)

        self.c.addTimer.clicked.connect(self.open_timer_dialog)
        self.c.startTimer.clicked.connect(self.timer_toggle_start_pause)
        self.c.plusButton.clicked.connect(self.add_30)
        self.c.resetTimer.clicked.connect(self.timer_reset)

        self.c.addAlarm.clicked.connect(self.open_alarm_dialog)
        self.c.alarmSwitch.clicked.connect(self.alarm_switch_state)
        self.c.deleteAlarm.clicked.connect(self.alarm_delete)

        self.c.setRingPhoneButton.clicked.connect(self.set_ringtone)
        self.set_ringtone_name()

    def init_clocks(self):
        self.stopwatch = QTimer(self)
        self.timer = QTimer(self)
        self.alarm_timer = QTimer(self)

        self.elapsed_time = QTime(0, 0, 0)
        self.timer_time = QTime(0, 0, 0)
        self.alarm_time = QTime(0, 0, 0)

        self.isStopwatchRunning = False
        self.isAlarmOn = False
        self.isTimerRunning = False

        self.c.startTimer.setEnabled(False)

        self.player = QMediaPlayer(self)
        self.settings = QSettings("krzysztofkobra", "ClockApp")
        self.ringtone = self.settings.value("last_ringtone", None)
        self.default_ringtone = resource_path("res/audio/default.mp3")
        if self.ringtone is None:
            self.ringtone = self.default_ringtone

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
        self.update_labels(self.elapsed_time, self.c.hour, self.c.min, self.c.sec)
        self.c.resetButton.setVisible(False)

    def stopwatch_update_time(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        self.update_labels(self.elapsed_time, self.c.hour, self.c.min, self.c.sec)

    def open_timer_dialog(self):
        dialog = Timer()
        if dialog.exec() == QDialog.Accepted:
            self.timer_time = dialog.get_timer_time()
            self.update_labels(self.timer_time, self.c.hour_2, self.c.min_2, self.c.sec_2)
            if self.timer_time != QTime(0, 0, 0):
                self.c.resetTimer.setVisible(True)
                self.c.startTimer.setEnabled(True)

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
        self.update_labels(self.timer_time, self.c.hour_2, self.c.min_2, self.c.sec_2)

        self.c.resetTimer.setVisible(False)
        self.c.resetTimer.setEnabled(False)
        self.c.startTimer.setEnabled(False)

    def timer_stop(self):
        self.timer.stop()
        self.handle_ringtone()

        self.c.startTimer.setIcon(QIcon(self.play_icon_path))
        self.c.resetTimer.setVisible(False)
        self.c.resetTimer.setEnabled(False)

    def timer_tick(self):
        if self.timer_time == QTime(0, 0, 0):
            self.c.startTimer.setEnabled(False)
            self.timer_stop()
            return

        self.timer_time = self.timer_time.addSecs(-1)
        self.update_labels(self.timer_time, self.c.hour_2, self.c.min_2, self.c.sec_2)

    def add_30(self):
        self.timer_time = self.timer_time.addSecs(30)
        self.update_labels(self.timer_time, self.c.hour_2, self.c.min_2, self.c.sec_2)
        self.c.resetTimer.setVisible(True)
        self.c.resetTimer.setEnabled(True)
        self.c.startTimer.setEnabled(True)

    def open_alarm_dialog(self):
        dialog = Alarm()
        if dialog.exec() == QDialog.Accepted:
            self.alarm_time = dialog.get_alarm_time()
            self.update_labels(self.alarm_time, self.c.hour_3, self.c.min_3, self.c.sec_3)

            self.c.deleteAlarm.setVisible(True)
            self.c.alarmSwitch.setVisible(True)

            self.c.deleteAlarm.setEnabled(True)
            self.c.alarmSwitch.setEnabled(True)

            self.alarm_timer.start(1000)

            self.isAlarmOn = True
            self.c.alarmSwitch.setIcon(QIcon(self.circle_icon_path))

    def alarm_switch_state(self):
        if self.isAlarmOn:
            self.isAlarmOn = False
            self.c.alarmSwitch.setIcon(QIcon())
        else:
            self.isAlarmOn = True
            self.c.alarmSwitch.setIcon(QIcon(self.circle_icon_path))

    def alarm_delete(self):
        self.isAlarmOn = False
        self.alarm_time = QTime(0, 0, 0)

        self.c.deleteAlarm.setVisible(False)
        self.c.alarmSwitch.setVisible(False)

        self.update_labels(self.alarm_time, self.c.hour_3, self.c.min_3, self.c.sec_3)

        QMessageBox.information(self, "Alarm", "Alarm deleted!")

    def alarm(self):
        current_time = QTime.currentTime()
        current_hours = current_time.hour()
        current_minutes = current_time.minute()
        current_seconds = current_time.second()

        if (self.alarm_h == current_hours and
            self.alarm_m == current_minutes and
            self.alarm_s == current_seconds and
            self.isAlarmOn):

            self.isAlarmOn = False
            self.alarm_time = QTime(0, 0, 0)
            self.alarm_timer.stop()

            self.handle_ringtone()

            self.c.deleteAlarm.setVisible(False)
            self.c.alarmSwitch.setVisible(False)

            self.update_labels(self.alarm_time, self.c.hour_3, self.c.min_3, self.c.sec_3)

    def update_labels(self, time_obj, hour_label, min_label, sec_label):
        h = time_obj.hour()
        m = time_obj.minute()
        s = time_obj.second()
        hour_label.setText(f"{h:02}:")
        min_label.setText(f"{m:02}")
        sec_label.setText(f"{s:02}")

    def set_ringtone(self):
        ringtone_file, _ = QFileDialog.getOpenFileName(
            self, "Choose ringtone file", "", "Audio files (*.mp3 *.wav)"
        )

        if ringtone_file:
            self.settings.setValue("last_ringtone", ringtone_file)
            self.ringtone = ringtone_file
            print(f"Ringtone file selected: {ringtone_file}")
            self.set_ringtone_name()
        else:
            print("No ringtone file selected.")

    #spaghetti code
    def handle_ringtone(self):
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.ringtone)))
        self.player.play()

        msg = QMessageBox()
        msg.setWindowTitle("Alarm!")
        msg.setText("Time's up!")
        msg.setStandardButtons(QMessageBox.Ok)

        self.player.mediaStatusChanged.connect(self.handle_media_status)

        msg.exec()

        self.player.mediaStatusChanged.disconnect(self.handle_media_status)
        self.player.stop()

    def handle_media_status(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.player.stop()
            self.player.play()

    def set_ringtone_name(self):
        filename = os.path.basename(self.ringtone)
        name = filename.rsplit('.', 1)[0]
        fm = self.c.currentRingPhone.fontMetrics()
        elided = fm.elidedText(name, Qt.ElideRight, 250)
        self.c.currentRingPhone.setText(elided)