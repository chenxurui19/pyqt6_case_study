# -*- coding: utf-8 -*-
# @Time    : 2023/5/20 00:47
# @Author  : CXRui
# @File    : 12-QText输入多行文本.py
# @Description :
from PyQt6.QtWidgets import *
import sys


class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTextEdit控件演示")
        self.resize(300, 320)
        self.textEdit = QTextEdit()
        self.buttonText = QPushButton("显示文本")
        self.buttonHTML = QPushButton("显示HTML")
        self.buttonToText = QPushButton("获取文本")
        self.buttonToHTML = QPushButton("获取HTML")
        # 设置垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.buttonToHTML)
        self.setLayout(layout)
        # 绑定信号与槽
        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)
        self.buttonToText.clicked.connect(self.onClick_ButtonToText)
        self.buttonToHTML.clicked.connect(self.onClick_ButtonToHTML)

    def onClick_ButtonText(self):
        # 设置一般文本
        self.textEdit.setPlainText("Hello World，世界你好吗？")

    def onClick_ButtonToText(self):
        # 获取一般文本
        print(self.textEdit.toPlainText())

    def onClick_ButtonHTML(self):
        # 设置html文本
        self.textEdit.setHtml("<font color='blue' size='5'>Hello World</font>")

    def onClick_ButtonToHTML(self):
        # 获取html文本
        print(self.textEdit.toHtml())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec())

