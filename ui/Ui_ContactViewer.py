# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_qtdesigner/ContactViewer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ContactViewer(object):
    def setupUi(self, ContactViewer):
        ContactViewer.setObjectName("ContactViewer")
        ContactViewer.resize(370, 540)
        ContactViewer.setMinimumSize(QtCore.QSize(370, 540))
        ContactViewer.setMaximumSize(QtCore.QSize(370, 540))
        self.label_1 = QtWidgets.QLabel(ContactViewer)
        self.label_1.setGeometry(QtCore.QRect(50, 90, 81, 21))
        self.label_1.setObjectName("label_1")
        self.label_4 = QtWidgets.QLabel(ContactViewer)
        self.label_4.setGeometry(QtCore.QRect(50, 210, 81, 21))
        self.label_4.setObjectName("label_4")
        self.last_name = QtWidgets.QLineEdit(ContactViewer)
        self.last_name.setGeometry(QtCore.QRect(140, 130, 181, 22))
        self.last_name.setReadOnly(True)
        self.last_name.setObjectName("last_name")
        self.first_name = QtWidgets.QLineEdit(ContactViewer)
        self.first_name.setGeometry(QtCore.QRect(140, 90, 181, 22))
        self.first_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.first_name.setText("")
        self.first_name.setReadOnly(True)
        self.first_name.setObjectName("first_name")
        self.label_2 = QtWidgets.QLabel(ContactViewer)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 81, 21))
        self.label_2.setObjectName("label_2")
        self.telephone = QtWidgets.QLineEdit(ContactViewer)
        self.telephone.setGeometry(QtCore.QRect(140, 170, 181, 22))
        self.telephone.setText("")
        self.telephone.setReadOnly(True)
        self.telephone.setObjectName("telephone")
        self.contactName = QtWidgets.QLabel(ContactViewer)
        self.contactName.setGeometry(QtCore.QRect(55, 45, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.contactName.setFont(font)
        self.contactName.setText("")
        self.contactName.setAlignment(QtCore.Qt.AlignCenter)
        self.contactName.setObjectName("contactName")
        self.scrollArea = QtWidgets.QScrollArea(ContactViewer)
        self.scrollArea.setGeometry(QtCore.QRect(40, 385, 291, 101))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setKerning(True)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 291, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.url = QtWidgets.QLineEdit(ContactViewer)
        self.url.setGeometry(QtCore.QRect(140, 250, 181, 22))
        self.url.setText("")
        self.url.setReadOnly(True)
        self.url.setObjectName("url")
        self.edit_button = QtWidgets.QPushButton(ContactViewer)
        self.edit_button.setGeometry(QtCore.QRect(250, 10, 71, 32))
        self.edit_button.setObjectName("edit_button")
        self.label_5 = QtWidgets.QLabel(ContactViewer)
        self.label_5.setGeometry(QtCore.QRect(50, 250, 81, 21))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(ContactViewer)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 81, 21))
        self.label_3.setObjectName("label_3")
        self.notes = QtWidgets.QTextEdit(ContactViewer)
        self.notes.setGeometry(QtCore.QRect(140, 290, 181, 81))
        self.notes.setReadOnly(True)
        self.notes.setObjectName("notes")
        self.email = QtWidgets.QLineEdit(ContactViewer)
        self.email.setGeometry(QtCore.QRect(140, 210, 181, 22))
        self.email.setText("")
        self.email.setReadOnly(True)
        self.email.setObjectName("email")
        self.back_button = QtWidgets.QPushButton(ContactViewer)
        self.back_button.setGeometry(QtCore.QRect(50, 10, 71, 32))
        self.back_button.setObjectName("back_button")
        self.label_6 = QtWidgets.QLabel(ContactViewer)
        self.label_6.setGeometry(QtCore.QRect(50, 290, 81, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(ContactViewer)
        self.label_7.setGeometry(QtCore.QRect(50, 370, 60, 16))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(ContactViewer)
        QtCore.QMetaObject.connectSlotsByName(ContactViewer)

    def retranslateUi(self, ContactViewer):
        _translate = QtCore.QCoreApplication.translate
        ContactViewer.setWindowTitle(_translate("ContactViewer", "Form"))
        self.label_1.setText(_translate("ContactViewer", "First Name:"))
        self.label_4.setText(_translate("ContactViewer", "E-mail:"))
        self.last_name.setPlaceholderText(_translate("ContactViewer", "Last Name"))
        self.first_name.setPlaceholderText(_translate("ContactViewer", "First Name"))
        self.label_2.setText(_translate("ContactViewer", "Last Name:"))
        self.telephone.setPlaceholderText(_translate("ContactViewer", "Telephone"))
        self.url.setPlaceholderText(_translate("ContactViewer", "www.example.com"))
        self.edit_button.setText(_translate("ContactViewer", "Edit"))
        self.label_5.setText(_translate("ContactViewer", "Url:"))
        self.label_3.setText(_translate("ContactViewer", "Telephone:"))
        self.notes.setPlaceholderText(_translate("ContactViewer", "Notes..."))
        self.email.setPlaceholderText(_translate("ContactViewer", "example@email.com"))
        self.back_button.setText(_translate("ContactViewer", "Back"))
        self.label_6.setText(_translate("ContactViewer", "Notes:"))
        self.label_7.setText(_translate("ContactViewer", "Tags:"))

