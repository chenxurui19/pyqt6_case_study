# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 01:20
# @Author  : CXRui
# @File    : 40-span.py
# @Description :
import sys
from PyQt6.QtWidgets import *


class Span(QWidget):
    def __init__(self):
        super(Span, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("合并单元格")
        self.resize(439, 230)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(["姓名", "性别", "体重(kg)"])
        newItem = QTableWidgetItem("雷神")
        tableWidget.setItem(0, 0, newItem)
        tableWidget.setSpan(0, 0, 3, 1)

        newItem = QTableWidgetItem("男")
        tableWidget.setItem(0, 1, newItem)
        tableWidget.setSpan(0, 1, 2, 1)

        newItem = QTableWidgetItem("160")
        tableWidget.setItem(0, 2, newItem)
        tableWidget.setSpan(0, 2, 4, 1)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Span()
    example.show()
    sys.exit(app.exec())