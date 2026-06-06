# ============================================================
# Main Application UI
# Assembles all page UIs into a single dialog window
# ============================================================

from PySide6.QtCore import (QCoreApplication,
                            QMetaObject, QRect,
                            QSize)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QStackedWidget, QWidget
from ui.Home_UI import HomeUI
from ui.Students_UI import StudentUI
from ui.Class_UI import ClassUI
from ui.Grades_UI import GradesUI
from ui.Attendance_UI import AttendanceUI
from ui.Statistics_UI import StatisticsUI
from ui.Settings_UI import SettingsUI
from ui.Authentication_UI import AuthUI

class Ui_Dialog(HomeUI, StudentUI, ClassUI, GradesUI, AttendanceUI, StatisticsUI, SettingsUI, AuthUI):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        Dialog.resize(980, 560)
        ### ------ Stacked Widget (switches between authentication and main page) ------
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 990, 560))
        ### ------ Main container ------
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet("""
        #page {
            background-color: #f0f0f0;
        }
        """)

        ### ------ Home page ------
        self.Home_setup(Dialog)
        ### ------ Students page ------
        self.Students_setup(Dialog)
        ### ------ Class Page ------
        self.class_setup(Dialog)
        ### ------ Grades page ------
        self.grades_setup(Dialog)
        ### ------ Attendance page ------
        self.attendance_setup(Dialog)
        ### ------ Statistics page ------
        self.statistics_setup(Dialog)
        ### ------ Settings page ------
        self.Settings_setup(Dialog)
        ### ------------------------------
        self.stackedWidget.addWidget(self.page)

        ### ------ Authentication page ------
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.Auth_setup(Dialog)
        ### -------------------------------
        self.stackedWidget.addWidget(self.page_2)

        self.stackedWidget.setCurrentIndex(1) # sets current page to authentication page
        self.retranslateUi(Dialog)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Class Manager", None))
        icon = QIcon()
        icon.addFile(u"icons/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)

        self.Home_retranslate(Dialog)
        self.Students_retranslate(Dialog)
        self.Grades_retranslate(Dialog)
        self.Class_retranslate(Dialog)
        self.Attendance_retranslate(Dialog)
        self.Statistics_retranslate(Dialog)
        self.Settings_retranslate(Dialog)
        self.Auth_retranslate(Dialog)

