from distutils.command.build_clib import build_clib
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt
import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
import serial
import matplotlib.pyplot as plt
import random
from serial import *
import turtle
import time
import sys
from collections import deque
from threading import Thread
import threading
#
left_val = 0
right_val = 0
front_val = 0
bottom_val = 0
ser = serial.Serial('COM4', baudrate=115200, timeout=0.1)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(254, 30, 101, 41))
        self.StartButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(100, 100, 100);")
        self.StartButton.setObjectName("StartButton")
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(420, 30, 101, 41))
        self.StopButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(100, 100, 100);")
        self.StopButton.setObjectName("StopButton")
        self.labelRight = QtWidgets.QLabel(self.centralwidget)
        self.labelRight.setGeometry(QtCore.QRect(40, 160, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelRight.setFont(font)
        self.labelRight.setObjectName("labelRight")
        self.labelTop = QtWidgets.QLabel(self.centralwidget)
        self.labelTop.setGeometry(QtCore.QRect(40, 203, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelTop.setFont(font)
        self.labelTop.setObjectName("labelTop")
        self.labelBottom = QtWidgets.QLabel(self.centralwidget)
        self.labelBottom.setGeometry(QtCore.QRect(40, 245, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelBottom.setFont(font)
        self.labelBottom.setObjectName("labelBottom")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(320, 290, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.labelCleaningProgress = QtWidgets.QLabel(self.centralwidget)
        self.labelCleaningProgress.setGeometry(QtCore.QRect(40, 290, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCleaningProgress.setFont(font)
        self.labelCleaningProgress.setObjectName("labelCleaningProgress")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 410, 47, 13))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.labelCleaningProgress_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelCleaningProgress_2.setGeometry(QtCore.QRect(20, 520, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCleaningProgress_2.setFont(font)
        self.labelCleaningProgress_2.setObjectName("labelCleaningProgress_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 100, 411, 261))
        self.groupBox.setObjectName("groupBox")
        self.lcdNumberLeft = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumberLeft.setGeometry(QtCore.QRect(330, 20, 64, 23))
        self.lcdNumberLeft.setObjectName("lcdNumberLeft")
        self.labelLeft = QtWidgets.QLabel(self.groupBox)
        self.labelLeft.setGeometry(QtCore.QRect(10, 20, 281, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.labelLeft.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelLeft.setFont(font)
        self.labelLeft.setObjectName("labelLeft")
        self.lcdNumberRight = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumberRight.setGeometry(QtCore.QRect(330, 60, 64, 23))
        self.lcdNumberRight.setObjectName("lcdNumberRight")
        self.lcdNumberBottom = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumberBottom.setGeometry(QtCore.QRect(330, 140, 64, 23))
        self.lcdNumberBottom.setObjectName("lcdNumberBottom")
        self.lcdNumberTop = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumberTop.setGeometry(QtCore.QRect(330, 100, 64, 23))
        self.lcdNumberTop.setObjectName("lcdNumberTop")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 410, 411, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.labelRight_2 = QtWidgets.QLabel(self.groupBox_2)
        self.labelRight_2.setGeometry(QtCore.QRect(20, 30, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelRight_2.setFont(font)
        self.labelRight_2.setObjectName("labelRight_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(320, 40, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.labelRight_3 = QtWidgets.QLabel(self.groupBox_2)
        self.labelRight_3.setGeometry(QtCore.QRect(300, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelRight_3.setFont(font)
        self.labelRight_3.setStyleSheet("color: rgb(255, 255, 0);")
        self.labelRight_3.setObjectName("labelRight_3")
        self.PositionLabel = QtWidgets.QLabel(self.centralwidget)
        self.PositionLabel.setGeometry(QtCore.QRect(270, 522, 101, 31))
        self.PositionLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.PositionLabel.setObjectName("PositionLabel")
        self.Pos = QtWidgets.QLabel(self.centralwidget)
        self.Pos.setGeometry(QtCore.QRect(380, 525, 121, 21))
        self.Pos.setStyleSheet("color: rgb(255, 0, 255);")
        self.Pos.setObjectName("Pos")
        self.Current_overlap = QtWidgets.QLabel(self.centralwidget)
        self.Current_overlap.setGeometry(QtCore.QRect(500, 530, 101, 20))
        self.Current_overlap.setStyleSheet("color: rgb(255, 255, 255);")
        self.Current_overlap.setObjectName("Current_overlap")
        self.Overlap = QtWidgets.QLabel(self.centralwidget)
        self.Overlap.setGeometry(QtCore.QRect(600, 530, 47, 13))
        self.Overlap.setStyleSheet("color: rgb(170, 85, 255);")
        self.Overlap.setObjectName("Overlap")
        self.ReturnHomeButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReturnHomeButton.setGeometry(QtCore.QRect(580, 30, 101, 41))
        self.ReturnHomeButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(100, 100, 100);")
        self.ReturnHomeButton.setObjectName("ReturnHomeButton")
        self.groupBox.raise_()
        self.StartButton.raise_()
        self.StopButton.raise_()
        self.labelRight.raise_()
        self.labelTop.raise_()
        self.labelBottom.raise_()
        self.progressBar.raise_()
        self.labelCleaningProgress.raise_()
        self.label_6.raise_()
        self.labelCleaningProgress_2.raise_()
        self.groupBox_2.raise_()
        self.PositionLabel.raise_()
        self.Pos.raise_()
        self.Current_overlap.raise_()
        self.Overlap.raise_()
        self.ReturnHomeButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuEPR400_ICK2 = QtWidgets.QMenu(self.menubar)
        self.menuEPR400_ICK2.setObjectName("menuEPR400_ICK2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuEPR400_ICK2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        '''My Code'''
        # self.StartButton.clicked.connect(self.StartClick)
        # self.StopButton.clicked.connect(self.StopClick)
        self._update_timer = QtCore.QTimer()
        self._update_timer.timeout.connect(self.print_distance)
        self._update_timer.start(0.1)

        self.StartButton.clicked.connect(self.StartClick)
        self.StopButton.clicked.connect(self.StopClick)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StartButton.setText(_translate("MainWindow", "START"))
        self.StopButton.setText(_translate("MainWindow", "STOP"))
        self.labelRight.setText(_translate("MainWindow", "Distance From Right Frame (cm):"))
        self.labelTop.setText(_translate("MainWindow", "Distance From Top Frame (cm):"))
        self.labelBottom.setText(_translate("MainWindow", "Distance From Bottom Frame (cm):"))
        self.labelCleaningProgress.setText(_translate("MainWindow", "Cleaning Progress:"))
        self.labelCleaningProgress_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">STARTED</span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Position Data"))
        self.labelLeft.setText(_translate("MainWindow", "Distance From Left Frame (cm):"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Contamination Data"))
        self.labelRight_2.setText(_translate("MainWindow", "Contamination Detected?"))
        self.labelRight_3.setText(_translate("MainWindow", "YES or NO"))
        self.PositionLabel.setText(_translate("MainWindow", "Current Position:"))
        self.Pos.setText(_translate("MainWindow", "Pos"))
        self.Current_overlap.setText(_translate("MainWindow", "Current Overlap:"))
        self.Overlap.setText(_translate("MainWindow", "Overlap"))
        self.ReturnHomeButton.setText(_translate("MainWindow", "Return Home"))
        self.menuEPR400_ICK2.setTitle(_translate("MainWindow", "EPR400 ICK2"))


    def StartClick(self, MainWindow):
        self.labelCleaningProgress_2.setText("Cleaning Started!")
        # global plotting_Flag
        plotting_Flag = 1
        ser.write(plotting_Flag)
        print(plotting_Flag)


    def StopClick(self, MainWindow):
        self.labelCleaningProgress_2.setText("Cleaning Stopped!")
        # global plotting_Flag
        plotting_Flag = 0
        ser.write(plotting_Flag)
        print(plotting_Flag)

    def Left_LCD_change(self, value):
        self.lcdNumberLeft.display(value)


    def Right_LCD_change(self, value):
        self.lcdNumberRight.display(value)


    def Top_LCD_change(self, value):
        self.lcdNumberTop.display(value)


    def Bottom_LCD_change(self, value):
        self.lcdNumberBottom.display(value)

    def checkValue(self, lefter, righter, fronter, bottomer):
        if (lefter > 12) and (righter < 12) and (fronter > 12) and (bottomer < 12):
            self.Pos.setText('Bottom Right')
        elif (lefter > 12) and (righter < 12) and (fronter > 12) and (bottomer > 12):
            self.Pos.setText('Right')
        elif (lefter > 12) and (righter < 12) and (fronter < 12) and (bottomer > 12):
            self.Pos.setText('Top Right')
        elif (lefter > 12) and (righter > 12) and (fronter > 12) and (bottomer > 12):
            self.Pos.setText('Middle')
        elif (lefter > 12) and (righter > 12) and (fronter > 12) and (bottomer < 12):
            self.Pos.setText('Bottom')
        elif (lefter > 12) and (righter > 12) and (fronter < 12) and (bottomer > 12):
            self.Pos.setText('Top')
        elif (lefter < 12) and (righter > 12) and (fronter > 12) and (bottomer < 12):
            self.Pos.setText('Bottom Left')
        elif (lefter < 12) and (righter > 12) and (fronter > 12) and (bottomer > 12):
            self.Pos.setText('Left')
        elif (lefter < 12) and (righter > 12) and (fronter < 12) and (bottomer > 12):
            self.Pos.setText('Top Left')


    def print_distance(self):

        global left_val
        global right_val
        global front_val
        global bottom_val

        data = ser.readline()
        print(data)

        if 'LV' in data.decode():
            left_decoded = data.decode()
            left = left_decoded.split(' ')
            left_val = int(left[1])
            # print('Left :', left_val)
            self.Left_LCD_change(left_val)
        if 'RV' in data.decode():
            right_decoded = data.decode()
            right = right_decoded.split(' ')
            right_val = int(right[1])
            self.Right_LCD_change(right_val)
            # print('Right :', right_val)
        if 'FV' in data.decode():
            front_decoded = data.decode()
            front = front_decoded.split(' ')
            front_val = int(front[1])
            self.Top_LCD_change(front_val)
            # print('Front :', front_val)
        if 'BV' in data.decode():
            bottom_decoded = data.decode()
            bottom = bottom_decoded.split(' ')
            bottom_val = int(bottom[1])
            # print('Bottom :', bottom_val)
            self.Bottom_LCD_change(bottom_val)

        self.checkValue(lefter=left_val, righter=right_val, fronter=front_val, bottomer=bottom_val)

        if 'YES' in data.decode():
            self.labelRight_3.setText('YES')
            font = QtGui.QFont()
            font.setPointSize(14)
            self.labelRight_3.setFont(font)
            self.labelRight_3.setStyleSheet("color: rgb(255, 255, 0);")
        if 'NO' in data.decode():
            self.labelRight_3.setText('NO')
            font = QtGui.QFont()
            font.setPointSize(14)
            self.labelRight_3.setFont(font)
            self.labelRight_3.setStyleSheet("color: rgb(255, 255, 0);")
    # Press the green button in the gutter to run the script.




def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

