from PyQt5.QtWidgets import QPushButton
import contactviewer_controller as cv


# ContactButton generalizes buttons in contact list
# when clicked, the view changes to button's specific contact ContactViewer
class ContactButton(QPushButton):
    def __init__(self, contact, main_window):
        super().__init__()

        self.mw = main_window
        self.contact = contact

        self.defineButton()

    # add properties and behaviour to the button
    def defineButton(self):
        c = self.contact
        self.setText(c.getFirstName() + " " + c.getLastName())
        self.setFixedHeight(50)
        self.clicked.connect(self.viewContactInfo)

    # go to contact details view
    def viewContactInfo(self):
        # Get MainWindow from ContactButton
        # is there a more efficient way?
        mw = self.parentWidget().parentWidget().parentWidget().parentWidget().parentWidget()
        mw.setCentralWidget(cv.ContactViewer(self.contact))

