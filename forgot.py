from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from db_func import check_email,email_auth
from email_auth2 import Ui_Dialog8

class Ui_Dialog7(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 100)
        Dialog.setWindowIcon(QtGui.QIcon('icon.jpg'))
        Dialog.setMinimumSize(QtCore.QSize(350, 100))
        Dialog.setMaximumSize(QtCore.QSize(350, 100))

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 65, 50, 20))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10,10,330,40))
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(60, 67, 180, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 65, 75, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda : self.send(self.lineEdit.text(), Dialog))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def send(self,email,d):
        if check_email(email):
            x = email_auth(email)
            d.close()
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Dialog8()
            self.ui.setupUi(self.window,x,d,email)
            self.window.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Forgot My Password"))
        self.label.setText(_translate("Dialog", "Email:"))
        self.label_2.setText(_translate("Dialog", "We will now send you an email containing an authentication code \n"
                                                  "please enter your email address you used to sign up to JacBank"))
        self.pushButton.setText(_translate("Dialog", "Send"))

