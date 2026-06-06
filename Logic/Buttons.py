# ============================================================
# Buttons Handler
# Handles all button click events and user interactions
# ============================================================

import os

from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QAbstractItemView,
                               QTableWidget)
from PySide6.QtCore import Qt, QDate, QRect

from Logic.Functions import (hash_password,
                       save_data,
                       load_data,
                       KDF2,
                       decrypt_data,
                       encrypt_data,
                       add_student,
                       add_class,
                       add_subject,
                       add_grade,
                       SALT)
from Logic.Utils import (wrap_with_shadow,
                   unwrap_shadow,
                   update_line,
                   reset_line,
                   update_line2,
                   reset_line2,
                   animate_page,
                   widgets_operations,
                   refresh_combo_id)
from Display.Graphs import (refresh_graph1,
                              refresh_graph2,
                              refresh_graph3,
                              refresh_graph4,
                              refresh_graph5,
                              refresh_graph6,
                              refresh_graph7,
                              refresh_graph8)
from Display.Tables import (refresh_attendance,
                              refresh_grades,
                              refresh_subject,
                              refresh_add,
                              refresh_view,
                              refresh_class)

import re
import random
import sqlite3


conn = sqlite3.connect('data.db')
c = conn.cursor()

# ============================================================
# Authentication Buttons
# ============================================================

def creat_clicked(self):
    """ Creates a new account """

    self.ui.ClassComboBox2.clear()
    self.ui.ClassComboBox.clear()
    username = str(self.ui.lineEdit_n.text())
    password = str(self.ui.lineEdit_2_n.text())
    data = load_data()

    # checks username and password strength
    if username == "" or password == "":
        reset_line(self.ui.lineEdit_n)
        reset_line(self.ui.lineEdit_2_n)
        self.ui.label_errn.setText("Please enter both username and password")
        self.ui.label_errn.show()
        update_line(self.ui.lineEdit_n)
        update_line(self.ui.lineEdit_2_n)
        self.ui.label_errn.repaint()
        return

    if re.search(r'[^a-zA-Z0-9_]', username) or len(username) < 3 or len(username) > 15:
        reset_line(self.ui.lineEdit_n)
        reset_line(self.ui.lineEdit_2_n)
        self.ui.label_errn.setText("Username is invalid")
        update_line(self.ui.lineEdit_n)
        self.ui.label_errn.show()
        return

    for i in data:
        if username == i["username"]:
            reset_line(self.ui.lineEdit_n)
            reset_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.setText("Username already exists")
            update_line(self.ui.lineEdit_n)
            self.ui.label_errn.show()
            return
    if len(password) < 8:
        reset_line(self.ui.lineEdit_n)
        reset_line(self.ui.lineEdit_2_n)
        self.ui.label_errn.setText("The password must be at least 8 characters long.")
        update_line(self.ui.lineEdit_2_n)
        self.ui.label_errn.show()
        return
    elif not re.search(r"[A-Z]", password):
        reset_line(self.ui.lineEdit_n)
        reset_line(self.ui.lineEdit_2_n)
        self.ui.label_errn.setText("The password must include at least one uppercase letter.")
        update_line(self.ui.lineEdit_2_n)
        self.ui.label_errn.show()
        return
    elif not re.search(r"[a-z]", password):
        reset_line(self.ui.lineEdit_n)
        reset_line(self.ui.lineEdit_2_n)
        self.ui.label_errn.setText("The password must include at least one lowercase letter.")
        update_line(self.ui.lineEdit_2_n)
        self.ui.label_errn.show()
        return
    elif not re.search(r"[0-9]", password):
        reset_line(self.ui.lineEdit_n)
        reset_line(self.ui.lineEdit_2_n)
        self.ui.label_errn.setText("The password must include at least one number.")
        update_line(self.ui.lineEdit_2_n)
        self.ui.label_errn.show()
        return
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        reset_line(self.ui.lineEdit_n)
        reset_line(self.ui.lineEdit_2_n)
        self.ui.label_errn.setText("The password must include at least one special character.")
        update_line(self.ui.lineEdit_2_n)
        self.ui.label_errn.show()
        return

    # random salt
    salt = os.urandom(16)
    # new user information
    new_user = {"username": username, "password": hash_password(password, salt), "salt": salt.hex(), "max_score": 20}
    data.append(new_user)
    self.current_user.append(username) # Active user
    self.current_password.append(password)
    self.ui.label_errn.hide()
    self.ui.welcome_label.setText(f"Welcome {username}")
    self.ui.welcome_label.show()
    animate_page(self, self.ui.page, 1, 0)
    self.ui.stackedWidget.setCurrentIndex(0)
    save_data(data)

    for i in self.lines:
        i.clear()
        reset_line(i)
    self.salt = SALT(self.current_user[-1])
    self.kdf = KDF2(self.current_password[-1], self.salt)
    home_clicked(self)


def log_clicked(self):
    """ LogIn to existing account """

    self.ui.ClassComboBox2.clear()
    self.ui.ClassComboBox.clear()
    username = str(self.ui.lineEdit_5.text())
    password = str(self.ui.lineEdit_6.text())
    data = load_data()
    # checks username and passsword
    if username == "" or password == "":
        reset_line(self.ui.lineEdit_5)
        reset_line(self.ui.lineEdit_6)
        self.ui.label_errn.setText("Please enter both username and password")
        self.ui.label_errn.show()
        update_line(self.ui.lineEdit_5)
        update_line(self.ui.lineEdit_6)
        self.ui.label_errn.repaint()
        return
    for i in data:
        if i["username"] == username and i["password"] == hash_password(password, bytes.fromhex(i["salt"])):
            # LogIn
            reset_line(self.ui.lineEdit_5)
            reset_line(self.ui.lineEdit_6)
            self.ui.label_errn.hide()
            self.ui.welcome_label.setText(f"Welcome {username}")
            self.ui.welcome_label.show()
            self.current_user.append(username)
            self.current_password.append(password)

            animate_page(self, self.ui.page, 1, 0)
            self.ui.stackedWidget.setCurrentIndex(0)

            home_clicked(self)
            self.salt = SALT(self.current_user[-1])
            self.kdf = KDF2(self.current_password[-1], self.salt)


            for i in self.lines:
                i.clear()
                reset_line(i)
            return
    update_line(self.ui.lineEdit_5)
    update_line(self.ui.lineEdit_6)
    self.ui.label_errn.setText("Invalid username or password")
    self.ui.label_errn.show()
    return


# ============================================================
# Home Buttons
# ============================================================

