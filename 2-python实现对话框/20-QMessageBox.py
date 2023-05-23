# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 12:03
# @Author  : CXRui
# @File    : 20-QMessageBox.py
# @Description :
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QMessageBox案例")
        self.resize(300, 400)
        layout = QVBoxLayout()
        self.button1 = QPushButton()
        self.button1.setText("显示关于对话框")
        self.button1.clicked.connect(self.showDialog)
        self.button2 = QPushButton()
        self.button2.setText("显示消息对话框")
        self.button2.clicked.connect(self.showDialog)
        self.button3 = QPushButton()
        self.button3.setText("显示消息对话框")
        self.button3.clicked.connect(self.showDialog)
        self.button4 = QPushButton()
        self.button4.setText("显示警告对话框")
        self.button4.clicked.connect(self.showDialog)
        self.button5 = QPushButton()
        self.button5.setText("显示错误对话框")
        self.button5.clicked.connect(self.showDialog)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        self.setLayout(layout)

    def showDialog(self):
        text = self.sender().text()     # 获得信号发送者的文本信息
        if text == "显示关于对话框":
            QMessageBox.about(self, "关于", "这是一个关于对话框")
        elif text == "显示消息对话框":
            # 消息对话框具有返回值
            reply = QMessageBox.information(self, "消息", "这是一个消息对话框", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            print(reply == QMessageBox.StandardButton.Yes)  # 可以对返回值进行判断得到用户选择的消息
        elif text == "显示警告对话框":
            QMessageBox.warning(self, "警告", "这是一个警告对话框", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)
        elif text == "显示错误对话框":
            QMessageBox.critical(self, "警告", "这是一个警告对话框", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)
        elif text == "显示提问对话框":
            QMessageBox.question(self, "警告", "这是一个警告对话框", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMessageBoxDemo()
    main.show()
    sys.exit(app.exec())