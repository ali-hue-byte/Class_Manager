from PySide6.QtCore import (QRect,Qt,QTimer,QPropertyAnimation, QEasingCurve)
from PySide6.QtWidgets import QLabel,QPushButton
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QGraphicsDropShadowEffect,
                               QFrame)

import os

from cryptography.fernet import Fernet
import hashlib

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

import pickle
import sqlite3
DATA_FILE = "data.pkl"
USER = "users.pkl"

conn = sqlite3.connect("data.db")
c = conn.cursor()
def add_student(user, first, last, student_id, birth,classe ,gender, phone, email, address):
    c.execute(
        "INSERT OR REPLACE INTO students (user, student_id, first_name, last_name, birth_date,class, gender, address, email, Number) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)",
        (user, student_id, first, last, birth,classe, gender, address, email, phone)
    )
    conn.commit()
def add_class(user,class_name,max_students,Total_students):
    c.execute("INSERT OR REPLACE INTO classes (user, class_name, max_students, Total_students)"
              "VALUES (?, ?, ?, ?)",
              (user, class_name, max_students, Total_students))
    conn.commit()
def add_subject(user,subject,coeff):
    c.execute("INSERT OR REPLACE INTO subjects (user, subject_name, coeff)"
              "VALUES (?, ?, ?)",
              (user, subject, coeff))
    conn.commit()
def mark_attendance(user,id,date,status):
    c.execute("INSERT OR REPLACE INTO attendance (user, student_id, date, status)"
              "VALUES (?, ?, ?, ?) ",
              (user, id, date, status))
    conn.commit()
def add_grade(user, id , subject, grade):
    c.execute("INSERT OR REPLACE INTO grades (user, student_id, subject, grade)"
              "VALUES (?, ?, ?, ?)",
              (user, id, subject, grade))

    conn.commit()

def select_class(user,classe):
    c.execute("SELECT * FROM classes WHERE user = ? AND class_name = ?", ( user,classe))
    return c.fetchone()
def delete_student(user,id):
    c.execute("DELETE FROM students WHERE student_id=? AND user=?", (id, user))
    conn.commit()
def delete_class(user,classe):
    c.execute("DELETE FROM classes WHERE class_name = ? AND user=?", (classe, user))
    conn.commit()
def delete_subject_(user,subject):
    c.execute("DELETE FROM subjects WHERE user = ? AND subject_name = ?", (user, subject))
    c.execute("DELETE FROM grades WHERE user = ? AND subject = ?", (user, subject))
    conn.commit()
def animate_title(title, start, end):
    if hasattr(title, "anim"):
        title.anim.stop()

    title.anim = QPropertyAnimation(title, b"pos")
    title.anim.setDuration(200)
    title.anim.setStartValue(start)
    title.anim.setEndValue(end)
    title.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
    title.anim.start()




def load_data():
    if os.path.exists(USER):
        with open(USER, "rb") as f:
            return pickle.load(f)
    else:
        return []

def save_data(data):
    with open(USER, "wb") as f:
        pickle.dump(data, f)




def KDF2(password, salt):
    e_password = password.encode() if isinstance(password, str) else password
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    return Fernet(base64.urlsafe_b64encode(kdf.derive(e_password)))

def encrypt_data(data, fernet):

    return fernet.encrypt(data.encode()).decode()

def decrypt_data(data, fernet):
    if isinstance(data, str):
        data = data.encode()
    return fernet.decrypt(data).decode()

def hash_password(password, salt):
    return hashlib.sha256(password.encode() + salt).hexdigest()


