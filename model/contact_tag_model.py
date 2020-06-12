from db import Db


# model for contacttag
# it handles the db ContactsTags table
class ContactTagModel:
    def __init__(self):
        self.con_id = ""
        self.tag_id = ""

    # setter methods
    def setContactId(self, con_id):
        self.con_id = con_id

    def setTagId(self, tag_id):
        self.tag_id = tag_id
        self.tag_id = tag_id

    # getter methods
    def getContactId(self):
        return self.con_id

    def getTagId(self):
        return self.tag_id

    # return the ids of contacts with specific tag
    def searchContactsByTag(self):
        db = Db()
        ids = db.getContactsFromTag(self.tag_id)
        return ids

    # return all tags associated to a contact id
    def getTagFromId(self):
        db = Db()
        tags = db.getTagsFromContactId(self.con_id)
        return tags

    # store in the database a specific tuple (con_id, tag_id)
    def addContactTag(self):
        db = Db()
        con_id = self.con_id
        tag_id = self.tag_id
        if (con_id != "" and con_id is not None and tag_id !="" and tag_id is not None):
            db.addContactTag(con_id, tag_id)

    # delete all (con_id, tag_id) tuples with a specific contact id
    def deleteContactTagsFromId(self):
        db = Db()
        con_id = self.con_id
        db.deleteContactTagsFromId(con_id)
