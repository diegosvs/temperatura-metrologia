# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste-tela.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Bt1 = QtWidgets.QPushButton(self.centralwidget)
        self.Bt1.setGeometry(QtCore.QRect(210, 100, 93, 28))
        self.Bt1.setObjectName("Bt1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 180, 121, 41))
        self.label.setObjectName("label")
        self.Bt2 = QtWidgets.QPushButton(self.centralwidget)
        self.Bt2.setGeometry(QtCore.QRect(390, 100, 93, 28))
        self.Bt2.setObjectName("Bt2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Bt1.clicked.connect(self.label.hide)
        self.Bt2.clicked.connect(self.label.raise)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Bt1.setText(_translate("MainWindow", "texto 1"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.Bt2.setText(_translate("MainWindow", "teste 2"))


