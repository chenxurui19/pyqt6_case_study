# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 19:12
# @Author  : CXRui
# @File    : 61-拖动边界控件.py
# @Description :
"""
QSplitter:实现在垂直和水平方向，拖动控件之间的边界的控件
"""
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
"""
实现垂直和水平方向，拖动控件之间的边界的控件
"""


class Splitter(QWidget):
    def __init__(self):
        super(Splitter, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        self.setWindowTitle("QSplitter例子")
        self.setGeometry(300, 300, 300, 200)
        topLeft = QFrame()
        topLeft.setFrameShape(QFrame.Shape.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.Shape.StyledPanel)
        textedit = QTextEdit()
        splitter1 = QSplitter(Qt.Orientation.Horizontal)
        textedit = QTextEdit()
        splitter1.addWidget(topLeft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([200, 100])
        splitter2 = QSplitter(Qt.Orientation.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        hbox.addWidget(splitter2)
        self.setLayout(hbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Splitter()
    demo.show()
    sys.exit(app.exec())