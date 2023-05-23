# -*- coding: utf-8 -*-
# @Time    : 2023/5/20 00:15
# @Author  : CXRui
# @File    : 10-用掩码限制QLineEdit控件的输入.py
# @Description :
from PyQt6.QtWidgets import *
import sys


class QLineEditMask(QWidget):
    def __init__(self):
        super(QLineEditMask, self).__init__()
        self.initUI()

    def initUI(self):
        formLayout = QFormLayout()
        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()
        # 后参数位输入时默认显示内容
        ipLineEdit.setInputMask("000.000.000.000;_")
        macLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        dateLineEdit.setInputMask("000-00-00_")
        licenseLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")
        formLayout.addRow("数字掩码", ipLineEdit)
        formLayout.addRow("Mac掩码", macLineEdit)
        formLayout.addRow("日期掩码", dateLineEdit)
        formLayout.addRow("许可证掩码", licenseLineEdit)
        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditMask()
    main.show()
    sys.exit(app.exec())