def home_clicked(self):
    """ Displays Home screen """


    c.execute("SELECT * FROM subjects WHERE user=?", (self.current_user[-1],))
    subjects = len(c.fetchall())
    c.execute("SELECT * FROM students WHERE user=?", (self.current_user[-1],))
    students = len(c.fetchall())
    c.execute("SELECT * FROM classes WHERE user=?", (self.current_user[-1],))
    classes = len(c.fetchall())
    # Display data information
    self.ui.label_6.setText(str(subjects))
    self.ui.label_4.setText(str(classes))
    self.ui.label_2.setText(str(students))
    self.ui.info.hide()

    wrap_with_shadow(self.ui.frame_5, 90)
    wrap_with_shadow(self.ui.frame_4, 90)
    wrap_with_shadow(self.ui.frame_3, 90)

    self.ui.Add_top_btn.hide()
    self.ui.View_top_btn.hide()

    widgets_operations(self, "widgets_home")

    self.ui.dateEdit_add_student.setDate(QDate.currentDate())



def exit_clicked(self):
    """ Logs out the current user and returns to authentication page """
    animate_page(self, self.ui.page_2, 1, 0)
    home_clicked(self)
    self.ui.stackedWidget.setCurrentIndex(1)
    return

def students_clicked(self):
    """ Navigates to the Add Student section """

    self.ui.info.hide()
    self.ui.Add_top_btn.show()
    self.ui.View_top_btn.show()

    wrap_with_shadow(self.ui.Add_button_Student, 70)
    wrap_with_shadow(self.ui.Cancel_button_Student, 70)

    unwrap_shadow(self.ui.tableWidget_subjects)
    widgets_operations(self, "widgets_student_add")

    for i in [self.ui.lastnameline, self.ui.Firstnameline]:
        reset_line2(i)
    self.ui.Add_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                      "color :rgb(24, 182, 255);\n"
                                      "border: none;\n"
                                      "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                      "}\n"
                                      "")
    self.ui.View_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                       "font: 700 9pt \"Yu Gothic UI\";")
    self.ui.ClassComboBox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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

    self.ui.Subject_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                          "color :rgb(24, 182, 255);\n"
                                          "border: none;\n"
                                          "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                          "}\n"
                                          "")
    self.ui.grades_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                         "font: 700 9pt \"Yu Gothic UI\";")
    self.ui.dateEdit_add_student.setStyleSheet(u"QDateEdit {border-radius: 15px;\n"
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
    refresh_add(self, self.current_user[-1], self.current_password[-1])

def classe_clicked(self):
    """ Displays classes page """

    self.ui.info.hide()
    widgets_operations(self, "widgets_class")

    self.ui.Subject_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                          "color :rgb(24, 182, 255);\n"
                                          "border: none;\n"
                                          "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                          "}\n"
                                          "")
    self.ui.grades_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                         "font: 700 9pt \"Yu Gothic UI\";")

    wrap_with_shadow(self.ui.tableWidget_class, 70)
    wrap_with_shadow(self.ui.add_button_class, 70)
    wrap_with_shadow(self.ui.cancel_button_class, 70)
    self.ui.Edit_button_class.setGeometry(
        QRect(810, 500, 91, 31))

    wrap_with_shadow(self.ui.Edit_button_class, 70)

    self.ui.Save_button_class.hide()
    self.ui.Cancel_edit_button_class.hide()

    self.ui.Add_top_btn.hide()
    self.ui.View_top_btn.hide()
    refresh_class(self, self.current_user[-1], self.current_password[-1])

def Grades_clicked(self):
    """ Displays grades page """
    self.ui.info.hide()
    widgets_operations(self, "widgets_grades")

    self.ui.Cancel_button_Grades.hide()
    self.ui.Edit_button_Grades.hide()
    self.ui.Save_button_Grades.hide()
    self.ui.Cancel_button_Subject.hide()
    self.ui.Save_button_Subject.hide()

    self.ui.Edit_button_Subject.setGeometry(QRect(810, 500, 91, 31))

    wrap_with_shadow(self.ui.Edit_button_Subject, 70)
    self.ui.tableWidget_grades.hide()
    self.ui.class3.hide()
    self.ui.ClassComboBox3.hide()
    reset_line2(self.ui.subjectline)
    reset_line2(self.ui.coeffline)
    wrap_with_shadow(self.ui.add_button_subject, 70)
    wrap_with_shadow(self.ui.cancel_button_subject, 70)

    wrap_with_shadow(self.ui.tableWidget_subjects, 70)

    self.ui.Save_button_class.hide()
    self.ui.Cancel_edit_button_class.hide()

    self.ui.Add_top_btn.hide()
    self.ui.View_top_btn.hide()

    refresh_subject(self, self.current_user[-1])
    self.ui.tableWidget_subjects.setFocusPolicy(Qt.NoFocus)
    self.ui.tableWidget_subjects.setSelectionMode(QAbstractItemView.NoSelection)
    self.ui.tableWidget_subjects.setEditTriggers(QTableWidget.NoEditTriggers)
    self.ui.subjectline.clear()
    self.ui.coeffline.clear()
    self.ui.Subject_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                          "color :rgb(24, 182, 255);\n"
                                          "border: none;\n"
                                          "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                          "}\n"
                                          "")
    self.ui.grades_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                         "font: 700 9pt \"Yu Gothic UI\";")



def attendance(self):
    """ Displays attendance page """
    self.ui.Add_top_btn.hide()
    self.ui.View_top_btn.hide()
    self.ui.info.hide()
    widgets_operations(self, "widget_Attendance")

    wrap_with_shadow(self.ui.tableWidget_att, 70)
    refresh_attendance(self, self.current_user[-1], self.current_password[-1], clear=True)


def statistics(self):
    """ Displays statistics page """

    self.ui.info.hide()
    widgets_operations(self, "widgets_statistics")

    self.ui.Add_top_btn.hide()
    self.ui.View_top_btn.hide()
    self.ui.performance.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                     "color :rgb(24, 182, 255);\n"
                                     "border: none;\n"
                                     "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                     "}\n"
                                     "")
    self.ui.ranking.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                  "font: 700 9pt \"Yu Gothic UI\";")
    self.ui.attendancetop.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                        "font: 700 9pt \"Yu Gothic UI\";")
    self.ui.other.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                "font: 700 9pt \"Yu Gothic UI\";")
    refresh_graph1(self, self.current_user[-1], self.current_password[-1])
    refresh_graph2(self, self.current_user[-1], self.current_password[-1])
    animate_page(self, self.ui.Graph_frame, 1, 0, "white", 15, 351, 321)
    animate_page(self, self.ui.Graph_frame_2, 1, 0, "white", 15, 351, 321)


# ============================================================
# Classes Buttons
# ============================================================

