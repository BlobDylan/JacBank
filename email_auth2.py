from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from db_func import email_auth
from change_password import Ui_Dialog9
from hashlib import sha224


class Ui_Dialog8(object):
    def setupUi(self, Dialog, code_hash,dialog2,email):
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

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 15, 75, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda : self.check_hash(self.code_hash, self.lineEdit.text(),Dialog,dialog2,email))

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 15, 75, 25))
        self.pushButton_2.setObjectName("pushButton2")
        self.pushButton_2.clicked.connect(lambda : self.resend(email))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def resend(self,email):
        self.code_hash = email_auth(email)
        msg = QMessageBox()
        msg.setText("New code sent")
        msg.setWindowTitle("JacBank")
        msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
        msg.exec()

    def check_hash(self, code_hash, user_input,d,dialog2,email):
        if code_hash == sha224(user_input.encode('utf-8')).hexdigest():
            d.close()
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Dialog9()
            self.ui.setupUi(self.window, d,dialog2, email)
            self.window.show()
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
