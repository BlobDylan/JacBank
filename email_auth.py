from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from db_func import newUser,email_auth
from hashlib import sha224


"""This is the file containing the UI needed to display the dialog where the user can 
enter the code he received in his email in order to sign up"""


class Ui_Dialog6(object):
    def setupUi(self, Dialog, code_hash, username, password,dialog2,email):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 50)
        Dialog.setWindowIcon(QtGui.QIcon('icon.jpg'))
        Dialog.setMinimumSize(QtCore.QSize(420, 50))
        Dialog.setMaximumSize(QtCore.QSize(420, 50))

        self.code_hash = code_hash
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 15, 50, 20))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(60, 17, 180, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 15, 75, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda : self.check_hash(self.code_hash, self.lineEdit.text(),username,password,Dialog,dialog2,email))

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 15, 75, 25))
        self.pushButton_2.setObjectName("pushButton2")
        self.pushButton_2.clicked.connect(lambda : self.resend(email))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def resend(self,email):
        """resend's the email"""
        self.code_hash = email_auth(email)
        msg = QMessageBox()
        msg.setText("New code sent")
        msg.setWindowTitle("JacBank")
        msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
        msg.exec()

    def check_hash(self, code_hash, user_input,username,password,d,dialog2,email):
        """checks if the code the user inputted was correct"""
        if code_hash == sha224(user_input.encode('utf-8')).hexdigest():
            newUser(username, password,email)
            msg = QMessageBox()
            msg.setText("Welcome!")
            msg.setWindowTitle("JacBank")
            msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
            msg.exec()
            d.close()
            dialog2.close()
        else:
            msg = QMessageBox()
            msg.setText("Wrong code")
            msg.setWindowTitle("JacBank")
            msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
            msg.exec()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Email Authentication"))
        self.label.setText(_translate("Dialog", "Code:"))
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.pushButton_2.setText(_translate("Dialog", "Resend"))
