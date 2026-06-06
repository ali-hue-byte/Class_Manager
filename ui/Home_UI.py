# ============================================================
# Home Page UI
# Defines the home page layout and widgets
# ============================================================

from PySide6.QtCore import (QCoreApplication, QRect, QSize, Qt, )
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QFrame, QLabel, QPushButton, QSizePolicy, QToolButton)


class HomeUI(object):
    def Home_setup(self, Dialog):
        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(720, 260, 191, 171))
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 40px;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 30, 151, 21))
        self.label_5.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                   "font: 700 15pt \"Yu Gothic UI\";")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 90, 191, 41))
        self.label_6.setStyleSheet(u"color: rgba(45, 45, 45, 120);\n"
                                   "font: 700 26pt \"Tahoma\";")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, -12, 1001, 71))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                   "\n"
                                   "\n"
                                   "")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.settings_button = QPushButton(self.frame_2)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setGeometry(QRect(870, 30, 31, 26))
        self.settings_button.setStyleSheet(u"QPushButton:hover {\n"
                                           "background-color: rgba(0, 0, 0, 0.1);\n"
                                           "}")
        icon1 = QIcon()
        icon1.addFile(u"icons/home_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_button.setIcon(icon1)
        self.settings_button.setFlat(True)
        self.exit_button = QPushButton(self.frame_2)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(920, 30, 31, 26))
        self.exit_button.setStyleSheet(u"QPushButton:hover {\n"
                                       "background-color: rgba(0, 0, 0, 0.1);\n"
                                       "}")
        icon2 = QIcon()
        icon2.addFile(u"icons/exit_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exit_button.setIcon(icon2)
        self.exit_button.setFlat(True)
        self.info_button = QPushButton(self.frame_2)
        self.info_button.setObjectName(u"info_button")
        self.info_button.setGeometry(QRect(820, 30, 31, 26))
        self.info_button.setStyleSheet(u"QPushButton:hover {\n"
                                       "background-color: rgba(0, 0, 0, 0.1);\n"
                                       "}")
        icon3 = QIcon()
        icon3.addFile(u"icons/info_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.info_button.setIcon(icon3)
        self.info_button.setFlat(True)
        self.welcome_label = QLabel(self.page)
        self.welcome_label.setObjectName(u"welcome_label")
        self.welcome_label.setGeometry(QRect(190, 80, 801, 101))
        self.welcome_label.setStyleSheet(
            'font: 900 28pt "Arial";'
            'color: #000000;'
        )
        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(460, 260, 191, 171))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 40px;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 151, 21))
        self.label_3.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                   "font: 700 15pt \"Yu Gothic UI\";")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 90, 191, 41))
        self.label_4.setStyleSheet(u"color: rgba(45, 45, 45, 120);\n"
                                   "font: 700 26pt \"Tahoma\";")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(200, 260, 191, 171))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 40px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 151, 21))
        self.label.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                 "font: 700 15pt \"Yu Gothic UI\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 90, 191, 41))
        self.label_2.setStyleSheet(u"color: rgba(45, 45, 45, 120);\n"
                                   "font: 700 26pt \"Tahoma\";")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -1, 151, 571))
        self.frame.setStyleSheet(u"\n"
                                 "background-color: rgb(25, 86, 179);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Students_button = QPushButton(self.frame)
        self.Students_button.setObjectName(u"Students_button")
        self.Students_button.setGeometry(QRect(0, 200, 151, 61))
        self.Students_button.setStyleSheet(u"QPushButton{font: 900 9pt \"Segoe UI\";\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "text-align: left;\n"
                                           "background-color: rgb(25, 86, 179);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "background-color: rgba(0, 0, 0, 0.1);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "text-align: left;\n"
                                           "}")
        icon4 = QIcon()
        icon4.addFile(u"icons/Student's_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Students_button.setIcon(icon4)
        self.Students_button.setIconSize(QSize(60, 80))
        self.Students_button.setCheckable(False)
        self.Students_button.setChecked(False)
        self.Students_button.setAutoRepeat(False)
        self.Students_button.setAutoExclusive(False)
        self.Students_button.setFlat(True)
        self.Logo_button = QToolButton(self.frame)
        self.Logo_button.setObjectName(u"Logo_button")
        self.Logo_button.setGeometry(QRect(10, 0, 121, 61))
        self.Logo_button.setStyleSheet(u"QToolButton {\n"
                                       "  background-color: transparent;\n"
                                       "  border: none;\n"
                                       "  padding: 6px 8px;\n"
                                       "  color: #2B2B2B;\n"
                                       "}\n"
                                       "\n"
                                       "QToolButton:hover {\n"
                                       "  background-color: rgba(0, 0, 0, 0.04);\n"
                                       "  border-radius: 6px;\n"
                                       "}\n"
                                       "\n"
                                       "QToolButton:pressed {\n"
                                       "  background-color: rgba(0, 0, 0, 0.08);\n"
                                       "}\n"
                                       "")
        icon5 = QIcon()
        icon5.addFile(u"icons/icon_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Logo_button.setIcon(icon5)
        self.Logo_button.setIconSize(QSize(120, 120))
        self.Grades_button = QPushButton(self.frame)
        self.Grades_button.setObjectName(u"Grades_button")
        self.Grades_button.setGeometry(QRect(0, 260, 151, 61))
        self.Grades_button.setStyleSheet(u"QPushButton{font: 900 9pt \"Segoe UI\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "text-align: left;\n"
                                         "background-color: rgb(25, 86, 179);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background-color: rgba(0, 0, 0, 0.1);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "text-align: left;\n"
                                         "}")
        icon6 = QIcon()
        icon6.addFile(u"icons/grades_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Grades_button.setIcon(icon6)
        self.Grades_button.setIconSize(QSize(70, 50))
        self.Grades_button.setFlat(True)
        self.Attendance_button = QPushButton(self.frame)
        self.Attendance_button.setObjectName(u"Attendance_button")
        self.Attendance_button.setGeometry(QRect(0, 320, 151, 61))
        self.Attendance_button.setStyleSheet(u"QPushButton{font: 900 9pt \"Segoe UI\";\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "text-align: left;\n"
                                             "background-color: rgb(25, 86, 179);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "background-color: rgba(0, 0, 0, 0.1);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "text-align: left;\n"
                                             "}")
        icon7 = QIcon()
        icon7.addFile(u"icons/Attendance_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Attendance_button.setIcon(icon7)
        self.Attendance_button.setIconSize(QSize(50, 80))
        self.Attendance_button.setFlat(True)
        self.Statistics_button = QPushButton(self.frame)
        self.Statistics_button.setObjectName(u"Statistics_button")
        self.Statistics_button.setGeometry(QRect(0, 380, 151, 61))
        self.Statistics_button.setStyleSheet(u"QPushButton{font: 900 9pt \"Segoe UI\";\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "text-align: left;\n"
                                             "background-color: rgb(25, 86, 179);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "background-color: rgba(0, 0, 0, 0.1);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "text-align: left;\n"
                                             "}")
        icon8 = QIcon()
        icon8.addFile(u"icons/statistics_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Statistics_button.setIcon(icon8)
        self.Statistics_button.setIconSize(QSize(70, 50))
        self.Statistics_button.setFlat(True)
        self.Classes_button = QPushButton(self.frame)
        self.Classes_button.setObjectName(u"Classes_button")
        self.Classes_button.setGeometry(QRect(0, 140, 151, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Classes_button.sizePolicy().hasHeightForWidth())
        self.Classes_button.setSizePolicy(sizePolicy)
        self.Classes_button.setMouseTracking(True)
        self.Classes_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Classes_button.setAutoFillBackground(False)
        self.Classes_button.setStyleSheet(u"QPushButton{font: 900 9pt \"Segoe UI\";\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "text-align: left;\n"
                                          "background-color: rgb(25, 86, 179);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background-color: rgba(0, 0, 0, 0.1);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "text-align: left;\n"
                                          "}")
        icon9 = QIcon()
        icon9.addFile(u"icons/classes_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Classes_button.setIcon(icon9)
        self.Classes_button.setIconSize(QSize(60, 60))
        self.Classes_button.setFlat(True)

    def Home_retranslate(self, Dialog):
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Total Subjects :", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"", None))
        self.settings_button.setText("")
        self.exit_button.setText("")
        self.info_button.setText("")
        self.welcome_label.setText(QCoreApplication.translate("Dialog", u"", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Total Classes :", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Total Students :", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"", None))
        self.Students_button.setText(QCoreApplication.translate("Dialog", u"     Students", None))
        self.Logo_button.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.Grades_button.setText(QCoreApplication.translate("Dialog", u"        Grades", None))
        self.Attendance_button.setText(QCoreApplication.translate("Dialog", u"   Attendance", None))
        self.Statistics_button.setText(QCoreApplication.translate("Dialog", u"      Statistics", None))
        self.Classes_button.setText(QCoreApplication.translate("Dialog", u"        Classes", None))
