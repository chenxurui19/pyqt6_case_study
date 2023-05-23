# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 13:25
# @Author  : CXRui
# @File    : 22-QFontDialog字体对话框.py
# @Description :
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class QFontDialogDemo(QWidget):
    def __init__(self):
        super(QFontDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Font Dialog例子")
        layout = QVBoxLayout()
        self.fontButton = QPushButton("请选择字体")
        self.fontButton.clicked.connect(self.getFont)
        layout.addWidget(self.fontButton)

        self.fontLabel = QLabel("Hello,测试字体例子")
        layout.addWidget(self.fontLabel)
        self.setLayout(layout)
        self.resize(300, 200)

    def getFont(self):
        # 第一个参数是选中的元素，第二个参数是否点击退出
        font, ok = QFontDialog.getFont()
        if ok:
            self.fontLabel.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()
    sys.exit(app.exec())
