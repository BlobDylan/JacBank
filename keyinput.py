from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from db_func import decode,get_website_password,get_hash_with_id
from handlePassword import copy_to_clipboard,try_auto_enter_password,auto_enter_password
from hashlib import sha224

class Ui_Dialog4(object):
    def setupUi(self, Dialog,id,index,website_names,url,xpath,mode):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 50)
        Dialog.setWindowIcon(QtGui.QIcon('icon.jpg'))
        Dialog.setMinimumSize(QtCore.QSize(350, 50))
        Dialog.setMaximumSize(QtCore.QSize(350, 50))
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
        self.pushButton.clicked.connect(lambda : self.handle(id,index,website_names,Dialog,url,xpath,mode))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def handle(self,id,index,t,d,url,xpath,mode):
        if (sha224(self.lineEdit.text().encode('utf-8')).hexdigest() == get_hash_with_id(id)):
            password = (decode(self.lineEdit.text(), str(get_website_password(id, str(t[index][0])))))
            if(mode == "copy"):
                self.copy(password,d)

            elif(mode == "open"):
                self.open(url, xpath, password)
        else:
            msg = QMessageBox()
            msg.setText("Wrong password")
            msg.setWindowTitle("JacBank")
            msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
            msg.exec()

    def copy(self,password,d):
        copy_to_clipboard(password)
        d.close()

    def open(self,url,xpath,password):
        if xpath is not None:
            if '.' not in xpath:
                x = auto_enter_password(url,password,xpath)
                if x == 1:
                    msg = QMessageBox()
                    msg.setText("Auto-Enter failed")
                    msg.setWindowTitle("JacBank")
                    msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                    msg.exec()
            else:
                x = try_auto_enter_password(url, password)
                if x == 1:
                    msg = QMessageBox()
                    msg.setText("Auto-Enter failed")
                    msg.setWindowTitle("JacBank")
                    msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                    msg.exec()
        else:
            x = try_auto_enter_password(url,password)
            if x == 1:
                msg = QMessageBox()
                msg.setText("Auto-Enter failed")
                msg.setWindowTitle("JacBank")
                msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                msg.exec()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Password Input"))
        self.label.setText(_translate("Dialog", "password:"))
        self.pushButton.setText(_translate("Dialog", "Ok"))

