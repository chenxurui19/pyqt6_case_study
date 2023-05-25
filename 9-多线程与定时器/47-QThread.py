# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 13:42
# @Author  : CXRui
# @File    : 47-QThread.py
# @Description :
"""
线程类，可以实现计数器的效果
QLCDNumber: 模拟LED显示效果
WorkThread(QThread): 自定义信号，实现在不同线程中信息的交互
"""
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

sec = 0     # 当前计时器


class WorkThread(QThread):  # 工作线程
    timer = pyqtSignal()    # 每隔1秒发送一次信号
    end = pyqtSignal()      # 计数完成后发送一次信号

    def run(self):
        while True:
            self.sleep(1)   # 休眠1秒
            if sec == 5:
                self.end.emit()  # 发送end信号
                break
            self.timer.emit()   # 发送timer信号


class Counter(QWidget):     # 主线程
    def __init__(self, parent=None):
        super(Counter, self).__init__(parent)
        self.resize(300, 120)
        layout = QVBoxLayout()
        self.lcdNumber = QLCDNumber()
        layout.addWidget(self.lcdNumber)
        button = QPushButton("开始计数")
        layout.addWidget(button)
        self.workThread = WorkThread()      # 创建工作线程
        self.workThread.timer.connect(self.countTime)
        self.workThread.end.connect(self.end)
        button.clicked.connect(self.work)
        self.setLayout(layout)

    def countTime(self):
        global sec      # 声明全局变量
        sec += 1
        self.lcdNumber.display(sec)

    def end(self):
        # 弹出对话框
        QMessageBox.information(self, "消息", "计数结束", QMessageBox.StandardButton.Ok)

    def work(self):
        self.workThread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Counter()
    form.show()
    sys.exit(app.exec())
