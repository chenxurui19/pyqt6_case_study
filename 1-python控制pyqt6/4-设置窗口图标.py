# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 16:43
# @Author  : CXRui
# @File    : 4-设置窗口图标.py
# @Description :
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, QWidget
from PyQt6.QtGui import QIcon
import ctypes


class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口
        self.setGeometry(300, 300, 250, 250)
        # 设置窗口标题
        self.setWindowTitle("窗口标题设置demo")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../icon_image/favicon.ico'))
    main = IconForm()
    main.show()
    sys.exit(app.exec())