def Add_class_clicked(self):
    """ Adds a new class to SQLite database """

    c.execute("SELECT class_name FROM classes WHERE user=?", (self.current_user[-1],))
    classes_rows = c.fetchall()
    classes = [x[0] for x in classes_rows]
    class_ = self.ui.Classnameline.text()
    MaxxStudents = self.ui.maxstudentsline.text()

    # checks for errors
    err = False
    if class_ == "" or not re.fullmatch(r"[A-Za-z0-9éàèîêâôûç ]+", class_) or len(class_) < 2:
        err = True
        self.ui.requirederrclass.setText("Please Enter a Valid Class Name")
        self.update_line2(self.ui.Classnameline)
        self.ui.requirederrclass.show()
    elif class_ in classes:
        err = True
        update_line2(self.ui.Classnameline)
        self.ui.requirederrclass.setText("Class Already exists")
        self.ui.requirederrclass.show()
    else:
        self.ui.requirederrclass.setText("Please Enter a Valid Class Name")
        reset_line2(self.ui.Classnameline)
        self.ui.requirederrclass.hide()
    if MaxxStudents == "" or not MaxxStudents.isdigit():
        err = True
        self.ui.requirederrmax.setText("Please enter a valid numeric value")
        update_line2(self.ui.maxstudentsline)
        self.ui.requirederrmax.show()
    elif int(MaxxStudents) < 2:
        err = True
        update_line2(self.ui.maxstudentsline)
        self.ui.requirederrmax.setText("That can't be a Class")
        self.ui.requirederrmax.show()
    else:
        reset_line2(self.ui.maxstudentsline)
        self.ui.requirederrmax.hide()

    if err == True:
        return

    add_class(self.current_user[-1], class_, MaxxStudents, 0)

    self.ui.Edit_button_class.show()
    wrap_with_shadow(self.ui.Edit_button_class, 70)
    unwrap_shadow(self.ui.Save_button_class)
    unwrap_shadow(self.ui.Cancel_edit_button_class)
    self.ui.Save_button_class.hide()
    self.ui.Cancel_edit_button_class.hide()
    self.ui.tableWidget_class.setSelectionMode(QAbstractItemView.NoSelection)
    self.ui.tableWidget_class.setEditTriggers(QTableWidget.NoEditTriggers)
    refresh_class(self, self.current_user[-1], self.current_password[-1])

    for i in self.widgets:
        i.clear() if "widgets_to_clear" in self.widgets[i] else None


def cancel_class(self):
    """ Cancels adding class operation """

    for i in [self.ui.Classnameline, self.ui.maxstudentsline]:
        i.clear()
        reset_line2(i)

def Edit_btn2(self):
    """ Makes class table cells editable """

    self.ui.Save_button_class.show()
    self.ui.Cancel_edit_button_class.show()
    self.ui.Cancel_edit_button_class.setGeometry(QRect(860, 500, 91, 31))
    self.ui.Save_button_class.setGeometry(QRect(760, 500, 91, 31))
    self.ui.Edit_button_class.hide()

    unwrap_shadow(self.ui.Edit_button_class)
    wrap_with_shadow(self.ui.Save_button_class, 70)
    wrap_with_shadow(self.ui.Cancel_edit_button_class, 70)

    self.ui.tableWidget_class.setEditTriggers(QTableWidget.AllEditTriggers)
    self.ui.tableWidget_class.setSelectionMode(QAbstractItemView.SingleSelection)

    for i in range(self.ui.tableWidget_class.rowCount()):
        item = self.ui.tableWidget_class.item(i, 2)
        if item:
            item.setBackground(QColor("#FFF9C4"))

    for i in range(2):
        self.ui.tableWidget.setItemDelegateForColumn(i, self.delegue)


def Canceled2(self):
    """ Cancels editing class table operation """

    self.ui.Edit_button_class.show()
    self.ui.Edit_button_class.setGeometry(QRect(810, 500, 91, 31))
    self.ui.Save_button_class.hide()
    self.ui.Cancel_edit_button_class.hide()
    self.ui.errlbl2.hide()

    wrap_with_shadow(self.ui.Edit_button_class, 70)
    unwrap_shadow(self.ui.Save_button_class)
    unwrap_shadow(self.ui.Cancel_edit_button_class)

    refresh_class(self, self.current_user[-1], self.current_password[-1])
    self.ui.tableWidget_class.setSelectionMode(QAbstractItemView.NoSelection)
    self.ui.tableWidget_class.setEditTriggers(QTableWidget.NoEditTriggers)


def Save_btn_2(self):
    """ Saves Edited classes information """

    err = False
    new_data = {"Classes": {}}
    for i in range(self.ui.tableWidget_class.rowCount()):
        name = self.ui.tableWidget_class.item(i, 0).text() if self.ui.tableWidget_class.item(i, 0) else ""
        total = self.ui.tableWidget_class.item(i, 1).text() if self.ui.tableWidget_class.item(i, 1) else 0
        max = self.ui.tableWidget_class.item(i, 2).text() if self.ui.tableWidget_class.item(i, 2) else 0

        if not max.isdigit():
            err = True
            item = self.ui.tableWidget_class.item(i, 2)
            if item:
                item.setBackground(QColor("#F8D7DA"))
        else:
            item = self.ui.tableWidget_class.item(i, 2)
            if item:
                item.setBackground(QColor("#FFF9C4"))

        new_data["Classes"][name] = {"class_Name": name,
                                     "Max_students": max,
                                     "Total_students": total}

    if err:
        self.ui.errlbl2.show()
        return
    for i, j in new_data["Classes"].items():
        add_class(self.current_user[-1], i, j["Max_students"], j["Total_students"])

    self.ui.errlbl2.hide()

    self.ui.Edit_button_class.show()
    self.ui.Edit_button_class.setGeometry(QRect(810, 500, 91, 31))
    wrap_with_shadow(self.ui.Edit_button_class, 70)
    unwrap_shadow(self.ui.Save_button_class)
    unwrap_shadow(self.ui.Cancel_edit_button_class)
    self.ui.Save_button_class.hide()
    self.ui.Cancel_edit_button_class.hide()
    refresh_class(self, self.current_user[-1], self.current_password[-1])
    self.ui.tableWidget_class.setSelectionMode(QAbstractItemView.NoSelection)
    self.ui.tableWidget_class.setEditTriggers(QTableWidget.NoEditTriggers)



# ============================================================
# Students Buttons
# ============================================================

