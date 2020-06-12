from db import Db


# model for tag
# it handles the db Tags table
class TagModel:
    def __init__(self):
        self.t_id = ""
        self.tag_name = ""

    # setter methods
    def setAllFields(self, t_id, tag_name):
        self.t_id = t_id
        self.tag_name = tag_name

    def setId(self, t_id):
        self.t_id = t_id

    def setTagName(self, tag_name):
        self.tag_name = tag_name

    # getter methods
    def getId(self):
        return self.t_id

    def getTagName(self):
        return self.tag_name

    # get tag_id from tag_name
    def getTagIdfromName(self, tag_name):
        db = Db()
        t_id = db.getTagIdfromName(tag_name)
        return t_id[0]

    # save tag in database
    def addTag(self):
        db = Db()
        tag_name = self.tag_name
        if (tag_name !="" and tag_name is not None):
            db.addTag(tag_name)

    # retrieve from database all tags
    def getDBTags(self):
        db = Db()
        tags = db.getTags()
        return tags

