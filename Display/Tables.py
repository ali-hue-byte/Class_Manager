# ============================================================
# Tables display
# Handles all data placement in tables
# ============================================================

from functools import partial

from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import (QFrame,
                               QTableWidgetItem,
                               QPushButton, QWidget)

from PySide6.QtCore import QRect, QSize
from Logic.Functions import (load_data,
                       decrypt_data,
                       add_class,
                       mark_attendance,
                       select_class,
                       delete_student,
                       delete_class,
                       delete_subject_,
                       wrap_with_shadow2,
                       wrap_with_shadow,
                       unwrap_shadow)

from Logic.Utils import InfoButton
                   

from PySide6.QtCore import Qt

import sqlite3


conn = sqlite3.connect('data.db')
c = conn.cursor()

def refresh_attendance(self, user, password, clear=False):
    """ Loads the attendance table for marking student presence and absence """
    # Data
    c.execute("SELECT class_name FROM classes WHERE user = ? ", (user,))
    classes = c.fetchall()

    c.execute("SELECT * FROM students WHERE user = ?", (user,))
    students = c.fetchall()

    desired_class = self.ui.ClassComboBox4.currentText() # Current class
    # Refill ComboBox safely to avoid duplicates
    if clear:
       self.ui.ClassComboBox4.clear()
    for i, x in enumerate(classes):
        if self.ui.ClassComboBox4.findText(x[0]) == -1:
            self.ui.ClassComboBox4.insertItem(i, x[0])

    self.ui.ClassComboBox4.setCurrentText(desired_class)
    current_class = self.ui.ClassComboBox4.currentText()
    unwrap_shadow(self.ui.tableWidget_att)
    self.ui.tableWidget_att.setRowCount(0)
    x = 860
    y = 170
    h = 20
    w = 60
    for i in students:

        date = self.ui.dateEdit2.date().toString("yyyy-MM-dd") # Desired date
        c.execute("SELECT status FROM attendance WHERE user = ? AND student_id = ? AND date = ?",
                  (user, i[0], date))
        attendance = c.fetchone() # Attendance data for student i
        status = attendance[0] if attendance else "not assigned" # Attendance status

        # Functions for table buttons
        def presentt(id=i[0]):
            mark_attendance(user, id, date, "present")

            refresh_attendance(self, user, password)

        def absentt(id=i[0]):
            mark_attendance(user, id, date, "absent")

            refresh_attendance(self, user, password)

        def excusedt(id=i[0]):
            mark_attendance(user, id, date, "excused")

            refresh_attendance(self, user, password)

        if decrypt_data(i[5], self.kdf) != current_class: # skips other classes
            continue

        # Loads data to the table
        row = self.ui.tableWidget_att.rowCount()
        self.ui.tableWidget_att.insertRow(row)
        self.ui.tableWidget_att.setItem(row, 0, QTableWidgetItem(str(i[0])))
        self.ui.tableWidget_att.setItem(row, 1, QTableWidgetItem(
            decrypt_data(i[2], self.kdf) + " " + decrypt_data(i[3], self.kdf)))

        frame = QFrame()
        frame.setGeometry(QRect(0, 0, 200, 40))

        # Icons
        iconpre = QIcon()
        iconpre.addFile(u"icons/present.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        iconabs = QIcon()
        iconabs.addFile(u"icons/absent.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        iconex = QIcon()
        iconex.addFile(u"icons/excused.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        # Buttons
        absent = InfoButton(frame, self.ui.page, "Absent", QRect(x, y, w, h))
        absent.setGeometry(QRect(130, 2, 50, 36))
        absent.setIcon(iconabs)
        present = InfoButton(frame, self.ui.page, "Present", QRect(x - 120, y, w, h))
        present.setGeometry(QRect(10, 2, 50, 36))
        present.setIcon(iconpre)
        excused = InfoButton(frame, self.ui.page, "Excused", QRect(x - 60, y, w, h))
        excused.setGeometry(QRect(70, 2, 50, 36))
        excused.setIcon(iconex)
        y += 40
        for widget in [absent, present, excused]:
            widget.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);\n"
                                 "border-radius: 5px;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color: #F0F0F0;\n"
                                 "}")
        if status == "present":
            present.setStyleSheet("QPushButton{background-color: #90EE90;\n"
                                  "border-radius: 5px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color: #4CBB17;\n"
                                  "}")
        else:
            present.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);\n"
                                  "border-radius: 5px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color: #F0F0F0;\n"
                                  "}")
        if status == "absent":
            absent.setStyleSheet("QPushButton{background-color: #E53935;\n"
                                 "border-radius: 5px;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color: #C62828;\n"
                                 "}")
        else:
            absent.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);\n"
                                 "border-radius: 5px;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color: #F0F0F0;\n"
                                 "}")
        if status == "excused":
            excused.setStyleSheet("QPushButton{background-color: #FFEA00;\n"
                                  "border-radius: 5px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color: #E1C16E;\n"
                                  "}")
        else:
            excused.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);\n"
                                  "border-radius: 5px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color: #F0F0F0;\n"
                                  "}")
        # Connects buttons for each student
        absent.clicked.connect(partial(absentt))
        present.clicked.connect(partial(presentt))
        excused.clicked.connect(partial(excusedt))

        self.ui.tableWidget_att.setCellWidget(row, 2, frame)

    # Center-align all cell contents
    for row in range(self.ui.tableWidget_att.rowCount()):
        for col in range(self.ui.tableWidget_att.columnCount()):
            item = self.ui.tableWidget_att.item(row, col)
            if item is None:
                item = QTableWidgetItem("")
                self.ui.tableWidget_att.setItem(row, col, item)
            item.setTextAlignment(Qt.AlignCenter)

    wrap_with_shadow2(self.ui.tableWidget_att, 70)


