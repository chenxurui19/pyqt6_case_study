# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 13:34
# @Author  : CXRui
# @File    : 46-QTimer.singleShot.py
# @Description :
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
"""
指定定时器只执行一次方式，可以用于一次性计时，更加便捷
"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel("<font color=red size=140><b>Hello World，窗口在5秒后自动关闭！</b></font>")
    # 设置窗口样式
    label.setWindowFlag(Qt.WindowType.SplashScreen | Qt.WindowType.FramelessWindowHint)
    label.show()
    QTimer.singleShot(5000, app.quit)       # 定时器定时5s只执行一次
    sys.exit(app.exec())
