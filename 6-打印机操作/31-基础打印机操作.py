# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 17:18
# @Author  : CXRui
# @File    : 31-基础打印机操作.py
# @Description :

from PyQt6 import QtGui, QtWidgets, QtPrintSupport
from PyQt6.QtWidgets import *
import sys
"""
操作步骤：
1. 获取打印机对象
2. 将输出内容转为打印机
"""


class PrintSupport(QMainWindow):
    def __init__(self):
        super(PrintSupport, self).__init__()
        self.setGeometry(500, 200, 300, 300)
        self.button = QPushButton('打印QTextEdit控件中的内容', self)
        self.button.setGeometry(20, 20, 260, 30)
        self.editor = QTextEdit('默认文本', self)
        self.editor.setGeometry(20, 60, 260, 200)

        self.button.clicked.connect(self.print_content)

    def print_content(self):
        printer = QtPrintSupport.QPrinter()
        painter = QtGui.QPainter()
        # 将绘制的目标重定向到打印机
        painter.begin(printer)
        screen = self.editor.grab()
        painter.drawPixmap(10, 10, screen)
        painter.end()
        print("print")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = PrintSupport()
    gui.show()
    app.exec()
