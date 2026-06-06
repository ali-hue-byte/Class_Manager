from Logic.Utils import HoverButton

from PySide6.QtCore import (QCoreApplication, QDate, QRect, Qt)
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (QDialog, QLabel, QLineEdit, QPushButton,
                               QComboBox, QDateEdit, QTableWidget,
                               QTableWidgetItem, QHeaderView,
                               QAbstractItemView)

class StudentUI(QDialog):
    def Students_setup(self, Dialog):
        self.stackedWidget.addWidget(self.page)
        self.Add_top_btn = QPushButton(self.frame_2)
        self.Add_top_btn.setObjectName(u"Add_top_btn")
        self.Add_top_btn.setGeometry(QRect(480, 40, 81, 31))
        self.Add_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                       "color :rgb(24, 182, 255);\n"
                                       "border: none;\n"
                                       "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                       "}\n"
                                       "")
        self.Add_top_btn.setFlat(True)
        self.View_top_btn = QPushButton(self.frame_2)
        self.View_top_btn.setObjectName(u"View_top_btn")
        self.View_top_btn.setGeometry(QRect(570, 40, 81, 31))
        self.View_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                        "font: 700 9pt \"Yu Gothic UI\";")
        self.View_top_btn.setFlat(True)
        self.dateEdit_add_student = QDateEdit(self.page)
        self.dateEdit_add_student.setObjectName(u"dateEdit")
        self.dateEdit_add_student.setGeometry(QRect(730, 200, 221, 41))
        self.dateEdit_add_student.setStyleSheet(u"QDateEdit {border-radius: 15px;\n"
                                                "border: 1px solid grey;\n"
                                                "padding: 6px 8px;\n"
                                                "background-color: rgb(255,255,255)\n"
                                                "}\n"
                                                "\n"
                                                "QDateEdit::up-button {width: 0;}\n"
                                                "QDateEdit::down-button {width: 0;}\n"
                                                "\n"
                                                "QDateEdit:hover {border: 2px solid black;\n"
                                                "padding : 5px 7px;}\n"
                                                "\n"
                                                "QDateEdit:focus {border: 2px solid #0078d7;\n"
                                                "\n"
                                                "}\n"
                                                "QDateEdit::drop-down {\n"
                                                "subcontrol-origin: padding;\n"
                                                "subcontrol-position: right center;\n"
                                                "width: 30px;\n"
                                                "border-top-right-radius: 15px;\n"
                                                "border-bottom-right-radius: 15px;\n"
                                                "}\n"
                                                "QDateEdit::down-arrow {\n"
                                                "image: url(icons/calendar.png);\n"
                                                "width: 15px;\n"
                                                "height: 15px;\n"
                                                "}")
        self.dateEdit_add_student.setDate(QDate.currentDate())
        self.dateEdit_add_student.setCalendarPopup(True)
        self.Firstnameline = QLineEdit(self.page)
        self.Firstnameline.setObjectName(u"Firstnameline")
        self.Firstnameline.setGeometry(QRect(300, 130, 221, 41))
        self.Firstnameline.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
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
        self.GenderComboBox = QComboBox(self.page)
        self.GenderComboBox.addItem("")
        self.GenderComboBox.addItem("")
        self.GenderComboBox.setObjectName(u"GenderComboBox")
        self.GenderComboBox.setGeometry(QRect(300, 200, 221, 41))
        self.GenderComboBox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
                                          "border-radius : 15px ;\n"
                                          "padding : 6px 8px;\n"
                                          "background-color: rgb(255,255,255)\n"
                                          "}\n"
                                          "QComboBox:drop-down { width: 0;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:hover{border: 2px solid black ;\n"
                                          "padding : 5px 7px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:focus {\n"
                                          "  border : 2px solid #0078d7;\n"
                                          "}\n"
                                          "\n"
                                          "")
        self.GenderComboBox.setMaxVisibleItems(2)
        self.Firstname = QLabel(self.page)
        self.Firstname.setObjectName(u"Firstname")
        self.Firstname.setGeometry(QRect(170, 140, 111, 16))
        self.Firstname.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                     "font: 600 12pt \"Segoe UI\";")
        self.lastname = QLabel(self.page)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(580, 140, 141, 16))
        self.lastname.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                    "font: 600 12pt \"Segoe UI\";")
        self.birth = QLabel(self.page)
        self.birth.setObjectName(u"birth")
        self.birth.setGeometry(QRect(580, 210, 141, 16))
        self.birth.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                 "font: 600 12pt \"Segoe UI\";")

        self.Class1 = QLabel(self.page)
        self.Class1.setObjectName(u"Class1")
        self.Class1.setGeometry(QRect(170, 310, 121, 16))
        self.Class1.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")
        self.Gender = QLabel(self.page)
        self.Gender.setObjectName(u"Gender")
        self.Gender.setGeometry(QRect(170, 210, 121, 16))
        self.Gender.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")
        self.phone = QLabel(self.page)
        self.phone.setObjectName(u"phone")
        self.phone.setGeometry(QRect(580, 410, 141, 16))
        self.phone.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                 "font: 600 12pt \"Segoe UI\";")
        self.Email = QLabel(self.page)
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(170, 410, 121, 16))
        self.Email.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                 "font: 600 12pt \"Segoe UI\";")
        self.Address = QLabel(self.page)
        self.Address.setObjectName(u"Address")
        self.Address.setGeometry(QRect(170, 480, 121, 16))
        self.Address.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                   "font: 600 12pt \"Segoe UI\";")
        self.label_21 = QLabel(self.page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(180, 85, 201, 31))
        self.label_21.setStyleSheet(u"font: 700 20pt \"Segoe UI Variable\";\n"
                                    "color: rgb(51, 51, 51);")
        self.lastnameline = QLineEdit(self.page)
        self.lastnameline.setObjectName(u"lastnameline")
        self.lastnameline.setGeometry(QRect(730, 130, 221, 41))
        self.lastnameline.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
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
        self.label_22 = QLabel(self.page)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(180, 255, 251, 31))
        self.label_22.setStyleSheet(u"font: 700 20pt \"Segoe UI Variable\";\n"
                                    "color: rgb(51, 51, 51);")
        self.ClassComboBox = QComboBox(self.page)
        self.ClassComboBox.setObjectName(u"ClassComboBox")

        self.ClassComboBox.setGeometry(QRect(300, 300, 221, 41))
        self.ClassComboBox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.errclasse = QLabel(self.page)
        self.errclasse.setObjectName(u"errclasse")
        self.errclasse.setGeometry(QRect(310, 340, 300, 16))
        self.errclasse.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.errclasse.hide()
        self.label_23 = QLabel(self.page)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(180, 355, 181, 31))
        self.label_23.setStyleSheet(u"font: 700 20pt \"Segoe UI Variable\";\n"
                                    "color: rgb(51, 51, 51);")
        self.Emailine = QLineEdit(self.page)
        self.Emailine.setObjectName(u"Emailine")
        self.Emailine.setGeometry(QRect(300, 400, 221, 41))
        self.Emailine.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
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
        self.AdressLine = QLineEdit(self.page)
        self.AdressLine.setObjectName(u"AdressLine")
        self.AdressLine.setGeometry(QRect(300, 470, 221, 41))
        self.AdressLine.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
                                      "border-radius : 15px ;\n"
                                      "padding : 6px 8px ;\n"
                                      "background-color: rgb(255,255,255)\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:hover{border: 2px solid black;\n"
                                      "padding : 5px 7px;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:focus {\n"
                                      "  border : 2px solid #0078d7;\n"
                                      "}")
        self.Numberline = QLineEdit(self.page)
        self.Numberline.setObjectName(u"Numberline")
        self.Numberline.setGeometry(QRect(730, 400, 221, 41))
        self.Numberline.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
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
        self.label_24 = QLabel(self.page)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(160, 60, 221, 41))
        self.label_24.setStyleSheet(u"\n"
                                    "font: 9pt \"Segoe UI\";\n"
                                    "color: rgb(229, 83, 61);")
        self.Add_button_Student = HoverButton(self.page)
        self.Add_button_Student.setObjectName(u"Add_button")
        self.Add_button_Student.setGeometry(QRect(760, 500, 91, 31))
        self.Add_button_Student.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                              "color : rgb(255,255,255);\n"
                                              "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                              "border-radius: 15px}\n"
                                              "\n"
                                              "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                              "color: rgb(255,255,255)\n"
                                              "}")
        self.Cancel_button_Student = HoverButton(self.page)
        self.Cancel_button_Student.setObjectName(u"Cancel_button")
        self.Cancel_button_Student.setGeometry(QRect(860, 500, 91, 31))
        self.Cancel_button_Student.setStyleSheet(u"QPushButton {background-color: rgb(209, 213, 219);\n"
                                                 "color: rgb(55, 65, 81);\n"
                                                 "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                                 "border-radius: 15px\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {background-color: rgb(156,163,175)}")
        self.requirederrfirst = QLabel(self.page)
        self.requirederrfirst.setObjectName(u"requirederrfirst")
        self.requirederrfirst.setGeometry(QRect(310, 170, 111, 16))
        self.requirederrfirst.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.requirederrlast = QLabel(self.page)
        self.requirederrlast.setObjectName(u"requirederrlast")
        self.requirederrlast.setGeometry(QRect(740, 170, 111, 16))
        self.requirederrlast.setStyleSheet(u"color: rgb(220, 38, 38);")

        self.birtherr = QLabel(self.page)
        self.birtherr.setObjectName(u"birtherr")
        self.birtherr.setGeometry(QRect(730, 240, 221, 41))
        self.birtherr.setStyleSheet(u"color: rgb(220, 38, 38);")

        self.tableWidget = QTableWidget(self.page)  # View students table
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(160, 130, 820, 340))
        self.tableWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
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

        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        vheader = self.tableWidget.verticalHeader()
        vheader.setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.setColumnWidth(0, 80)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 50)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setColumnWidth(6, 150)
        self.tableWidget.setColumnWidth(7, 70)
        self.Save_button_View = HoverButton(self.page)
        self.Save_button_View.setObjectName(u"Edit_button")
        self.Save_button_View.setGeometry(QRect(760, 500, 91, 31))

        self.Save_button_View.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                            "color : rgb(255,255,255);\n"
                                            "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                            "border-radius: 15px}\n"
                                            "\n"
                                            "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                            "color: rgb(255,255,255)\n"
                                            "}")
        self.Edit_button_View = HoverButton(self.page)
        self.Edit_button_View.setObjectName(u"Edit_button")
        self.Edit_button_View.setGeometry(QRect(810, 500, 91, 31))

        self.Edit_button_View.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                            "color : rgb(255,255,255);\n"
                                            "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                            "border-radius: 15px}\n"
                                            "\n"
                                            "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                            "color: rgb(255,255,255)\n"
                                            "}")
        self.Cancel_button_View = HoverButton(self.page)
        self.Cancel_button_View.setObjectName(u"Cancel_button2")
        self.Cancel_button_View.setGeometry(QRect(860, 500, 91, 31))

        self.Cancel_button_View.setStyleSheet(u"QPushButton {background-color: rgb(209, 213, 219);\n"
                                              "color: rgb(55, 65, 81);\n"
                                              "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                              "border-radius: 15px\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {background-color: rgb(156,163,175)}")

        self.errlbl = QLabel(self.page)
        self.errlbl.setObjectName(u"requirederrfirst_2")
        self.errlbl.setGeometry(QRect(180, 80, 270, 16))
        self.errlbl.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.errlbl.hide()



        self.ClassComboBox2 = QComboBox(self.page)
        self.ClassComboBox2.setObjectName(u"ClassComboBox2")
        self.ClassComboBox2.setGeometry(QRect(740, 80, 221, 41))
        self.ClassComboBox2.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.class2 = QLabel(self.page)
        self.class2.setObjectName(u"class2")
        self.class2.setGeometry(QRect(680, 90, 41, 16))
        self.class2.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")

        self.requirederrfirst_2 = QLabel(self.page)
        self.requirederrfirst_2.setObjectName(u"requirederrfirst_2")
        self.requirederrfirst_2.setGeometry(QRect(310, 450, 111, 16))
        self.requirederrfirst_2.setStyleSheet(u"color: rgb(220, 38, 38);")

        self.requirederrfirst_3 = QLabel(self.page)
        self.requirederrfirst_3.setObjectName(u"requirederrfirst_3")
        self.requirederrfirst_3.setGeometry(QRect(740, 450, 111, 16))
        self.requirederrfirst_3.setStyleSheet(u"color: rgb(220, 38, 38);")

    def Students_retranslate(self, Dialog):
        self.Add_top_btn.setText(QCoreApplication.translate("Dialog", u"Add Student", None))
        self.View_top_btn.setText(QCoreApplication.translate("Dialog", u"View Students", None))
        self.Firstnameline.setText("")
        self.GenderComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Male", None))
        self.GenderComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Female", None))
        self.Firstname.setText(QCoreApplication.translate("Dialog", u"First Name*     :", None))
        self.lastname.setText(QCoreApplication.translate("Dialog", u"Last Name*          :", None))
        self.birth.setText(QCoreApplication.translate("Dialog", u"Date Of Birth*      :", None))
        self.Class1.setText(QCoreApplication.translate("Dialog", u"Class*               : ", None))
        self.Gender.setText(QCoreApplication.translate("Dialog", u"Gender*           :", None))
        self.phone.setText(QCoreApplication.translate("Dialog", u"Contact Number  :", None))
        self.Email.setText(QCoreApplication.translate("Dialog", u"Email                :", None))
        self.Address.setText(QCoreApplication.translate("Dialog", u"Home Address :", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"Personal info ", None))
        self.lastnameline.setText("")
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Academic info ", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"Contact info ", None))
        self.Emailine.setText("")
        self.Emailine.setPlaceholderText(QCoreApplication.translate("Dialog", u"example123@gmail.com", None))
        self.AdressLine.setText("")
        self.Numberline.setText("")
        self.Numberline.setPlaceholderText(QCoreApplication.translate("Dialog", u"", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Fields marked with * are required\n"
                                                                   "", None))
        self.Add_button_Student.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.Cancel_button_Student.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.Edit_button_View.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.Save_button_View.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.Cancel_button_View.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.errclasse.setText(QCoreApplication.translate("Dialog", u"There are no classes yet", None))
        self.requirederrfirst_3.setText(QCoreApplication.translate("Dialog", u"Invalid Number", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Full Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Date of Birth", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"M/F", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Address", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Number", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Email", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"Delete", None));

        self.requirederrfirst.setText(QCoreApplication.translate("Dialog", u"This field is required", None))
        self.requirederrlast.setText(QCoreApplication.translate("Dialog", u"This field is required", None))
        self.birtherr.setText(QCoreApplication.translate("Dialog", u"Is the student’s birth date in the future?", None))
        self.requirederrfirst_2.setText(QCoreApplication.translate("Dialog", u"Invalid Email", None))
        self.errlbl.setText(QCoreApplication.translate("Dialog", u"Please ensure all entered information is correct", None))
        self.class2.setText(QCoreApplication.translate("Dialog", u"Class     ", None))

