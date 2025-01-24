from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 500)
        Form.setStyleSheet("background-color: rgb(53, 53, 53);\n"
"color: rgb(236, 236, 236);\n"
"")
        self.startButton = QtWidgets.QPushButton(Form)
        self.startButton.setGeometry(QtCore.QRect(25, 40, 75, 75))
        self.startButton.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"                border-radius: 30px;        \n"
"                border: 2px solid rgb(236, 236, 236);")
        self.startButton.setText("")
        self.startButton.setObjectName("startButton")
        self.min = QtWidgets.QLabel(Form)
        self.min.setGeometry(QtCore.QRect(293, 30, 60, 70))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.min.setFont(font)
        self.min.setStyleSheet("background-color: transparent")
        self.min.setObjectName("min")
        self.sec = QtWidgets.QLabel(Form)
        self.sec.setGeometry(QtCore.QRect(300, 70, 40, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sec.setFont(font)
        self.sec.setStyleSheet("background-color: transparent;")
        self.sec.setObjectName("sec")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(215, 25, 150, 110))
        self.frame.setStyleSheet("background-color: transparent; \n"
"    border: 5px solid rgb(236, 236, 236);     \n"
"    border-radius: 50%;            \n"
"    ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.hour = QtWidgets.QLabel(Form)
        self.hour.setGeometry(QtCore.QRect(250, 30, 50, 70))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.hour.setFont(font)
        self.hour.setStyleSheet("background-color: transparent")
        self.hour.setObjectName("hour")
        self.resetButton = QtWidgets.QPushButton(Form)
        self.resetButton.setGeometry(QtCore.QRect(125, 60, 40, 40))
        self.resetButton.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"                border-radius: 15px;        \n"
"               border: 2px solid rgb(236, 236, 236);\n"
"hover{\n"
"    background-color: rgb(175, 175, 175)\n"
"}\n"
"    ")
        self.resetButton.setText("")
        self.resetButton.setObjectName("resetButton")
        self.startButton2 = QtWidgets.QPushButton(Form)
        self.startButton2.setGeometry(QtCore.QRect(25, 210, 75, 75))
        self.startButton2.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"                border-radius: 30px;        \n"
"                border: 2px solid rgb(236, 236, 236);")
        self.startButton2.setText("")
        self.startButton2.setObjectName("startButton2")
        self.resetButton2 = QtWidgets.QPushButton(Form)
        self.resetButton2.setGeometry(QtCore.QRect(125, 230, 40, 40))
        self.resetButton2.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"                border-radius: 15px;        \n"
"               border: 2px solid rgb(236, 236, 236);\n"
"hover{\n"
"    background-color: rgb(175, 175, 175)\n"
"}\n"
"    ")
        self.resetButton2.setText("")
        self.resetButton2.setObjectName("resetButton2")
        self.min_2 = QtWidgets.QLabel(Form)
        self.min_2.setGeometry(QtCore.QRect(293, 200, 60, 70))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.min_2.setFont(font)
        self.min_2.setStyleSheet("background-color: transparent")
        self.min_2.setObjectName("min_2")
        self.hour_2 = QtWidgets.QLabel(Form)
        self.hour_2.setGeometry(QtCore.QRect(250, 200, 50, 70))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.hour_2.setFont(font)
        self.hour_2.setStyleSheet("background-color: transparent")
        self.hour_2.setObjectName("hour_2")
        self.sec_2 = QtWidgets.QLabel(Form)
        self.sec_2.setGeometry(QtCore.QRect(300, 240, 40, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sec_2.setFont(font)
        self.sec_2.setStyleSheet("background-color: transparent;")
        self.sec_2.setObjectName("sec_2")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(215, 195, 150, 110))
        self.frame_2.setStyleSheet("background-color: transparent; \n"
"    border: 5px solid rgb(236, 236, 236);     \n"
"    border-radius: 50%;            \n"
"    ")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.plusButton = QtWidgets.QPushButton(self.frame_2)
        self.plusButton.setEnabled(False)
        self.plusButton.setGeometry(QtCore.QRect(30, 60, 50, 35))
        self.plusButton.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"                border-radius: 15px;        \n"
"               border: 2px solid rgb(236, 236, 236);\n"
"hover{\n"
"    background-color: rgb(175, 175, 175)\n"
"}\n"
"    ")
        self.plusButton.setText("")
        self.plusButton.setObjectName("plusButton")
        self.addAlarmButton = QtWidgets.QPushButton(Form)
        self.addAlarmButton.setGeometry(QtCore.QRect(25, 380, 75, 75))
        self.addAlarmButton.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"                border-radius: 30px;        \n"
