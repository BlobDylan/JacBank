from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from db_func import email_auth, check_username,check_email
from email_auth import Ui_Dialog6

class Ui_Dialog5(object):
    def cancel(self,d):
        d.close()
    def signup(self,username, password, re,email,d):
        if password == re:
            if " " not in username and username is not '' and " " not in password and password is not '' and " " not in email and email is not '':
                r = check_username(username)
                if r == 'taken':
                    msg = QMessageBox()
                    msg.setText("Username taken")
                    msg.setWindowTitle("JacBank")
                    msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                    msg.exec()

                elif(check_email(email)):
                    msg = QMessageBox()
                    msg.setText("Email in use")
                    msg.setWindowTitle("JacBank")
                    msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                    msg.exec()
                else:
                    try:
                        x = email_auth(email)
                        self.window = QtWidgets.QDialog()
                        self.ui = Ui_Dialog6()
                        self.ui.setupUi(self.window, x, username, password,d,email)
                        self.window.show()

                    except:
                        msg = QMessageBox()
                        msg.setText("Failed to send email")
                        msg.setWindowTitle("JacBank")
                        msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                        msg.exec()

            elif username is '' and password is '':
                msg = QMessageBox()
                msg.setText("Username and Password fields are empty")
                msg.setWindowTitle("JacBank")
                msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                msg.exec()

            elif username is '' and password is not '':
                msg = QMessageBox()
                msg.setText("Username field is empty")
                msg.setWindowTitle("JacBank")
                msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                msg.exec()

            elif password is '' and username is not '':
                msg = QMessageBox()
                msg.setText("Password field is empty")
                msg.setWindowTitle("JacBank")
                msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                msg.exec()

            elif " " in username and " " not in password and password is not '':
                msg = QMessageBox()
                msg.setText("Username contains spaces")
                msg.setWindowTitle("JacBank")
                msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                msg.exec()

            elif " " in password and " " not in username and username is not '':
                msg = QMessageBox()
                msg.setText("Password contains spaces")
                msg.setWindowTitle("JacBank")
                msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                msg.exec()

            elif " " in password and " " in username:
                msg = QMessageBox()
                msg.setText("Username and Password contain spaces")
                msg.setWindowTitle("JacBank")
                msg.exec()

        else:
            msg = QMessageBox()
            msg.setText("Password fields don't match")
            msg.setWindowTitle("JacBank")
            msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
            msg.exec()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 300)
        Dialog.setMinimumSize(QtCore.QSize(332, 300))
        Dialog.setMaximumSize(QtCore.QSize(332, 300))
        Dialog.setWindowIcon(QtGui.QIcon('icon.jpg'))

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 311, 61))
        self.textBrowser.setObjectName("textBrowser")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 90, 61, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 61, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 101, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 101, 16))
        self.label_4.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 90, 241, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 130, 241, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 170, 201, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)

        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 210, 271, 20))
        self.lineEdit_4.setObjectName("lineEdit_3")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda : self.signup(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), Dialog))

        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(20, 260, 75, 23))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.clicked.connect(lambda : self.cancel(Dialog))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sign Up"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600; color:#aa0000;\">Sign Up</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "Username:"))
        self.label_2.setText(_translate("Dialog", "Password:"))
        self.label_3.setText(_translate("Dialog", "Re-Enter Password:"))
        self.label_4.setText(_translate("Dialog", "Email: "))
        self.pushButton.setText(_translate("Dialog", "Done"))
        self.pushButton2.setText(_translate("Dialog", "Cancel"))