def Add_top_clicked(self):
    """ Navigates to add student section """

    self.ui.Add_top_btn.show()
    self.ui.View_top_btn.show()

    wrap_with_shadow(self.ui.Add_button_Student, 70)
    wrap_with_shadow(self.ui.Cancel_button_Student, 70)
    widgets_operations(self, "widgets_student_add")

    self.ui.ClassComboBox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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

    self.ui.Add_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                      "color :rgb(24, 182, 255);\n"
                                      "border: none;\n"
                                      "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                      "}\n"
                                      "")
    self.ui.View_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                       "font: 700 9pt \"Yu Gothic UI\";")
    self.ui.dateEdit_add_student.setStyleSheet(u"QDateEdit {border-radius: 15px;\n"
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
    refresh_add(self, self.current_user[-1], self.current_password[-1])

def view_top_clicked(self):
    """ Navigates to view students section """

    self.ui.Add_top_btn.show()
    self.ui.View_top_btn.show()

    wrap_with_shadow(self.ui.tableWidget, 70)
    self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
    self.ui.tableWidget.verticalHeader().setHighlightSections(False)
    widgets_operations(self, "widgets_student_view")

    self.ui.Edit_button_View.setGeometry(QRect(810, 500, 91, 31))
    wrap_with_shadow(self.ui.Edit_button_View, 70)

    self.ui.Cancel_button_View.hide()
    self.ui.Save_button_View.hide()

    self.ui.View_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                       "color :rgb(24, 182, 255);\n"
                                       "border: none;\n"
                                       "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                       "}\n"
                                       "")
    self.ui.Add_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                      "font: 700 9pt \"Yu Gothic UI\";")
    refresh_view(self, self.current_user[-1], self.current_password[-1], clear=True) # load students table

def Edit_btn(self):
    """ Makes student table cells editable """

    self.ui.Save_button_View.show()
    self.ui.Cancel_button_View.show()
    self.ui.Cancel_button_View.setGeometry(QRect(860, 500, 91, 31))
    self.ui.Save_button_View.setGeometry(QRect(760, 500, 91, 31))

    self.ui.Edit_button_View.hide()
    unwrap_shadow(self.ui.Edit_button_View)
    wrap_with_shadow(self.ui.Save_button_View, 70)
    wrap_with_shadow(self.ui.Cancel_button_View, 70)

    self.ui.tableWidget.setEditTriggers(QTableWidget.AllEditTriggers)
    self.ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
    for i in range(self.ui.tableWidget.rowCount()):
        for j in range(4, 7):
            item = self.ui.tableWidget.item(i, j)
            if item:
                item.setBackground(QColor("#FFF9C4"))

    for i in range(4):
        self.ui.tableWidget.setItemDelegateForColumn(i, self.delegue)


def Save_btn_(self):
    """ Saves students table edited data """

    new_data = {}
    err = False

    for i in range(self.ui.tableWidget.rowCount()):
        def error(row=i, column=5):
            item = self.ui.tableWidget.item(row, column)
            if item:
                item.setBackground(QColor("#F8D7DA"))

        def reset(row=i, column=5):
            item = self.ui.tableWidget.item(row, column)
            if item:
                item.setBackground(QColor("#FFF9C4"))

        ID = self.ui.tableWidget.item(i, 0).text() if self.ui.tableWidget.item(i, 0) else ""
        fullname = (self.ui.tableWidget.item(i, 1).text() if self.ui.tableWidget.item(i, 0) else "").split(" ")
        date = self.ui.tableWidget.item(i, 2).text() if self.ui.tableWidget.item(i, 0) else ""
        gender = self.ui.tableWidget.item(i, 3).text() if self.ui.tableWidget.item(i, 0) else ""
        adress = self.ui.tableWidget.item(i, 4).text() if self.ui.tableWidget.item(i, 0) else ""
        num = self.ui.tableWidget.item(i, 5).text() if self.ui.tableWidget.item(i, 0) else ""
        email = self.ui.tableWidget.item(i, 6).text() if self.ui.tableWidget.item(i, 0) else ""

        if (num != "" and not num.isdigit()):
            error()

            err = True
        else:

            reset()
        if (email != "" and (not email.endswith(".com") or not re.search("@", email))):
            error(i, 6)

            err = True
        else:
            reset(i, 6)

        if (adress != "" and not re.fullmatch(r"[A-Za-z0-9 ]+", adress)):
            error(i, 4)

            err = True
        else:

            reset(i, 4)

        added = {"firstname": encrypt_data(fullname[0], self.kdf),
                 "lastname": encrypt_data(fullname[1], self.kdf),
                 "gender": encrypt_data(gender, self.kdf),
                 "birth_date": encrypt_data(date, self.kdf),
                 "class": encrypt_data(self.ui.ClassComboBox2.currentText(), self.kdf
                                       ),
                 "email": encrypt_data(email, self.kdf),
                 "number": encrypt_data(num, self.kdf),
                 "address": encrypt_data(adress, self.kdf),
                 }
        new_data[ID] = added
    if err:
        self.ui.errlbl.show()
        return
    else:
        self.ui.errlbl.hide()

    for i, j in new_data.items():
        add_student(self.current_user[-1],
                    j["firstname"],
                    j["lastname"],
                    i,
                    j["birth_date"],
                    j["class"],
                    j["gender"],
                    j["number"],
                    j["email"],
                    j["address"])
    self.ui.Edit_button_View.show()
    self.ui.Edit_button_View.setGeometry(QRect(810, 500, 91, 31))

    wrap_with_shadow(self.ui.Edit_button_View, 70)
    unwrap_shadow(self.ui.Save_button_View)
    unwrap_shadow(self.ui.Cancel_button_View)
    self.ui.Save_button_View.hide()
    self.ui.Cancel_button_View.hide()
    refresh_view(self, self.current_user[-1], self.current_password[-1], clear=True)
    self.ui.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
    self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)


def Canceled(self):
    """ Cancels editing students table operation """

    self.ui.Edit_button_View.show()
    self.ui.Edit_button_View.setGeometry(QRect(810, 500, 91, 31))

    wrap_with_shadow(self.ui.Edit_button_View, 70)
    unwrap_shadow(self.ui.Save_button_View)
    unwrap_shadow(self.ui.Cancel_button_View)
    self.ui.Save_button_View.hide()
    self.ui.Cancel_button_View.hide()
    self.ui.errlbl.hide()

    refresh_view(self, self.current_user[-1], self.current_password[-1], clear=True)
    self.ui.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
    self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

