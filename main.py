from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.Ui_ContactsManager import Ui_ContactsManager

import contactlist_controller as cl


class ContactsManager(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the user interface from Designer.
        self.view = Ui_ContactsManager()
        self.view.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ContactsManager()

    window.setCentralWidget(cl.ContactList())
    window.show()
    sys.exit(app.exec_())


