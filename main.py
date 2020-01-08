from PyQt5 import QtWidgets
from gui import Ui_MainWindow
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.add_item)

    def add_item(self):
        input_text = self.ui.lineEdit.text()
        self.ui.List.addItem(input_text)
        print(input_text)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())