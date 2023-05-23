# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 12:34
# @Author  : CXRui
# @File    : 21-QinputDialog输入对话框.py
# @Description :
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class QInputDialogDemo(QWidget):
    def __init__(self):
        super(QInputDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("输入对话框")
        layout = QFormLayout()
        self.button1 = QPushButton("获取列表中的选项")  # 点击按钮弹出相应的文本
        self.button1.clicked.connect(self.getItem)
        self.lineEdit1 = QLineEdit()
        layout.addRow(self.button1, self.lineEdit1)

        self.button2 = QPushButton("获取字符串")
        self.button2.clicked.connect(self.getText)
        self.lineEdit2 = QLineEdit()
        layout.addRow(self.button2, self.lineEdit2)

        self.button3 = QPushButton("获取整数")
        self.button3.clicked.connect(self.getInt)
        self.lineEdit3 = QLineEdit()
        layout.addRow(self.button3, self.lineEdit3)

        self.setLayout(layout)

    def getItem(self):
        items = ("C", "C++", "Ruby", "Python", "Java")
        # 第一个是选择的按钮，第二个是点击取消
        item, ok = QInputDialog.getItem(self, "请选择编程语言", "语言列表", items)
        if ok and item:
            self.lineEdit1.setText(item)

    def getText(self):
        # 第一个是选择的按钮，第二个是点击取消
        text, ok = QInputDialog.getText(self, "文本输入框", "输入姓名")
        if ok and text:
            self.lineEdit2.setText(text)

    def getInt(self):
        num, ok = QInputDialog.getInt(self, "整数输入框", "输入数字")
        if ok and num:
            self.lineEdit3.setText(str(num))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()
    sys.exit(app.exec())