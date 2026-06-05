
from PySide6.QtWidgets import (QVBoxLayout, QSizePolicy)

from Functions import (load_data, decrypt_data)

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sqlite3


conn = sqlite3.connect('data.db')
c = conn.cursor()

def refresh_graph1(self, user, password):
    data = load_data()
    for i in data:
        if i["username"] == user:
            max_score = i["max_score"]
    bars = None

    c.execute("SELECT * FROM students WHERE user=?", (user,))
    students = c.fetchall()
    c.execute("SELECT class_name FROM classes WHERE user=?", (user,))
    classes_rows = c.fetchall()

    c.execute("SELECT * from subjects WHERE user=?", (user,))
    subjects = c.fetchall()

    classes = [x[0] for x in classes_rows]
    coeffs = []
    for z in subjects:
        coeffs.append(int(z[2]))
    data_classes = []
    for i in classes:
        class_average = []

        for j in students:
            student_average = []
            if decrypt_data(j[5], self.kdf) != i:
                continue
            c.execute("SELECT * FROM grades WHERE user = ? AND student_id = ?", (user, j[0]))
            grades = c.fetchall()
            for k in grades:
                c.execute("SELECT coeff FROM subjects WHERE user = ? AND subject_name = ?", (user, k[2]))
                coeff = c.fetchone()[0]
                student_average.append(float(k[3]) * int(coeff))
            class_average.append(sum(student_average) / sum(coeffs)) if sum(coeffs) != 0 else None
        data_classes.append(sum(class_average) / len(class_average)) if len(
            class_average) > 0 else data_classes.append(0)
    layout = self.ui.Graph_frame.layout()
    if layout is None:
        layout = QVBoxLayout(self.ui.Graph_frame)
        self.ui.Graph_frame.setLayout(layout)
    else:

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
                widget.deleteLater()
    fig, ax = plt.subplots(figsize=(5, 3))

    if classes == [] or sum(coeffs) == 0:
        ax.text(0.5, 0.5, "No data available", ha="center", va="center", fontsize=12)
    else:

        bars = ax.bar(classes, data_classes)
        ax.set_ylim(0, int(max_score))
        fig.tight_layout()
        fig.subplots_adjust(bottom=0.2, left=0.15)
        for label in ax.get_xticklabels():
            label.set_rotation(90)
        for bar in bars:
            bar.set_facecolor("#2563EB")
            bar.set_edgecolor("#1E40AF")
    canvas = FigureCanvas(fig)
    canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    canvas.updateGeometry()
    canvas.draw()

    layout.addWidget(canvas)
    if bars is not None:
        self.ui.Graph_frame_2.bars = bars
        self.ui.Graph_frame_2.canvas = canvas
        self.ui.Graph_frame_2.ax = ax


def refresh_graph2(self, user, password):
    data = load_data()
    for i in data:
        if i["username"] == user:
            max_score = i["max_score"]
    bars = None
    c.execute("SELECT subject_name FROM subjects WHERE user=?", (user,))
    subjects_rows = c.fetchall()
    subjects = [x[0] for x in subjects_rows]

    c.execute("SELECT * FROM students WHERE user=?", (user,))
    students = c.fetchall()
    average_per_subject = []
    for subject in subjects:
        note = []
        for i in students:
            c.execute("SELECT * FROM grades WHERE user=? AND student_id = ?", (user, i[0]))
            grades = c.fetchall()
            for x in grades:
                if x[2] != subject:
                    continue
                note.append(float(x[3]))
        average_per_subject.append(sum(note) / len(note)) if len(note) > 0 else average_per_subject.append(0)

    layout = self.ui.Graph_frame_2.layout()
    if layout is None:
        layout = QVBoxLayout(self.ui.Graph_frame_2)
        self.ui.Graph_frame_2.setLayout(layout)
    else:

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
                widget.deleteLater()

    fig, ax = plt.subplots(figsize=(5, 3))
    if subjects == []:
        ax.text(0.5, 0.5, "No data available", ha="center", va="center", fontsize=12)
    else:

        bars = ax.bar(subjects, average_per_subject)
        ax.set_ylim(0, int(max_score))
        fig.tight_layout()
        fig.subplots_adjust(bottom=0.2, left=0.15)
        for label in ax.get_xticklabels():
            label.set_rotation(90)
        for bar in bars:
            bar.set_facecolor("#2563EB")
            bar.set_edgecolor("#1E40AF")

    canvas = FigureCanvas(fig)
    canvas.updateGeometry()
    canvas.draw()
    layout.addWidget(canvas)
    if bars is not None:
        self.ui.Graph_frame.bars = bars
        self.ui.Graph_frame.canvas = canvas
        self.ui.Graph_frame.ax = ax


