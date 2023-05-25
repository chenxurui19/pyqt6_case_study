# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 01:08
# @Author  : CXRui
# @File    : 39-setTextAlignment.py
# @Description :
"""
在pyqt5中可以设置单元格的文本对齐方式
"""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class CellTextAligment(QWidget):
    def __init__(self):
        super(CellTextAligment, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置单元格的文本对齐方式")
        self.resize(430, 230)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(["姓名", "性别", "体重(kg)"])
        newItem = QTableWidgetItem("雷神")
        newItem.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem("男")
        newItem.setTextAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom)
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("190")
        newItem.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        tableWidget.setItem(0, 2, newItem)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = CellTextAligment()
    example.show()
    sys.exit(app.exec())
