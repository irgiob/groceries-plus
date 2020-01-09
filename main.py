from PyQt5 import QtWidgets, QtCore
from gui import Ui_MainWindow
import sys
import json
import pyperclip

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
        self.ui.new_item_input_2.returnPressed.connect(self.add_item)
        self.ui.new_item_input_3.returnPressed.connect(self.add_item)
        self.ui.new_item_input_4.returnPressed.connect(self.add_item)
        self.ui.add_item_button.clicked.connect(self.add_item)
        self.ui.delete_button.clicked.connect(self.del_item)

        # update item info
        self.ui.edit_button.clicked.connect(self.update_item)

        # list click
        self.ui.grocery_list.itemClicked.connect(self.open_item)

        # export shopping list
        self.ui.export_button.clicked.connect(self.export_list)

    # checks for existing grocery list or makes one if none
    def open_grocery_list(self):
        try:
            data_file = open('data.txt')
            self.data = json.load(data_file)
            for item in list(self.data.keys()):
                self.insert_in_list(item)
        except IOError:
            self.data = {}
            data_file = open('data.txt', 'w')
            json.dump(self.data,data_file)
        finally:
            data_file.close()
        return self.data

    # add new item to grocery list
    def add_item(self):
        # grabs text from input boxes
        name = self.ui.new_item_input.text().capitalize()
        desc = self.ui.new_item_input_2.text()
        price = self.ui.new_item_input_3.text()
        quan = self.ui.new_item_input_4.text()
        is_valid = self.is_valid_item(name, desc, price, quan)
        # adds item to data file & list if not already there
        if not (name in self.data) and is_valid:
            self.data[name] = {
                'Description': str(desc), 
                'Price':f'${price}', 
                'Quantity': int(quan), 
                'Include in list?': True
            }
            self.insert_in_list(name)
            print(f'log: {name} added to grocery list')
        # empties input boxes
        self.ui.new_item_input.setText('')
        self.ui.new_item_input_2.setText('')
        self.ui.new_item_input_3.setText('')
        self.ui.new_item_input_4.setText('')

    # checks if item added is valid
    def is_valid_item(self, name, desc, price, quan):
        # initalize popup message incase invalid
        popup = QtWidgets.QMessageBox()
        popup.setWindowTitle("Invalid Item Alert")
        # check if each input box is filled
        if len(name) < 1 or len(desc) < 1 or len(price) < 1 or len(quan) < 1:
            popup.setText("Invalid. All boxes must be filled.")
            x = popup.exec_()
            return False
        # check if name has only letter
        elif not name.isalpha():
            popup.setText("Invalid. Name must be alphabet only.")
            x = popup.exec_()
            return False
        # check if price and quantity are numbers
        elif not (price.replace('.','',1).isdigit() and quan.isdigit()):
            popup.setText("Invalid. Price or quantity is not a number")
            x = popup.exec_()
            return False
        return True

    # adds item to list with checkbox
    def insert_in_list(self, input_text):
        added_item = QtWidgets.QListWidgetItem()
        added_item.setFlags(added_item.flags() | QtCore.Qt.ItemIsUserCheckable)
        # sets the checkbox in the list based on bool value in data
        if self.data[input_text]['Include in list?'] == True:
            added_item.setCheckState(QtCore.Qt.Checked)
        else:
            added_item.setCheckState(QtCore.Qt.Unchecked)
        # adds the text to the list
        added_item.setText(input_text)
        self.ui.grocery_list.addItem(added_item)

    # delete item from grocery list & data file, including info panel
    def del_item(self):
        sel_items = self.ui.grocery_list.selectedItems()
        for item in sel_items:
            self.ui.grocery_list.takeItem(self.ui.grocery_list.row(item))
            self.data.pop(item.text())
        for i in range(NUM_ITEM_OPTIONS):
            row = self.ui.item_info.item(i, 1)
            row.setText('')

    # updates table with item info from data file
    def open_item(self, item):
        is_in_list = (item.checkState() == QtCore.Qt.Checked)
        self.data[item.text()]['Include in list?'] = is_in_list
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

    # export shopping list
    def export_list(self):
        output_text = ''
        budget = 0
        message = 'The shopping list has been exported.\n'
        # add each item to the list and add it to the budget
        for item in self.data:
            if self.data[item]['Include in list?'] == True:
                price = self.data[item]['Price'][1:]
                quantity = self.data[item]['Quantity']
                output_text += f'{quantity}x {item:<15} ${price}\n'
                budget += float(price) * int(quantity)
        # add budget to the list if option is checked
        if self.ui.budget_button.isChecked():
            output_text += f'Overall budget required: ${budget:.2f}.'
            message += f'Overall budget required: ${budget:.2f}.'
        # copy the shopping list to the clipboard
        pyperclip.copy(output_text)
        pyperclip.paste()  
        # create popup message stating the list has been exported
        popup = QtWidgets.QMessageBox()
        popup.setWindowTitle("Shopping List Exported")
        popup.setText(message)
        x = popup.exec_()


    # saves changes to grocery list at exit
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