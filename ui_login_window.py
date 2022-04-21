# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_windowRQkRjz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(279, 280)
        MainWindow.setMinimumSize(QSize(279, 280))
        MainWindow.setMaximumSize(QSize(279, 280))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Tw Cen MT")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_4.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_4, 0, Qt.AlignRight)


        self.gridLayout.addLayout(self.horizontalLayout_2, 10, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 9, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 8, 0, 1, 1, Qt.AlignHCenter)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.gridLayout.addWidget(self.checkBox, 6, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(200, 0))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_2.setMaxLength(32)
        self.lineEdit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_2.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_2, 4, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 0))
        self.lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit.setMaxLength(32)
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEdit, 5, 0, 1, 1, Qt.AlignHCenter)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 279, 21))
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.pushButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PyChatLink", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pas de compte PyChatLink ?", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<a href=\"javascript:void(0)\">Cr\u00e9ez-en un maitenant !</a>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"   Se connecter   ", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Rester connect\u00e9", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identifiant", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Connectez-vous", None))
    # retranslateUi

