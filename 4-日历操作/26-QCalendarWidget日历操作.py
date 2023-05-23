# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 15:14
# @Author  : CXRui
# @File    : 26-QCalendarWidget日历操作.py
# @Description :
import sys, math
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar, self).__init__()
        self.initUI()

    def initUI(self):
        self.cal = QCalendarWidget(self)    # 创建日历对象
        self.cal.setMinimumDate(QDate(1988, 1, 1))    # 设置最小日期
        self.cal.setMaximumDate(QDate(2088, 1, 1))    # 设置最大日期
        self.cal.setGridVisible(True)                 # 设置网格
        self.cal.move(20, 20)                         # 移动显示
        self.cal.clicked.connect(self.showDate)       # 绑定槽
        self.label = QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString("yyyy-MM-dd dddd"))
        self.label.move(20, 300)
        self.resize(400, 350)
        self.setWindowTitle("日历演示")

    def showDate(self, date):   # 在label上显示当前选中的日期
        # 获取日期的方式
        self.label.setText((self.cal.selectedDate().toString("yyyy-MM-dd dddd")))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyCalendar()
    main.show()
    sys.exit(app.exec())
