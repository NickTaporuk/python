#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore

App = QtGui.QApplication(sys.argv)
MW = QtGui.QMainWindow()
MW.setWindowTitle("First application in QT")
MW.resize(300, 300)
label = QtGui.QLabel('<center>Hello world</center>')
btnQuit = QtGui.QPushButton("&Exit")
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
MW.setLayout(vbox)
QtCore.QObject.connect( btnQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
MW.show()
Result = App.exec_()
sys.exit(Result)
