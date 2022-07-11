# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 249)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(530, 60, 89, 25))
        self.Login.setObjectName("Login")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(530, 100, 89, 25))
        self.exit.setObjectName("exit")
        self.Register = QtWidgets.QPushButton(self.centralwidget)
        self.Register.setGeometry(QtCore.QRect(530, 140, 89, 25))
        self.Register.setObjectName("Register")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 60, 335, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.labelU = QtWidgets.QLabel(self.layoutWidget)
        self.labelU.setObjectName("labelU")
        self.verticalLayout_2.addWidget(self.labelU)
        self.labelP = QtWidgets.QLabel(self.layoutWidget)
        self.labelP.setObjectName("labelP")
        self.verticalLayout_2.addWidget(self.labelP)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Server = QtWidgets.QLineEdit(self.layoutWidget)
        self.Server.setObjectName("Server")
        self.verticalLayout.addWidget(self.Server)
        self.User = QtWidgets.QLineEdit(self.layoutWidget)
        self.User.setObjectName("User")
        self.verticalLayout.addWidget(self.User)
        self.Password = QtWidgets.QLineEdit(self.layoutWidget)
        self.Password.setObjectName("Password")
        self.verticalLayout.addWidget(self.Password)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Login.setText(_translate("MainWindow", "Login"))
        self.exit.setText(_translate("MainWindow", "exit"))
        self.Register.setText(_translate("MainWindow", "Register"))
        self.label.setText(_translate("MainWindow", "Server"))
        self.labelU.setText(_translate("MainWindow", "User"))
        self.labelP.setText(_translate("MainWindow", "Password"))
