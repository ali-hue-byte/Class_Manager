from Logic.Utils import HoverButton

from PySide6.QtCore import (QCoreApplication, QRect, Qt)

from PySide6.QtWidgets import (QLabel,QLineEdit,QTableWidget, QTableWidgetItem, QHeaderView,QAbstractItemView)

class ClassUI(object):
    def class_setup(self, Dialog):
        self.Classnameline = QLineEdit(self.page)
        self.Classnameline.setObjectName(u"Classnameline")
        self.Classnameline.setGeometry(QRect(290, 90, 221, 41))
        self.Classnameline.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
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
        self.requirederrclass = QLabel(self.page)
        self.requirederrclass.setObjectName(u"requirederrclass")
        self.requirederrclass.setGeometry(QRect(290, 135, 200, 16))
        self.requirederrclass.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.classname = QLabel(self.page)
        self.classname.setObjectName(u"classname")
        self.classname.setGeometry(QRect(170, 100, 101, 16))
        self.classname.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                     "font: 600 12pt \"Segoe UI\";")
        self.maxstudents = QLabel(self.page)
        self.maxstudents.setObjectName(u"maxstudents")
        self.maxstudents.setGeometry(QRect(590, 100, 141, 16))
        self.maxstudents.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                       "font: 600 12pt \"Segoe UI\";")
        self.maxstudentsline = QLineEdit(self.page)
        self.maxstudentsline.setObjectName(u"maxstudentsline")
        self.maxstudentsline.setGeometry(QRect(730, 90, 221, 41))
        self.maxstudentsline.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
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
        self.requirederrmax = QLabel(self.page)
        self.requirederrmax.setObjectName(u"requirederrmax")
        self.requirederrmax.setGeometry(QRect(730, 135, 200, 16))
        self.requirederrmax.setStyleSheet(u"color: rgb(220, 38, 38);")

        self.tableWidget_class = QTableWidget(self.page)  # Classes tables
        if (self.tableWidget_class.columnCount() < 4):
            self.tableWidget_class.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_class.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_class.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_class.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_class.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_class.setObjectName(u"tableWidget_class")
        self.tableWidget_class.setGeometry(QRect(170, 200, 801, 280))
        self.tableWidget_class.horizontalHeader().setDefaultSectionSize(190)
        self.tableWidget_class.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_class.verticalHeader().setStretchLastSection(False)
        self.tableWidget_class.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_class.setShowGrid(True)
        self.tableWidget_class.setStyleSheet(u"QHeaderView::section {\n"
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
        self.tableWidget_class.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_class.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_class.setEditTriggers(QTableWidget.NoEditTriggers)
        header = self.tableWidget_class.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        vheader = self.tableWidget_class.verticalHeader()
        vheader.setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget_class.verticalHeader().setHighlightSections(False)

        self.Save_button_class = HoverButton(self.page)
        self.Save_button_class.setObjectName(u"Edit_button")
        self.Save_button_class.setGeometry(QRect(760, 500, 91, 31))
        self.Save_button_class.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                             "color : rgb(255,255,255);\n"
                                             "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                             "border-radius: 15px}\n"
                                             "\n"
                                             "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                             "color: rgb(255,255,255)\n"
                                             "}")
        self.Edit_button_class = HoverButton(self.page)
        self.Edit_button_class.setObjectName(u"Edit_button")
        self.Edit_button_class.setGeometry(QRect(810, 500, 91, 31))
        self.Edit_button_class.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                             "color : rgb(255,255,255);\n"
                                             "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                             "border-radius: 15px}\n"
                                             "\n"
                                             "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                             "color: rgb(255,255,255)\n"
                                             "}")
        self.Cancel_edit_button_class = HoverButton(self.page)
        self.Cancel_edit_button_class.setObjectName(u"Cancel_button2")
        self.Cancel_edit_button_class.setGeometry(QRect(860, 500, 91, 31))
        self.Cancel_edit_button_class.setStyleSheet(u"QPushButton {background-color: rgb(209, 213, 219);\n"
                                                    "color: rgb(55, 65, 81);\n"
                                                    "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                                    "border-radius: 15px\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:hover {background-color: rgb(156,163,175)}")

        self.add_button_class = HoverButton(self.page)
        self.add_button_class.setObjectName(u"add_button_class")
        self.add_button_class.setGeometry(QRect(470, 160, 101, 31))
        self.add_button_class.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                            "color : rgb(255,255,255);\n"
                                            "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                            "border-radius: 15px}\n"
                                            "\n"
                                            "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                            "color: rgb(255,255,255)\n"
                                            "}")
        self.cancel_button_class = HoverButton(self.page)
        self.cancel_button_class.setObjectName(u"cancel_button_class")
        self.cancel_button_class.setGeometry(QRect(580, 160, 101, 31))
        self.cancel_button_class.setStyleSheet(u"QPushButton {background-color: rgb(209, 213, 219);\n"
                                               "color: rgb(55, 65, 81);\n"
                                               "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                               "border-radius: 15px\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {background-color: rgb(156,163,175)}")

        self.errlbl2 = QLabel(self.page)
        self.errlbl2.setObjectName(u"requirederrfirst_22")
        self.errlbl2.setGeometry(QRect(180, 160, 270, 16))
        self.errlbl2.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.errlbl2.hide()



    def Class_retranslate(self, Dialog):
        self.Cancel_edit_button_class.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.Edit_button_class.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.Save_button_class.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.classname.setText(QCoreApplication.translate("Dialog", u"Class Name   :", None))
        self.maxstudents.setText(QCoreApplication.translate("Dialog", u"Max Students    :", None))
        self.maxstudentsline.setText("")

        ___qtablewidgetitem = self.tableWidget_class.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Class name", None));
        ___qtablewidgetitem1c = self.tableWidget_class.horizontalHeaderItem(1)
        ___qtablewidgetitem1c.setText(QCoreApplication.translate("Dialog", u"Total Students", None));
        ___qtablewidgetitem2c = self.tableWidget_class.horizontalHeaderItem(2)
        ___qtablewidgetitem2c.setText(QCoreApplication.translate("Dialog", u"Max Students", None));
        ___qtablewidgetitem3c = self.tableWidget_class.horizontalHeaderItem(3)
        ___qtablewidgetitem3c.setText(QCoreApplication.translate("Dialog", u"Delete", None));
        self.add_button_class.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.cancel_button_class.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.requirederrclass.setText(QCoreApplication.translate("Dialog", u"Please Enter a Valid Class Name", None))
        self.requirederrmax.setText(QCoreApplication.translate("Dialog", u"Please enter a valid numeric value", None))
        self.Classnameline.setText("")
        self.errlbl2.setText(QCoreApplication.translate("Dialog", u"Please ensure all entered information is correct", None))
