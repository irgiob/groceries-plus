# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'price_scrape_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

NUM_ITEM_OPTIONS = 3

class Ui_Scraper(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 191, 271))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 20, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(220, 50, 161, 192))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(85)
        self.tableWidget.verticalHeader().setDefaultSectionSize(54)
        self.tableWidget.verticalHeader().setMinimumSectionSize(21)

        for j in range(NUM_ITEM_OPTIONS):
            item = QtWidgets.QTableWidgetItem()
            item.setText("WOO")
            self.tableWidget.setItem(j-1, 1, item)

        self.retranslateUi(Dialog)
        #self.buttonBox.accepted.connect(Dialog.accept)
        #self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Online Item Select"))
        self.label.setText(_translate("Dialog", "Online Item Select"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Name"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Price"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Discount"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Value"))
