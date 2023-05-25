# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 15:59
# @Author  : CXRui
# @File    : 2-主窗口居中显示.py
# @Description :
import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QApplication
"""
左上顶点x坐标 = （屏幕宽度 - 显示窗口宽度） / 2
左上顶点y坐标 = （屏幕高度 - 显示窗口高度） / 2
"""


class CenterWindow(QMainWindow):
    """
    inhrent QMainWindow
    """
    def __init__(self):
        super(CenterWindow, self).__init__()
        # 设置窗口标题
        self.setWindowTitle("My first main window!")
        # 设置窗口大小
        self.resize(400, 300)
        self.center()

    def center(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        window_geometry = self.frameGeometry()
        print(screen_geometry.center().x())
        print(screen_geometry.center().y())
        x = screen_geometry.center().x() - window_geometry.width() / 2
        y = screen_geometry.center().y() - window_geometry.height() / 2
        self.move(int(x), int(y))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../icon_image/favicon.ico'))
    main = CenterWindow()
    main.show()
    sys.exit(app.exec())
