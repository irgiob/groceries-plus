# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groceries_plus_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

NUM_ITEM_OPTIONS = 4

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grocery_list = QtWidgets.QListWidget(self.centralwidget)
        self.grocery_list.setGeometry(QtCore.QRect(30, 60, 281, 481))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.grocery_list.setFont(font)
        self.grocery_list.setObjectName("grocery_list")
        self.add_item_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_item_button.setGeometry(QtCore.QRect(340, 460, 113, 32))
        self.add_item_button.setObjectName("add_item_button")
        self.new_item_input = QtWidgets.QLineEdit(self.centralwidget)
        self.new_item_input.setGeometry(QtCore.QRect(350, 340, 321, 21))
        self.new_item_input.setInputMask("")
        self.new_item_input.setText("")
        self.new_item_input.setReadOnly(False)
        self.new_item_input.setClearButtonEnabled(False)
        self.new_item_input.setObjectName("new_item_input_name")
        self.app_title = QtWidgets.QLabel(self.centralwidget)
        self.app_title.setGeometry(QtCore.QRect(30, 10, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.app_title.setFont(font)
        self.app_title.setObjectName("app_title")
        self.item_info = QtWidgets.QTableWidget(self.centralwidget)
        self.item_info.setGeometry(QtCore.QRect(340, 60, 431, 192))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.item_info.setFont(font)
        self.item_info.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.item_info.setRowCount(4)
        self.item_info.setColumnCount(2)
        self.item_info.setObjectName("item_info")
        for i in range(2):
            for j in range(NUM_ITEM_OPTIONS):
                item = QtWidgets.QTableWidgetItem()
                self.item_info.setItem(j, i, item)
        self.item_info.horizontalHeader().setVisible(False)
        self.item_info.horizontalHeader().setCascadingSectionResizes(False)
        self.item_info.horizontalHeader().setDefaultSectionSize(214)
        self.item_info.horizontalHeader().setMinimumSectionSize(25)
        self.item_info.verticalHeader().setVisible(False)
        self.item_info.verticalHeader().setCascadingSectionResizes(False)
        self.item_info.verticalHeader().setDefaultSectionSize(47)
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(660, 260, 113, 32))
        self.delete_button.setObjectName("delete_button")
        self.edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_button.setGeometry(QtCore.QRect(550, 260, 113, 32))
        self.edit_button.setObjectName("edit_button")
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(350, 260, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.info_label.setFont(font)
        self.info_label.setObjectName("info_label")
        self.add_item_label = QtWidgets.QLabel(self.centralwidget)
        self.add_item_label.setGeometry(QtCore.QRect(350, 310, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.add_item_label.setFont(font)
        self.add_item_label.setObjectName("add_item_label")
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setGeometry(QtCore.QRect(612, 490, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.export_button.setFont(font)
        self.export_button.setObjectName("export_button")
        self.budget_button = QtWidgets.QRadioButton(self.centralwidget)
        self.budget_button.setGeometry(QtCore.QRect(630, 470, 181, 20))
        self.budget_button.setObjectName("budget_button")
        self.budget_button.setChecked(True)
        self.new_item_input_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.new_item_input_2.setGeometry(QtCore.QRect(350, 370, 321, 21))
        self.new_item_input_2.setInputMask("")
        self.new_item_input_2.setText("")
        self.new_item_input_2.setReadOnly(False)
        self.new_item_input_2.setClearButtonEnabled(False)
        self.new_item_input_2.setObjectName("new_item_input_desc")
        self.new_item_input_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.new_item_input_3.setGeometry(QtCore.QRect(350, 400, 321, 21))
        self.new_item_input_3.setInputMask("")
        self.new_item_input_3.setText("")
        self.new_item_input_3.setReadOnly(False)
        self.new_item_input_3.setClearButtonEnabled(False)
        self.new_item_input_3.setObjectName("new_item_input_price")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(340, 290, 431, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.new_item_input_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.new_item_input_4.setGeometry(QtCore.QRect(350, 430, 321, 21))
        self.new_item_input_4.setInputMask("")
        self.new_item_input_4.setText("")
        self.new_item_input_4.setReadOnly(False)
        self.new_item_input_4.setClearButtonEnabled(False)
        self.new_item_input_4.setObjectName("new_item_input_quan")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.New = QtWidgets.QAction(MainWindow)
        self.New.setObjectName("New")
        self.Open = QtWidgets.QAction(MainWindow)
        self.Open.setObjectName("Open")
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Groceries+"))
        self.add_item_button.setText(_translate("MainWindow", "Add"))
        self.new_item_input.setPlaceholderText(_translate("MainWindow", "Item Name"))
        self.app_title.setText(_translate("MainWindow", "Groceries+"))
        __sortingEnabled = self.item_info.isSortingEnabled()
        self.item_info.setSortingEnabled(False)
        item = self.item_info.item(0, 0)
        item.setText(_translate("MainWindow", "Description"))
        item = self.item_info.item(1, 0)
        item.setText(_translate("MainWindow", "Price"))
        item = self.item_info.item(2, 0)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.item_info.item(3, 0)
        item.setText(_translate("MainWindow", "Include in list?"))
        self.item_info.setSortingEnabled(__sortingEnabled)
        self.delete_button.setText(_translate("MainWindow", "Delete Item"))
        self.edit_button.setText(_translate("MainWindow", "Update Info"))
        self.info_label.setText(_translate("MainWindow", "Item Info"))
        self.add_item_label.setText(_translate("MainWindow", "Add new item"))
        self.export_button.setText(_translate("MainWindow", "Export Grocery List"))
        self.budget_button.setText(_translate("MainWindow", "Include budget"))
        self.new_item_input_2.setPlaceholderText(_translate("MainWindow", "Description/Brand"))
        self.new_item_input_3.setPlaceholderText(_translate("MainWindow", "Price/unit"))
        self.new_item_input_4.setPlaceholderText(_translate("MainWindow", "Quantity"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.New.setText(_translate("MainWindow", "New Grocery List"))
        self.Open.setText(_translate("MainWindow", "Open Grocery List"))
