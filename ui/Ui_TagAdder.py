# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_qtdesigner/TagAdder.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TagAdder(object):
    def setupUi(self, TagAdder):
        TagAdder.setObjectName("TagAdder")
        TagAdder.resize(370, 540)
        TagAdder.setMinimumSize(QtCore.QSize(370, 540))
        TagAdder.setMaximumSize(QtCore.QSize(370, 540))
        self.label_7 = QtWidgets.QLabel(TagAdder)
        self.label_7.setGeometry(QtCore.QRect(50, 180, 60, 16))
        self.label_7.setObjectName("label_7")
        self.back_button = QtWidgets.QPushButton(TagAdder)
        self.back_button.setGeometry(QtCore.QRect(50, 20, 71, 32))
        self.back_button.setObjectName("back_button")
        self.tag_name = QtWidgets.QLineEdit(TagAdder)
        self.tag_name.setGeometry(QtCore.QRect(50, 110, 271, 22))
        self.tag_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tag_name.setText("")
        self.tag_name.setReadOnly(False)
        self.tag_name.setObjectName("tag_name")
        self.scrollArea = QtWidgets.QScrollArea(TagAdder)
        self.scrollArea.setGeometry(QtCore.QRect(40, 215, 291, 261))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setKerning(True)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 291, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.save_button = QtWidgets.QPushButton(TagAdder)
        self.save_button.setGeometry(QtCore.QRect(45, 140, 281, 32))
        self.save_button.setObjectName("save_button")
        self.newContact = QtWidgets.QLabel(TagAdder)
        self.newContact.setGeometry(QtCore.QRect(105, 55, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.newContact.setFont(font)
        self.newContact.setAlignment(QtCore.Qt.AlignCenter)
        self.newContact.setObjectName("newContact")
        self.back_button.raise_()
        self.tag_name.raise_()
        self.scrollArea.raise_()
        self.save_button.raise_()
        self.newContact.raise_()
        self.label_7.raise_()

        self.retranslateUi(TagAdder)
        QtCore.QMetaObject.connectSlotsByName(TagAdder)

    def retranslateUi(self, TagAdder):
        _translate = QtCore.QCoreApplication.translate
        TagAdder.setWindowTitle(_translate("TagAdder", "Form"))
        self.label_7.setText(_translate("TagAdder", "Tags:"))
        self.back_button.setText(_translate("TagAdder", "Back"))
        self.tag_name.setPlaceholderText(_translate("TagAdder", "Tag Name"))
        self.save_button.setText(_translate("TagAdder", "Save"))
        self.newContact.setText(_translate("TagAdder", "New Tag"))

