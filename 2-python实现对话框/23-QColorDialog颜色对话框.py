# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 13:36
# @Author  : CXRui
# @File    : 23-QColorDialog颜色对话框.py
# @Description :
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Color Dialog例子")
        layout = QVBoxLayout()
        self.colorButton = QPushButton("设置字体颜色")
        self.colorButton.clicked.connect(self.getColor)
        layout.addWidget(self.colorButton)

        self.colorButton1 = QPushButton("设置背景颜色")
        self.colorButton1.clicked.connect(self.getBGColor)
        layout.addWidget(self.colorButton1)

        self.colorLabel = QLabel("Hello，测试颜色例子")
        layout.addWidget(self.colorLabel)
        self.setLayout(layout)
        self.resize(300, 200)

    def getColor(self):   # 设置文字颜色
        # 返回值只有一个，为对应颜色
        color = QColorDialog.getColor()
        p = self.colorLabel.palette() # 创建调色板对象
        p.setColor(QPalette.ColorRole.WindowText, color)
        self.colorLabel.setPalette(p)

    def getBGColor(self):   # 设置背景颜色
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.ColorRole.Window, color)
        self.colorLabel.setAutoFillBackground(True)     # 设置背景颜色
        self.colorLabel.setPalette(p)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec())


