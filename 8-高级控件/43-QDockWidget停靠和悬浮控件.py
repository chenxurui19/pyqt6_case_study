# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 11:45
# @Author  : CXRui
# @File    : 43-QDockWidget停靠和悬浮控件.py
# @Description :
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class  DockeDemo(QMainWindow):
    def __init__(self, parent=None):
        super(DockeDemo, self).__init__(parent)
        self.setWindowTitle("停靠控件(QDockWidget)")
        self.resize(400, 300)
        layout = QHBoxLayout()
        self.items = QDockWidget("Dockable", self)      # 创建悬浮停靠对象
        self.listWidget = QListWidget()
        self.listWidget.addItem("item1")
        self.listWidget.addItem("item2")
        self.listWidget.addItem("item3")
        self.items.setWidget(self.listWidget)
        self.setCentralWidget(QLineEdit())

        # 修改默认为悬浮
        self.items.setFloating(True)
        # 添加停靠窗口，默认停靠位置是右侧
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.items)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DockeDemo()
    demo.show()
    sys.exit(app.exec())