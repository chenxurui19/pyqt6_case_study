# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 11:55
# @Author  : CXRui
# @File    : 19-对话框demo.py
# @Description :
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class DialogDemo(QMainWindow):
    def __init__(self):
        super(DialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Dialog案例")
        self.resize(300, 200)
        self.button = QPushButton(self)
        self.button.setText("弹出对话框")
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        button = QPushButton("确定", dialog)      # 创建对话框对象
        button.clicked.connect(dialog.close)
        button.move(50, 50)
        dialog.setWindowTitle("对话框")            # 对话框基础设置和主窗口相同
        dialog.setWindowModality(Qt.WindowModality.ApplicationModal)    # 对话框中，主窗口的控件不可用
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DialogDemo()
    main.show()
    sys.exit(app.exec())

