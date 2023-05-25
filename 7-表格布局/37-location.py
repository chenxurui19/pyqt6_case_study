# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 00:39
# @Author  : CXRui
# @File    : 37-location.py
# @Description :
import sys
from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from PyQt6.QtGui import QColor, QBrush
"""
数据的定位：findItems 
"""


class DataLocation(QWidget):
    def __init__(self):
        super(DataLocation, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget例子")
        self.resize(600, 680)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(40)
        tableWidget.setColumnCount(4)
        layout.addWidget(tableWidget)
        for i in range(40):     # 在表格中添加数据
            for j in range(4):
                itemContent = "(%d, %d)" % (i, j)
                tableWidget.setItem(i, j, QTableWidgetItem(itemContent))
        self.setLayout(layout)
        text = '(13'
        # 第三个数据为匹配的方式，有多种匹配方式可选
        items = tableWidget.findItems(text, QtCore.Qt.MatchFlag.MatchStartsWith)
        if len(items) > 0:
            item = items[0]
            item.setBackground(QBrush(QColor(0, 255, 0)))   # 设置背景颜色
            item.setBackground(QBrush(QColor(255, 0, 0)))   # 设置字体颜色
            row = item.row()                                # 获得元素行数
            # 定位到指定的行，滚动条滚动到对应位置
            tableWidget.verticalScrollBar().setSliderPosition(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = DataLocation()
    example.show()
    sys.exit(app.exec())