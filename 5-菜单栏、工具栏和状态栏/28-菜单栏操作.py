# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 15:42
# @Author  : CXRui
# @File    : 28-菜单栏操作.py
# @Description :
import sys, math
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        bar = self.menuBar()        # 获取当前窗口菜单栏
        file = bar.addMenu("文件")   # 添加菜单栏内容
        file.addAction("新建")       # 添加带有动作的菜单
        save = QAction("保存", self)
        save.setShortcut("Ctrl + S")  # 设置快捷键
        file.addAction(save)
        save.triggered.connect(self.process)

        edit = bar.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")
        self.resize(300, 200)

    def process(self, a):
        print(self.sender().text())     # 获取点击文本内容


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Menu()
    main.show()
    sys.exit(app.exec())