def refresh_grades(self, user, password, clear = False):
    """ Loads students grades per subject in a table """

    data = load_data()
    max_score = 0
    for i in data:
        if i["username"] == user:
            max_score = i["max_score"]
    unwrap_shadow(self.ui.tableWidget_grades)
    # Data
    current_class1 = self.ui.ClassComboBox3.currentText()
    c.execute("SELECT class_name FROM classes WHERE user = ?", (user,))
    classes = c.fetchall()

    c.execute("SELECT subject_name FROM subjects WHERE user = ?", (user,))
    subjects = c.fetchall()
    c.execute("SELECT * FROM students WHERE user = ?", (user,))
    students = c.fetchall()

    # Refill ComboBox safely to avoid duplicates
    if clear :
       self.ui.ClassComboBox3.clear()
    for i, x in enumerate(classes):
        if self.ui.ClassComboBox3.findText(x[0]) == -1:
            self.ui.ClassComboBox3.insertItem(i, x[0])
    self.ui.ClassComboBox3.setCurrentText(current_class1)
    current_class = self.ui.ClassComboBox3.currentText()

    self.ui.tableWidget_grades.setRowCount(0)


    self.ui.tableWidget_grades.setColumnCount(len(subjects) + 3)
    # Fill table headers with subjects and "average" label
    for j, i in enumerate(subjects, start=2):
        self.ui.tableWidget_grades.setHorizontalHeaderItem(j, QTableWidgetItem(i[0]))

    self.ui.tableWidget_grades.setHorizontalHeaderItem(self.ui.tableWidget_grades.columnCount() - 1, QTableWidgetItem("Average"))

    for i in students:
        if decrypt_data(i[5], self.kdf) != current_class: # skips other classes
            continue

        grades = []

        row = self.ui.tableWidget_grades.rowCount()
        self.ui.tableWidget_grades.insertRow(row)

        self.ui.tableWidget_grades.setItem(row, 0, QTableWidgetItem(str(i[0])))
        self.ui.tableWidget_grades.setItem(row, 1, QTableWidgetItem(
            decrypt_data(i[2], self.kdf) + " " + decrypt_data(i[3], self.kdf)))
        for ix in range(2, self.ui.tableWidget_grades.columnCount()):
            subject = self.ui.tableWidget_grades.horizontalHeaderItem(ix).text()
            c.execute("SELECT grade FROM grades WHERE user = ? AND student_id = ? AND subject=?", (user, i[0], subject))
            showed_grades = c.fetchone()
            c.execute("SELECT coeff FROM subjects WHERE user =? AND subject_name =?", (user, subject))
            rows = c.fetchone()
            coeff = rows[0] if rows else 0
            if showed_grades is None:
                self.ui.tableWidget_grades.setItem(row, ix, QTableWidgetItem(""))
            else:
                self.ui.tableWidget_grades.setItem(row, ix, QTableWidgetItem(str(showed_grades[0])))
                grades.append((int(showed_grades[0]), int(coeff)))

        # Average score per student
        average = []
        total_coeff = 0
        for mark in grades:
            average.append(mark[0] * mark[1])
            total_coeff += mark[1]
        self.ui.tableWidget_grades.setItem(row, self.ui.tableWidget_grades.columnCount() - 1,
                                           QTableWidgetItem(str(round(sum(average) / total_coeff, 2)))) if total_coeff != 0 else QTableWidgetItem("")
        item = self.ui.tableWidget_grades.item(row, self.ui.tableWidget_grades.columnCount() - 1)
        if total_coeff != 0 and sum(average) / total_coeff < (int(max_score) // 2):
            if item:
                item.setBackground(QColor("#FADBD8")) # Failed
        else:
            if item:
                item.setBackground(QColor("#D4EDDA")) # Passed

    # Center-align all cell contents
    for row in range(self.ui.tableWidget_grades.rowCount()):
        for col in range(self.ui.tableWidget_grades.columnCount()):
            item = self.ui.tableWidget_grades.item(row, col)
            if item is None:
                item = QTableWidgetItem("")
                self.ui.tableWidget.setItem(row, col, item)
            item.setTextAlignment(Qt.AlignCenter)

    wrap_with_shadow2(self.ui.tableWidget_grades, 70)



def refresh_subject(self, user):
    """ Populates the subjects table with subject names and coefficients """
    self.ui.tableWidget_subjects.setRowCount(0)

    unwrap_shadow(self.ui.tableWidget_subjects)
    c.execute("SELECT * FROM subjects WHERE user=?", (user,))
    subjects = c.fetchall()

    for i, j in enumerate(subjects):
        def delete_subject(de=j):
            delete_subject_(user, de[1])
            refresh_subject(self,user)

        self.ui.tableWidget_subjects.insertRow(i)
        self.ui.tableWidget_subjects.setItem(i, 0, QTableWidgetItem(j[1]))
        self.ui.tableWidget_subjects.setItem(i, 1, QTableWidgetItem(str(j[2])))
        self.container2 = QWidget()
        self.container2.setGeometry(QRect(0, 0, 200, 40))
        self.delete_btn2 = QPushButton(self.container2)
        icon = QIcon()
        icon.addFile(u"icons/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_btn2.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                       "color : rgb(255,255,255);\n"
                                       "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                       "border-radius: 15px}\n"
                                       "\n"
                                       "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                       "color: rgb(255,255,255)\n"
                                       "}")
        self.delete_btn2.setIcon(icon)
        self.delete_btn2.setGeometry(QRect(65, 2, 60, 30))
        self.delete_btn2.clicked.connect(partial(delete_subject))
        self.ui.tableWidget_subjects.setCellWidget(i, 2, self.container2)

    # Center-align all cell contents
    for row in range(self.ui.tableWidget_subjects.rowCount()):
        for col in range(self.ui.tableWidget_subjects.columnCount()):
            item = self.ui.tableWidget_subjects.item(row, col)
            if item is None:
                item = QTableWidgetItem("")
                self.ui.tableWidget_subjects.setItem(row, col, item)
            item.setTextAlignment(Qt.AlignCenter)

    wrap_with_shadow2(self.ui.tableWidget_subjects, 70)


