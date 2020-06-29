from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtGui

from ui.Ui_ContactList import Ui_ContactList

from model.contact_model import ContactModel
from model.tag_model import TagModel
from model.contact_button_model import ContactButton

import tagadder_controller as ta
import contactadder_controller as ca


# controller for the contactlist view
class ContactList(QWidget):
    def __init__(self):
        super().__init__()
        # Set up the user interface from Designer.
        self.view = Ui_ContactList()
        self.view.setupUi(self)

        self.addContactIcon()
        self.buttonBehavior()
        self.inputChanged()
        self.showAllContacts()
        self.showFields()
        self.showTags()

    # add contact icon to add QPushButton
    def addContactIcon(self):
        addIcon = QtGui.QPixmap("icon/addcontact.png")
        self.view.add_button.setIcon(QtGui.QIcon(addIcon))
        self.view.add_button.setIconSize(QSize(32, 32))

    # define buttons behaviour.
    def buttonBehavior(self):
        self.view.add_button.clicked.connect(self.showContactAdder)
        self.view.tag_button.clicked.connect(self.showTagAdder)

    # when some input changes (searchbar/orderby/tagselection) do a real time search
    # connect any 'input changed' to realTimeSearch() function
    def inputChanged(self):
        self.view.searchbar.textChanged.connect(self.realTimeSearch)
        self.view.orderby.currentTextChanged.connect(self.realTimeSearch)
        self.view.scroll_tag.currentTextChanged.connect(self.realTimeSearch)

    # show in a button list all the contacts of the database represented by a customized button (ContactButton)
    # ContactModel is used to retrieve the data from Contacts table in "ContactsManager.db".
    def showAllContacts(self):
        contacts = ContactModel().getContacts()
        if contacts is not None:
            for c in contacts:
                contact_model = ContactModel()
                contact_model.setAllFields(c[0], c[1], c[2], c[3], c[4], c[5], c[6])
                c_button = ContactButton(contact_model, self)
                self.view.buttonListLayout.setAlignment(Qt.AlignTop)
                self.view.buttonListLayout.addWidget(c_button)

    # show in a button list the result of realTimeSearch(). Each contact is represented by a
    # customized button (ContactButton)
    # ContactModel is used to retrieve the data from Contacts table in "ContactsManager.db".
    def showContacts(self, contacts):
        if contacts is not None:
            for c in contacts:
                contact_model = ContactModel()
                contact_model.setAllFields(c[0], c[1], c[2], c[3], c[4], c[5], c[6])
                c_button = ContactButton(contact_model, self)
                self.view.buttonListLayout.setAlignment(Qt.AlignTop)
                self.view.buttonListLayout.addWidget(c_button)

    # Show contacts fields in a scrollBar ("order by")
    # ContactModel is used to retrieve the data from Contacts table in "ContactsManager.db".
    def showFields(self):
        contact_model = ContactModel()
        contact_fields = contact_model.getContactFields()

        self.field_list = list()
        self.field_list.append([contact_fields[1], "First Name"])
        self.field_list.append([contact_fields[2], "Last Name"])

        for field in self.field_list:
            self.view.orderby.addItem(field[1])

    # Show all the tags in a scrollBar ("filter by")
    # TagModel is used to retrieve the data from Tags table in "ContactsManager.db".
    def showTags(self):
        tag_model = TagModel()
        tags = tag_model.getDBTags()
        tag_placeholder = "Select a tag..."
        self.view.scroll_tag.addItem(tag_placeholder)
        for tag in tags:
            self.view.scroll_tag.addItem(tag[1])

    # Contacts real time search
    # ContactModel and ContactTagModel are used to retrieve data in Contact and ContactsTags tables
    # in "ContactsManager.db".
    def realTimeSearch(self):
        # contact_model = ContactModel()
        # print("inputchanged")

        text_to_search = self.view.searchbar.toPlainText()
        # convert orderby selection into db exact field
        orderby = next(x[0] for x in self.field_list if x[1] == self.view.orderby.currentText())
        if self.view.scroll_tag.currentText() != "Select a tag...":
            selected_tag = self.view.scroll_tag.currentText()
        else:
            selected_tag = None
        # clear contactList
        for i in reversed(range(self.view.buttonListLayout.count())):
            self.view.buttonListLayout.itemAt(i).widget().setParent(None)
        # print("selected tag", selected_tag)
        # print("order by", orderby)
        contacts = ContactModel().contactSearch(text_to_search, orderby, selected_tag)

        self.showContacts(contacts)

    # change view from ContactList to ContactAdder
    def showContactAdder(self):
        self.parentWidget().setCentralWidget(ca.ContactAdder())

    # change view from ContactList to TagAdder
    def showTagAdder(self):
        self.parentWidget().setCentralWidget(ta.TagAdder())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = QMainWindow()
    cl = ContactList()
    window.setCentralWidget(cl)
    window.show()
    sys.exit(app.exec_())
