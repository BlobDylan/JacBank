from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from db_func import add_new_website,get_hash_with_id
from hashlib import sha224

class Ui_Dialog2(object):

    def setupUi(self, Dialog,id):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 220)
        Dialog.setMinimumSize(QtCore.QSize(400, 220))
        Dialog.setMaximumSize(QtCore.QSize(400, 220))
        Dialog.setWindowIcon(QtGui.QIcon('icon.jpg'))

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(45, 20, 340, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 50, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 50, 16))
        self.label_3.setObjectName("label_3")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(65, 50, 320, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(65, 80, 320, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushButtonok = QtWidgets.QPushButton(Dialog)
        self.pushButtonok.setGeometry(QtCore.QRect(15, 180, 75, 25))
        self.pushButtonok.setObjectName("pushButtonok")
        self.pushButtonok.clicked.connect(lambda: self.ok(id,Dialog))

        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 100, 381, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 250, 381, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 71, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 115, 200, 16))
        self.label_5.setObjectName("label_5")

        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(30, 140, 81, 17))
        self.checkBox.setObjectName("checkBox")


        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(110, 140, 110, 17))
        self.checkBox_2.setObjectName("checkBox_2")


        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(230, 140, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(300, 140, 81, 17))
        self.checkBox_4.setObjectName("checkBox_4")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 180, 75, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda : self.cancel(Dialog))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def cancel(self,d):
        d.close()
    def ok(self,id,d):
        if(sha224(self.lineEdit_3.text().encode('utf-8')).hexdigest() == get_hash_with_id(id)):
            self.sl = self.checkBox.isChecked()
            self.cl = self.checkBox_2.isChecked()
            self.n = self.checkBox_3.isChecked()
            self.ch = self.checkBox_4.isChecked()
            if self.lineEdit.text() is not '' and self.lineEdit_3.text() is not '' and " " not in self.lineEdit_3.text():
                if(self.sl or self.cl or self.n or self.ch):
                    print(id)
                    print(self.lineEdit.text())
                    print(self.sl)
                    print(self.cl)
                    print(self.n)
                    print(self.ch)
                    add_new_website(id, self.lineEdit.text(), self.sl, self.cl, self.n, self.ch, self.lineEdit_3.text(), self.lineEdit_2.text())
                    d.close()
                else:
                    msg = QMessageBox()
                    msg.setText("No checkboxes checked")
                    msg.setWindowTitle("JacBank")
                    msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                    msg.exec()
            elif self.lineEdit.text() is '' and self.lineEdit_3.text() is '':
                msg = QMessageBox()
                msg.setText("Name and Key fields are empty")
                msg.setWindowTitle("JacBank")
                msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                msg.exec()

            elif self.lineEdit.text() is '' and self.lineEdit_3.text() is not '':
                msg = QMessageBox()
                msg.setText("Name field is empty")
                msg.setWindowTitle("JacBank")
                msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                msg.exec()

            elif self.lineEdit_3.text() is '' and self.lineEdit.text() is not '':
                msg = QMessageBox()
                msg.setText("Key field is empty")
                msg.setWindowTitle("JacBank")
                msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                msg.exec()
            else:
                msg = QMessageBox()
                msg.setText("Key contains spaces")
                msg.setWindowTitle("JacBank")
                msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                msg.exec()
        else:
            msg = QMessageBox()
            msg.setText("Wrong password")
            msg.setWindowTitle("JacBank")
            msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
            msg.exec()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Password"))
        self.label.setText(_translate("Dialog", "Name:"))
        self.label_2.setText(_translate("Dialog", "LogIn Link:"))
        self.label_3.setText(_translate("Dialog", "Password:"))
        self.label_5.setText(_translate("Dialog", "Generation Settings:"))
        self.checkBox.setText(_translate("Dialog", "small letters"))
        self.checkBox_2.setText(_translate("Dialog", "CAPITAL LETTERS"))
        self.checkBox_3.setText(_translate("Dialog", "12345"))
        self.checkBox_4.setText(_translate("Dialog", "!@#$%^&"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButtonok.setText(_translate("Dialog", "Ok"))