def add_btn_clicked(self):
    """ Adds a new student's encrypted information to database """

    err = False

    first_name = self.ui.Firstnameline.text()
    last_name = self.ui.lastnameline.text()
    gender = self.ui.GenderComboBox.currentText()
    date = self.ui.dateEdit_add_student.date()
    date_str = date.toString("yyyy-MM-dd")
    classe = self.ui.ClassComboBox.currentText()
    email = self.ui.Emailine.text()
    number = self.ui.Numberline.text()
    address = self.ui.AdressLine.text()

    if date > QDate.currentDate():
        err = True
        self.ui.birtherr.show()
        self.ui.dateEdit_add_student.setStyleSheet((u"QDateEdit {\n"
                                        "    border-radius: 12px;\n"
                                        "    padding: 8px 12px;\n"
                                        "    background-color: rgba(255, 255, 255, 220);\n"
                                        "    border: 2px solid red;\n"
                                        "    color: #003366;\n"
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
                                        "}"
                                        ))
    else:
        self.ui.birtherr.hide()
        self.ui.dateEdit_add_student.setStyleSheet(u"QDateEdit {border-radius: 15px;\n"
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

    if first_name == "":
        self.ui.requirederrfirst.setText("This field is required")
        self.ui.requirederrfirst.show()
        update_line2(self.ui.Firstnameline)
        err = True
    elif not re.fullmatch(r"[A-Za-zéêàâîôûçè ]+", first_name):
        self.ui.requirederrfirst.setText("Invalid First Name")
        self.ui.requirederrfirst.show()
        update_line2(self.ui.Firstnameline)
        err = True
    else:
        self.ui.requirederrfirst.hide()
        reset_line2(self.ui.Firstnameline)

    if last_name == "":
        self.ui.requirederrlast.setText("This field is required")
        self.ui.requirederrlast.show()
        update_line2(self.ui.lastnameline)
        err = True
    elif not re.fullmatch(r"[A-Za-zéêàâîôûçè ]+", last_name):
        self.ui.requirederrlast.setText("Invalid Last Name")
        self.ui.requirederrlast.show()
        update_line2(self.ui.lastnameline)
        err = True
    else:
        self.ui.requirederrlast.hide()
        reset_line2(self.ui.lastnameline)

    if email != "":
        if not email.endswith(".com") or not re.search("@", email):
            self.ui.requirederrfirst_2.show()
            update_line2(self.ui.Emailine)
            err = True

        else:
            self.ui.requirederrfirst_2.hide()
            reset_line2(self.ui.Emailine)


    else:
        self.ui.requirederrfirst_2.hide()
        reset_line2(self.ui.Emailine)

    if number != "":
        if number.isdigit() and 7 <= len(str(number)) <= 15:
            self.ui.requirederrfirst_3.hide()
            reset_line2(self.ui.Numberline)


        else:
            self.ui.requirederrfirst_3.show()
            update_line2(self.ui.Numberline)
            err = True

    else:
        self.ui.requirederrfirst_3.hide()
        reset_line2(self.ui.Numberline)

    if classe == "":
        self.ui.errclasse.show()
        self.ui.ClassComboBox.setStyleSheet(u"QComboBox { border : 2px solid red ;\n"
                                            "border-radius : 15px ;\n"
                                            "padding : 5px 7px;  \n"
                                            "background-color: rgb(255,255,255)\n"
                                            "}\n"
                                            "QComboBox:drop-down { width: 0;\n"
                                            "}\n"
                                            )
        err = True
    else:
        self.ui.errclasse.hide()
        self.ui.ClassComboBox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
    c.execute("SELECT * FROM classes WHERE user=? AND class_name=?", (self.current_user[-1], classe))
    rows_classes = c.fetchone()

    if int(rows_classes[3]) == int(rows_classes[2]):
        err = True
        self.ui.errclasse.setText("This Class is full")
        self.ui.errclasse.show()
        self.ui.ClassComboBox.setStyleSheet(u"QComboBox { border : 2px solid red ;\n"
                                            "border-radius : 15px ;\n"
                                            "padding : 5px 7px;  \n"
                                            "background-color: rgb(255,255,255)\n"
                                            "}\n"
                                            "QComboBox:drop-down { width: 0;\n"
                                            "}\n"
                                            )
    else:
        self.ui.errclasse.setText("There are no classes yet")
        self.ui.errclasse.hide()
        self.ui.ClassComboBox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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

    if err:
        return
    c.execute("SELECT * FROM students WHERE user=?", (self.current_user[-1],))
    rows_students = c.fetchall()
    student_id = random.randint(10000000, 99999999)
    for i in rows_students:
        if i[0] == student_id:
            student_id = random.randint(10000000, 99999999)
    c.execute("SELECT * FROM subjects WHERE user=?", (self.current_user[-1],))
    rows_subjects = c.fetchall()

    if rows_subjects != []:

        for i in rows_subjects:
            add_grade(self.current_user[-1], student_id, i[1], 0)

    add_student(
        self.current_user[-1],
        encrypt_data(first_name, self.kdf),
        encrypt_data(last_name, self.kdf),
        student_id,
        encrypt_data(date_str, self.kdf),
        encrypt_data(classe, self.kdf),
        encrypt_data(gender, self.kdf),
        encrypt_data(number, self.kdf),
        encrypt_data(email, self.kdf),
        encrypt_data(address, self.kdf)
    )
    c.execute("SELECT * FROM classes WHERE user=?", (self.current_user[-1],))
    rows_classes2 = c.fetchall()
    for i in rows_classes2:
        if i[1] == classe:
            maxs = i[2]
            tot = i[3]
    add_class(self.current_user[-1], classe, maxs, tot + 1)

    refresh_add(self, self.current_user[-1], self.current_password[-1])

    for i in self.widgets :
        i.clear() if "widgets_to_clear" in self.widgets[i] else None


def cancel_clicked(self):
    """ Cancels adding student operation """

    for i in self.widgets :
        if "widgets_to_clear" in self.widgets[i] :
           i.clear()
           reset_line2(i)
        elif "error_labels" in self.widgets[i]:
            i.hide()
    self.ui.ClassComboBox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
    self.ui.dateEdit_add_student.setStyleSheet(u"QDateEdit {border-radius: 15px;\n"
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


# ============================================================
# Grades Buttons
# ============================================================


def Subjects(self):
    """ Displays subjects page """

    self.ui.info.hide()
    self.ui.Edit_button_Grades.hide()

    self.ui.Edit_button_Subject.show()
    self.ui.Edit_button_Subject.setGeometry(QRect(810, 500, 91, 31))
    wrap_with_shadow(self.ui.Edit_button_Subject, 70)
    self.ui.tableWidget_subjects.show()
    self.ui.tableWidget_grades.hide()
    self.ui.add_button_subject.show()
    self.ui.cancel_button_subject.show()
    self.ui.requirederrsubject.hide()
    self.ui.requirederrcoeff.hide()
    self.ui.class3.hide()
    self.ui.subjectline.show()
    self.ui.coeffline.show()
    self.ui.birtherr.hide()
    self.ui.subject_name.show()
    self.ui.coeff.show()
    self.ui.ClassComboBox3.hide()
    unwrap_shadow(self.ui.tableWidget_grades)
    wrap_with_shadow(self.ui.tableWidget_subjects, 70)
    self.ui.Subject_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                          "color :rgb(24, 182, 255);\n"
                                          "border: none;\n"
                                          "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                          "}\n"
                                          "")
    self.ui.grades_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                         "font: 700 9pt \"Yu Gothic UI\";")
    self.ui.subjectline.clear()
    self.ui.coeffline.clear()
    self.ui.Save_button_Grades.hide()
    self.ui.Cancel_button_Grades.hide()
    refresh_subject(self, self.current_user[-1])

    self.ui.tableWidget_subjects.setFocusPolicy(Qt.NoFocus)
    self.ui.tableWidget_subjects.setSelectionMode(QAbstractItemView.NoSelection)
    self.ui.tableWidget_subjects.setEditTriggers(QTableWidget.NoEditTriggers)


