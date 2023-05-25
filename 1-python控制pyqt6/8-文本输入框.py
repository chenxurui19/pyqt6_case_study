# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 19:44
# @Author  : CXRui
# @File    : 8-文本输入框.py
# @Description :
from PyQt6.QtWidgets import *
import sys
"""
文本框的基本功能：输入单行的文本
主要有四种回显方式：
1.Normal    --输入就显示
2.NoEcho    --输入后不显示
3.Password  --输入后显示特定字符
4.PasswordEchoOneEdit   --短暂显示输入内容，之后显示特定字符
"""


class QLineEditEchoMode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("文本输入框的回显模式")
        # 使用表单布局
        formLayout = QFormLayout()
        # 添加文本输入框控件
        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit= QLineEdit()

        # 添加控件至布局
        # 第一个参数为文本前的标签内容
        formLayout.addRow("Normal", normalLineEdit)
        formLayout.addRow("NoEcho", noEchoLineEdit)
        formLayout.addRow("Password", passwordLineEdit)
        formLayout.addRow("PasswordEchoOnEdit", passwordEchoOnEditLineEdit)

        # 设置显示提示
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        # 设置回响模式
        normalLineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.EchoMode.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec())
