# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'restartDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(343, 128)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/window_icon/assets/window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.restartLater = QtWidgets.QPushButton(Dialog)
        self.restartLater.setGeometry(QtCore.QRect(225, 100, 111, 29))
        self.restartLater.setAutoDefault(False)
        self.restartLater.setObjectName("restartLater")
        self.restartNow = QtWidgets.QPushButton(Dialog)
        self.restartNow.setGeometry(QtCore.QRect(110, 100, 111, 29))
        self.restartNow.setObjectName("restartNow")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 341, 91))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Reboot Required"))
        self.restartLater.setText(_translate("Dialog", "Restart Later"))
        self.restartNow.setText(_translate("Dialog", "Restart Now"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>The changes you have applied require a system restart to take effect. Would you like to restart now or later?</p></body></html>"))

import resource_rc
