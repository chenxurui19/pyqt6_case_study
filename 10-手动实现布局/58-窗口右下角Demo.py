# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 15:47
# @Author  : CXRui
# @File    : 58-窗口右下角Demo.py
# @Description :
import sys, math
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class RightBottomButton(QWidget):

    def __init__(self):
        super(RightBottomButton, self).__init__()
        self.setWindowTitle("让按钮永远在右下角")
        self.resize(400, 300)
        okButton = QPushButton("确定")
        cancelButton = QPushButton("取消")
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        vbox = QVBoxLayout()
        btn1 = QPushButton("按钮1")
        btn2 = QPushButton("按钮2")
        btn3 = QPushButton("按钮3")
        vbox.addStretch(0)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = RightBottomButton()
    main.show()
    sys.exit(app.exec())