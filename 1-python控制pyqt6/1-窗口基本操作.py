# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 15:47
# @Author  : CXRui
# @File    : 1-窗口基本操作.py
# @Description :
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon
"""
主窗口基本操作
主窗口有三种类型：
QMainWindow:可以包含菜单栏、工具栏、状态栏和标题栏，是最常见的窗口形式
QWidget:对话窗口的基类，没有菜单栏、工具栏、状态栏（常见为弹出窗口)
QDialog:不确定窗口的用途，就使用该窗口
"""


class FirstWindow(QMainWindow):
    """
    inhrent QMainWindow
    """
    def __init__(self):
        super(FirstWindow, self).__init__()
        self.setWindowTitle("My first main window!")
        self.resize(400, 300)
        self.statue = self.statusBar()
        self.statue.showMessage("This wil last 5's!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("../icon_image/favicon.ico"))
    main = FirstWindow()
    main.show()
    sys.exit(app.exec())