# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 10:52
# @Author  : CXRui
# @File    : 41-QTabWidget选项卡控件.py
# @Description :
"""
选项卡：QTabWidget
容器控件的作用，就是为了在页面的控件
选项卡控件就是可以在多个页面中显示
"""
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class TabWidgetDemo(QTabWidget):
    def __init__(self, parent=None):
        super(TabWidgetDemo, self).__init__()
        self.setWindowTitle("选项卡控件：QTabWidget")
        self.resize(400, 300)
        # 创建用于显示控件的窗口
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.addTab(self.tab1, "选项卡1")      # 页面和选项卡绑定
        self.addTab(self.tab2, "选项卡2")
        self.addTab(self.tab3, "选项卡3")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.setTabText(0, "联系方式")      # 选项卡主题
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))
        layout.addRow(QLabel("性别"), sex)
        layout.addRow("生日", QLineEdit())
        self.setTabText(1, "个人详细信息")
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.setTabText(2, "教育程度")
        self.tab3.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TabWidgetDemo()
    demo.show()
    sys.exit(app.exec())


