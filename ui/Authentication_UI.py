# ============================================================
# Authentication Page UI
# Defines the authentication page layout and widgets
# ============================================================

from Logic.Utils import HoverButton

from PySide6.QtCore import (QCoreApplication, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QIcon, QPixmap)
from PySide6.QtWidgets import (QFrame, QLabel, QLineEdit, QSizePolicy, QToolButton)

class AuthUI(object):
    def Auth_setup(self, Dialog):
        self.label_n = QLabel(self.page_2)
        self.label_n.setObjectName(u"label_n")
        self.label_n.setGeometry(QRect(0, -20, 991, 601))
        self.label_n.setPixmap(QPixmap(u"background.png"))
        self.frame_n = QFrame(self.page_2)
        self.frame_n.setObjectName(u"frame_n")
        self.frame_n.setGeometry(QRect(560, 50, 371, 461))
        self.frame_n.setStyleSheet(u"    background-color: rgba(255, 255, 255, 30);\n"
                                   "    border-radius: 25px;\n"
                                   "    border: 1px solid rgba(255, 255, 255, 140);")
        self.frame_n.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_n.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_n = QLineEdit(self.frame_n)
        self.lineEdit_n.setObjectName(u"lineEdit_n")
        self.lineEdit_n.setGeometry(QRect(40, 160, 291, 41))
        self.lineEdit_n.setStyleSheet(u"QLineEdit {\n"
                                      "    border-radius: 12px;\n"
                                      "    padding: 8px 12px;\n"
                                      "    background-color: rgba(255, 255, 255, 220);\n"
                                      "    border: none;\n"
                                      "    color: #003366;\n"
                                      "}\n"
                                      "")
        self.lineEdit_2_n = QLineEdit(self.frame_n)
        self.lineEdit_2_n.setObjectName(u"lineEdit_2_n")
        self.lineEdit_2_n.setGeometry(QRect(40, 250, 291, 41))
        self.lineEdit_2_n.setStyleSheet(u"QLineEdit {\n"
                                        "    border-radius: 12px;\n"
                                        "    padding: 8px 12px;\n"
                                        "    background-color: rgba(255, 255, 255, 220);\n"
                                        "    border: none;\n"
                                        "    color: #003366;\n"
                                        "}\n"
                                        "")
        self.lineEdit_2_n.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton_n = HoverButton(self.frame_n)
        self.pushButton_n.setObjectName(u"pushButton_n")
        self.pushButton_n.setGeometry(QRect(80, 340, 211, 51))
        self.pushButton_n.setStyleSheet(u"QPushButton {\n"
                                        "    background-color: rgb(0, 52, 101);\n"
                                        "    font: 700 10pt \"Segoe UI\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(0, 72, 141); \n"
                                        "}\n"
                                        "")
        self.toolButton_2 = QToolButton(self.frame_n)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(300, 260, 21, 22))
        self.toolButton_2.setStyleSheet(u"QToolButton {\n"
                                        "    background-color: transparent;\n"
                                        "    border: none;\n"
                                        "    padding: 0px;\n"
                                        "}\n"
                                        "\n"
                                        "QToolButton:hover {\n"
                                        "    background-color: rgba(0,0,0,0.1);\n"
                                        "    border-radius: 6px;\n"
                                        "}\n"
                                        "")
        icon10 = QIcon()
        icon10.addFile(u"icons/hide_pss.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_2.setIcon(icon10)
        self.toolButton_2.setAutoRaise(True)
        self.label_12 = QLabel(self.page_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(1630, 100, 491, 71))
        self.label_12.setStyleSheet(u"font: 900 28pt \"Segoe UI Black\";\n"
                                    "color: rgb(255, 255, 255);")
        self.frame_6 = QFrame(self.page_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(1050, 50, 371, 461))
        self.frame_6.setStyleSheet(u"    background-color: rgba(255, 255, 255, 30);\n"
                                   "    border-radius: 25px;\n"
                                   "    border: 1px solid rgba(255, 255, 255, 140);")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_5 = QLineEdit(self.frame_6)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(32, 160, 301, 41))
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
                                      "    border-radius: 12px;\n"
                                      "    padding: 8px 12px;\n"
                                      "    background-color: rgba(255, 255, 255, 220);\n"
                                      "    border: none;\n"
                                      "    color: #003366;\n"
                                      "}\n"
                                      "")
        self.lineEdit_6 = QLineEdit(self.frame_6)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(30, 250, 301, 41))
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
                                      "    border-radius: 12px;\n"
                                      "    padding: 8px 12px;\n"
                                      "    background-color: rgba(255, 255, 255, 220);\n"
                                      "    border: none;\n"
                                      "    color: #003366;\n"
                                      "}\n"
                                      "")
        self.lineEdit_6.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton_5 = HoverButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(80, 340, 211, 51))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
                                        "    background-color: rgb(0, 52, 101);\n"
                                        "    font: 700 10pt \"Segoe UI\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(0, 72, 141); \n"
                                        "}\n"
                                        "")
        self.toolButton = QToolButton(self.frame_6)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(300, 260, 21, 22))
        self.toolButton.setStyleSheet(u"QToolButton {\n"
                                      "    background-color: transparent;\n"
                                      "    border: none;\n"
                                      "    padding: 0px;\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:hover {\n"
                                      "    background-color: rgba(0,0,0,0.1);\n"
                                      "    border-radius: 6px;\n"
                                      "}\n"
                                      "")
        self.toolButton.setIcon(icon10)
        self.toolButton.setAutoRaise(True)
        self.label_6_n = QLabel(self.page_2)
        self.label_6_n.setObjectName(u"label_6_n")
        self.label_6_n.setGeometry(QRect(30, 180, 291, 71))
        self.label_6_n.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                     "font: 600 11pt \"Segoe UI Semibold\";")
        self.label_4_n = QLabel(self.page_2)
        self.label_4_n.setObjectName(u"label_4_n")
        self.label_4_n.setGeometry(QRect(600, 280, 51, 16))
        self.label_4_n.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(1180, 70, 111, 81))
        self.label_8.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
                                   "color: rgb(255,255,255); font-size:25pt;")
        self.label_5_n = QLabel(self.page_2)
        self.label_5_n.setObjectName(u"label_5_n")
        self.label_5_n.setGeometry(QRect(20, 100, 491, 71))
        self.label_5_n.setStyleSheet(u"font: 900 28pt \"Segoe UI Black\";\n"
                                     "color: rgb(255, 255, 255);")
        self.label_11 = QLabel(self.page_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(1080, 280, 49, 16))
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7_n = QLabel(self.page_2)
        self.label_7_n.setObjectName(u"label_7_n")
        self.label_7_n.setGeometry(QRect(660, 450, 191, 21))
        self.label_errn = QLabel(Dialog)
        self.label_errn.setObjectName(u"label")
        self.label_errn.setGeometry(QRect(570, 480, 370, 16))
        self.label_errn.setStyleSheet(u"QLabel {\n"
                                      "    color: rgb(211, 47, 47);  /* error red */\n"
                                      "    font: 600 10pt \"Segoe UI\";\n"
                                      "}\n"
                                      "")
        self.label_errn.hide()
        self.label_3_n = QLabel(self.page_2)
        self.label_3_n.setObjectName(u"label_3_n")
        self.label_3_n.setGeometry(QRect(600, 190, 61, 16))
        self.label_3_n.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(1080, 190, 81, 16))
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13 = QLabel(self.page_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(1640, 180, 291, 71))
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                    "font: 600 11pt \"Segoe UI Semibold\";")
        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(1140, 450, 191, 16))
        self.label_2_n = QLabel(self.page_2)
        self.label_2_n.setObjectName(u"label_2_n")
        self.label_2_n.setGeometry(QRect(630, 90, 250, 44))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.label_2_n.sizePolicy().hasHeightForWidth())
        self.label_2_n.setSizePolicy(sizePolicy1)
        self.label_2_n.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
                                     "color: rgb(255,255,255); font-size:25pt;")
        self.label_2_n.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

    def Auth_retranslate(self, Dialog):
        self.label_n.setText("")
        self.label_n.setText("")
        self.pushButton_n.setText(QCoreApplication.translate("Dialog", u"Sign up", None))
        self.toolButton_2.setText("")
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Welcome back !", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"LOG IN", None))
        self.toolButton.setText("")
        self.label_6_n.setText(QCoreApplication.translate("Dialog", u"Manage students and classes\n"
                                                                    "simply, efficiently, and securely.", None))
        self.label_4_n.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"LOG IN", None))
        self.label_5_n.setText(QCoreApplication.translate("Dialog", u"Welcome to ClassManager", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_7_n.setText(
            QCoreApplication.translate("Dialog", u"Already have an account? <a href=\"login\">Log in</a>\n"
                                                 "", None))
        self.label_3_n.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Manage students and classes\n"
                                                                   "simply, efficiently, and securely.", None))
        self.label_10.setText(
            QCoreApplication.translate("Dialog", u"Don't have an account? <a href=\"create\">Create one</a>\n"
                                                 "", None))
        self.label_2_n.setText(QCoreApplication.translate("Dialog", u"Create account", None))
