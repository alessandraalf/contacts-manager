from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtCore import Qt

from ui.Ui_ContactViewer import Ui_ContactViewer

from model.contact_model import ContactModel
from model.contact_tag_model import ContactTagModel

import contactlist_controller as cl
import contacteditor_controller as ce


# controller for the contactviewer view
class ContactViewer(QWidget):
    def __init__(self, contact):
        super().__init__()

        self.contact = contact

        # Set up the user interface from Designer.
        self.view = Ui_ContactViewer()
        self.view.setupUi(self)

        self.buttonBehavior()
        self.showContactData()
        self.showTags()

    # define buttons behaviour.
    def buttonBehavior(self):
        self.view.back_button.clicked.connect(self.showContactList)
        self.view.edit_button.clicked.connect(self.showContactEditor)

    # shows the data for a specific contact
    def showContactData(self):
        v = self.view
        c = self.contact
        v.contactName.setText(c.getFirstName() + " " + c.getLastName())
        v.first_name.setText(c.getFirstName())
        v.last_name.setText(c.getLastName())
        v.telephone.setText(c.getTelephone())
        v.email.setText(c.getEmail())
        v.url.setText(c.getUrl())
        v.notes.setText(c.getNotes())

    # Show contact tags
    # TagModel and ContactTagModel are used to retrieve the data from Tags and ContactsTags tables
    # in "ContactsManager.db".
    # every tag associated to the contact is represented by a QLabel.
    def showTags(self):
        contact_tag_model = ContactTagModel()
        contact_tag_model.setContactId(self.contact.getId())
        contact_tags = contact_tag_model.getTagFromId()
        current_tags = []
        self.view.scrollAreaWidgetContents.layout().setAlignment(Qt.AlignTop)
        for t in contact_tags:
            # print("tag", t)
            current_tags.append(t[0])
        for t in current_tags:
            tag = QLabel()
            tag.setText(t)
            self.view.scrollAreaWidgetContents.layout().addWidget(tag)

    # change view from ContactViewer to ContactList
    def showContactList(self):
        self.parentWidget().setCentralWidget(cl.ContactList())

    # change view from ContactViewer to ContactEditor
    def showContactEditor(self):
        self.parentWidget().setCentralWidget(ce.ContactEditor(self.contact))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = QMainWindow()
    # Prova
    a = ContactModel()
    a.setFirstName("ale")
    a.setLastName("alfa")
    a.setTelephone("00555")
    ###
    ca = ContactViewer(a)
    window.setCentralWidget(ca)
    window.show()
    sys.exit(app.exec_())


