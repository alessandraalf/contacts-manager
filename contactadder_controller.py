from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QCheckBox

from ui.Ui_ContactAdder import Ui_ContactAdder

from model.contact_model import ContactModel
from model.tag_model import TagModel
from model.contact_tag_model import ContactTagModel

import contactlist_controller as cl


# controller for the contactadder view
class ContactAdder(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.view = Ui_ContactAdder()
        self.view.setupUi(self)

        self.showTags()
        self.buttonBehavior()
        self.enableSaveButton()

    # TagModel is used to retrieve the data from Tags table in "ContactsManager.db".
    # every tag in the database is represented by a checkbox in "Tags" scroll area.
    def showTags(self):
        tag_model = TagModel()
        tags = tag_model.getDBTags()
        for t in tags:
            checkbox = QCheckBox()
            checkbox.setMinimumHeight(20)
            checkbox.setText(t[1])
            self.view.scrollAreaWidgetContents.layout().addWidget(checkbox)

    # define buttons behaviour.
    def buttonBehavior(self):
        self.view.back_button.clicked.connect(self.showContactList)
        self.view.save_button.clicked.connect(self.addContact)

    # enable save button when telephone field is not empty
    def enableSaveButton(self):
        self.view.telephone.textChanged.connect(self.telephoneAdded)

    # check if telephone field is not empty and enable save button
    def telephoneAdded(self):
        if not self.view.telephone.text():
            self.view.save_button.setEnabled(False)
        else:
            self.view.save_button.setEnabled(True)

    # Add a contact
    # ContactModel and ContactTagModel are used to add the data in Contacts and ContactsTags tables
    # in "ContactsManager.db".
    # (the contact id is generated in sqlite with 'AUTOINCREMENT')
    # TagModel is used to retrieve the data from Tags table in "ContactsManager.db".
    def addContact(self):
        first_name = self.view.first_name.text()
        last_name = self.view.last_name.text()
        telephone = self.view.telephone.text()
        email = self.view.email.text()
        url = self.view.url.text()
        notes = self.view.notes.toPlainText()

        # check for minimum data required
        if ((first_name is not None and first_name != "") or (last_name is not None and last_name != "")
                and telephone is not None and telephone != ""):
            new_contact = ContactModel()
            new_contact.setFields(first_name, last_name, telephone, email, url, notes)
            new_contact.addContact()

            # get the contact id from Contacts table in "ContactsManager.db".
            c_id = new_contact.getContactIdFromNameTel()

            # select checked tags and add the info in ContactsTags table as a tuple (c_id, t_id)
            tags = self.view.scrollAreaWidgetContents.layout()
            items = (tags.itemAt(i).widget() for i in range(tags.count()))
            for i in items:
                if i.isChecked():
                    # print("checked", i)
                    tag_model = TagModel()
                    tag_id = tag_model.getTagIdfromName(i.text())
                    contact_tag_model = ContactTagModel()
                    contact_tag_model.setContactId(c_id)
                    contact_tag_model.setTagId(tag_id)
                    contact_tag_model.addContactTag()
        self.showContactList()

    # change view from ContactAdder to ContactList
    def showContactList(self):
        self.parentWidget().setCentralWidget(cl.ContactList())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = QMainWindow()
    ca = ContactAdder()
    window.setCentralWidget(ca)
    window.show()
    sys.exit(app.exec_())

