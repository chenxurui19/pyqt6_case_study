# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 17:18
# @Author  : CXRui
# @File    : 6-QLabel基础.py
# @Description :
import sys
from PyQt6.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QLabel, QWidget
from PyQt6.QtGui import QPixmap, QPalette
from PyQt6.QtCore import Qt


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建标签
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        # 设置标签内容
        # 添加文本信息
        label1.setText("<font color=yellow>这是一个文本标签。</font>")
        # 允许背景填充
        label1.setAutoFillBackground(True)
        # 创建背景
        palette = QPalette()
        # 设置背景色
        palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.blue)
        # 设置背景
        label1.setPalette(palette)
        # 文本居中
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # 设置超链接
        label2.setText("<a href='#'>欢迎使用python GUI程序</a>")
        # 设置居中
        label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap("../images/python.png"))
        # 如果设为True，用浏览器打开网页，如果设为False，调用槽函数
        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://item.jd.com/12417265.htmk'>感谢关注《Python从菜鸟到高手》</a>")
        label4.setAlignment(Qt.AlignmentFlag.AlignRight)
        label4.setToolTip("这是一个超级链接")

        # 垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        # 关联槽
        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)
        # 添加布局
        self.setLayout(vbox)
        self.setWindowTitle("QLabel控件演示")

    # 设置槽
    def linkHovered(self):
        print("当鼠标滑过label2标签时,触发事件")

    def linkClicked(self):
        print("当鼠标单击label4标签时，触发事件")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec())
