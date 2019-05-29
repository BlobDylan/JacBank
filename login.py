from PyQt5.QtWidgets import QDialog, QApplication,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from app import Ui_MainWindow
from signUp import Ui_Dialog5
from db_func import *

class Ui_Dialog(object):
    def openWindow(self):
        if self.lineEdit.text() is not '' and self.lineEdit_2.text() is not '':
            id = login(self.lineEdit.text(),self.lineEdit_2.text())
            print(id)
            if id is not None:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.window,id[0][0])
                MainWindow.hide()
                self.window.show()
            else:
                msg = QMessageBox()
                msg.setText("Wrong information")
                msg.setWindowTitle("JacBank")
                msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                msg.exec()
                print('no user and password found')
        else:
            if self.lineEdit.text() is '' and self.lineEdit_2.text() is not '':
                msg = QMessageBox()
                msg.setText("Username field is empty")
                msg.setWindowTitle("JacBank")
                msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                msg.exec()
            elif self.lineEdit_2.text() is '' and self.lineEdit.text() is not '':
                msg = QMessageBox()
                msg.setText("Password field is empty")
                msg.setWindowTitle("JacBank")
                msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                msg.exec()
            else:
                msg = QMessageBox()
                msg.setText("Password and Username fields are empty")
                msg.setWindowTitle("JacBank")
                msg.setWindowIcon(QtGui.QIcon('icon.jpg'))
                msg.exec()

    def opensignup(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog5()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Login")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        Dialog.setWindowIcon(QtGui.QIcon('icon.jpg'))

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 380, 90))
        self.textBrowser.setObjectName("textBrowser")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 120, 50, 15))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 60, 20))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 60, 15))
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 140, 290, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 200, 290, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(20, 250, 75, 23))
        self.pushButton2.setObjectName("pushButton2")

        self.pushButton.clicked.connect(self.openWindow)
        self.pushButton2.clicked.connect(self.opensignup)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Log-In"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:50px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:600; color:#aa0000;\">Jac</span><span style=\" font-size:48pt; font-weight:600; color:#a6a6a6;\">Bank</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "Log-In:"))
        self.label_2.setText(_translate("Dialog", "Username:"))
        self.label_3.setText(_translate("Dialog", "Password:"))
        self.pushButton.setText(_translate("Dialog", "Log-In"))
        self.pushButton2.setText(_translate("Dialog", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


