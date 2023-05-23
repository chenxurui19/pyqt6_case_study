# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 19:30
# @Author  : CXRui
# @File    : 7-label与伙伴控件.py
# @Description :
from PyQt6.QtWidgets import *
import sys


class QLabelBuddy(QDialog):
    # QDialog是对话框类
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置标题
        self.setWindowTitle("QLabel与伙伴控件")
        # 通过&添加热键
        nameLabel = QLabel('&Name', self)
        # 文本输入框
        nameLineEdit = QLineEdit(self)
        # 设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel("&Password", self)
        passwordLineEdit = QLineEdit(self)
        passwordLabel.setBuddy(passwordLineEdit)

        # 创建按钮
        btnOK = QPushButton("&OK")
        btnCancel = QPushButton("&Cancel")

        # 使用栅格布局
        mainLayout = QGridLayout(self)

        # 设置栅格布局
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)

        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)

        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec())