def refresh_add(self, user, password):
    """ Refills Class ComboBox in Students page """
    c.execute("SELECT class_name FROM classes WHERE user = ?", (user,))
    classes = c.fetchall()
    self.ui.ClassComboBox.clear()
    for i, x in enumerate(classes):
        if self.ui.ClassComboBox.findText(x[0]) == -1:
            self.ui.ClassComboBox.insertItem(i, x[0])


def refresh_view(self, user, password, clear = False):
    """ Populates the students table with decrypted student data """
    current_class1 = self.ui.ClassComboBox2.currentText()

    if clear:
      self.ui.ClassComboBox2.clear()

    unwrap_shadow(self.ui.tableWidget)

    c.execute("SELECT * FROM students WHERE user=?", (user,))
    rows_students = c.fetchall()
    c.execute("SELECT * FROM classes WHERE user=?", (user,))
    rows_class = c.fetchall()

    for i, x in enumerate(rows_class):
        if self.ui.ClassComboBox2.findText(x[1]) == -1:
            self.ui.ClassComboBox2.insertItem(i, x[1])
    self.ui.ClassComboBox2.setCurrentText(current_class1)

    current_class = self.ui.ClassComboBox2.currentText()
    self.ui.tableWidget.setRowCount(0)

    for y in rows_students:
        def delete_btn(student_id=y[0], re=y): # deletes a students using button

            unwrap_shadow(self.ui.tableWidget)
            delete_student(user, student_id)
            classe = select_class(user, decrypt_data(re[5], self.kdf))

            total = classe[3] - 1
            add_class(user, classe[1], classe[2], total)

            refresh_view(self, user, password)
            wrap_with_shadow(self.ui.tableWidget, 70)

        if decrypt_data(y[5], self.kdf) != current_class:
            continue

        # Inserts data to table
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)

        self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(y[0])))
        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(
            decrypt_data(y[2], self.kdf) + " " + decrypt_data(y[3], self.kdf)))
        self.ui.tableWidget.setItem(row, 2,
                                    QTableWidgetItem(decrypt_data(y[4], self.kdf)))
        self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(decrypt_data(y[6], self.kdf)))
        self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(decrypt_data(y[7], self.kdf)))
        self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(decrypt_data(y[9], self.kdf)))
        self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(decrypt_data(y[8], self.kdf)))
        # Container for delete button
        self.container = QWidget()
        self.container.setGeometry(QRect(0, 0, 100, 40))
        self.delete_btn = QPushButton(self.container)
        icon = QIcon()
        icon.addFile(u"icons/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_btn.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                      "color : rgb(255,255,255);\n"
                                      "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                      "border-radius: 15px}\n"
                                      "\n"
                                      "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                      "color: rgb(255,255,255)\n"
                                      "}")
        self.delete_btn.setIcon(icon)
        self.delete_btn.setGeometry(QRect(20, 2, 50, 30))
        self.delete_btn.clicked.connect(partial(delete_btn)) # Connects button for each student
        self.ui.tableWidget.setCellWidget(row, 7, self.container)

        # Center-align all cell contents
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                if item is None:
                    item = QTableWidgetItem("")
                    self.ui.tableWidget.setItem(row, col, item)
                item.setTextAlignment(Qt.AlignCenter)
    wrap_with_shadow2(self.ui.tableWidget, 70)