def Grades_top(self):
    """ Navigates to grades section """

    self.ui.info.show()
    self.ui.Edit_button_Grades.show()
    self.ui.Edit_button_Grades.setGeometry(
        QRect(810, 500, 91, 31))
    wrap_with_shadow(self.ui.Edit_button_Grades, 70)
    unwrap_shadow(self.ui.Cancel_button_Grades)
    unwrap_shadow(self.ui.Save_button_Grades)
    self.ui.Cancel_button_Grades.hide()

    self.ui.Save_button_Grades.hide()
    self.ui.errlbl3.hide()
    reset_line2(self.ui.subjectline)
    reset_line2(self.ui.coeffline)
    self.ui.tableWidget_subjects.hide()
    self.ui.tableWidget_grades.show()
    self.ui.add_button_subject.hide()
    self.ui.requirederrsubject.hide()
    self.ui.birtherr.hide()
    self.ui.requirederrcoeff.hide()
    self.ui.cancel_button_subject.hide()
    self.ui.class3.show()
    self.ui.ClassComboBox3.show()
    self.ui.requirederrcoeff.hide()
    self.ui.requirederrsubject.hide()
    self.ui.add_button_subject.hide()
    self.ui.cancel_button_subject.hide()
    self.ui.subjectline.hide()
    self.ui.coeffline.hide()
    self.ui.subject_name.hide()
    self.ui.coeff.hide()
    self.ui.Cancel_button_Subject.hide()
    self.ui.Save_button_Subject.hide()
    self.ui.Edit_button_Subject.hide()
    wrap_with_shadow(self.ui.tableWidget_grades, 70)
    unwrap_shadow(self.ui.Edit_button_Subject)
    unwrap_shadow(self.ui.tableWidget_subjects)
    self.ui.grades_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                         "color :rgb(24, 182, 255);\n"
                                         "border: none;\n"
                                         "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                         "}\n"
                                         "")
    self.ui.Subject_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                          "font: 700 9pt \"Yu Gothic UI\";")
    refresh_grades(self, self.current_user[-1], self.current_password[-1], clear=True)


def add_subject_btn(self):
    """ Adds a new subject to SQLite database """

    err = False
    subject = self.ui.subjectline.text()
    coeff = self.ui.coeffline.text()
    if coeff == "" or not coeff.isdigit():
        self.ui.requirederrcoeff.show()
        update_line2(self.ui.coeffline)
        err = True
    else:
        self.ui.requirederrcoeff.hide()
        reset_line2(self.ui.coeffline)
    if subject == "" or not re.fullmatch(r"^[a-zA-Z0-9 ]+$", subject):
        self.ui.requirederrsubject.show()
        update_line2(self.ui.subjectline)
        err = True
    else:
        self.ui.requirederrsubject.hide()
        reset_line2(self.ui.subjectline)

    if err:
        return

    c.execute("SELECT * FROM students WHERE user = ?", (self.current_user[-1],))
    students_rows = c.fetchall()

    for i in students_rows:
        add_grade(self.current_user[-1], i[0], subject, 0)

    add_subject(self.current_user[-1], subject, coeff)

    refresh_subject(self, self.current_user[-1])
    for i in [self.ui.subjectline, self.ui.coeffline]:
        i.clear()
        reset_line2(i)
    self.ui.requirederrcoeff.hide()
    self.ui.requirederrsubject.hide()


def cancelsub(self):
    """ Cancels add subject operation """

    for i in [self.ui.subjectline, self.ui.coeffline]:
        i.clear()
        reset_line2(i)
    self.ui.requirederrcoeff.hide()
    self.ui.requirederrsubject.hide()


def Edit_btn3(self):
    """ Makes subjects table editable """

    self.ui.Save_button_Subject.show()
    self.ui.Cancel_button_Subject.show()
    self.ui.Save_button_Subject.setGeometry(QRect(760, 500, 91, 31))
    self.ui.Cancel_button_Subject.setGeometry(QRect(860, 500, 91, 31))

    self.ui.Edit_button_Subject.hide()
    unwrap_shadow(self.ui.Edit_button_Subject)
    wrap_with_shadow(self.ui.Save_button_Subject, 70)
    wrap_with_shadow(self.ui.Cancel_button_Subject, 70)

    self.ui.tableWidget_subjects.setEditTriggers(QTableWidget.AllEditTriggers)
    self.ui.tableWidget_subjects.setSelectionMode(QAbstractItemView.SingleSelection)

    for i in range(self.ui.tableWidget_subjects.rowCount()):
        item = self.ui.tableWidget_subjects.item(i, 1)
        if item:
            item.setBackground(QColor("#FFF9C4"))

    for i in range(1):
        self.ui.tableWidget_subjects.setItemDelegateForColumn(i, self.delegue)


def Canceled3(self):
    """ Cancels editing subject operation """

    self.ui.Edit_button_Subject.show()
    self.ui.Edit_button_Subject.setGeometry(QRect(810, 500, 91, 31))
    wrap_with_shadow(self.ui.Edit_button_Subject, 70)
    unwrap_shadow(self.ui.Save_button_Subject)
    unwrap_shadow(self.ui.Cancel_button_Subject)
    self.ui.Save_button_Subject.hide()
    self.ui.Cancel_button_Subject.hide()
    self.ui.errlbl3.hide()

    refresh_subject(self, self.current_user[-1])
    self.ui.tableWidget_subjects.setSelectionMode(QAbstractItemView.NoSelection)
    self.ui.tableWidget_subjects.setEditTriggers(QTableWidget.NoEditTriggers)


