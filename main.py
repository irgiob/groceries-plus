from PyQt5 import QtWidgets
from gui import Ui_MainWindow
import sys
import json

NUM_ITEM_OPTIONS = 4

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        # initialize main window
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.data = self.open_grocery_list()

        # add & delete item functions
        self.ui.new_item_input.returnPressed.connect(self.add_item)
        self.ui.add_item.clicked.connect(self.add_item)
        self.ui.delete_button.clicked.connect(self.del_item)

        # update item info
        self.ui.edit_button.clicked.connect(self.update_item)

        # list click
        self.ui.grocery_list.itemClicked.connect(self.open_item)

    # checks for existing grocery list or makes one if none
    def open_grocery_list(self):
        try:
            data_file = open('data.txt')
            data = json.load(data_file)
            for item in list(data.keys()):
                self.ui.grocery_list.addItem(item)
        except IOError:
            data = {}
            data_file = open('data.txt', 'w')
            json.dump(data,data_file)
        finally:
            data_file.close()
        return data

    # add new item to grocery list
    def add_item(self):
        input_text = self.ui.new_item_input.text()
        if not (input_text in self.data):
            self.ui.grocery_list.addItem(input_text)
            self.data[input_text] = {'Description':'N/A', 'Price':'N/A', 'Quantity': 1, 'Include in list?': True}
        self.ui.new_item_input.setText('')
        print(f'log: {input_text} added to grocery list')

    # delete items from grocery list
    def del_item(self):
        sel_items = self.ui.grocery_list.selectedItems()
        for item in sel_items:
            self.ui.grocery_list.takeItem(self.ui.grocery_list.row(item))
            self.data.pop(item.text())
        for i in range(NUM_ITEM_OPTIONS):
            row = self.ui.item_info.item(i, 1)
            row.setText('')

    # get details on sepecific items
    def open_item(self, item):
        for i in range(len(self.data[item.text()])):
            row = self.ui.item_info.item(i, 1)
            row.setText(str(list(self.data[item.text()].values())[i]))

    # updates details on grocery list items
    def update_item(self):
        sel_item = self.ui.grocery_list.selectedItems()[0].text()
        for i in range(NUM_ITEM_OPTIONS):
            key = self.ui.item_info.item(i, 0).text()
            val = self.ui.item_info.item(i, 1).text()
            self.data[sel_item][key] = val
        print(f'Updated info: {self.data}')

    # saves changes to grocery list at exitg
    def closeEvent(self, event):
        print(f'Saved data: {self.data}')
        with open('data.txt', 'w') as outfile:
            json.dump(self.data, outfile)
        outfile.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())