def refresh_class(self, user, password):
    """ Populates the classes table with class names and student counts """

    self.ui.tableWidget_class.setRowCount(0)

    c.execute("SELECT * FROM classes WHERE user=?", (user,))
    rows_class = c.fetchall()
    c.execute("SELECT * FROM students WHERE user=?", (user,))
    rows_students = c.fetchall()

    for j, x in enumerate(rows_class):
        students_to_delete = []

        def delete_class2(de=x[1]): # deletes a class using button
            unwrap_shadow(self.ui.tableWidget_class)
            delete_class(user, de)
            for d in rows_students:
                if decrypt_data(d[5], self.kdf) == de:
                    students_to_delete.append(d[0])
            for i in students_to_delete:
                delete_student(user, i)

            refresh_class(self, user, password)
            refresh_view(self, user, password)
            wrap_with_shadow2(self.ui.tableWidget_class, 70)

        # Insert classes data to table
        self.ui.tableWidget_class.insertRow(j)

        self.ui.tableWidget_class.setItem(j, 0, QTableWidgetItem(x[1]))

        self.ui.tableWidget_class.setItem(j, 1, QTableWidgetItem(str(x[3])))
        self.ui.tableWidget_class.setItem(j, 2, QTableWidgetItem(str(x[2])))
        self.container_ = QWidget()
        self.container_.setGeometry(QRect(0, 0, 100, 40))
        self.delete_btn_ = QPushButton(self.container_)
        self.delete_btn_.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                       "color : rgb(255,255,255);\n"
                                       "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                       "border-radius: 15px}\n"
                                       "\n"
                                       "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                       "color: rgb(255,255,255)\n"
                                       "}")
        self.delete_btn_.setGeometry(QRect(70, 2, 60, 30))
        icon = QIcon()
        icon.addFile(u"icons/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_btn_.setIcon(icon)
        self.delete_btn_.clicked.connect(partial(delete_class2)) # Connects button for each student
        self.ui.tableWidget_class.setCellWidget(j, 3, self.container_)
    wrap_with_shadow2(self.ui.tableWidget_class, 70)
