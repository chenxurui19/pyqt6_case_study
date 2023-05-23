# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 00:37
# @Author  : CXRui
# @File    : 18-QSpinBox计时器.py
# @Description :
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QSpinBox演示")
        self.resize(300, 100)
        layout = QVBoxLayout()
        self.label = QLabel("当前值")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.sb = QSpinBox()    # 创建计数器对象
        self.sb.setValue(18)    # 设置初始值
        self.sb.setRange(10, 38)    # 设置区间
        self.sb.setSingleStep(3)    # 设置步长
        layout.addWidget(self.sb)
        self.sb.valueChanged.connect(self.valueChange)
        self.setLayout(layout)

    def valueChange(self):
        self.label.setText("当前值；" + str(self.sb.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()
    sys.exit(app.exec())