def refresh_graph3(self, user, password):
    c.execute("SELECT class_name FROM classes WHERE user=?", (user,))
    classes_rows = c.fetchall()
    classes = [x[0] for x in classes_rows]

    c.execute("SELECT * FROM students WHERE user=?", (user,))
    students_rows = c.fetchall()

    current_class = self.ui.comboBox2_5.currentText()

    if self.ui.comboBox2_5.findText("all") == -1:
        self.ui.comboBox2_5.insertItem(0, "all")
    for i, x in enumerate(classes, start=1):
        if self.ui.comboBox2_5.findText(x) == -1:
            self.ui.comboBox2_5.insertItem(i, x)
    self.ui.comboBox2_5.setCurrentText(current_class)
    classe = self.ui.comboBox2_5.currentText()
    date = self.ui.dateEdit5.date()

    students = 0
    present = 0
    absent = 0
    excused = 0

    for i in students_rows:
        if classe != "all":
            if decrypt_data(i[5], self.kdf) != classe:
                continue
        c.execute("SELECT * FROM attendance WHERE user=? AND student_id = ?", (user, i[0]))
        attendance = c.fetchall()
        for a in attendance:
            if a[2] != date.toString("yyyy-MM-dd"):
                continue
            if a[3] == "present":
                present += 1
            elif a[3] == "absent":
                absent += 1
            elif a[3] == "excused":
                excused += 1
        students += 1

    layout = self.ui.Graph_frame_8.layout()
    if layout is None:
        layout = QVBoxLayout(self.ui.Graph_frame_8)
        self.ui.Graph_frame_8.setLayout(layout)
    else:

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
                widget.deleteLater()

    fig, ax = plt.subplots(figsize=(5, 5))
    if students == 0:
        ax.text(0.5, 0.5, "No Data Available",
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=14,
                transform=ax.transAxes)
        ax.axis('off')
    else:
        attendance_data = [round(present / students * 100),
                           round(absent / students * 100),
                           round(excused / students * 100),
                           round((students - (present + absent + excused)) / students * 100)]
        wedges, texts, autotexts = ax.pie(attendance_data, labels=None, autopct="%1.1f%%", radius=1.55)
        fig.subplots_adjust(bottom=0.3, left=0.15)

        colors = ["#22C55E", "#EF4444", "#F59E0B", "#9CA3AF"]

        for w, ma in zip(wedges, colors):
            w.set_facecolor(ma)

        fig.legend(
            wedges,
            ["Present", "Absent", "Excused", "Not Assigned"],
            loc="lower center",
            bbox_to_anchor=(0.5, -0.05),
            ncol=2,
            frameon=False,
            columnspacing=2,
            handletextpad=0.6
        )

    canvas = FigureCanvas(fig)
    canvas.updateGeometry()
    canvas.draw()

    layout.addWidget(canvas)


