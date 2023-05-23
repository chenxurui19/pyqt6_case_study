# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 00:05
# @Author  : CXRui
# @File    : 16-QComboBox下来列表控件.py
# @Description :
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("下拉列表控件演示")
        self.resize(300, 100)
        layout = QVBoxLayout()
        self.label = QLabel("请选择编程语言")
        self.cb = QComboBox()
        self.cb.addItem("C++")
        self.cb.addItem("Python")
        self.cb.addItems(["Java", "C#", "Ruby"])
        self.cb.currentIndexChanged.connect(self.selectionChange)   # 获取当前选中元素的索引
        layout.addWidget(self.label)
        layout.addWidget(self.cb)
        self.setLayout(layout)

    def selectionChange(self, i):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()
        for count in range(self.cb.count()):
            print("item" + str(count) + "=" + self.cb.itemText(count))
        print("current index", i, "selection changed", self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec())
