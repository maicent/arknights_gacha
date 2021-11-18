from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
from index import *
import function
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 127)
        MainWindow.setWindowIcon(QIcon('images/ico.jpg'))
        MainWindow.setStyleSheet("background-image:url(images/bg1.jpg)")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 20, 100, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 50, 100, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 50, 110, 20))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 48, 20))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 48, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(240, 20, 48, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(25, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(105, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 90, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralWidget)

        self.pushButton.clicked.connect(self.word_get)
        self.pushButton_3.clicked.connect(self.token_in)
        self.pushButton_2.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "方舟寻访统计工具"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入帐号"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "请输入token"))
        self.label.setText(_translate("MainWindow", "帐号"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.label_3.setText(_translate("MainWindow", "Token"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))
        self.pushButton_3.setText(_translate("MainWindow", "强制登录"))

    def token_in(self):
        login_token = self.lineEdit_3.text()
        ak = function.Arknights(1, 1)
        ak.gacha_list(login_token)
        ui_index.show()
        MainWindow.close()

    def word_get(self):
        login_user = self.lineEdit.text()
        login_password = self.lineEdit_2.text()
        if login_user is not None:
            ak = function.Arknights(login_user, login_password)
            if ak.login() == 0:
                ak.gacha_list(ak.get_token())
                ui_index.show()
                MainWindow.close()
            elif ak.login() == 1:
                QMessageBox.warning(self, "警告", "登录太频繁", QMessageBox.Yes)
                self.lineEdit.setFocus()
            else:
                QMessageBox.warning(self, "警告", "用户名或密码错误！", QMessageBox.Yes)
                self.lineEdit.setFocus()
        else:
            QMessageBox.warning(self, "警告", "请输入用户名密码！", QMessageBox.Yes)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui_index = index_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