def refresh_graph4(self, user, password):
    c.execute("SELECT class_name FROM classes WHERE user=?", (user,))
    classes_rows = c.fetchall()
    classes = [x[0] for x in classes_rows]

    c.execute("SELECT * FROM students WHERE user=?", (user,))
    students = c.fetchall()

    current_class = self.ui.comboBox2_6.currentText()
    year1 = self.ui.comboBox2_7.currentText()

    if self.ui.comboBox2_6.findText("all") == -1:
        self.ui.comboBox2_6.insertItem(0, "all")
    for i, x in enumerate(classes, start=1):
        if self.ui.comboBox2_6.findText(x) == -1:
            self.ui.comboBox2_6.insertItem(i, x)
    self.ui.comboBox2_6.setCurrentText(current_class)
    classe = self.ui.comboBox2_6.currentText()

    years = []
    for x in students:
        if classe != "all":
            if decrypt_data(x[5], self.kdf) != classe:
                continue
        c.execute("SELECT * FROM attendance WHERE user =? AND student_id = ?", (user, x[0]))
        attendance = c.fetchall()
        for j in attendance:
            if j[2][:4] not in years:
                years.append(j[2][:4])
    for a, x in enumerate(years):
        if self.ui.comboBox2_7.findText(x) == -1:
            self.ui.comboBox2_7.insertItem(a, x)
    self.ui.comboBox2_7.setCurrentText(year1)
    attendance = []
    months_data = {
        "01": 0,
        "02": 0,
        "03": 0,
        "04": 0,
        "05": 0,
        "06": 0,
        "07": 0,
        "08": 0,
        "09": 0,
        "10": 0,
        "11": 0,
        "12": 0
    }

    year = self.ui.comboBox2_7.currentText()
    for x in students:
        if classe != "all":
            if decrypt_data(x[5], self.kdf) != classe:
                continue
        c.execute("SELECT * FROM attendance WHERE user =? AND student_id = ?", (user, x[0]))
        attendance_2 = c.fetchall()
        for qz in attendance_2:

            if qz[2][:4] != year:
                continue
            if qz[3] == "present":
                months_data[qz[2][5:7]] = months_data.get(qz[2][5:7], 0) + 1

    d = 0
    for i in students:

        if classe != "all":
            if decrypt_data(i[5], self.kdf) != classe:
                continue
        c.execute("SELECT * FROM attendance WHERE user =? AND student_id = ?", (user, i[0]))
        attendance_3 = c.fetchall()
        for j in attendance_3:
            if j[2][:4] != year:
                continue
            d += 1

    layout = self.ui.Graph_frame_7.layout()
    if layout is None:
        layout = QVBoxLayout(self.ui.Graph_frame_7)
        self.ui.Graph_frame_7.setLayout(layout)
    else:

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
                widget.deleteLater()

    fig, ax = plt.subplots(figsize=(5, 5))

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    if d == 0:
        percentages = [0] * 12
    else:
        percentages = [round(x / d * 100) for x in months_data.values()]
    ax.plot(months, percentages)
    for label in ax.get_xticklabels():
        label.set_rotation(90)
    ax.set_ylim(0, 100)
    fig.subplots_adjust(bottom=0.3, right=0.95, left=0.08)

    canvas = FigureCanvas(fig)
    canvas.updateGeometry()
    canvas.draw()
    layout.addWidget(canvas)


def refresh_graph5(self, user, password, clear = False):
    c.execute("SELECT class_name FROM classes WHERE user=?", (user,))
    classes_rows = c.fetchall()

    classes = [x[0] for x in classes_rows]
    c.execute("SELECT * FROM students WHERE user=?", (user,))
    students = c.fetchall()

    c.execute("SELECT * FROM subjects WHERE user=?", (user,))
    subjects = c.fetchall()
    for i in [self.ui.top1_name, self.ui.top1_id, self.ui.top1_grade,
              self.ui.top2_name, self.ui.top2_id, self.ui.top2_grade,
              self.ui.top3_name, self.ui.top3_id, self.ui.top3_grade,
              self.ui.top4_name, self.ui.top4_id, self.ui.top4_grade,
              self.ui.top5_name, self.ui.top5_id, self.ui.top5_grade]:
        i.setText("")

    current_class = self.ui.comboBox2_2.currentText()
    if clear :
      self.ui.comboBox2_2.clear()
    if self.ui.comboBox2_2.findText("all") == -1:
        self.ui.comboBox2_2.insertItem(0, "all")
    for i, x in enumerate(classes, start=1):
        if self.ui.comboBox2_2.findText(x) == -1:
            self.ui.comboBox2_2.insertItem(i, x)
    self.ui.comboBox2_2.setCurrentText(current_class)
    classe = self.ui.comboBox2_2.currentText()
    top_students = []
    students_averages = {}
    subjects_data = {subject[1]: int(subject[2]) for subject in subjects}
    for i in students:
        if classe != "all":
            if decrypt_data(i[5], self.kdf) != classe:
                continue
        average = []
        c.execute("SELECT * FROM grades WHERE user=? AND student_id=?", (user, i[0]))
        grades = c.fetchall()
        for x in grades:
            average.append(float(x[3]) * subjects_data[x[2]])
        students_averages[i[0]] = sum(average) / sum(subjects_data.values())

    for z in range(5):
        if students_averages:
            maxi = max(students_averages, key=students_averages.get)
            top_students.append((maxi, round(students_averages[maxi], 2)))
            del students_averages[maxi]

    for i, j in zip(top_students, [(self.ui.top1_name, self.ui.top1_id, self.ui.top1_grade),
                                   (self.ui.top2_name, self.ui.top2_id, self.ui.top2_grade),
                                   (self.ui.top3_name, self.ui.top3_id, self.ui.top3_grade),
                                   (self.ui.top4_name, self.ui.top4_id, self.ui.top4_grade),
                                   (self.ui.top5_name, self.ui.top5_id, self.ui.top5_grade)]):
        c.execute("SELECT first_name FROM students WHERE user=? and student_id=?", (user, i[0]))
        firstname_row = c.fetchone()
        c.execute("SELECT last_name FROM students WHERE user=? and student_id=?", (user, i[0]))
        lastname_row = c.fetchone()
        firstname = decrypt_data(firstname_row[0], self.kdf)
        lastname = decrypt_data(lastname_row[0], self.kdf)
        j[0].setText(f"{firstname} {lastname}")
        j[1].setText(str(i[0]))
        j[2].setText(str(i[1]))


