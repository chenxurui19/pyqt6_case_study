# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 14:38
# @Author  : CXRui
# @File    : 24-拖动操作.py
# @Description :
import sys, math
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class MyComboBox(QComboBox):    # 定义事件
    def __init__(self):
        super(MyComboBox, self).__init__()
        self.setAcceptDrops(True)   # 控件接收拖动

    def dragEnterEvent(self, e):
        print(e)
        if e.mimeData().hasText():
            e.accept()      # 接受文本
        else:
            e.ignore()      # 忽略

    def dropEvent(self, e):
        self.addItem(e.mimeData().text())   # 添加文本


class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo, self).__init__()
        formLayout = QFormLayout()
        formLayout.addRow(QLabel("请将左边的文本拖拽到右边的下拉列表中"))
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)   # 让QLineEdit控件可拖动
        combo = MyComboBox()
        formLayout.addRow(lineEdit, combo)
        self.setLayout(formLayout)
        self.setWindowTitle("拖拽案例")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrapDropDemo()
    main.show()
    sys.exit(app.exec())