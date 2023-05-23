# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 15:56
# @Author  : CXRui
# @File    : 29-工具栏.py
# @Description :
import sys, math
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class Toolbar(QMainWindow):
    def __init__(self):
        super(Toolbar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("工具栏例子")
        self.resize(300, 200)
        tb1 = self.addToolBar("File")                               # 创建工具栏对象
        new = QAction(QIcon("../images/new.png"), "new", self)      # 创建action
        tb1.addAction(new)                                          # 添加action

        open = QAction(QIcon("../images/open.png"), "open", self)
        tb1.addAction(open)

        save = QAction(QIcon("../images/save.png"), "save", self)
        tb1.addAction(save)

        tb2 = self.addToolBar("File1")
        new1 = QAction(QIcon("../images/new.png"), "新建", self)
        tb2.addAction(new1)
        tb2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)  # 设置图标和文本显示方式
        tb1.actionTriggered.connect(self.toolbtnpressed)
        tb2.actionTriggered.connect(self.toolbtnpressed)

    def toolbtnpressed(self, a):
        print("按下的工具按钮是", a.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Toolbar()
    main.show()
    sys.exit(app.exec())
