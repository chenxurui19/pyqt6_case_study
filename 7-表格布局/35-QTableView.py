# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 17:46
# @Author  : CXRui
# @File    : 35-QTableView.py
# @Description :
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys
"""
该控件可以帮助我们实现显示二维表数据(显示n*m数据)
使用方法：需要创建QTableView实例和一个数据源（Model），然后将两者关联
"""


class TableView(QWidget):
    def __init__(self, arg=None):
        super(TableView, self).__init__()
        self.setWindowTitle("QTableView表格视图控件演示")
        self.resize(500, 300)
        self.model = QStandardItemModel(4, 4)   # 创建数据源对象
        self.model.setHorizontalHeaderLabels(["id", "姓名", "年龄"])  # 设置标题
        self.tableview = QTableView()
        self.tableview.setModel(self.model)     # 关联QtableView控件和Model
        item1 = QStandardItem("10")
        item2 = QStandardItem("雷神")
        item3 = QStandardItem("2000")
        self.model.setItem(0, 0, item1)
        self.model.setItem(0, 1, item2)
        self.model.setItem(0, 2, item3)

        item31 = QStandardItem("30")
        item32 = QStandardItem("死亡女神")
        item33 = QStandardItem("3000")
        self.model.setItem(2, 0, item31)
        self.model.setItem(2, 1, item32)
        self.model.setItem(2, 2, item33)
        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = TableView()
    table.show()
    sys.exit(app.exec())