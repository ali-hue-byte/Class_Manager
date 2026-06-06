# ============================================================
# Helpful functions
# Contains utility functions for :
# - SQLite database operations (students, classes, grades, attendance)
# - Data encryption and decryption
# - Password hashing
# - User data (load/save)
# ============================================================



import os
from cryptography.fernet import Fernet
import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import pickle
import sqlite3

USER = "users.pkl"

conn = sqlite3.connect("data.db")
c = conn.cursor()


def add_student(user, first, last, student_id, birth,classe ,gender, phone, email, address):
    """ Adds or replaces a student in the SQLite database """

    c.execute(
        "INSERT OR REPLACE INTO students (user, student_id, first_name, last_name, birth_date,class, gender, address, email, Number) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)",
        (user, student_id, first, last, birth,classe, gender, address, email, phone)
    )
    conn.commit()


def add_class(user,class_name,max_students,Total_students):
    """ Adds or replaces a class in the SQLite database """

    c.execute("INSERT OR REPLACE INTO classes (user, class_name, max_students, Total_students)"
              "VALUES (?, ?, ?, ?)",
              (user, class_name, max_students, Total_students))
    conn.commit()


def add_subject(user,subject,coeff):
    """ Adds or replaces a subject in the SQLite database """

    c.execute("INSERT OR REPLACE INTO subjects (user, subject_name, coeff)"
              "VALUES (?, ?, ?)",
              (user, subject, coeff))
    conn.commit()


def mark_attendance(user,id,date,status):
    """ Marks or updates a student's attendance in the SQLite database """

    c.execute("INSERT OR REPLACE INTO attendance (user, student_id, date, status)"
              "VALUES (?, ?, ?, ?) ",
              (user, id, date, status))
    conn.commit()


def add_grade(user, id , subject, grade):
    """ Adds or replaces a grade in the SQLite database """

    c.execute("INSERT OR REPLACE INTO grades (user, student_id, subject, grade)"
              "VALUES (?, ?, ?, ?)",
              (user, id, subject, grade))

    conn.commit()


def select_class(user,classe):
    """ Selects a class from the SQLite database """

    c.execute("SELECT * FROM classes WHERE user = ? AND class_name = ?", ( user,classe))
    return c.fetchone()


def delete_student(user,id):
    """ Deletes a student from the SQLite database """

    c.execute("DELETE FROM students WHERE student_id=? AND user=?", (id, user))
    conn.commit()


def delete_class(user,classe):
    """ Deletes a class from the SQLite database """

    c.execute("DELETE FROM classes WHERE class_name = ? AND user=?", (classe, user))
    conn.commit()

def delete_subject_(user,subject):
    """ Deletes a subject from the SQLite database """

    c.execute("DELETE FROM subjects WHERE user = ? AND subject_name = ?", (user, subject))
    c.execute("DELETE FROM grades WHERE user = ? AND subject = ?", (user, subject))
    conn.commit()

def widgets_operations(self, choice):
    for i,j in self.widgets.items():
        if choice not in j or "error_labels" in j:
            i.hide()
            unwrap_shadow(i)

        else :
            i.show()

        if "widgets_to_clear" in j :
            i.clear()
            unwrap_shadow(i)


def refresh_combo_id(self, user, classe):
    c.execute("SELECT student_id,class FROM students WHERE user =? ", (user,))
    students_rows = c.fetchall()
    students = []
    self.ui.id_combobox.clear()
    for i in students_rows:
        if decrypt_data(i[1], self.kdf) == classe:
            students.append(str(i[0]))
    for i, j in enumerate(students):
        if self.ui.id_combobox.findText(j) == -1:
            self.ui.id_combobox.insertItem(i, j)

def load_data():
    """ Loads users data from pickle file (username / hash of password / maximum score) """

    if os.path.exists(USER):
        with open(USER, "rb") as f:
            return pickle.load(f)
    else:
        return []


def save_data(data):
    """ Saves users data to pickle file """

    with open(USER, "wb") as f:
        pickle.dump(data, f)




def KDF2(password, salt):
    """ Derives a Fernet encryption key from password and salt using PBKDF2-SHA256 """

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

def SALT(user):
    data = load_data()
    for i in data:
        if i["username"] == user:
            salt = i["salt"]
    return bytes.fromhex(salt)


def wrap_with_shadow(widget, opacity=120):
    """ Gives shadow effect to a widget """
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
    """ Gives shadow effect to tables """
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
    """ Removes shadow effect """
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
