# ============================================================
# Student Management System
# Main application file
# Author: Ali El Gueloui
# ============================================================


import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QStyledItemDelegate)
from App import Ui_Dialog
from PySide6.QtCore import QPoint, QDate

from PySide6.QtCore import Qt

from Display.Graphs import (refresh_graph3,
                    refresh_graph4,
                    refresh_graph5,
                    refresh_graph6,
                    refresh_graph7)

from Display.Tables import (refresh_attendance,
                    refresh_grades,
                    refresh_view)
from Logic.Utils import (creat_acc_animation,
                   creat_log_animation,
                   toogle,
                         refresh_combo_id)
from Logic.Buttons import (Edit_btn,
                     Save_btn_,
                     Canceled,
                     Edit_btn2,
                     Canceled2,
                     Save_btn_2,
                     creat_clicked,
                     log_clicked,
                     exit_clicked,
                     students_clicked,
                     Add_top_clicked,
                     home_clicked,
                     add_btn_clicked,
                     cancel_clicked,
                     view_top_clicked,
                     classe_clicked,
                     Add_class_clicked,
                     Grades_clicked,
                     Subjects,
                     Grades_top,
                     add_subject_btn,
                     cancelsub,
                     Edit_btn3,
                     Canceled3,
                     Save_btn_3,
                     Edit_btn_4,
                     Canceled4,
                     Save_btn_4,
                     attendance,
                     statistics,
                     attendance_top,
                     performance,
                     ranking,
                     other,
                     edit_page,

                     transfer,
                     set)
import sqlite3

### ------ Database initialization ------
conn = sqlite3.connect('data.db')
c = conn.cursor()
## Stores encrypted student information
c.execute('''CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER,
                    user TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    birth_date TEXT,
                    class TEXT,
                    gender TEXT,
                    address TEXT,
                    email TEXT,
                    Number INTEGER,
                    PRIMARY KEY(student_id, user))''')
## Stores classes and their capacity
c.execute('''CREATE TABLE IF NOT EXISTS classes (
                   user TEXT,
                   class_name TEXT,
                   max_students INTEGER,
                   Total_students INTEGER,
                   PRIMARY KEY(class_name, user)
                   )''')
## Stores subjects created by each user
c.execute('''CREATE TABLE IF NOT EXISTS subjects  (
                   user TEXT,
                   subject_name TEXT,
                   coeff INTEGER,
                   PRIMARY KEY(user, subject_name)
                   )''')
## Stores students grades per subject
c.execute('''CREATE TABLE IF NOT EXISTS grades (
                   user TEXT,
                   student_id INTEGER,
                   subject TEXT,
                   grade INTEGER,
                   PRIMARY KEY (user, student_id, subject)
                   )''')
## Tracks daily students attendance
c.execute('''CREATE TABLE IF NOT EXISTS attendance (
                   user TEXT,
                   student_id INTEGER,
                   date TEXT,
                   status TEXT,
                   PRIMARY KEY (user, student_id, date))''')
conn.commit()

## This delegate makes table cells read-only
class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return None


