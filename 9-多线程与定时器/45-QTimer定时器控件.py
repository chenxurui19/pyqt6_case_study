# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 12:18
# @Author  : CXRui
# @File    : 45-QTimer定时器控件.py
# @Description :
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel
from PyQt6.QtCore import QDateTime, QTimer
import sys
from datetime import datetime


class ShowTime(QWidget):
    def __init__(self, parent=None):
        super(ShowTime, self).__init__()
        self.setWindowTitle("动态显示当前时间")
        self.label1 = QLabel("显示当前时间")
        self.label2 = QLabel("显示耗费时间")
        self.start_time = QDateTime.currentDateTime().time()
        self.current_time = QDateTime.currentDateTime().time()
        self.startBtn = QPushButton("开始")       # 开始定时器按钮
        self.endBtn = QPushButton("结束")         # 定制定时器按钮
        layout = QGridLayout()                   # 网格布局
        self.timer = QTimer()                    # 创建定时器对象
        self.timer.timeout.connect(self.showTime)
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.label2, 0, 1)
        layout.addWidget(self.startBtn, 1, 0)
        layout.addWidget(self.endBtn, 1, 1)
        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)
        self.setLayout(layout)
        self.resize(400, 300)

    def showTime(self):
        time = QDateTime.currentDateTime()      # 获取当前时间
        # 格式化时间
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label1.setText(timeDisplay)
        self.current_time = datetime.now()
        print(self.current_time - self.start_time)
        cost_time = self.current_time - self.start_time
        self.label2.setText(str(cost_time))

    def startTimer(self):
        self.timer.start(1000)      # 开始定时,参数为定时时间间隔
        self.startBtn.setEnabled(False)     # 设置开始按钮不可用
        self.endBtn.setEnabled(True)
        self.start_time = datetime.now()
        print(self.start_time)

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ShowTime()
    form.show()
    sys.exit(app.exec())
