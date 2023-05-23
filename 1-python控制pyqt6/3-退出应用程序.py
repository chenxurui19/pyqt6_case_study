# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 16:22
# @Author  : CXRui
# @File    : 3-退出应用程序.py
# @Description :
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, QWidget


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(300, 120)
        self.setWindowTitle("quit_app")

        # 添加push button
        self.button1 = QPushButton("Quit APP")
        # 将信号与槽相关联
        self.button1.clicked.connect(self.ButtonOnClick)

        # 设置水平布局
        layout = QHBoxLayout()
        # 添加按钮到布局
        layout.addWidget(self.button1)

        # 创建一个frame
        mainfram = QWidget()
        # 将layout添加到frame
        mainfram.setLayout(layout)

        self.setCentralWidget(mainfram)

    # 自定义槽,按钮点击的方法
    def ButtonOnClick(self):
        sender = self.sender()
        print(sender.text() + "button is clicked!")
        app = QApplication.instance()
        # 退出程序
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec())
