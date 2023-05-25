# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 14:43
# @Author  : CXRui
# @File    : 48-绝对布局.py
# @Description :
import sys, math
from PyQt6.QtWidgets import *

"""
绝对布局可以通过指定控件的(x,y)来控制控件的位置，从而模仿出绝对布局的效果
"""


class AbsoluteLayout(QWidget):
    def __init__(self):
        super(AbsoluteLayout, self).__init__()
        self.setWindowTitle("绝对布局")
        self.label1 = QLabel("欢迎", self)
        self.label1.move(15, 20)    # 使用move方法实现绝对布局的效果
        self.label2 = QLabel("学习", self)
        self.label2.move(35, 40)
        self.label3 = QLabel("PyQt5", self)
        self.label3.move(55, 80)
        self.resize(400, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AbsoluteLayout()
    main.show()
    sys.exit(app.exec())