def Save_btn_3(self):
    """ Saves subjects edited information """

    err = False
    new_data = {"Subjects": {}}
    for i in range(self.ui.tableWidget_subjects.rowCount()):
        subject = self.ui.tableWidget_subjects.item(i, 0).text()
        coeff = self.ui.tableWidget_subjects.item(i, 1).text()
        if coeff == "" or not coeff.isdigit():
            err = True
            item = self.ui.tableWidget_subjects.item(i, 1)
            if item:
                item.setBackground(QColor("#F8D7DA"))
        else:
            item = self.ui.tableWidget_subjects.item(i, 1)
            if item:
                item.setBackground(QColor("#FFF9C4"))

        new_data["Subjects"][subject] = {"subject": subject, "coeff": coeff}

    if err:
        self.ui.errlbl3.show()
        return
    for i, j in new_data["Subjects"].items():
        add_subject(self.current_user[-1], i, j["coeff"])

    self.ui.errlbl3.hide()

    self.ui.Edit_button_Subject.show()
    self.ui.Edit_button_Subject.setGeometry(QRect(810, 500, 91, 31))
    wrap_with_shadow(self.ui.Edit_button_Subject, 70)
    unwrap_shadow(self.ui.Save_button_Subject)
    unwrap_shadow(self.ui.Cancel_button_Subject)
    self.ui.Save_button_Subject.hide()
    self.ui.Cancel_button_Subject.hide()
    refresh_subject(self, self.current_user[-1])
    self.ui.tableWidget_subjects.setSelectionMode(QAbstractItemView.NoSelection)
    self.ui.tableWidget_subjects.setEditTriggers(QTableWidget.NoEditTriggers)


def Edit_btn_4(self):
    """ Makes grades table editable """

    self.ui.Edit_button_Grades.hide()
    unwrap_shadow(self.ui.Edit_button_Grades)
    self.ui.Save_button_Grades.show()
    self.ui.Cancel_button_Grades.show()
    self.ui.Cancel_button_Grades.setGeometry(QRect(860, 500, 91, 31))
    self.ui.Save_button_Grades.setGeometry(QRect(760, 500, 91, 31))
    wrap_with_shadow(self.ui.Save_button_Grades, 70)
    wrap_with_shadow(self.ui.Cancel_button_Grades, 70)

    self.ui.tableWidget_grades.setEditTriggers(QTableWidget.AllEditTriggers)
    self.ui.tableWidget_grades.setSelectionMode(QAbstractItemView.SingleSelection)

    for i in range(self.ui.tableWidget_grades.rowCount()):
        for j in range(2, self.ui.tableWidget_grades.columnCount() - 1):
            item = self.ui.tableWidget_grades.item(i, j)
            if item:
                item.setBackground(QColor("#FFF9C4"))

    for i in range(2):
        self.ui.tableWidget_grades.setItemDelegateForColumn(i, self.delegue)

    self.ui.tableWidget_grades.setItemDelegateForColumn(self.ui.tableWidget_grades.columnCount() - 1, self.delegue)


def Canceled4(self):
    """ Cancels editing grades table operation """

    self.ui.Edit_button_Grades.show()
    self.ui.Edit_button_Grades.setGeometry(QRect(810, 500, 91, 31))
    wrap_with_shadow(self.ui.Edit_button_Grades, 70)
    unwrap_shadow(self.ui.Save_button_Grades)
    unwrap_shadow(self.ui.Cancel_button_Grades)
    self.ui.Save_button_Grades.hide()
    self.ui.Cancel_button_Grades.hide()
    self.ui.errlbl3.hide()

    refresh_grades(self, self.current_user[-1], self.current_password[-1], clear=True)
    self.ui.tableWidget_grades.setSelectionMode(QAbstractItemView.NoSelection)
    self.ui.tableWidget_grades.setEditTriggers(QTableWidget.NoEditTriggers)


def Save_btn_4(self):
    """ Saves edited grades information"""

    data = load_data()
    for i in data:
        if i["username"] == self.current_user[-1]:
            max_score = i["max_score"]

    err = False
    entering_data = {}
    for i in range(self.ui.tableWidget_grades.rowCount()):
        new_grades = {}

        id = self.ui.tableWidget_grades.item(i, 0).text()

        for j in range(2, self.ui.tableWidget_grades.columnCount() - 1):
            grades = []

            subject = self.ui.tableWidget_grades.horizontalHeaderItem(j).text()
            marks = self.ui.tableWidget_grades.item(i, j).text().strip()
            marks2 = marks.replace(",", ".")

            if marks2 == "":
                err = True
                item = self.ui.tableWidget_grades.item(i, j)
                item.setBackground(QColor("#F8D7DA"))
            else:
                item = self.ui.tableWidget_grades.item(i, j)
                item.setBackground(QColor("#FFF9C4"))

            try:
                grades = [float(x) for x in marks2.split(" ")]
                item = self.ui.tableWidget_grades.item(i, j)
                item.setBackground(QColor("#FFF9C4"))
            except ValueError:
                err = True
                item = self.ui.tableWidget_grades.item(i, j)
                item.setBackground(QColor("#F8D7DA"))

            if round(sum(grades) / len(grades), 2) > int(max_score):
                err = True
                item = self.ui.tableWidget_grades.item(i, j)
                item.setBackground(QColor("#F8D7DA"))
            else:
                item = self.ui.tableWidget_grades.item(i, j)
                item.setBackground(QColor("#FFF9C4"))

            new_grades[subject] = round(sum(grades) / len(grades), 2)

        entering_data.update({id: new_grades})

    if err:
        return

    for i, j in entering_data.items():
        for x, y in j.items():
            add_grade(self.current_user[-1], i, x, y)

    refresh_grades(self, self.current_user[-1], self.current_password[-1], clear=True)

    self.ui.Save_button_Grades.hide()
    unwrap_shadow(self.ui.Save_button_Grades)
    self.ui.Cancel_button_Grades.hide()
    unwrap_shadow(self.ui.Cancel_button_Grades)
    self.ui.Edit_button_Grades.show()
    self.ui.Edit_button_Grades.setGeometry(QRect(810, 500, 91, 31))
    wrap_with_shadow(self.ui.Edit_button_Grades, 70)
    self.ui.tableWidget_grades.setSelectionMode(QAbstractItemView.NoSelection)
    self.ui.tableWidget_grades.setEditTriggers(QTableWidget.NoEditTriggers)



# ============================================================
# Statistics Buttons
# ============================================================

def performance(self):
    """ Displays students performance graphs """

    self.ui.info.hide()
    widgets_operations(self, "widgets_statistics")

    self.ui.Add_top_btn.hide()
    self.ui.View_top_btn.hide()
    self.ui.performance.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                     "color :rgb(24, 182, 255);\n"
                                     "border: none;\n"
                                     "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                     "}\n"
                                     "")
    self.ui.ranking.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                  "font: 700 9pt \"Yu Gothic UI\";")
    self.ui.attendancetop.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                        "font: 700 9pt \"Yu Gothic UI\";")
    self.ui.other.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                "font: 700 9pt \"Yu Gothic UI\";")
    refresh_graph1(self, self.current_user[-1], self.current_password[-1])
    refresh_graph2(self, self.current_user[-1], self.current_password[-1])
    animate_page(self, self.ui.Graph_frame, 1, 0, "white", 15, 351, 321)
    animate_page(self, self.ui.Graph_frame_2, 1, 0, "white", 15, 351, 321)