class Main_app(QMainWindow):
    def __init__(self):
        super().__init__()

        ### ------ UI SETUP ------
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.delegue = ReadOnlyDelegate()
        self.current_user = [] # Active user
        self.current_password = []
        self.animations = []
        self.animations2 = []

        self.setFixedSize(990, 560)
        self.ui.label_errn.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icon_show = QIcon("icons/view_pss.png")
        self.icon_hide = QIcon("icons/hide_pss.png")

        ### ------ Widgets pages map ------
        self.widgets = {self.ui.Firstnameline: ["widgets_to_clear", "widgets_student_add", "widget_student_edit"],
                        self.ui.lastnameline: ["widgets_to_clear", "widgets_student_add"],
                        self.ui.Emailine: ["widgets_to_clear", "widgets_student_add"],
                        self.ui.AdressLine: ["widgets_to_clear", "widgets_student_add"],
                        self.ui.Numberline: ["widgets_to_clear", "widgets_student_add"],
                        self.ui.Classnameline: ["widgets_to_clear", "widgets_class"],
                        self.ui.maxstudentsline: ["widgets_to_clear", "widgets_class"],
                        self.ui.dateEdit_add_student: ["widgets_student_add", "widget_student_edit"],
                        self.ui.GenderComboBox: ["widgets_student_add", "widget_student_edit"],
                        self.ui.Firstname: ["widgets_student_add", "widget_student_edit"],
                        self.ui.lastname: ["widgets_student_add", "widget_student_edit"],
                        self.ui.birth: ["widgets_student_add", "widget_student_edit"],
                        self.ui.Class1: ["widgets_student_add", "widget_student_edit"],
                        self.ui.Gender: ["widgets_student_add", "widget_student_edit"],
                        self.ui.phone: ["widgets_student_add", "widget_student_edit"],
                        self.ui.Email: ["widgets_student_add", "widget_student_edit"],
                        self.ui.Address: ["widgets_student_add", "widget_student_edit"],
                        self.ui.label_21: ["widgets_student_add", "widget_student_edit"],
                        self.ui.label_22: ["widgets_student_add", "widget_student_edit"],
                        self.ui.ClassComboBox: ["widgets_student_add", "widget_student_edit"],
                        self.ui.label_23: ["widgets_student_add", "widget_student_edit"],
                        self.ui.label_24: ["widgets_student_add", "widget_student_edit"],
                        self.ui.Add_button_Student: ["widgets_student_add"],
                        self.ui.Cancel_button_Student: ["widgets_student_add"],
                        self.ui.requirederrfirst: ["widgets_student_add", "error_labels"],
                        self.ui.requirederrlast:["widgets_student_add", "error_labels"],
                        self.ui.ClassComboBox2: ["widgets_student_view"],
                        self.ui.class2: ["widgets_student_view"],
                        self.ui.requirederrfirst_2: ["widgets_student_add", "widget_student_edit", "error_labels"],
                        self.ui.requirederrfirst_3: ["widgets_student_add", "widget_student_edit", "error_labels"],
                        self.ui.errclasse: ["widgets_student_add", "error_labels"],
                        self.ui.birtherr: ["widgets_student_add", "error_labels"],
                        self.ui.Add_top_btn: ["widgets_student_view","widgets_student_add","widget_student_edit"],
                        self.ui.View_top_btn: ["widgets_student_view","widgets_student_add","widget_student_edit"],
                        self.ui.tableWidget: ["widgets_student_view"],
                        self.ui.Save_button_View: ["widgets_student_view"],
                        self.ui.Cancel_button_View: ["widgets_student_view"],
                        self.ui.Edit_button_View: ["widgets_student_view"],
                        self.ui.errlbl: ["widgets_student_view", "error_labels"],
                        self.ui.label_5: ["widgets_home"],
                        self.ui.label_6: ["widgets_home"],
                        self.ui.welcome_label: ["widgets_home"],
                        self.ui.frame_4: ["widgets_home"],
                        self.ui.frame_5: ["widgets_home"],
                        self.ui.frame_3: ["widgets_home"],
                        self.ui.classname: ["widgets_class"],
                        self.ui.maxstudents: ["widgets_class"],
                        self.ui.tableWidget_class: ["widgets_class"],
                        self.ui.add_button_class: ["widgets_class"],
                        self.ui.cancel_button_class: ["widgets_class"],
                        self.ui.requirederrclass: ["widgets_class", "error_labels"],
                        self.ui.requirederrmax: ["widgets_class", "error_labels"],
                        self.ui.Save_button_class: ["widgets_class"],
                        self.ui.Cancel_edit_button_class: ["widgets_class"],
                        self.ui.Edit_button_class: ["widgets_class"],
                        self.ui.errlbl2: ["widgets_class", "error_labels"],
                        self.ui.tableWidget_grades: ["widgets_grades"],
                        self.ui.ClassComboBox3: ["widgets_grades"],
                        self.ui.class3: ["widgets_grades"],
                        self.ui.grades_top_btn: ["widgets_grades"],
                        self.ui.Subject_top_btn: ["widgets_grades"],
                        self.ui.tableWidget_subjects: ["widgets_grades"],
                        self.ui.add_button_subject: ["widgets_grades"],
                        self.ui.cancel_button_subject: ["widgets_grades"],
                        self.ui.requirederrsubject: ["widgets_grades", "error_labels"],
                        self.ui.requirederrcoeff: ["widgets_grades", "error_labels"],
                        self.ui.subject_name: ["widgets_grades"],
                        self.ui.subjectline: ["widgets_grades"],
                        self.ui.coeff: ["widgets_grades"],
                        self.ui.coeffline: ["widgets_grades"],
                        self.ui.Edit_button_Subject: ["widgets_grades"],
                        self.ui.Save_button_Subject: ["widgets_grades"],
                        self.ui.Cancel_button_Subject: ["widgets_grades"],
                        self.ui.errlbl3: ["widgets_grades", "error_labels"],
                        self.ui.Cancel_button_Grades: ["widgets_grades"],
                        self.ui.Edit_button_Grades: ["widgets_grades"],
                        self.ui.Save_button_Grades: ["widgets_grades"],
                        self.ui.date: ["widget_Attendance"],
                        self.ui.dateEdit2: ["widget_Attendance"],
                        self.ui.class4: ["widget_Attendance"],
                        self.ui.ClassComboBox4: ["widget_Attendance"],
                        self.ui.tableWidget_att: ["widget_Attendance"],
                        self.ui.errscore_lbl: ["error_labels"],
                        self.ui.performance: ["widgets_statistics", "widgets_statistics3", "widgets_statistics_2", "widgets_statistics_4"],
                        self.ui.attendancetop: ["widgets_statistics","widgets_statistics3","widgets_statistics_2","widgets_statistics_4"],
                        self.ui.other: ["widgets_statistics","widgets_statistics3","widgets_statistics_2","widgets_statistics_4"],
                        self.ui.ranking: ["widgets_statistics","widgets_statistics3","widgets_statistics_2","widgets_statistics_4"],
                        self.ui.Graph_frame_2: ["widgets_statistics"],
                        self.ui.Graph_frame: ["widgets_statistics"],
                        self.ui.average_class: ["widgets_statistics"],
                        self.ui.subject_averages: ["widgets_statistics"],
                        self.ui.Graph_frame_5: ["widgets_statistics3"],
                        self.ui.Graph_frame_6: ["widgets_statistics3"],
                        self.ui.comboBox2_1: ["widgets_statistics3"],
                        self.ui.comboBox2_2: ["widgets_statistics3"],
                        self.ui.class2_2: ["widgets_statistics3"],
                        self.ui.class2_1: ["widgets_statistics3"],
                        self.ui.top_students_3: ["widgets_statistics3"],
                        self.ui.top_students: ["widgets_statistics3"],
                        self.ui.Graph_frame_3: ["widgets_statistics_2"],
                        self.ui.Graph_frame_4: ["widgets_statistics_2"],
                        self.ui.comboBox2_3: ["widgets_statistics_2"],
                        self.ui.class2_3: ["widgets_statistics_2"],
                        self.ui.students_per_class: ["widgets_statistics_2"],
                        self.ui.malesfemales: ["widgets_statistics_2"],
                        self.ui.Graph_frame_7: ["widgets_statistics_4"],
                        self.ui.Graph_frame_8: ["widgets_statistics_4"],
                        self.ui.comboBox2_5: ["widgets_statistics_4"],
                        self.ui.dateEdit5: ["widgets_statistics_4"],
                        self.ui.comboBox2_6: ["widgets_statistics_4"],
                        self.ui.comboBox2_7: ["widgets_statistics_4"],
                        self.ui.attendace_title: ["widgets_statistics_4"],
                        self.ui.attendace_title2: ["widgets_statistics_4"],
                        self.ui.year: ["widgets_statistics_4"],
                        self.ui.classe: ["widgets_statistics_4"],
                        self.ui.score_settings_lbl: ["widgets_edit"],
                        self.ui.max_score_lbl: ["widgets_edit"],
                        self.ui.score_line: ["widgets_edit"],
                        self.ui.set_btn: ["widgets_edit"],
                        self.ui.transfe_lbl: ["widgets_edit"],
                        self.ui.transfer_btn: ["widgets_edit"],
                        self.ui.from_lbl: ["widgets_edit"],
                        self.ui.from_combobox: ["widgets_edit"],
                        self.ui.to_lbl: ["widgets_edit"],
                        self.ui.to_combobox: ["widgets_edit"],
                        self.ui.id_lbl2: ["widgets_edit"],
                        self.ui.id_combobox: ["widgets_edit"],
                        self.ui.info2: ["widgets_edit"],

        }

        ## Helpful Lists in animations
        self.widgets_acc = [{"widget": self.ui.frame_n, "pos_off": QPoint(-490, 50), "pos_on": QPoint(560, 50)},
                            {"widget": self.ui.label_3_n, "pos_off": QPoint(-450, 190), "pos_on": QPoint(600, 190)},
                            {"widget": self.ui.label_4_n, "pos_off": QPoint(-450, 280), "pos_on": QPoint(600, 280)},
                            {"widget": self.ui.label_2_n, "pos_off": QPoint(-410, 90), "pos_on": QPoint(640, 90)},
                            {"widget": self.ui.label_7_n, "pos_off": QPoint(-390, 450), "pos_on": QPoint(660, 450)},
                            {"widget": self.ui.label_5_n, "pos_off": QPoint(-1000, 100), "pos_on": QPoint(20, 100)},
                            {"widget": self.ui.label_6_n, "pos_off": QPoint(-620, 180), "pos_on": QPoint(30, 180)},
                            {"widget": self.ui.label_errn, "pos_on": QPoint(570, 480), "pos_off": QPoint(50, 480)},
                            ]

        self.widgets_log = [{"widget": self.ui.label_8, "pos_on": QPoint(180, 70), "pos_off": QPoint(1180, 70)},
                            {"widget": self.ui.label_9, "pos_on": QPoint(80, 190), "pos_off": QPoint(1080, 190)},
                            {"widget": self.ui.frame_6, "pos_on": QPoint(50, 50), "pos_off": QPoint(1050, 50)},
                            {"widget": self.ui.label_10, "pos_on": QPoint(140, 450), "pos_off": QPoint(1140, 450)},
                            {"widget": self.ui.label_11, "pos_on": QPoint(80, 280), "pos_off": QPoint(1080, 280)},
                            {"widget": self.ui.label_12, "pos_on": QPoint(630, 100), "pos_off": QPoint(1630, 100)},
                            {"widget": self.ui.label_13, "pos_on": QPoint(640, 180), "pos_off": QPoint(1640, 180)}]
        self.lines = [self.ui.lineEdit_n, self.ui.lineEdit_2_n, self.ui.lineEdit_5, self.ui.lineEdit_6]

        ### ------ Inital Widgets state ------
        for i in self.widgets:
            i.hide()

        for i in [self.ui.comboBox2_5, self.ui.comboBox2_6, self.ui.comboBox2_3]:
            i.insertItem(0, "all")
        self.ui.comboBox2_7.insertItem(0, str(QDate.currentDate().year()))

        ### ------ Signal connexions ------
        ## -- Create account page --
        self.ui.pushButton_n.clicked.connect(lambda: creat_clicked(self))
        self.ui.toolButton_2.clicked.connect(lambda: toogle(self, self.ui.lineEdit_2_n, self.ui.toolButton_2))
        self.ui.label_7_n.linkActivated.connect(lambda: creat_acc_animation(self, self.widgets_acc, self.widgets_log))
        ## -- LogIn page --
        self.ui.pushButton_5.clicked.connect(lambda: log_clicked(self))
        self.ui.toolButton.clicked.connect(lambda: toogle(self, self.ui.lineEdit_6, self.ui.toolButton))
        self.ui.label_10.linkActivated.connect(lambda: creat_log_animation(self, self.widgets_log, self.widgets_acc))
        ## -- Home page --
        # Buttons at the top
        self.ui.exit_button.clicked.connect(lambda: exit_clicked(self))
        self.ui.info_button.clicked.connect(lambda: edit_page(self))
        self.ui.settings_button.clicked.connect(lambda: home_clicked(self))
        # Buttons at the left
        self.ui.Students_button.clicked.connect(lambda: students_clicked(self))
        self.ui.Classes_button.clicked.connect(lambda: classe_clicked(self))
        self.ui.Grades_button.clicked.connect(lambda: Grades_clicked(self))
        self.ui.Attendance_button.clicked.connect(lambda: attendance(self))
        self.ui.Statistics_button.clicked.connect(lambda: statistics(self))


        ## -- Classes page --
        self.ui.add_button_class.clicked.connect(lambda: Add_class_clicked(self))
        self.ui.cancel_button_class.clicked.connect(lambda: cancel_clicked(self))
        self.ui.Edit_button_class.clicked.connect(lambda: Edit_btn2(self))
        self.ui.Cancel_edit_button_class.clicked.connect(lambda: Canceled2(self))
        self.ui.Save_button_class.clicked.connect(lambda: Save_btn_2(self))

        ## -- Students page --
        # Buttons at the top
        self.ui.View_top_btn.clicked.connect(lambda: view_top_clicked(self))
        self.ui.Add_top_btn.clicked.connect(lambda: Add_top_clicked(self))
        # Add page
        self.ui.Add_button_Student.clicked.connect(lambda: add_btn_clicked(self))
        self.ui.Cancel_button_Student.clicked.connect(lambda: cancel_clicked(self))
        # View page
        self.ui.ClassComboBox2.currentTextChanged.connect(lambda: refresh_view(self, self.current_user[-1], self.current_password[-1]))
        self.ui.Edit_button_View.clicked.connect(lambda: Edit_btn(self))
        self.ui.Cancel_button_View.clicked.connect(lambda: Canceled(self))
        self.ui.Save_button_View.clicked.connect(lambda: Save_btn_(self))

        ## -- Grades page --
        # Buttons at the top
        self.ui.grades_top_btn.clicked.connect(lambda: Grades_top(self))
        self.ui.Subject_top_btn.clicked.connect(lambda: Subjects(self))
        # Subjects
        self.ui.add_button_subject.clicked.connect(lambda: add_subject_btn(self))
        self.ui.cancel_button_subject.clicked.connect(lambda: cancelsub(self))
        self.ui.Edit_button_Subject.clicked.connect(lambda: Edit_btn3(self))
        self.ui.Cancel_button_Subject.clicked.connect(lambda: Canceled3(self))
        self.ui.Save_button_Subject.clicked.connect(lambda: Save_btn_3(self))
        # Grades
        self.ui.ClassComboBox3.currentTextChanged.connect(lambda: refresh_grades(self, self.current_user[-1], self.current_password[-1]))
        self.ui.Edit_button_Grades.clicked.connect(lambda: Edit_btn_4(self))
        self.ui.Cancel_button_Grades.clicked.connect(lambda: Canceled4(self))
        self.ui.Save_button_Grades.clicked.connect(lambda: Save_btn_4(self))

        ## -- Attendance page --
        self.ui.ClassComboBox4.currentTextChanged.connect(lambda: refresh_attendance(self, self.current_user[-1], self.current_password[-1]))
        self.ui.dateEdit2.dateChanged.connect(lambda: refresh_attendance(self, self.current_user[-1], self.current_password[-1], clear=True))

        ## -- Statistics page --
        # Buttons at the top
        self.ui.attendancetop.clicked.connect(lambda: attendance_top(self))
        self.ui.performance.clicked.connect(lambda: performance(self))
        self.ui.ranking.clicked.connect(lambda: ranking(self))
        self.ui.other.clicked.connect(lambda: other(self))
        # Attendance
        self.ui.dateEdit5.dateChanged.connect(lambda: refresh_graph3(self, self.current_user[-1], self.current_password[-1]))
        self.ui.comboBox2_5.currentTextChanged.connect(lambda: refresh_graph3(self, self.current_user[-1], self.current_password[-1]))
        self.ui.comboBox2_6.currentTextChanged.connect(lambda: refresh_graph4(self, self.current_user[-1], self.current_password[-1]))
        self.ui.comboBox2_7.currentTextChanged.connect(lambda: refresh_graph4(self, self.current_user[-1], self.current_password[-1]))
        # Students ranking
        self.ui.comboBox2_2.currentTextChanged.connect(lambda: refresh_graph5(self, self.current_user[-1], self.current_password[-1]))
        self.ui.comboBox2_1.currentTextChanged.connect(lambda: refresh_graph6(self, self.current_user[-1], self.current_password[-1]))
        # Other
        self.ui.comboBox2_3.currentTextChanged.connect(lambda: refresh_graph7(self, self.current_user[-1], self.current_password[-1]))

        ## -- Settings page --
        self.ui.from_combobox.currentTextChanged.connect(lambda: refresh_combo_id(self, self.current_user[-1], self.ui.from_combobox.currentText()))
        self.ui.transfer_btn.clicked.connect(lambda: transfer(self))
        self.ui.set_btn.clicked.connect(lambda: set(self))

        ##---------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_app()
    window.show()
    sys.exit(app.exec())