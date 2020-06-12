from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtCore import Qt

from ui.Ui_TagAdder import Ui_TagAdder

from model.tag_model import TagModel

import contactlist_controller as cl


# controller for the tagadder view
class TagAdder(QWidget):
    def __init__(self):
        super().__init__()
        # Set up the user interface from Designer.
        self.view = Ui_TagAdder()
        self.view.setupUi(self)

        self.showTags()
        self.buttonBehavior()

    # Show existent tags
    # TagModel is used to retrieve the data from Tags table in "ContactsManager.db".
    # every tag is represented by a QLabel.
    def showTags(self):
        tag_model = TagModel()
        tags = tag_model.getDBTags()
        self.view.scrollAreaWidgetContents.layout().setAlignment(Qt.AlignTop)
        for t in tags:
            item = QLabel(t[1])
            self.view.scrollAreaWidgetContents.layout().addWidget(item)

    # define buttons behaviour.
    def buttonBehavior(self):
        self.view.tag_name.returnPressed.connect(self.addTag)
        self.view.save_button.clicked.connect(self.addTag)
        self.view.back_button.clicked.connect(self.showContactList)

    # Add tag
    # Each tag is associated to a TagModel
    # tag data are stored in Tags table of "ContactsDatabase.db"
    def addTag(self):
        tag_name = self.view.tag_name.text()
        if (tag_name != "" and tag_name is not None):
            new_tag = TagModel()
            new_tag.setTagName(tag_name)
            new_tag.addTag()
            # when a new tag is added, defaultTagList() is called to refresh the tag list
            self.defaultTagList()
            # clear text in qline
            self.view.tag_name.setText("")

    # refresh the tag list
    def defaultTagList(self):
        for i in reversed(range(self.view.scrollAreaWidgetContents.layout().count())):
            tag = self.view.scrollAreaWidgetContents.layout().itemAt(i).widget()
            # remove it from the layout list
            self.view.scrollAreaWidgetContents.layout().removeWidget(tag)
            # remove it from the gui
            tag.setParent(None)
        self.showTags()
        # print("default")

    # change view from TagAdder to ContactList
    def showContactList(self):
        self.parentWidget().setCentralWidget(cl.ContactList())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = QMainWindow()
    ta = TagAdder()
    window.setCentralWidget(ta)
    window.show()
    sys.exit(app.exec_())