class InfoButton(QPushButton):
    def __init__(self, parent=None, page=None, text=None, pos=None):
        super().__init__(parent)
        self.label = QLabel(page)
        self.label.setText(text)
        self.label.setGeometry(pos)

        self.label.setStyleSheet(u"QLabel{\n"
                                 "background-color: #E6EBF2;\n"
                                 "border : 1px solid #CBD5E1;\n"
                                 "color: #1F2A44;\n"
                                 "border-radius: 5px;\n"
                                 "font-size: 12px;\n"
                                 "}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.hide()

        self.hover_timer = QTimer(self)
        self.hover_timer.setSingleShot(True)
        self.hover_timer.timeout.connect(self.label.show)

    def enterEvent(self, event):
        self.hover_timer.start(500)

        self.label.raise_()

    def leaveEvent(self, event):
        self.hover_timer.stop()
        self.label.hide()


class HoverButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(100)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.original_rect = None

    def enterEvent(self, event):
        self.anim.stop()
        if self.original_rect == None:
            self.original_rect = self.geometry()

        self.anim.setStartValue(self.geometry())
        target = QRect(
            self.original_rect.x() - 3,
            self.original_rect.y() - 3,
            self.original_rect.width() + 6,
            self.original_rect.height() + 6
        )
        self.anim.setEndValue(target)
        self.anim.start()

        super().enterEvent(event)

    def leaveEvent(self, event):
        if self.original_rect:
            self.anim.stop()
            self.anim.setStartValue(self.geometry())

            self.anim.setEndValue(self.original_rect)
            self.anim.start()
        super().leaveEvent(event)


class HoverFrame(QFrame):
    def __init__(self, parent=None,
                 frame=None,
                 start=None,
                 end=None,
                 start2=None,
                 end2=None,
                 title=None,
                 start3=None,
                 end3=None,
                 title2=None,
                 start4=None,
                 end4=None,
                 bars=None,
                 canvas=None,
                 ax=None,
                 combo1=None,
                 com1s=None,
                 com1e=None,

                 lbl=None,
                 lbls=None,
                 lble=None,
                 wedges=None,
                 texts=None):
        super().__init__(parent)
        self.anim = QPropertyAnimation(self, b"geometry")

        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)

        self.frame = frame

        self.start = start
        self.end = end
        self.start2 = start2
        self.end2 = end2
        self.title = title
        self.start3 = start3
        self.end3 = end3
        self.title2 = title2
        self.start4 = start4
        self.end4 = end4
        self.bars = bars
        self.canvas = canvas
        self.ax = ax
        self.combo1 = combo1
        self.texts = texts

        self.lbl = lbl

        self.com1s = com1s
        self.com1e = com1e

        self.lbls = lbls
        self.lble = lble

        self.wedges = wedges
        self.saved_colors = None

        self.anim2 = QPropertyAnimation(self.frame, b"geometry")
        self.anim2.setDuration(200)

    def enterEvent(self, event):
        self.saved_colors = None
        self.anim2.stop()
        self.anim.stop()
        self.anim.setStartValue(self.start)
        self.anim.setEndValue(self.end)
        self.anim.start()

        self.anim2.setStartValue(self.start2)
        self.anim2.setEndValue(self.end2)
        self.anim2.start()

        if self.title:
            animate_title(self.title, self.start3, self.end3)

        if self.title2:
            animate_title(self.title2, self.start4, self.end4)

        if self.bars and self.canvas:
            for bar in self.bars:
                bar.set_facecolor("#9e9e9e")
                bar.set_edgecolor("#616161")
            self.ax.tick_params(axis="x", colors="#9e9e9e")
            self.ax.tick_params(axis="y", colors="#9e9e9e")
            for spine in self.ax.spines.values():
                spine.set_edgecolor("#9e9e9e")
            self.canvas.draw()
        if self.frame:
            self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                     "border-radius: 15px;\n"
                                     "border: 2px solid grey;")
        if self.title:
            self.title2.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                      "color: #808080;")
        if self.combo1 and self.lbl:
            animate_title(self.combo1, self.com1s, self.com1e)

            animate_title(self.lbl, self.lbls, self.lble)

        if self.wedges:
            if self.saved_colors == None:
                self.saved_colors = [wedge.get_facecolor() for wedge in self.wedges]
            for widget in self.wedges:
                widget.set_facecolor("#9e9e9e")
            for t in self.texts:
                t.set_color("#9e9e9e")

            self.canvas.draw()

        super().enterEvent(event)

    def leaveEvent(self, event):

        self.anim.stop()
        self.anim.setStartValue(self.end)

        self.anim.setEndValue(self.start)
        self.anim.start()

        self.anim2.stop()
        self.anim2.setStartValue(self.end2)
        self.anim2.setEndValue(self.start2)
        self.anim2.start()

        if self.title:
            animate_title(self.title, self.end3, self.start3)

        if self.title2:
            animate_title(self.title2, self.end4, self.start4)

        if self.bars and self.canvas:
            for bar in self.bars:
                bar.set_facecolor("#2563EB")
                bar.set_edgecolor("#124187")
            self.ax.tick_params(axis="x", colors="#000000")
            self.ax.tick_params(axis="y", colors="#000000")
            for spine in self.ax.spines.values():
                spine.set_edgecolor("#000000")

            self.canvas.draw()
        if self.frame:
            self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                     "border-radius: 15px;\n"
                                     "border: 2px solid black;")
        if self.title:
            self.title2.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                      "color: rgb(34, 34, 34);")
        if self.combo1 and self.lbl:
            animate_title(self.combo1, self.com1e, self.com1s)

            animate_title(self.lbl, self.lble, self.lbls)

        if self.wedges:
            for wedge, color in zip(self.wedges, self.saved_colors):
                wedge.set_facecolor(color)
            for t in self.texts:
                t.set_color("#000000")
            self.canvas.draw()

        super().leaveEvent(event)



def wrap_with_shadow(widget, opacity=120):
    shadow = widget.graphicsEffect()

    if isinstance(shadow, QGraphicsDropShadowEffect):
        shadow.setColor(QColor(0, 0, 0, opacity))
        return

    shadow = QGraphicsDropShadowEffect(widget)
    shadow.setBlurRadius(25)
    shadow.setXOffset(0)
    shadow.setYOffset(6)
    shadow.setColor(QColor(0, 0, 0, opacity))

    widget.setGraphicsEffect(shadow)


def wrap_with_shadow2(frame, x):
    wrapper = getattr(frame, "_shadow_wrapper", None)

    if wrapper:
        try:
            _ = wrapper.graphicsEffect()
            shadow = wrapper.graphicsEffect()
            if shadow:
                shadow.setColor(QColor(0, 0, 0, x))
            return
        except RuntimeError:
            wrapper = None

    parent = frame.parentWidget()

    wrapper = QFrame(parent)
    wrapper.setGeometry(
        frame.x() - 10,
        frame.y() - 10,
        frame.width() + 20,
        frame.height() + 20
    )
    wrapper.setStyleSheet("background: transparent;")

    frame.setParent(wrapper)
    frame.move(10, 10)

    shadow = QGraphicsDropShadowEffect(wrapper)
    shadow.setBlurRadius(25)
    shadow.setXOffset(0)
    shadow.setYOffset(6)
    shadow.setColor(QColor(0, 0, 0, x))
    wrapper.setGraphicsEffect(shadow)

    wrapper.show()

    frame._shadow_wrapper = wrapper


def unwrap_shadow(frame):
    wrapper = getattr(frame, "_shadow_wrapper", None)
    if not wrapper:
        return
    original_parent = wrapper.parentWidget()
    if not original_parent:
        return
    global_pos = wrapper.pos() + frame.pos()
    frame.setParent(original_parent)
    frame.move(global_pos)
    wrapper.setGraphicsEffect(None)
    wrapper.deleteLater()
    frame._shadow_wrapper = None




