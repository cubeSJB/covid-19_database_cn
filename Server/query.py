# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Query_Main(object):
    def setupUi(self, Query_Main):
        Query_Main.setObjectName("Query_Main")
        Query_Main.resize(424, 334)
        self.Query = QtWidgets.QPushButton(Query_Main)
        self.Query.setGeometry(QtCore.QRect(290, 40, 89, 25))
        self.Query.setObjectName("Query")
        self.pushButton_2 = QtWidgets.QPushButton(Query_Main)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 80, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget = QtWidgets.QWidget(Query_Main)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 40, 221, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Area = QtWidgets.QLineEdit(self.layoutWidget)
        self.Area.setObjectName("Area")
        self.verticalLayout.addWidget(self.Area)
        self.Date = QtWidgets.QDateEdit(self.layoutWidget)
        self.Date.setObjectName("Date")
        self.verticalLayout.addWidget(self.Date)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.Info = QtWidgets.QTextEdit(Query_Main)
        self.Info.setGeometry(QtCore.QRect(50, 110, 331, 191))
        self.Info.setObjectName("Info")

        self.retranslateUi(Query_Main)
        QtCore.QMetaObject.connectSlotsByName(Query_Main)

    def retranslateUi(self, Query_Main):
        _translate = QtCore.QCoreApplication.translate
        Query_Main.setWindowTitle(_translate("Query_Main", "Query"))
        self.Query.setText(_translate("Query_Main", "Query"))
        self.pushButton_2.setText(_translate("Query_Main", "Back"))
        self.label.setText(_translate("Query_Main", "Area"))
        self.label_2.setText(_translate("Query_Main", "Date"))
