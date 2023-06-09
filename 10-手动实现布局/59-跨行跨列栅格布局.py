# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 15:58
# @Author  : CXRui
# @File    : 59-跨行跨列栅格布局.py
# @Description :
import sys, math
from PyQt6.QtWidgets import *


class GridForm(QWidget):
    def __init__(self):
        super(GridForm, self).__init__()
        self.setWindowTitle("栅格布局：表单设计")
        titleLabel = QLabel("标题")
        authorLabel = QLabel("作者")
        contentLabel = QLabel("内容")
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        contentEdit = QTextEdit()
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(titleLabel, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(authorLabel, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        grid.addWidget(contentLabel, 3, 0)
        grid.addWidget(contentEdit, 3, 1, 5, 1)
        self.setLayout(grid)
        self.resize(350, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = GridForm()
    main.show()
    sys.exit(app.exec())