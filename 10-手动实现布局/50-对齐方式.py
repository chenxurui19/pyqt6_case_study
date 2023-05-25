# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 15:02
# @Author  : CXRui
# @File    : 50-对齐方式.py
# @Description :
import sys, math
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class HBoxLayoutAlign(QWidget):
    def __init__(self):
        super(HBoxLayoutAlign, self).__init__()
        self.setWindowTitle("水平盒布局")
        hlayout = QHBoxLayout()
        # 第二个参数：设置控件间距之间的伸缩量
        # 第三个参数：指定对齐方式
        hlayout.addWidget(QPushButton("按钮1"), 2, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        hlayout.addWidget(QPushButton("按钮2"), 4, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        hlayout.addWidget(QPushButton("按钮3"), 1, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        hlayout.addWidget(QPushButton("按钮4"), 1, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        hlayout.addWidget(QPushButton("按钮5"), 1, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        hlayout.setSpacing(40)
        self.setLayout(hlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = HBoxLayoutAlign()
    main.show()
    sys.exit(app.exec())