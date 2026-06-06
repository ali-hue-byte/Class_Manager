# ============================================================
# Attendance Page UI
# Defines the attendance marking page layout and widgets
# ============================================================



from PySide6.QtCore import (QCoreApplication, QDate, QRect,Qt)
from PySide6.QtWidgets import (QLabel,QComboBox, QDateEdit, QTableWidget, QTableWidgetItem, QHeaderView,
                               QAbstractItemView)

class AttendanceUI(object):
    def attendance_setup(self, Dialog):
        self.dateEdit2 = QDateEdit(self.page)
        self.dateEdit2.setObjectName(u"dateEdit2")
        self.dateEdit2.setGeometry(QRect(260, 80, 221, 41))
        self.dateEdit2.setStyleSheet(u"QDateEdit {border-radius: 15px;\n"
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
        self.dateEdit2.setDate(QDate.currentDate())
        self.dateEdit2.setCalendarPopup(True)

        self.ClassComboBox4 = QComboBox(self.page)
        self.ClassComboBox4.setObjectName(u"ClassComboBox4")
        self.ClassComboBox4.setGeometry(QRect(740, 80, 221, 41))
        self.ClassComboBox4.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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

        self.class4 = QLabel(self.page)
        self.class4.setObjectName(u"class4")
        self.class4.setGeometry(QRect(680, 90, 41, 16))
        self.class4.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")
        self.date = QLabel(self.page)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(200, 90, 41, 16))
        self.date.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                "font: 600 12pt \"Segoe UI\";")

        self.tableWidget_att = QTableWidget(self.page)  # Attendance page

        if (self.tableWidget_att.columnCount() < 3):
            self.tableWidget_att.setColumnCount(3)
        __qtablewidgetitema = QTableWidgetItem()
        self.tableWidget_att.setHorizontalHeaderItem(0, __qtablewidgetitema)
        __qtablewidgetitem1a = QTableWidgetItem()
        self.tableWidget_att.setHorizontalHeaderItem(1, __qtablewidgetitem1a)
        __qtablewidgetitem2a = QTableWidgetItem()
        self.tableWidget_att.setHorizontalHeaderItem(2, __qtablewidgetitem2a)
        __qtablewidgetitem3s = QTableWidgetItem()
        self.tableWidget_att.setHorizontalHeaderItem(3, __qtablewidgetitem3s)
        self.tableWidget_att.setObjectName(u"tableWidget_att")
        self.tableWidget_att.setGeometry(QRect(270, 150, 610, 340))
        self.tableWidget_att.horizontalHeader().setDefaultSectionSize(190)
        self.tableWidget_att.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_att.verticalHeader().setStretchLastSection(False)
        self.tableWidget_att.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_att.setShowGrid(True)
        self.tableWidget_att.setStyleSheet(u"QHeaderView::section {\n"
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
        self.tableWidget_att.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_att.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_att.setEditTriggers(QTableWidget.NoEditTriggers)
        header = self.tableWidget_att.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        vheader = self.tableWidget_att.verticalHeader()
        vheader.setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget_att.verticalHeader().setHighlightSections(False)
        self.tableWidget_att.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def Attendance_retranslate(self, Dialog):
        ___qtablewidgetitema = self.tableWidget_att.horizontalHeaderItem(0)
        ___qtablewidgetitema.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem1a = self.tableWidget_att.horizontalHeaderItem(1)
        ___qtablewidgetitem1a.setText(QCoreApplication.translate("Dialog", u"Full Name", None));
        ___qtablewidgetitem2a = self.tableWidget_att.horizontalHeaderItem(2)
        ___qtablewidgetitem2a.setText(QCoreApplication.translate("Dialog", u"Status", None));
        self.class4.setText(QCoreApplication.translate("Dialog", u"Class     ", None))
        self.date.setText(QCoreApplication.translate("Dialog", u"Date     ", None))
