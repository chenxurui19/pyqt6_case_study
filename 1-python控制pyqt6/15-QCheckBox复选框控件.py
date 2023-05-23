# -*- coding: utf-8 -*-
# @Time    : 2023/5/22 23:49
# @Author  : CXRui
# @File    : 15-QCheckBox复选框控件.py
# @Description :
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("复选框控件演示")
        layout = QHBoxLayout()      # 水平布局
        self.checkBox1 = QCheckBox("复选框控件1")
        self.checkBox1.setChecked(True)     # 默认选中
        self.checkBox1.stateChanged.connect(lambda:self.checkboxState(self.checkBox1))
        layout.addWidget(self.checkBox1)

        self.checkBox2 = QCheckBox("复选框控件2")
        self.checkBox2.stateChanged.connect(lambda:self.checkboxState(self.checkBox2))
        layout.addWidget(self.checkBox2)

        self.checkBox3 = QCheckBox("半选中")
        self.checkBox3.setTristate(True)        # 设置能够处于半选中状态
        self.checkBox3.setCheckState(Qt.CheckState.PartiallyChecked)    # 设置半选中状态
        layout.addWidget(self.checkBox3)
        self.setLayout(layout)

    def checkboxState(self, cb):
        check1Status = self.checkBox1.text() + ", isChecked=" + str(self.checkBox1.isChecked()) + ",checkState=" + str(self.checkBox1.checkState())
        check2Status = self.checkBox2.text() + ", isChecked=" + str(self.checkBox2.isChecked()) + ",checkState=" + str(self.checkBox2.checkState())
        check3Status = self.checkBox3.text() + ", isChecked=" + str(self.checkBox3.isChecked()) + ",checkState=" + str(self.checkBox3.checkState())
        print(check1Status + check2Status + check3Status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec())
