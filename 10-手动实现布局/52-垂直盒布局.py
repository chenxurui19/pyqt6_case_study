# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 15:19
# @Author  : CXRui
# @File    : 52-垂直盒布局.py
# @Description :
import sys, math
from PyQt6.QtWidgets import *


class VBoxLayout(QWidget):
    def __init__(self):
        super(VBoxLayout, self).__init__()
        self.setWindowTitle("垂直盒布局")
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("按钮1"))
        layout.addWidget(QPushButton("按钮2"))
        layout.addWidget(QPushButton("按钮3"))
        layout.addWidget(QPushButton("按钮4"))
        layout.addWidget(QPushButton("按钮5"))
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = VBoxLayout()
    main.show()
    sys.exit(app.exec())
