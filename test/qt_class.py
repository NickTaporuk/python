#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PyQt4 import QtGui, QtCore


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Hello World")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.btnQuit = QtGui.QPushButton("Exit")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.connect(self.btnQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