def attendance_top(self):
    """ Displays attendance graphs """

    self.ui.attendancetop.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                        "color :rgb(24, 182, 255);\n"
                                        "border: none;\n"
                                        "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                        "}\n"
                                        "")
    self.ui.ranking.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                  "font: 700 9pt \"Yu Gothic UI\";")
    self.ui.performance.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                     "font: 700 9pt \"Yu Gothic UI\";")
    self.ui.other.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                "font: 700 9pt \"Yu Gothic UI\";")
    self.ui.info.hide()
    widgets_operations(self, "widgets_statistics_4")

    refresh_graph3(self, self.current_user[-1], self.current_password[-1])
    refresh_graph4(self, self.current_user[-1], self.current_password[-1])
    animate_page(self, self.ui.Graph_frame_7, 1, 0, "white", 15, 561, 331)
    animate_page(self, self.ui.Graph_frame_8, 1, 0, "white", 15, 191, 181)

def ranking(self):
    """ Displays ranking leaderboards """

    self.ui.info.hide()
    widgets_operations(self, "widgets_statistics3")

    self.ui.ranking.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                  "color :rgb(24, 182, 255);\n"
                                  "border: none;\n"
                                  "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                  "}\n"
                                  "")
    self.ui.performance.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                     "font: 700 9pt \"Yu Gothic UI\";")
    self.ui.attendancetop.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                        "font: 700 9pt \"Yu Gothic UI\";")
    self.ui.other.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                "font: 700 9pt \"Yu Gothic UI\";")

    refresh_graph5(self, self.current_user[-1], self.current_password[-1])
    refresh_graph6(self, self.current_user[-1], self.current_password[-1])
    animate_page(self, self.ui.Graph_frame_5, 1, 0, "white", 45, 351, 341)
    animate_page(self, self.ui.Graph_frame_6, 1, 0, "white", 45, 351, 341)


def other(self):
    """ Displays gender distribution and students per class graphs """

    self.ui.info.hide()
    widgets_operations(self, "widgets_statistics_2")


    self.ui.other.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                "color :rgb(24, 182, 255);\n"
                                "border: none;\n"
                                "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                "}\n"
                                "")
    self.ui.performance.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                     "font: 700 9pt \"Yu Gothic UI\";")
    self.ui.attendancetop.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                        "font: 700 9pt \"Yu Gothic UI\";")
    self.ui.ranking.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                  "font: 700 9pt \"Yu Gothic UI\";")

    refresh_graph7(self, self.current_user[-1], self.current_password[-1])
    refresh_graph8(self, self.current_user[-1], self.current_password[-1])
    animate_page(self, self.ui.Graph_frame_3, 1, 0, "white", 15, 351, 321)
    animate_page(self, self.ui.Graph_frame_4, 1, 0, "white", 15, 351, 321)



# ============================================================
# Settings Buttons
# ============================================================

def edit_page(self):
    """ Navigates to settings/edit page """

    self.ui.to_combobox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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

    self.ui.info.hide()
    widgets_operations(self, "widgets_edit")

    self.ui.Add_top_btn.hide()
    self.ui.View_top_btn.hide()
    data = load_data()
    for i in data:
        if i["username"] == self.current_user[-1] and int(i["max_score"]) == 20:
            self.ui.info2.hide()
    wrap_with_shadow(self.ui.transfer_btn, 70)
    wrap_with_shadow(self.ui.set_btn, 70)

    c.execute("SELECT class_name FROM classes WHERE user = ?", (self.current_user[-1],))
    class_rows = c.fetchall()
    classes = [x[0] for x in class_rows]
    reset_line2(self.ui.score_line)

    for i, j in enumerate(classes):
        if self.ui.to_combobox.findText(j) == -1:
            self.ui.to_combobox.insertItem(i, j)
        if self.ui.from_combobox.findText(j) == -1:
            self.ui.from_combobox.insertItem(i, j)
    classe = self.ui.to_combobox.currentText()
    refresh_combo_id(self, self.current_user[-1], classe)


def transfer(self):
    """ Transfers a student from one class to another """

    fro = self.ui.from_combobox.currentText()
    to = self.ui.to_combobox.currentText()
    student = self.ui.id_combobox.currentText()
    c.execute("SELECT Total_students FROM classes WHERE user = ? AND class_name = ?", (self.current_user[-1], fro))
    from_students = c.fetchone()
    c.execute("SELECT Total_students FROM classes WHERE user = ? AND class_name = ?", (self.current_user[-1], to))
    to_students = c.fetchone()
    c.execute("SELECT max_students FROM classes WHERE user = ? AND class_name = ?", (self.current_user[-1], to))
    max_students = c.fetchone()
    if to_students < max_students: # Check if destination class has available spots

        c.execute("UPDATE students SET class =? WHERE user =? AND student_id = ?",
                  (encrypt_data(to, self.kdf), self.current_user[-1], student))
        c.execute("""UPDATE classes SET Total_students=? WHERE user=? AND class_name=?""",
                  (int(to_students[0]) + 1, self.current_user[-1], to))
        conn.commit()
        c.execute("""UPDATE classes SET Total_students=? WHERE user=? AND class_name=?""",
                  (int(from_students[0]) - 1, self.current_user[-1], fro))
        conn.commit()

        refresh_combo_id(self, self.current_user[-1], self.ui.from_combobox.currentText())
        self.ui.to_combobox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
    else :

        self.ui.to_combobox.setStyleSheet(u"QComboBox { border : 2px solid red ;\n"
                                            "border-radius : 15px ;\n"
                                            "padding : 5px 7px;  \n"
                                            "background-color: rgb(255,255,255)\n"
                                            "}\n"
                                            "QComboBox:drop-down { width: 0;\n"
                                            "}\n"
                                            )




def set(self):
    """ Sets maximum score """

    self.ui.info2.hide()
    data = load_data()
    err = False
    c.execute("SELECT grade FROM grades WHERE user =?", (self.current_user[-1],))
    grades = c.fetchall()
    grades2 = [int(x[0]) for x in grades]
    score = self.ui.score_line.text()

    if not re.fullmatch(r"[0-9]+", score):
        self.ui.errscore_lbl.setText("Invalid Score")
        self.ui.errscore_lbl.show()
        update_line2(self.ui.score_line)
        return
    for i in grades2:
        if i > int(score):
            err = True
    if err:
        self.ui.errscore_lbl.setText("Some marks exceed the maximum score you entered.")
        update_line2(self.ui.score_line)
        self.ui.errscore_lbl.show()
        return
    reset_line2(self.ui.score_line)
    self.ui.errscore_lbl.hide()
    for i in data:
        if i["username"] == self.current_user[-1]:
            i.update({"max_score": score})
    self.ui.score_line.setText("")

    save_data(data)
    self.ui.info2.show() if int(score) != 20 else self.ui.info2.hide()