"                border: 2px solid rgb(236, 236, 236);")
        self.addAlarmButton.setText("")
        self.addAlarmButton.setObjectName("addAlarmButton")
        self.deleteAlarmButton = QtWidgets.QPushButton(Form)
        self.deleteAlarmButton.setEnabled(False)
        self.deleteAlarmButton.setGeometry(QtCore.QRect(125, 420, 40, 40))
        self.deleteAlarmButton.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"                border-radius: 15px;        \n"
"               border: 2px solid rgb(236, 236, 236);\n"
"hover{\n"
"    background-color: rgb(175, 175, 175)\n"
"}\n"
"    ")
        self.deleteAlarmButton.setText("")
        self.deleteAlarmButton.setObjectName("deleteAlarmButton")
        self.confirmAlarmButton = QtWidgets.QPushButton(Form)
        self.confirmAlarmButton.setEnabled(False)
        self.confirmAlarmButton.setGeometry(QtCore.QRect(125, 375, 40, 40))
        self.confirmAlarmButton.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"                border-radius: 15px;        \n"
"               border: 2px solid rgb(236, 236, 236);\n"
"hover{\n"
"    background-color: rgb(175, 175, 175)\n"
"}\n"
"    ")
        self.confirmAlarmButton.setText("")
        self.confirmAlarmButton.setObjectName("confirmAlarmButton")
        self.min_3 = QtWidgets.QLabel(Form)
        self.min_3.setGeometry(QtCore.QRect(298, 365, 60, 70))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.min_3.setFont(font)
        self.min_3.setStyleSheet("background-color: transparent")
        self.min_3.setObjectName("min_3")
        self.hour_3 = QtWidgets.QLabel(Form)
        self.hour_3.setGeometry(QtCore.QRect(255, 365, 50, 70))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.hour_3.setFont(font)
        self.hour_3.setStyleSheet("background-color: transparent")
        self.hour_3.setObjectName("hour_3")
        self.sec_3 = QtWidgets.QLabel(Form)
        self.sec_3.setGeometry(QtCore.QRect(305, 405, 40, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sec_3.setFont(font)
        self.sec_3.setStyleSheet("background-color: transparent;")
        self.sec_3.setObjectName("sec_3")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(220, 360, 150, 110))
        self.frame_3.setStyleSheet("background-color: transparent; \n"
"    border: 5px solid rgb(236, 236, 236);     \n"
"    border-radius: 50%;            \n"
"    ")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame.raise_()
        self.startButton.raise_()
        self.min.raise_()
        self.sec.raise_()
        self.hour.raise_()
        self.resetButton.raise_()
        self.startButton2.raise_()
        self.resetButton2.raise_()
        self.min_2.raise_()
        self.hour_2.raise_()
        self.sec_2.raise_()
        self.frame_2.raise_()
        self.addAlarmButton.raise_()
        self.deleteAlarmButton.raise_()
        self.confirmAlarmButton.raise_()
        self.min_3.raise_()
        self.hour_3.raise_()
        self.sec_3.raise_()
        self.frame_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.min.setText(_translate("Form", "00"))
        self.sec.setText(_translate("Form", "00"))
        self.hour.setText(_translate("Form", "00:"))
        self.min_2.setText(_translate("Form", "00"))
        self.hour_2.setText(_translate("Form", "00:"))
        self.sec_2.setText(_translate("Form", "00"))
        self.min_3.setText(_translate("Form", "00"))
        self.hour_3.setText(_translate("Form", "00:"))
        self.sec_3.setText(_translate("Form", "00"))
