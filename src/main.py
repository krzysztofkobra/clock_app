import sys

from PyQt5.QtWidgets import QApplication

from alarm import Alarm
from timer import Timer
from clock import ClockApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClockApp()
    window.show()
    sys.exit(app.exec())