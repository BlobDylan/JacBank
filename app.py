from PyQt5 import QtCore, QtGui, QtWidgets
from new import Ui_Dialog2
from edit import Ui_Dialog3
from keyinput import Ui_Dialog4
from db_func import *


class Ui_MainWindow(object):
    def refresh(self,id,main):
        main.close()
        if id is not None:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window,id)
            self.window.show()

    def web_checked(self,website_names,urls,id):
        for i in range(len(self.lst)):
            if self.lst[i].isChecked():
                self.openDialog2(id,website_names[i][0],urls[i][0],i)
                self.lst[i].setChecked(False)

    def copy_checked(self,website_names,id,lst2):
        for i in range(len(lst2)):
            if lst2[i].isChecked():
                index = i
                lst2[i].setChecked(False)

        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog4()
        self.ui.setupUi(self.window, id, index,website_names,None,None,"copy")
        self.window.show()
#
    def openDialog(self, id):
        if id is not None:
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Dialog2()
            self.ui.setupUi(self.window, id)
            self.window.show()

    def openDialog2(self, id,webname,url,i):
        if id is not None:
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Dialog3()
            self.ui.setupUi(self.window, id,webname,url,i)
            self.window.show()

    def setupUi(self, MainWindow, id):
        website_names = get_website_names(id)
        urls = get_website_urls(id)
        x = ''
        self.lst = []
        self.lst2 = []
        MainWindow.setObjectName("JacBank")
        MainWindow.resize(480, 640)
        MainWindow.setMinimumSize(QtCore.QSize(480, 640))
        MainWindow.setMaximumSize(QtCore.QSize(480, 640))
        MainWindow.setStyleSheet("QMainWindow {background: 'white';}");
        MainWindow.setWindowIcon(QtGui.QIcon('icon.jpg'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 30, 380, 90))
        self.textBrowser.setObjectName("textBrowser")

        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 190, 460, 400))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        if website_names is not None:
            for i in range(len(website_names)):
                btn = QtWidgets.QPushButton(self.formLayoutWidget)
                btn2 = QtWidgets.QPushButton(self.formLayoutWidget)

                btn.setObjectName("web" + str(i))
                btn2.setObjectName("cop" + str(i))

                btn.setCheckable(True)
                btn2.setCheckable(True)

                btn.clicked.connect(lambda : self.web_checked(website_names,urls,id))
                btn2.clicked.connect(lambda : self.copy_checked(website_names,id,self.lst2))

                self.formLayout.setWidget(i, QtWidgets.QFormLayout.LabelRole, btn2)
                self.formLayout.setWidget(i, QtWidgets.QFormLayout.FieldRole, btn)

                self.lst2.append(btn2)
                self.lst.append(btn)


        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 460, 30))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.openDialog(id))
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(lambda : self.refresh(id,MainWindow))
        self.horizontalLayout.addWidget(self.pushButton2)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 170, 460, 15))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 20))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow, website_names)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, t):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JaqueBank"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:50px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:600; color:#bf0e01;\">Jac</span><span style=\" font-size:48pt; font-weight:600; color:#a6a6a6;\">Bank</span></p></body></html>"))

        if t is not None:
            for i in range(len(t)):
                self.lst[i].setText(_translate("MainWindow", str(t[i][0])))
                self.lst2[i].setText(_translate("MainWindow", "Copy"))

        self.pushButton2.setText(_translate("MainWindow", "Refresh"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
