# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 16:43
# @Author  : CXRui
# @File    : 30-状态栏.py
# @Description :
import sys, math
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class StatusBar(QMainWindow):
    def __init__(self):
        super(StatusBar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("状态栏演示")
        self.resize(300, 200)
        bar = self.menuBar()                        # 创建菜单对象
        file = bar.addMenu("File")                  # 添加菜单对象
        file.addAction("show")
        file.triggered.connect(self.processTrigger) # 绑定槽

        self.setCentralWidget(QTextEdit())
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def processTrigger(self, q):
        if q.text() == "show":
            self.statusBar.showMessage(q.text() + "菜单被点击了", 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StatusBar()
    main.show()
    sys.exit(app.exec())