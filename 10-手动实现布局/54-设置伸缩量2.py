# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 15:37
# @Author  : CXRui
# @File    : 54-设置伸缩量2.py
# @Description :
import sys, math
from PyQt6.QtWidgets import *


class Stretch(QWidget):
    def __init__(self):
        super(Stretch, self).__init__()
        self.resize(800, 100)
        btn1 = QPushButton("按钮1")
        btn2 = QPushButton("按钮2")
        btn3 = QPushButton("按钮3")
        btn4 = QPushButton("按钮4")
        btn5 = QPushButton("按钮5")
        layout = QHBoxLayout()
        layout.addStretch(0)
        layout.addWidget(btn1)
        layout.addStretch(1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)

        btnOK = QPushButton("确定")
        btnCancel = QPushButton("取消")
        layout.addStretch(1)
        layout.addWidget(btnOK)
        layout.addWidget(btnCancel)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Stretch()
    main.show()
    sys.exit(app.exec())