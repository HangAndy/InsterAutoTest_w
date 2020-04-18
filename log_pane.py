#!/usr/bin/env python 
# encoding: utf-8 
"""
   ==============================================
    objectName： InsterAutoTest_w
    fileName：   log_pane
    Author:      Hang
    Date:        2020/4/13/013
    description: 
   ==============================================

"""

import sys
from time import sleep

from PyQt5 import QtGui
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtGui import QIcon, QTextCursor, QTextCharFormat, QTextImageFormat, QTextDocumentFragment, QTextListFormat, \
    QTextTableFormat, QTextFrameFormat
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, qApp, QPushButton, QLineEdit, QAction, QCompleter, QTextEdit

from ui_log_Pane import Ui_Form


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.setWindowTitle("")
        self.setWindowTitle("")
        self.resize(500, 500)
        self.setupUi(self)
        self.setup_ui()

    def setup_ui(self):
        pass

    # ================================== start

    def hang(self, num):
            self.log_textEdit.append(num)


# ================================== end

if __name__ == '__main__':
    # 测试
    # 判断当前模块是被导入执行还是直接执行
    app = QApplication(sys.argv)
    window = Window()
    # window = QWidget()
    window.show()
    sys.exit(app.exec_())
