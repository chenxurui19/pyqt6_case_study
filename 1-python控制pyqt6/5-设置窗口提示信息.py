# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 16:51
# @Author  : CXRui
# @File    : 5-设置窗口提示信息.py
# @Description :
import sys
from PyQt6.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QToolTip, QPushButton, QWidget
from PyQt6.QtGui import QFont


class Tooltip(QMainWindow):
    def __init__(self):
        super(Tooltip, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置字体
        QToolTip.setFont(QFont("SansSerif", 12))
        # 设置提示信息
        self.setToolTip("今天<b>星期二</b>")
        self.setGeometry(300, 300, 200, 300)
        self.setWindowTitle("设置控件提示消息")

        self.button1 = QPushButton("按钮1")
        # 设置按钮提示信息
        self.button1.setToolTip("这是一个按钮")
        # 创建一个布局
        layout = QHBoxLayout()
        # 将按钮加入布局
        layout.addWidget(self.button1)
        # 创建框架
        mainframe = QWidget()
        # 添加布局
        mainframe.setLayout(layout)
        # 居中显示
        self.setCentralWidget(mainframe)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Tooltip()
    main.show()
    sys.exit(app.exec())