# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 00:52
# @Author  : CXRui
# @File    : 38-font-color.py
# @Description :
"""
在pyqt5中可以设置单元格字体和颜色
"""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class CellFontAndColor(QWidget):
    def __init__(self):
        super(CellFontAndColor, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置单元格字体和颜色")
        self.resize(430, 230)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(["姓名", "性别", "体重(kg)"])
        newItem = QTableWidgetItem("雷神")
        newItem.setFont(QFont("Times", 14, QFont.Weight.Black))    # 字体设置
        newItem.setForeground(QBrush(QColor(255, 0, 0)))    # 颜色设置
        tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem("女")
        newItem.setForeground(QBrush(QColor(255, 255, 0)))  # 文字颜色设置
        newItem.setBackground(QBrush(QColor(0, 0, 255)))    # 背景颜色设置
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("160")
        newItem.setFont(QFont("Times", 20, QFont.Weight.Black))
        newItem.setForeground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 2, newItem)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = CellFontAndColor()
    example.show()
    sys.exit(app.exec())

