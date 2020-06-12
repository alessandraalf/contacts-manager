# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_qtdesigner/ContactsManager.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ContactsManager(object):
    def setupUi(self, ContactsManager):
        ContactsManager.setObjectName("ContactsManager")
        ContactsManager.resize(370, 540)
        ContactsManager.setMinimumSize(QtCore.QSize(370, 540))
        ContactsManager.setMaximumSize(QtCore.QSize(370, 540))
        self.centralwidget = QtWidgets.QWidget(ContactsManager)
        self.centralwidget.setObjectName("centralwidget")
        ContactsManager.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ContactsManager)
        self.statusbar.setObjectName("statusbar")
        ContactsManager.setStatusBar(self.statusbar)

        self.retranslateUi(ContactsManager)
        QtCore.QMetaObject.connectSlotsByName(ContactsManager)

    def retranslateUi(self, ContactsManager):
        _translate = QtCore.QCoreApplication.translate
        ContactsManager.setWindowTitle(_translate("ContactsManager", "Contacts Manager"))

