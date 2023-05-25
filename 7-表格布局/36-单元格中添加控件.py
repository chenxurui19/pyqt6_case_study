# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 19:43
# @Author  : CXRui
# @File    : 36-单元格中添加控件.py
# @Description :
"""
Pyqt6支持在单元格放置控件，所有的控件都可以放置在单元格中
常用控件设置：
1. setItem: 将文本放到单元格中
2. setCellWidget：将控件放到单元格中
3. setStyleSetXheet: 设置控件的样式（QSS）
"""
import sys
from PyQt6.QtWidgets import *


class PlaceControlInCell(QWidget):
    def __init__(self):
        super(PlaceControlInCell, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("单元格中放置控件")
        self.resize(430, 300)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()    # 创建表格对象
        tableWidget.setRowCount(4)      # 设置行数
        tableWidget.setColumnCount(3)   # 设置列数
        layout.addWidget(tableWidget)

        # 设置表格水平label
        tableWidget.setHorizontalHeaderLabels(["姓名", "性别", "体重（kg）"])
        textItem = QTableWidgetItem("小明")
        tableWidget.setItem(0, 0, textItem)     # 第一第二是item位置，第三个是item

        combox = QComboBox()
        combox.addItem('男')
        combox.addItem('女')
        # QSS Qt StyleSheet
        combox.setStyleSheet('QComboBox{margin:3px};')
        tableWidget.setCellWidget(0, 1, combox)

        modifyButton = QPushButton('修改')
        modifyButton.setDown(True)
        modifyButton.setStyleSheet('QPushButton{margin:3px};')
        tableWidget.setCellWidget(0, 2, modifyButton)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = PlaceControlInCell()
    example.show()
    sys.exit(app.exec())

