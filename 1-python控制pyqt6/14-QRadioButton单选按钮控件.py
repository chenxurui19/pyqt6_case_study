# -*- coding: utf-8 -*-
# @Time    : 2023/5/22 23:37
# @Author  : CXRui
# @File    : 14-QRadioButton单选按钮控件.py
# @Description :
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QRadioButton")
        layout = QHBoxLayout()
        self.button1 = QRadioButton("单选按钮1")
        self.button1.setChecked(True)
        self.button1.toggled.connect(self.buttonState)
        layout.addWidget(self.button1)

        self.button2 = QRadioButton("单选按钮2")
        self.button2.toggled.connect(self.buttonState)
        layout.addWidget(self.button2)
        self.setLayout(layout)
        self.resize(300, 200)

    def buttonState(self):
        radioButton = self.sender()     # 信号发送者
        if radioButton.isChecked() == True:
            print("<" + radioButton.text() + "> 被选中")
        else:
            print("<" + radioButton.text() + "> 被取消选中状态")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec())
