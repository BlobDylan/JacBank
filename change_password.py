from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from db_func import change_user_password
class Ui_Dialog9(object):
    def setupUi(self, Dialog, dialog2,dialog3,email):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 50)
        Dialog.setWindowIcon(QtGui.QIcon('icon.jpg'))
        Dialog.setMinimumSize(QtCore.QSize(350, 50))
        Dialog.setMaximumSize(QtCore.QSize(350, 50))

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 15, 90, 20))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 17, 160, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 15, 75, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda : self.change_password(self.lineEdit.text(), email,dialog2,dialog3,Dialog))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def change_password(self, newpass, email,dialog2,dialog3,d):
        change_user_password(newpass, email)
        msg = QMessageBox()
        msg.setText("Password Changed")
        msg.setWindowTitle("JacBank")
        msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
        msg.exec()
        d.close()
        dialog2.close()
        dialog3.close()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Password Change"))
        self.label.setText(_translate("Dialog", "New password:"))
        self.pushButton.setText(_translate("Dialog", "Ok"))