def refresh_graph6(self, user, password, clear = False):
    c.execute("SELECT class_name FROM classes WHERE user=?", (user,))
    classes_rows = c.fetchall()
    classes = [x[0] for x in classes_rows]
    c.execute("SELECT * FROM students WHERE user=?", (user,))
    students = c.fetchall()

    for i in [self.ui.top1_name_2, self.ui.top1_id_2, self.ui.top1_grade_2,
              self.ui.top2_name_2, self.ui.top2_id_2, self.ui.top2_grade_2,
              self.ui.top3_name_2, self.ui.top3_id_2, self.ui.top3_grade_2,
              self.ui.top4_name_2, self.ui.top4_id_2, self.ui.top4_grade_2,
              self.ui.top5_name_2, self.ui.top5_id_2, self.ui.top5_grade_2]:
        i.setText("")

    current_class = self.ui.comboBox2_1.currentText()
    if clear :
      self.ui.comboBox2_1.clear()

    if self.ui.comboBox2_1.findText("all") == -1:
        self.ui.comboBox2_1.insertItem(0, "all")
    for i, x in enumerate(classes, start=1):
        if self.ui.comboBox2_1.findText(x) == -1:
            self.ui.comboBox2_1.insertItem(i, x)
    self.ui.comboBox2_1.setCurrentText(current_class)
    classe = self.ui.comboBox2_1.currentText()

    top_students = []
    students_data = {}

    for i in students:
        if classe != "all":
            if decrypt_data(i[5], self.kdf) != classe:
                continue
        present = 0
        c.execute("SELECT status FROM attendance WHERE user=? and student_id=?", (user, i[0]))
        attendance = c.fetchall()
        for k in attendance:
            if k[0] == "present":
                present += 1
        students_data[i[0]] = round(present / len(attendance) * 100, 2) if len(attendance) != 0 else 0.0

    for i in range(5):
        if students_data:
            maxi = max(students_data, key=students_data.get)
            top_students.append((maxi, students_data[maxi]))
            del students_data[maxi]

    for i, j in zip(top_students, [(self.ui.top1_name_2, self.ui.top1_id_2, self.ui.top1_grade_2),
                                   (self.ui.top2_name_2, self.ui.top2_id_2, self.ui.top2_grade_2),
                                   (self.ui.top3_name_2, self.ui.top3_id_2, self.ui.top3_grade_2),
                                   (self.ui.top4_name_2, self.ui.top4_id_2, self.ui.top4_grade_2),
                                   (self.ui.top5_name_2, self.ui.top5_id_2, self.ui.top5_grade_2)]):
        c.execute("SELECT first_name FROM students WHERE user=? and student_id=?", (user, i[0]))
        firstname_row = c.fetchone()
        c.execute("SELECT last_name FROM students WHERE user=? and student_id=?", (user, i[0]))
        lastname_row = c.fetchone()
        firstname = decrypt_data(firstname_row[0], self.kdf)
        lastname = decrypt_data(lastname_row[0], self.kdf)
        j[0].setText(f"{firstname} {lastname}")
        j[1].setText(str(i[0]))
        j[2].setText(f"{i[1]}%")


