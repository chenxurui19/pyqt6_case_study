# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 14:06
# @Author  : CXRui
# @File    : 24-QFileDialog文件对话框.py
# @Description :
import sys
from PyQt6.QtCore import *
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.button1 = QPushButton("加载图片")
        self.button1.clicked.connect(self.loadImage)
        layout.addWidget(self.button1)
        self.imageLabel = QLabel()      # 负责显示加载的图片文件
        layout.addWidget(self.imageLabel)

        self.button2 = QPushButton("加载文件文本")
        self.button2.clicked.connect(self.loadText)
        layout.addWidget(self.button2)
        self.contents = QTextEdit()
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("文件对话框演示")

    def loadImage(self):
        # 第三个参数是路径，第四个是文件默认的文件格式
        # 两个返回参数，第二个是是否退出
        fname, _ = QFileDialog.getOpenFileName(self, "打开文件", ".", "图像文件(*.jpg *.png)")
        self.imageLabel.setPixmap(QPixmap(fname))

    def loadText(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)    # 设置打开文件格式
        dialog.setNameFilters(["All Files (*)"])        # 设置要打开的文件
        if dialog.exec():
            filenames = dialog.selectedFiles()
            f = open(filenames[0], encoding="utf-8", mode="r")
            with f:     # with语句可以自动关闭文件
                data = f.read()
                self.contents.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec())