
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from db_func import add_new_website, change_website_name, remove_website, get_website_names,change_website_xpath,get_xpath
from keyinput import Ui_Dialog4

class Ui_Dialog3(object):

    def setupUi(self, Dialog,id,webname,url,index):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 220)
        Dialog.setMinimumSize(QtCore.QSize(400, 150))
        Dialog.setMaximumSize(QtCore.QSize(400, 150))
        Dialog.setWindowIcon(QtGui.QIcon('icon.jpg'))

        website_names = get_website_names(id)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 20, 331, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(webname)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 51, 16))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 50, 311, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText(url)

        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(15, 110, 75, 25))
        self.pushButton_ok.setObjectName("pushButtonok")
        self.pushButton_ok.clicked.connect(lambda : self.ok(id,webname,self.lineEdit.text(),Dialog,self.lineEdit_3.text(),url))

        self.pushButton_delete = QtWidgets.QPushButton(Dialog)
        self.pushButton_delete.setGeometry(QtCore.QRect(225, 110, 75, 25))
        self.pushButton_delete.setObjectName("pushButtonok")
        self.pushButton_delete.clicked.connect(lambda : self.remove(id, webname, Dialog))

        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 250, 381, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.label_3.setObjectName("label_4")

        xpath = get_xpath(url)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 80, 331, 20))
        self.lineEdit_3.setObjectName("lineEdit_2")
        self.lineEdit_3.setStyleSheet("color: red;")
        if(xpath is not None):
            self.lineEdit_3.setText(xpath[0][0])
        else:
            self.lineEdit_3.setText("*Optional*")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 110, 75, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda : self.cancel(Dialog))

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 110, 75, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.open(Dialog,website_names,url,self.lineEdit_3.text(),index,id))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def cancel(self,d):
        d.close()

    def ok(self,id,webname,new_name,d,xpath,url):
        change_website_name(id,webname,new_name)
        change_website_xpath(id,url,xpath)
        d.close()

    def remove(self,id,webname,d):
        remove_website(id, webname)
        d.close()

    def open(self,d,website_names,url,xpath,index,id):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog4()
        self.ui.setupUi(self.window, id, index, website_names, url, xpath, "open")
        self.window.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit"))
        self.label.setText(_translate("Dialog", "Name:"))
        self.label_2.setText(_translate("Dialog", "LogIn Link:"))
        self.label_3.setText(_translate('Dialog', 'xpath:'))
        self.pushButton.setText(_translate("Dialog", "Cancel"))
        self.pushButton_2.setText(_translate("Dialog", "Open"))
        self.pushButton_ok.setText(_translate("Dialog", "Ok"))
        self.pushButton_delete.setText(_translate("Dialog", "Delete"))