def refresh_graph7(self, user, password):
    wedges = None
    texts = None
    autotexts = None

    current_class = self.ui.comboBox2_3.currentText()
    c.execute("SELECT * FROM students WHERE user = ?", (user,))
    students = c.fetchall()
    c.execute("SELECT class_name FROM classes WHERE user = ?", (user,))
    classes_rows = c.fetchall()
    classes = [x[0] for x in classes_rows]

    if self.ui.comboBox2_3.findText("all") == -1:
        self.ui.comboBox2_3.insertItem(0, "all")
    for i, x in enumerate(classes, start=1):
        if self.ui.comboBox2_3.findText(x) == -1:
            self.ui.comboBox2_3.insertItem(i, x)
    self.ui.comboBox2_3.setCurrentText(current_class)
    classe = self.ui.comboBox2_3.currentText()

    males = 0
    females = 0

    for i in students:
        if classe != "all":
            if classe != decrypt_data(i[5], self.kdf):
                continue
        if decrypt_data(i[6], self.kdf) == "Male":
            males += 1
        else:
            females += 1
    males_percentage = males / len(students) * 100 if len(students) != 0 else 0
    females_percentage = females / len(students) * 100 if len(students) != 0 else 0

    sizes = [males_percentage, females_percentage]
    labels = ["Male", "Female"]

    layout = self.ui.Graph_frame_4.layout()
    if layout is None:
        layout = QVBoxLayout(self.ui.Graph_frame_4)
        self.ui.Graph_frame_4.setLayout(layout)
    else:

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
                widget.deleteLater()

    fig = Figure(figsize=(5, 5))
    ax = fig.add_subplot(111)

    try:
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct="%1.1f%%")
    except (ValueError, ZeroDivisionError):
        ax.text(0.5, 0.5, "No Data Available",
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=14,
                transform=ax.transAxes)
        ax.axis('off')
    if len(students) == 0:
        ax.text(0.5, 0.5, "No Data Available",
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=14,
                transform=ax.transAxes)
        ax.axis('off')
    canvas = FigureCanvas(fig)
    canvas.updateGeometry()
    canvas.draw()
    self.ui.Graph_frame_3.wedges = wedges
    self.ui.Graph_frame_3.canvas = canvas
    self.ui.Graph_frame_3.texts = texts
    layout.addWidget(canvas)


def refresh_graph8(self, user, password):
    c.execute("SELECT * FROM students WHERE user = ?", (user,))
    students = c.fetchall()
    c.execute("SELECT class_name FROM classes WHERE user = ?", (user,))
    classes_rows = c.fetchall()
    wedges = None
    texts = None
    autotexts = None
    classes = [x[0] for x in classes_rows]
    classes_data = {}
    for x in classes:
        for i in students:
            if decrypt_data(i[5], self.kdf) == x:
                classes_data[x] = classes_data.get(x, 0) + 1

    labels = [x for x in classes_data.keys()]
    sizes = [x / len(students) * 100 if len(students) != 0 else 0 for x in
             classes_data.values()]
    layout = self.ui.Graph_frame_3.layout()
    if layout is None:
        layout = QVBoxLayout(self.ui.Graph_frame_3)
        self.ui.Graph_frame_3.setLayout(layout)
    else:

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
                widget.deleteLater()

    fig = Figure(figsize=(5, 5))
    ax = fig.add_subplot(111)

    try:
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct="%1.1f%%")
    except (ValueError, ZeroDivisionError):
        ax.text(0.5, 0.5, "No Data Available",
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=14,
                transform=ax.transAxes)
        ax.axis('off')
    if len(students) == 0:
        ax.text(0.5, 0.5, "No Data Available",
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=14,
                transform=ax.transAxes)
        ax.axis('off')
    canvas = FigureCanvas(fig)
    canvas.updateGeometry()
    canvas.draw()
    layout.addWidget(canvas)

    self.ui.Graph_frame_4.wedges = wedges
    self.ui.Graph_frame_4.canvas = canvas
    self.ui.Graph_frame_4.texts = texts