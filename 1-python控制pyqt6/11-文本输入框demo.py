# -*- coding: utf-8 -*-
# @Time    : 2023/5/20 00:24
# @Author  : CXRui
# @File    : 11-文本输入框demo.py
# @Description :
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
import sys


class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        edit1 = QLineEdit()
        # 使用int校验器
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)   # 设置最大位数
        edit1.setAlignment(Qt.AlignmentFlag.AlignRight)    # 文本右对齐，默认左对齐
        # 使用double校验器
        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99, 99.99, 2))    # 最后一个为精度
        # 使用掩码校验
        edit3 = QLineEdit()
        edit3.setInputMask("99_9999_999999;#")
        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textChanged)     # 绑定文本变化的槽
        # 使用密码回显模式
        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.EchoMode.Password)
        edit5.editingFinished.connect(self.enterPress)
        # 只读文本框
        edit6 = QLineEdit('Hello PyQt5')
        edit6.setReadOnly(True)
        # 创建表单布局
        formLayout = QFormLayout()
        formLayout.addRow("整数校验", edit1)
        formLayout.addRow("浮点数校验", edit2)
        formLayout.addRow("Input Mask", edit3)
        formLayout.addRow("文本变化", edit4)
        formLayout.addRow("密码", edit5)
        formLayout.addRow("只读", edit6)
        self.setLayout(formLayout)
        self.setWindowTitle("QLineEdit综合案例")

    def textChanged(self, text):    # 检测当文本输入内容发生变化
        print("输入的内容：" + text)

    def enterPress(self):
        print("已输入值")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditDemo()
    main.show()
    sys.exit(app.exec())
