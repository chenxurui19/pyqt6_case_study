# -*- coding: utf-8 -*-
# @Time    : 2023/5/22 23:15
# @Author  : CXRui
# @File    : 13-控件按钮.py
# @Description :
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
"""
QPushButton 一般按钮
AToolButton 工具条
QRadioButton    单选按钮
QCheckBox   多选按钮
"""


class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QPushButton Demo")
        layout = QVBoxLayout()
        self.button1 = QPushButton("第1个按钮")
        # 设置文本：1直接在生成按钮时添加 2使用setText函数设置
        self.button1.setText("First Button1")
        self.button1.setCheckable(True)     # 设置按钮的check
        self.button1.toggle()       # 设置按钮处于选中的状态
        # 当绑定多个槽时，对于不同的槽按照顺序进行调用
        self.button1.clicked.connect(self.buttonState)
        self.button1.clicked.connect(lambda :self.whichButton(self.button1))
        layout.addWidget(self.button1)

        self.button2 = QPushButton('图像按钮')  # 在文本面前显示图像
        self.button2.setIcon(QIcon(QPixmap('../images/python.png')))
        self.button2.clicked.connect(lambda :self.whichButton(self.button2))
        layout.addWidget(self.button2)

        self.button3 = QPushButton("不可用的按钮")
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        self.button4 = QPushButton("&MyButton")
        self.button4.setDefault(True)   # 设置默认按钮
        self.button4.clicked.connect(lambda :self.whichButton(self.button4))
        layout.addWidget(self.button4)
        self.setLayout(layout)
        self.resize(400, 300)

    def buttonState(self):
        if self.button1.isChecked():
            print("按钮1已经被选中")
        else:
            print("按钮1未被选中")

    def whichButton(self, btn):
        # 传入的参数就是当前被调用的按钮
        print("被单击的按钮是<" + btn.text() + ">")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec())