import sqlite3


# database for contacts and tags
class Db:
    def __init__(self):
        self.connection = sqlite3.connect("ContactsDatabase.db")
        self.createContactsTable()
        self.createTagsTable()
        self.createContactsTagsTable()

    # method to create Contacts table in database
    def createContactsTable(self):
        conn = self.connection
        conn.execute("CREATE TABLE IF NOT EXISTS "
                     "Contacts("
                     "c_id integer PRIMARY KEY AUTOINCREMENT, "
                     "first_name text, "
                     "last_name text, "
                     "tel text NOT NULL UNIQUE, "
                     "email text, "
                     "url text, "
                     "notes text)")
        conn.commit()

    # method to create Tags table in database
    def createTagsTable(self):
        conn = self.connection
        conn.execute("CREATE TABLE IF NOT EXISTS "
                     "Tags("
                     "t_id integer PRIMARY KEY AUTOINCREMENT,"
                     "tag_name text NOT NULL UNIQUE)")
        conn.commit()

    # method to create ContactsTags table in database
    def createContactsTagsTable(self):
        conn = self.connection
        conn.execute("CREATE TABLE IF NOT EXISTS "
                     "ContactsTags("
                     "con_id integer, "
                     "tag_id integer,"
                     "PRIMARY KEY (con_id, tag_id),"
                     "FOREIGN KEY (con_id) REFERENCES Contacts(c_id) ON DELETE CASCADE,"
                     "FOREIGN KEY (tag_id) REFERENCES Tags(t_id) ON DELETE CASCADE)")
        self.connection.commit()

    ###
    # "EDIT" database methods
    ###

    # -------------------------------------------------------------------------------
    # Contacts methods

    # add a contact in database
    def addContact(self, first_name, last_name, tel, email, url, notes):
        conn = self.connection
        conn.execute("INSERT OR INTO Contacts "
                     "VALUES(NULL,?,?,?,?,?,?)", (first_name, last_name, tel, email, url, notes))
        conn.commit()

    # update a contact (given contact id)
    def updateContact(self, c_id, first_name, last_name, tel, email, url, notes):
        conn = self.connection
        conn.execute("UPDATE Contacts SET first_name=?, last_name=?, tel=?, email=?, url=?, notes=? WHERE c_id=?",
                     (first_name, last_name, tel, email, url, notes, c_id))
        conn.commit()

    # delete a contact (given contact id)
    def deleteContact(self, c_id):
        conn = self.connection
        conn.execute("DELETE FROM Contacts WHERE c_id =?", (c_id,))
        conn.commit()

    # get contact from database (given contact id)
    def getContactfromId(self, c_id):
        conn = self.connection
        result = conn.execute("SELECT first_name, last_name, tel, email, url, notes FROM Contacts WHERE c_id=?", (c_id,))
        return result

    # contact search with order and filter
    def contactSearch(self, text, orderby, tag):
        conn = self.connection
        # without text search
        if text == "":
            if not tag:
                sql_query = "SELECT * from Contacts  ORDER BY {} COLLATE NOCASE".format(orderby)
            else:
                sql_query = "SELECT * from Contacts LEFT JOIN ContactsTags ON c_id=con_id LEFT JOIN Tags ON tag_id=t_id WHERE tag_name='"+tag+ "'GROUP BY first_name, last_name ORDER BY " + orderby + " COLLATE NOCASE"
        # with text search
        else:
            if not tag:
                sql_query = "SELECT * from Contacts LEFT JOIN ContactsTags ON c_id=con_id LEFT JOIN Tags ON tag_id=t_id WHERE first_name LIKE '%"+text+"%' OR last_name LIKE '%"+text+"%' GROUP BY first_name, last_name ORDER BY {} COLLATE NOCASE".format(orderby)

            else:
                sql_query = "SELECT * from Contacts LEFT JOIN ContactsTags ON c_id=con_id LEFT JOIN Tags ON tag_id=t_id WHERE tag_name='"+tag+"' AND (first_name LIKE '%"+text+"%' OR last_name LIKE '%"+text+"%') GROUP BY first_name, last_name ORDER BY " + orderby + " COLLATE NOCASE"

        result = conn.execute(sql_query)
        return result

    # get all contact of the database ordered by first_name, last_name
    def getContactsByFirstName(self):
        conn = self.connection
        result = conn.execute("SELECT * FROM Contacts ORDER BY first_name COLLATE NOCASE, last_name COLLATE NOCASE")
        return result

    # get contact id from first_name last_name tel
    def getContactIdFomNameTel(self, first_name, last_name, tel):
        conn = self.connection
        result = conn.execute("SELECT c_id FROM Contacts WHERE first_name = ? AND last_name = ? AND tel= ?",
                              (first_name, last_name, tel))
        return result.fetchone()

    # get Contacts schema
    def getContactSchema(self):
        conn = self.connection
        result = conn.execute("SELECT * FROM Contacts")
        return result

    # -------------------------------------------------------------------------------
    # Tags methods

    # add tag in database
    def addTag(self, tag_name):
        conn = self.connection
        conn.execute("INSERT OR IGNORE INTO Tags VALUES(NULL, ?)", (tag_name,))
        conn.commit()

    # get all tags of the database ordered by tag_name
    def getTags(self):
        conn = self.connection
        result = conn.execute("SELECT * FROM Tags ORDER BY tag_name COLLATE NOCASE")
        return result

    # get t_id from t_name
    def getTagIdfromName(self, tag_name):
        conn = self.connection
        result = conn.execute("SELECT t_id FROM Tags WHERE tag_name=?", (tag_name,))
        return result.fetchone()

    # -------------------------------------------------------------------------------
    # ContactsTags methods

    # add contact-tag in database
    def addContactTag(self, con_id, tag_id):
        conn = self.connection
        conn.execute("INSERT INTO ContactsTags VALUES(?,?)", (con_id, tag_id))
        conn.commit()

    # get tags given contact id
    def getTagsFromContactId(self, con_id):
        conn = self.connection
        result = conn.execute("SELECT tag_name FROM Tags INNER JOIN ContactsTags ON t_id=tag_id WHERE con_id=?", (con_id,))
        return result

    # get contact ids given a tag
    def getContactsFromTag(self, tag_name):
        conn = self.connection
        result = conn.execute("SELECT c_id FROM ContactsTags INNER JOIN Tags ON tag_id = t_id WHERE tag_name =?"
                              "ORDER BY lower(FIRST_NAME) ASC, LOWER(LAST_NAME) ASC", tag_name)
        return result

    # delete all the rows of the table with a specific id
    def deleteContactTagsFromId(self, con_id):
        conn = self.connection
        conn.execute("DELETE FROM ContactsTags WHERE con_id = ?", (con_id,))
        conn.commit()
