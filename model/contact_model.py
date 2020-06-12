from db import Db


# model for contact
# it handles the db Contacts table
class ContactModel:
    def __init__(self):
        self.c_id = ""
        self.first_name = ""
        self.last_name = ""
        self.tel = ""
        self.email = ""
        self.url = ""
        self.notes = ""

    # setter methods
    def setAllFields(self, c_id, first_name, last_name, tel, email, url, notes):
        self.c_id = c_id
        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.email = email
        self.url = url
        self.notes = notes

    def setFields(self, first_name, last_name, tel, email, url, notes):
        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.email = email
        self.url = url
        self.notes = notes

    def setId(self, c_id):
        self.c_id = c_id

    def setFirstName(self, first_name):
        self.first_name = first_name

    def setLastName(self, last_name):
        self.last_name = last_name

    def setTelephone(self, tel):
        self.tel = tel

    def setEmail(self, email):
        self.email = email

    def setUrl(self, url):
        self.url = url

    def setNotes(self, notes):
        self.notes = notes

    # getter methods
    def getId(self):
        return self.c_id

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getTelephone(self):
        return self.tel

    def getEmail(self):
        return self.email

    def getUrl(self):
        return self.url

    def getNotes(self):
        return self.notes

    # add contact data in the database
    def addContact(self):
        first_name = self.first_name
        last_name = self.last_name
        tel = self.tel
        email = self.email
        url = self.url
        notes = self.notes

        db = Db()
        # a contact must have at least a telephone number and a name
        if((first_name is not None and first_name != "") or (last_name is not None and last_name != "")
                and tel is not None and tel != ""):
            db.addContact(first_name, last_name, tel, email, url, notes)

    # get contacts from the database
    def getContacts(self):
        db = Db()
        contacts = db.getContactsByFirstName()
        return contacts

    # get all the contacts of the database
    def getDbContacts(self):
        db = Db()
        contacts = db.getContactsByFirstName()
        return contacts

    # update a contact
    def updateContact(self, c_id):
        db = Db()
        db.updateContact(c_id, self.first_name, self.last_name, self.tel, self.email, self.url, self.notes)

    # search contacts given searchText, filtered by tag and orderded by orderby
    def contactSearch(self, text, orderby, tag):
        db = Db()
        contacts = db.contactSearch(text, orderby, tag)
        return contacts

    # get a contact
    def getContactFromId(self):
        db = Db()
        contact = db.getContactfromId(self.c_id)
        return contact

    # get a contact with a given id
    def getContactFromId_v2(self, c_id):
        db = Db()
        contact = db.getContactfromId(c_id)
        return contact

    # get contact_id from contact name and telephone
    def getContactIdFromNameTel(self):
        db = Db()
        return db.getContactIdFomNameTel(self.first_name, self.last_name, self.tel)[0]

    # delete a contact
    def deleteContact(self):
        db = Db()
        db.deleteContact(self.c_id)

    # get contact fields names
    def getContactFields(self):
        db = Db()
        schema = db.getContactSchema()
        fields = []
        for f in schema.description:
            fields.append(f[0])
        return fields
