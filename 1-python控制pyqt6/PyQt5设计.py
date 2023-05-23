# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 14:14
# @Author  : CXRui
# @File    : PyQt5设计.py
# @Description :
import sys
import horizontal_layout_demo
from PyQt6.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    # 创建运行程序
    app = QApplication(sys.argv)
    # 创建主窗口
    mainwindow = QMainWindow()
    ui = horizontal_layout_demo.Ui_Dialog()
    # 向主窗口添加控件
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec())

