from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QCheckBox

from ui.Ui_ContactEditor import Ui_ContactEditor

from model.contact_model import ContactModel
from model.tag_model import TagModel
from model.contact_tag_model import ContactTagModel

import contactviewer_controller as cv
import contactlist_controller as cl


# controller for the contacteditor view
class ContactEditor(QWidget):
    def __init__(self, contact):
        super().__init__()

        self.contact = contact

        # Set up the user interface from Designer.
        self.view = Ui_ContactEditor()
        self.view.setupUi(self)

        self.showContactData()
        self.showTags()
        self.buttonBehavior()

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
    # every tag is represented by a checkbox, checked only if the contact is associated to it.
    def showTags(self):
        tag_model = TagModel()
        tags = tag_model.getDBTags()
        contact_tag_model = ContactTagModel()
        contact_tag_model.setContactId(self.contact.c_id)
        contact_tags = contact_tag_model.getTagFromId()
        current_tags = []

        for t in contact_tags:
            current_tags.append(t[0])
        # checkbox tag list
        for tag in tags:
            checkbox = QCheckBox()
            checkbox.setMinimumHeight(20)
            checkbox.setText(tag[1])
            if tag[1] in current_tags:
                checkbox.setChecked(True)
            self.view.scrollAreaWidgetContents.layout().addWidget(checkbox)

    # define buttons behaviour.
    def buttonBehavior(self):
        self.view.save_button.clicked.connect(self.updateContact)
        self.view.delete_button.clicked.connect(self.deleteContact)
        # Asyncronous updates
        self.view.first_name.textEdited.connect(self.asyncUpdateContact)
        self.view.last_name.textEdited.connect(self.asyncUpdateContact)
        self.view.telephone.textEdited.connect(self.asyncUpdateContact)
        self.view.email.textEdited.connect(self.asyncUpdateContact)
        self.view.url.textEdited.connect(self.asyncUpdateContact)

    # Save changes
    # ContactModel and ContactTagModel are used to update data in Contact and ContactsTags tables
    # in "ContactsManager.db".
    # In Contact table, contact standard info are updated in the specific row of the db
    # In ContactsTags table, all the existing rows are deleted and then re-inserted
    def updateContact(self):
        v = self.view
        c_id = self.contact.c_id
        first_name = v.first_name.text()
        last_name = v.last_name.text()
        tel = v.telephone.text()
        email = v.email.text()
        url = v.url.text()
        notes = v.notes.toPlainText()

        if (first_name != "" and first_name is not None and last_name != "" and last_name is not None):
            modified_contact = ContactModel()
            modified_contact.setFields(first_name, last_name, tel, email, url, notes)
            modified_contact.updateContact(c_id)

            tag_contact_model = ContactTagModel()
            tag_contact_model.setContactId(c_id)
            tag_contact_model.deleteContactTagsFromId()

            tags = v.scrollAreaWidgetContents.layout()

            items = (tags.itemAt(i).widget() for i in range(tags.count()))

            # select checked tags and add the info in ContactsTags table as a tuple (c_id, t_id)
            for i in items:
                if i.isChecked():
                    tag_model = TagModel()
                    tag_id = tag_model.getTagIdfromName(i.text())
                    contact_tag_model = ContactTagModel()
                    contact_tag_model.setContactId(c_id)
                    contact_tag_model.setTagId(tag_id)
                    contact_tag_model.addContactTag()

            self.showContactList()

    # Async Save changes
    # ContactModel and ContactTagModel are used to update data in Contact and ContactsTags tables
    # in "ContactsManager.db".
    # In Contact table, contact standard info are updated in the specific row of the db
    # In ContactsTags table, all the existing rows are deleted and then re-inserted
    def asyncUpdateContact(self):
        v = self.view
        c_id = self.contact.c_id
        first_name = v.first_name.text()
        last_name = v.last_name.text()
        tel = v.telephone.text()
        email = v.email.text()
        url = v.url.text()
        notes = v.notes.toPlainText()

        if (first_name != "" and first_name is not None and last_name != "" and last_name is not None):
            modified_contact = ContactModel()
            modified_contact.setFields(first_name, last_name, tel, email, url, notes)
            modified_contact.updateContact(c_id)

            tag_contact_model = ContactTagModel()
            tag_contact_model.setContactId(c_id)

            tag_contact_model.deleteContactTagsFromId()

            tags = v.scrollAreaWidgetContents.layout()

            items = (tags.itemAt(i).widget() for i in range(tags.count()))
            # select checked tags and add the info in ContactsTags table as a tuple (c_id, t_id)
            for i in items:
                if i.isChecked():
                    tag_model = TagModel()
                    tag_id = tag_model.getTagIdfromName(i.text())
                    contact_tag_model = ContactTagModel()
                    contact_tag_model.setContactId(c_id)
                    contact_tag_model.setTagId(tag_id)
                    contact_tag_model.addContactTag()

    # Delete Contact
    # ContactModel and ContactTagModel are used to delete data from Contact and ContactsTags tables
    # in "ContactsManager.db".
    def deleteContact(self):
        v = self.view
        first_name = v.first_name.text()
        last_name = v.last_name.text()
        telephone = v.telephone.text()
        email = v.email.text()
        url = v.url.text()
        notes = v.notes.toPlainText()

        # delete this contact from Contacts table
        contact_to_delete = ContactModel()
        c_id = self.contact.getId()
        contact_to_delete.setAllFields(c_id, first_name, last_name, telephone, email, url, notes)
        contact_to_delete.deleteContact()

        # delete tuples (c_id, t_id) from ContactsTags table
        contact_tag = ContactTagModel()
        contact_tag.setContactId(c_id)
        contact_tag.deleteContactTagsFromId()

        self.showContactList()

    # change view from ContactEditor to ContactViewer
    def showContactViewer(self):
        up_contact = ContactModel()
        up_contact.getContactFromId_v2(self.contact.c_id)

        self.parentWidget().setCentralWidget(cv.ContactViewer(up_contact))

    # change view from ContactEditor to ContactList
    def showContactList(self):
        self.parentWidget().setCentralWidget(cl.ContactList())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # Prova
    a = ContactModel()
    a.setFirstName("ale")
    a.setLastName("alfa")
    a.setTelephone("00555")
    # # #
    window = QMainWindow()
    ce = ContactEditor(a)
    window.setCentralWidget(ce)
    window.show()
    sys.exit(app.exec_())


