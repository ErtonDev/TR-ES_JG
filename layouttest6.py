# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boxpile.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setStyleSheet("color: rgb(246, 246, 246);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.mainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName("mainLayout")
        self.sideBarLayout = QtWidgets.QVBoxLayout()
        self.sideBarLayout.setSpacing(0)
        self.sideBarLayout.setObjectName("sideBarLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(254, 140, 10);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"padding: 50px;\n"
"padding-left: 40px;\n"
"text-align: left;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/logoTR_orange.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_2.setObjectName("pushButton_2")
        self.sideBarLayout.addWidget(self.pushButton_2)
        self.btnCalendario = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnCalendario.setFont(font)
        self.btnCalendario.setStyleSheet("QPushButton {\n"
"    padding: 20px;\n"
"    padding-left: 40px;\n"
"    text-align: left;\n"
"    color: rgb(8, 21, 63);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(246, 246, 246);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.btnCalendario.setObjectName("btnCalendario")
        self.sideBarLayout.addWidget(self.btnCalendario)
        self.btnSeguimiento = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnSeguimiento.setFont(font)
        self.btnSeguimiento.setStyleSheet("QPushButton {\n"
"    padding: 20px;\n"
"    padding-left: 40px;\n"
"    text-align: left;\n"
"    color: rgb(8, 21, 63);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(246, 246, 246)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"")
        self.btnSeguimiento.setObjectName("btnSeguimiento")
        self.sideBarLayout.addWidget(self.btnSeguimiento)
        self.btnBusqueda = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnBusqueda.setFont(font)
        self.btnBusqueda.setStyleSheet("QPushButton {\n"
"    padding: 20px;\n"
"    padding-left: 40px;\n"
"    text-align: left;\n"
"    color: rgb(8, 21, 63);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(246, 246, 246)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"")
        self.btnBusqueda.setObjectName("btnBusqueda")
        self.sideBarLayout.addWidget(self.btnBusqueda)
        self.sideBarFill = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.sideBarFill.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.sideBarFill.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sideBarFill.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sideBarFill.setObjectName("sideBarFill")
        self.sideBarLayout.addWidget(self.sideBarFill)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(8, 21, 63);\n"
"padding: 20px;\n"
"padding-left: 40px;\n"
"text-align: left")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/logoTR_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(45, 45))
        self.pushButton.setObjectName("pushButton")
        self.sideBarLayout.addWidget(self.pushButton)
        self.mainLayout.addLayout(self.sideBarLayout)
        self.bodyLayout = QtWidgets.QGridLayout()
        self.bodyLayout.setObjectName("bodyLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.horizontalLayoutWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setObjectName("loginPage")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.loginPage)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 801, 701))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.loginGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.loginGrid.setContentsMargins(0, 0, 0, 0)
        self.loginGrid.setSpacing(0)
        self.loginGrid.setObjectName("loginGrid")
        self.loginGrey6 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.loginGrey6.setStyleSheet("border-radius: 0px;")
        self.loginGrey6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginGrey6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginGrey6.setObjectName("loginGrey6")
        self.loginGrid.addWidget(self.loginGrey6, 2, 0, 1, 1)
        self.loginGrey4 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.loginGrey4.setStyleSheet("border-radius: 0px;")
        self.loginGrey4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginGrey4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginGrey4.setObjectName("loginGrey4")
        self.loginGrid.addWidget(self.loginGrey4, 1, 0, 1, 1)
        self.loginWidget = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.loginWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.loginWidget.setObjectName("loginWidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.loginWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 381, 471))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.loginVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.loginVLayout.setContentsMargins(0, 0, 0, 0)
        self.loginVLayout.setSpacing(0)
        self.loginVLayout.setObjectName("loginVLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.loginVLayout.addItem(spacerItem)
        self.loginLogo = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.loginLogo.setStyleSheet("padding-left: 80px;\n"
"padding-right: 80px;\n"
"")
        self.loginLogo.setText("")
        self.loginLogo.setIcon(icon)
        self.loginLogo.setIconSize(QtCore.QSize(140, 140))
        self.loginLogo.setObjectName("loginLogo")
        self.loginVLayout.addWidget(self.loginLogo)
        self.loginTitle = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(32)
        self.loginTitle.setFont(font)
        self.loginTitle.setStyleSheet("color: rgb(254, 140, 10);\n"
"padding-left: 40px;\n"
"padding-right: 40px;")
        self.loginTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.loginTitle.setObjectName("loginTitle")
        self.loginVLayout.addWidget(self.loginTitle)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.loginVLayout.addItem(spacerItem1)
        self.loginFormLayout = QtWidgets.QGridLayout()
        self.loginFormLayout.setObjectName("loginFormLayout")
        self.loginPassLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.loginPassLineEdit.setStyleSheet("QLineEdit {\n"
"    color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(207, 207, 207);\n"
"    background-color: rgb(246, 246, 246);\n"
"    margin: 5px;\n"
"    margin-right: 20px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(254, 140, 10);\n"
"    border-width: 2px;\n"
"}")
        self.loginPassLineEdit.setInputMask("")
        self.loginPassLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginPassLineEdit.setObjectName("loginPassLineEdit")
        self.loginFormLayout.addWidget(self.loginPassLineEdit, 1, 2, 1, 1)
        self.loginUserPic = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.loginUserPic.setStyleSheet("padding: 5px;\n"
"margin-left: 15px;")
        self.loginUserPic.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginUserPic.setIcon(icon2)
        self.loginUserPic.setIconSize(QtCore.QSize(25, 25))
        self.loginUserPic.setObjectName("loginUserPic")
        self.loginFormLayout.addWidget(self.loginUserPic, 0, 0, 1, 1)
        self.loginUserLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.loginUserLineEdit.setStyleSheet("QLineEdit {\n"
"    color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(207, 207, 207);\n"
"    background-color: rgb(246, 246, 246);\n"
"    margin: 5px;\n"
"    margin-right: 20px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(254, 140, 10);\n"
"    border-width: 2px;\n"
"}")
        self.loginUserLineEdit.setObjectName("loginUserLineEdit")
        self.loginFormLayout.addWidget(self.loginUserLineEdit, 0, 2, 1, 1)
        self.loginPassPic = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.loginPassPic.setStyleSheet("padding: 5px;\n"
"margin-left: 15px;")
        self.loginPassPic.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginPassPic.setIcon(icon3)
        self.loginPassPic.setIconSize(QtCore.QSize(25, 25))
        self.loginPassPic.setObjectName("loginPassPic")
        self.loginFormLayout.addWidget(self.loginPassPic, 1, 0, 1, 1)
        self.loginVLayout.addLayout(self.loginFormLayout)
        self.loginButtonsHLayout = QtWidgets.QHBoxLayout()
        self.loginButtonsHLayout.setSpacing(0)
        self.loginButtonsHLayout.setObjectName("loginButtonsHLayout")
        self.registerBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.registerBtn.setStyleSheet("QPushButton {\n"
"    border-width: 0px;\n"
"    color: rgb(8, 21, 63);\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding: 15px;\n"
"    margin: 20px;\n"
"    margin-right: 5px;\n"
"    border-radius: 5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207, 207, 207);\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(246, 246, 246);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.registerBtn.setObjectName("registerBtn")
        self.loginButtonsHLayout.addWidget(self.registerBtn)
        self.loginBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.loginBtn.setStyleSheet("QPushButton {\n"
"    border-width: 0px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(28, 85, 255, 255), stop:1 rgba(94, 134, 255, 255));\n"
"    padding: 15px;\n"
"    margin: 20px;\n"
"    margin-left: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(70, 117, 255, 255), stop:1 rgba(111, 147, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.99005, y1:0, x2:1, y2:1, stop:0 rgba(70, 117, 255, 255), stop:1 rgba(111, 147, 255, 255));\n"
"}")
        self.loginBtn.setObjectName("loginBtn")
        self.loginButtonsHLayout.addWidget(self.loginBtn)
        self.loginVLayout.addLayout(self.loginButtonsHLayout)
        self.loginGrid.addWidget(self.loginWidget, 1, 1, 1, 1)
        self.loginGrey8 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.loginGrey8.setStyleSheet("border-radius: 0px;")
        self.loginGrey8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginGrey8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginGrey8.setObjectName("loginGrey8")
        self.loginGrid.addWidget(self.loginGrey8, 2, 2, 1, 1)
        self.loginGrey7 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.loginGrey7.setStyleSheet("border-radius: 0px;")
        self.loginGrey7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginGrey7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginGrey7.setObjectName("loginGrey7")
        self.loginGrid.addWidget(self.loginGrey7, 2, 1, 1, 1)
        self.loginGrey5 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.loginGrey5.setStyleSheet("border-radius: 0px;")
        self.loginGrey5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginGrey5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginGrey5.setObjectName("loginGrey5")
        self.loginGrid.addWidget(self.loginGrey5, 1, 2, 1, 1)
        self.loginGrey3 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.loginGrey3.setStyleSheet("border-radius: 0px;")
        self.loginGrey3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginGrey3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginGrey3.setObjectName("loginGrey3")
        self.loginGrid.addWidget(self.loginGrey3, 0, 2, 1, 1)
        self.loginGrey2 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.loginGrey2.setStyleSheet("border-radius: 0px;")
        self.loginGrey2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginGrey2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginGrey2.setObjectName("loginGrey2")
        self.loginGrid.addWidget(self.loginGrey2, 0, 1, 1, 1)
        self.loginGrey1 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.loginGrey1.setStyleSheet("border-radius: 0px;")
        self.loginGrey1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginGrey1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginGrey1.setObjectName("loginGrey1")
        self.loginGrid.addWidget(self.loginGrey1, 0, 0, 1, 1)
        self.loginGrid.setColumnStretch(0, 100)
        self.loginGrid.setColumnStretch(1, 4)
        self.loginGrid.setColumnStretch(2, 100)
        self.loginGrid.setRowStretch(0, 1)
        self.loginGrid.setRowStretch(1, 5)
        self.loginGrid.setRowStretch(2, 1)
        self.stackedWidget.addWidget(self.loginPage)
        self.calendarioPage = QtWidgets.QWidget()
        self.calendarioPage.setObjectName("calendarioPage")
        self.stackedWidget.addWidget(self.calendarioPage)
        self.bodyLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.mainLayout.addLayout(self.bodyLayout)
        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 100)
        MainWindow.setCentralWidget(self.centralwidget)

        # General scaling
        mainLayoutWidget = QWidget()
        mainLayoutWidget.setLayout(self.mainLayout)
        MainWindow.setCentralWidget(mainLayoutWidget)

        # Body scaling
        self.loginPage.setLayout(self.loginGrid)

        # Login scaling
        self.loginWidget.setLayout(self.loginVLayout)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", " BoxPile"))
        self.btnCalendario.setText(_translate("MainWindow", "Calendario"))
        self.btnSeguimiento.setText(_translate("MainWindow", "Seguimiento"))
        self.btnBusqueda.setText(_translate("MainWindow", "Búsqueda"))
        self.pushButton.setText(_translate("MainWindow", "  @username\n"
"  0 Amigos"))
        self.loginTitle.setText(_translate("MainWindow", "BoxPile"))
        self.loginPassLineEdit.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.loginUserLineEdit.setPlaceholderText(_translate("MainWindow", "Nombre de usuario"))
        self.registerBtn.setText(_translate("MainWindow", "Crear cuenta"))
        self.loginBtn.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
