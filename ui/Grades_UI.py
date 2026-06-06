from Logic.Utils import HoverButton

from PySide6.QtCore import (QCoreApplication, QRect, Qt)
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (QLabel,
                               QLineEdit, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView,
                               QAbstractItemView)

class GradesUI(object):
    def grades_setup(self, Dialog):
        self.ClassComboBox3 = QComboBox(self.page)
        self.ClassComboBox3.setObjectName(u"ClassComboBox3")
        self.ClassComboBox3.setGeometry(QRect(740, 80, 221, 41))
        self.ClassComboBox3.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
                                          "border-radius : 15px ;\n"
                                          "padding : 6px 8px;  \n"
                                          "background-color: rgb(255,255,255)\n"
                                          "}\n"
                                          "QComboBox:drop-down { width: 0;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:hover{border: 2px solid black;\n"
                                          "padding : 5px 7px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:focus {\n"
                                          "  border : 2px solid #0078d7;\n"
                                          "}\n"
                                          "\n"
                                          "")

        self.class3 = QLabel(self.page)
        self.class3.setObjectName(u"class3")
        self.class3.setGeometry(QRect(680, 90, 41, 16))
        self.class3.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")

        self.tableWidget_grades = QTableWidget(self.page)  # grades table
        self.tableWidget_grades.setColumnCount(2)
        __qtablewidgetitemg = QTableWidgetItem()
        self.tableWidget_grades.setHorizontalHeaderItem(0, __qtablewidgetitemg)
        __qtablewidgetitem1g = QTableWidgetItem()
        self.tableWidget_grades.setHorizontalHeaderItem(1, __qtablewidgetitem1g)

        self.tableWidget_grades.setObjectName(u"tableWidget")
        self.tableWidget_grades.setGeometry(QRect(160, 130, 820, 340))
        self.tableWidget_grades.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.tableWidget_grades.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_grades.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_grades.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_grades.setShowGrid(True)
        self.tableWidget_grades.setStyleSheet(u"QHeaderView::section {\n"
                                              "background-color: rgb(25,86,179);\n"
                                              "color: white;\n"
                                              "font: 600 10pt \"Inter\";"
                                              "padding: 6px\n"
                                              "}\n"
                                              "QHeaderView::section:hover {\n"
                                              "background-color: rgb(20,70,150);\n"
                                              "padding: 6px\n"
                                              "}\n"
                                              "QHeaderView::section:pressed {\n"
                                              "background-color: rgb(15,55,120);\n"
                                              "padding: 6px\n"
                                              "}\n"
                                              "QTableWidget {"
                                              "border: none;\n}"
                                              "QTableWidget QLineEdit {\n"
                                              "background-color: rgb(255,255,255);"
                                              "border-bottom: 4px;"
                                              "}\n"
                                              "QScrollBar::horizontal {\n"
                                              "background-color: rgb(224,224,224);\n"
                                              "border: none;\n"
                                              "height: 15px;\n"
                                              "border-radius: 5px;\n"
                                              "}"
                                              "QScrollBar::handle:horizontal {\n"
                                              "background: rgb(25,86,179);\n"
                                              "min-width: 15px;\n"
                                              "border-radius: 6px;\n"
                                              "height: 15px;\n"
                                              "}\n"
                                              "QScrollBar::handle:horizontal:hover {\n"
                                              "background: rgb(20,70,150);\n"
                                              "height: 20px;\n"
                                              "}\n"
                                              "QScrollBar::add-line:horizontal,\n"
                                              "QScrollBar::sub-line:horizontal {\n"
                                              "border: none;\n"
                                              " background: none;\n"
                                              "width: 0px;\n"
                                              "}\n"
                                              "QScrollBar::add-page:horizontal,\n"
                                              "QScrollBar::sub-page:horizontal {\n"
                                              "background: none;\n"
                                              "}\n"
                                              "QScrollBar::vertical {\n"
                                              "background-color: rgb(224,224,224);\n"
                                              "border: none;\n"
                                              "width: 12px;\n"
                                              "border-radius: 5px;\n"
                                              "}"
                                              "QScrollBar::handle:vertical {\n"
                                              "background: rgb(25,86,179);\n"
                                              "min-width: 20px;\n"
                                              "border-radius: 6px;\n"
                                              "}\n"
                                              "QScrollBar::handle:vertical:hover {\n"
                                              "background: rgb(20,70,150);\n"
                                              "}\n"
                                              "QScrollBar::add-line:vertical,\n"
                                              "QScrollBar::sub-line:vertical {\n"
                                              "border: none;\n"
                                              "background: none;\n"
                                              "width: 0px;\n"
                                              "}\n"
                                              "QScrollBar::add-page:vertical,\n"
                                              "QScrollBar::sub-page:vertical {\n"
                                              "background: none;\n"
                                              "}\n"
                                              )

        self.tableWidget_grades.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_grades.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_grades.setEditTriggers(QTableWidget.NoEditTriggers)
        header = self.tableWidget_grades.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        vheader = self.tableWidget_grades.verticalHeader()
        vheader.setSectionResizeMode(QHeaderView.Fixed)

        self.Subject_top_btn = QPushButton(self.frame_2)
        self.Subject_top_btn.setObjectName(u"Add_top_btn")
        self.Subject_top_btn.setGeometry(QRect(480, 40, 81, 31))
        self.Subject_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                           "color :rgb(24, 182, 255);\n"
                                           "border: none;\n"
                                           "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                           "}\n"
                                           "")
        self.Subject_top_btn.setFlat(True)
        self.grades_top_btn = QPushButton(self.frame_2)
        self.grades_top_btn.setObjectName(u"View_top_btn")
        self.grades_top_btn.setGeometry(QRect(570, 40, 81, 31))
        self.grades_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                          "font: 700 9pt \"Yu Gothic UI\";")
        self.grades_top_btn.setFlat(True)

        self.tableWidget_subjects = QTableWidget(self.page)  # subjects table

        if (self.tableWidget_subjects.columnCount() < 3):
            self.tableWidget_subjects.setColumnCount(3)
        __qtablewidgetitems = QTableWidgetItem()
        self.tableWidget_subjects.setHorizontalHeaderItem(0, __qtablewidgetitems)
        __qtablewidgetitem1s = QTableWidgetItem()
        self.tableWidget_subjects.setHorizontalHeaderItem(1, __qtablewidgetitem1s)
        __qtablewidgetitem2s = QTableWidgetItem()
        self.tableWidget_subjects.setHorizontalHeaderItem(2, __qtablewidgetitem2s)
        __qtablewidgetitem3s = QTableWidgetItem()

        self.tableWidget_subjects.setHorizontalHeaderItem(3, __qtablewidgetitem3s)
        self.tableWidget_subjects.setObjectName(u"tableWidget_class")
        self.tableWidget_subjects.setGeometry(QRect(270, 220, 610, 270))
        self.tableWidget_subjects.horizontalHeader().setDefaultSectionSize(190)
        self.tableWidget_subjects.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_subjects.verticalHeader().setStretchLastSection(False)
        self.tableWidget_subjects.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_subjects.setShowGrid(True)
        self.tableWidget_subjects.setStyleSheet(u"QHeaderView::section {\n"
                                                "background-color: rgb(25,86,179);\n"
                                                "color: white;\n"
                                                "font: 600 10pt \"Inter\";"
                                                "padding: 6px\n"
                                                "}\n"
                                                "QHeaderView::section:hover {\n"
                                                "background-color: rgb(20,70,150);\n"
                                                "padding: 6px\n"
                                                "}\n"
                                                "QHeaderView::section:pressed {\n"
                                                "background-color: rgb(15,55,120);\n"
                                                "padding: 6px\n"
                                                "}\n"
                                                "QTableWidget {border: none}\n"
                                                "QTableWidget QLineEdit {\n"
                                                "background-color: rgb(255,255,255);"
                                                "}\n"
                                                "QScrollBar::vertical {\n"
                                                "background-color: rgb(224,224,224);\n"
                                                "border: none;\n"
                                                "width: 12px;\n"
                                                "border-radius: 5px;\n"
                                                "}"
                                                "QScrollBar::handle:vertical {\n"
                                                "background: rgb(25,86,179);\n"
                                                "min-width: 20px;\n"
                                                "border-radius: 6px;\n"
                                                "}\n"
                                                "QScrollBar::handle:vertical:hover {\n"
                                                "background: rgb(20,70,150);\n"
                                                "}\n"
                                                "QScrollBar::add-line:vertical,\n"
                                                "QScrollBar::sub-line:vertical {\n"
                                                "border: none;\n"
                                                "background: none;\n"
                                                "width: 0px;\n"
                                                "}\n"
                                                "QScrollBar::add-page:vertical,\n"
                                                "QScrollBar::sub-page:vertical {\n"
                                                "background: none;\n"
                                                "}\n"
                                                )
        self.tableWidget_subjects.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_subjects.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_subjects.setEditTriggers(QTableWidget.NoEditTriggers)
        header = self.tableWidget_subjects.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        vheader = self.tableWidget_subjects.verticalHeader()
        vheader.setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget_subjects.verticalHeader().setHighlightSections(False)
        self.tableWidget_subjects.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.add_button_subject = HoverButton(self.page)
        self.add_button_subject.setObjectName(u"add_button_class")
        self.add_button_subject.setGeometry(QRect(470, 160, 101, 31))
        self.add_button_subject.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                              "color : rgb(255,255,255);\n"
                                              "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                              "border-radius: 15px}\n"
                                              "\n"
                                              "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                              "color: rgb(255,255,255)\n"
                                              "}")
        self.cancel_button_subject = HoverButton(self.page)
        self.cancel_button_subject.setObjectName(u"cancel_button_class")
        self.cancel_button_subject.setGeometry(QRect(580, 160, 101, 31))
        self.cancel_button_subject.setStyleSheet(u"QPushButton {background-color: rgb(209, 213, 219);\n"
                                                 "color: rgb(55, 65, 81);\n"
                                                 "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                                 "border-radius: 15px\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {background-color: rgb(156,163,175)}")
        self.subjectline = QLineEdit(self.page)
        self.subjectline.setObjectName(u"Classnameline")
        self.subjectline.setGeometry(QRect(290, 90, 221, 41))
        self.subjectline.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
                                       "border-radius : 15px ;\n"
                                       "padding : 6px 8px;\n"
                                       "background-color: rgb(255,255,255)\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:hover{border: 2px solid black;\n"
                                       "padding : 5px 7px;\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:focus {\n"
                                       "  border : 2px solid #0078d7;\n"
                                       "}\n"
                                       "\n"
                                       "")
        self.requirederrsubject = QLabel(self.page)
        self.requirederrsubject.setObjectName(u"requirederrclass")
        self.requirederrsubject.setGeometry(QRect(290, 135, 200, 16))
        self.requirederrsubject.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.subject_name = QLabel(self.page)
        self.subject_name.setObjectName(u"classname")
        self.subject_name.setGeometry(QRect(170, 100, 101, 16))
        self.subject_name.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                        "font: 600 12pt \"Segoe UI\";")
        self.coeff = QLabel(self.page)
        self.coeff.setObjectName(u"maxstudents")
        self.coeff.setGeometry(QRect(590, 100, 141, 16))
        self.coeff.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                 "font: 600 12pt \"Segoe UI\";")
        self.coeffline = QLineEdit(self.page)
        self.coeffline.setObjectName(u"maxstudentsline")
        self.coeffline.setGeometry(QRect(730, 90, 221, 41))
        self.coeffline.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
                                     "border-radius : 15px ;\n"
                                     "padding : 6px 8px;\n"
                                     "background-color: rgb(255,255,255)\n"
                                     "}\n"
                                     "\n"
                                     "QLineEdit:hover{border: 2px solid black;\n"
                                     "padding : 5px 7px;\n"
                                     "}\n"
                                     "\n"
                                     "QLineEdit:focus {\n"
                                     "  border : 2px solid #0078d7;\n"
                                     "}\n"
                                     "\n"
                                     "")
        self.requirederrcoeff = QLabel(self.page)
        self.requirederrcoeff.setObjectName(u"requirederrmax")
        self.requirederrcoeff.setGeometry(QRect(730, 135, 200, 16))
        self.requirederrcoeff.setStyleSheet(u"color: rgb(220, 38, 38);")

        self.Save_button_Subject = HoverButton(self.page)
        self.Save_button_Subject.setObjectName(u"Edit_button")
        self.Save_button_Subject.setGeometry(QRect(760, 500, 91, 31))
        self.Save_button_Subject.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                               "color : rgb(255,255,255);\n"
                                               "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                               "border-radius: 15px}\n"
                                               "\n"
                                               "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                               "color: rgb(255,255,255)\n"
                                               "}")
        self.Edit_button_Subject = HoverButton(self.page)
        self.Edit_button_Subject.setObjectName(u"Edit_button")
        self.Edit_button_Subject.setGeometry(QRect(810, 500, 91, 31))
        self.Edit_button_Subject.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                               "color : rgb(255,255,255);\n"
                                               "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                               "border-radius: 15px}\n"
                                               "\n"
                                               "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                               "color: rgb(255,255,255)\n"
                                               "}")
        self.Cancel_button_Subject = HoverButton(self.page)
        self.Cancel_button_Subject.setObjectName(u"Cancel_button2")
        self.Cancel_button_Subject.setGeometry(QRect(860, 500, 91, 31))
        self.Cancel_button_Subject.setStyleSheet(u"QPushButton {background-color: rgb(209, 213, 219);\n"
                                                 "color: rgb(55, 65, 81);\n"
                                                 "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                                 "border-radius: 15px\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {background-color: rgb(156,163,175)}")
        self.Save_button_Grades = QPushButton(self.page)
        self.Save_button_Grades.setObjectName(u"Edit_button")
        self.Save_button_Grades.setGeometry(QRect(760, 500, 91, 31))
        self.Save_button_Grades.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                              "color : rgb(255,255,255);\n"
                                              "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                              "border-radius: 15px}\n"
                                              "\n"
                                              "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                              "color: rgb(255,255,255)\n"
                                              "}")
        self.Edit_button_Grades = HoverButton(self.page)
        self.Edit_button_Grades.setObjectName(u"Edit_button")
        self.Edit_button_Grades.setGeometry(QRect(810, 500, 91, 31))
        self.Edit_button_Grades.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                              "color : rgb(255,255,255);\n"
                                              "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                              "border-radius: 15px}\n"
                                              "\n"
                                              "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                              "color: rgb(255,255,255)\n"
                                              "}")
        self.Cancel_button_Grades = HoverButton(self.page)
        self.Cancel_button_Grades.setObjectName(u"Cancel_button2")
        self.Cancel_button_Grades.setGeometry(QRect(860, 500, 91, 31))
        self.Cancel_button_Grades.setStyleSheet(u"QPushButton {background-color: rgb(209, 213, 219);\n"
                                                "color: rgb(55, 65, 81);\n"
                                                "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                                "border-radius: 15px\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {background-color: rgb(156,163,175)}")

        self.errlbl3 = QLabel(self.page)
        self.errlbl3.setObjectName(u"errlbl3")
        self.errlbl3.setGeometry(QRect(180, 160, 270, 16))
        self.errlbl3.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.errlbl3.hide()

        self.info = QLabel(self.page)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(170, 80, 430, 16))
        self.info.setStyleSheet(u"color: #2196F3;")
        self.info.hide()

    def Grades_retranslate(self, Dialog):
        self.Subject_top_btn.setText(QCoreApplication.translate("Dialog", u"Subjects", None))
        self.grades_top_btn.setText(QCoreApplication.translate("Dialog", u"Grades", None))
        self.Edit_button_Subject.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.Save_button_Subject.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.Cancel_button_Subject.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.Edit_button_Grades.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.Save_button_Grades.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.Cancel_button_Grades.setText(QCoreApplication.translate("Dialog", u"Cancel", None))

        ___qtablewidgetitemg = self.tableWidget_grades.horizontalHeaderItem(0)
        ___qtablewidgetitemg.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem1g = self.tableWidget_grades.horizontalHeaderItem(1)
        ___qtablewidgetitem1g.setText(QCoreApplication.translate("Dialog", u"Full Name", None));

        self.subject_name.setText(QCoreApplication.translate("Dialog", u"Subject :", None))
        self.coeff.setText(QCoreApplication.translate("Dialog", u"Coefficient :", None))
        self.requirederrsubject.setText(QCoreApplication.translate("Dialog", u"Invalid Subject", None))
        self.requirederrcoeff.setText(QCoreApplication.translate("Dialog", u"Invalid Coefficient", None))

        self.add_button_subject.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.cancel_button_subject.setText(QCoreApplication.translate("Dialog", u"Cancel", None))

        ___qtablewidgetitems = self.tableWidget_subjects.horizontalHeaderItem(0)
        ___qtablewidgetitems.setText(QCoreApplication.translate("Dialog", u"Subject", None));
        ___qtablewidgetitem1cs = self.tableWidget_subjects.horizontalHeaderItem(1)
        ___qtablewidgetitem1cs.setText(QCoreApplication.translate("Dialog", u"Coefficient", None));
        ___qtablewidgetitem2cs = self.tableWidget_subjects.horizontalHeaderItem(2)
        ___qtablewidgetitem2cs.setText(QCoreApplication.translate("Dialog", u"Delete", None));

        self.info.setText(QCoreApplication.translate("Dialog", u"You can enter multiple marks separated by spaces (for multiple exams)",None))
        self.errlbl3.setText(QCoreApplication.translate("Dialog", u"Please ensure all entered information is correct", None))
        self.class3.setText(QCoreApplication.translate("Dialog", u"Class     ", None))
