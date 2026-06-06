from Logic.Utils import HoverFrame

from PySide6.QtCore import (QCoreApplication, QDate, QPoint, QRect, Qt, QPropertyAnimation)

from PySide6.QtWidgets import (QFrame, QLabel, QPushButton, QComboBox, QDateEdit)


class StatisticsUI(object):
    def statistics_setup(self, Dialog):
        self.performance = QPushButton(self.frame_2)
        self.performance.setObjectName(u"performance")
        self.performance.setGeometry(QRect(410, 40, 81, 31))
        self.performance.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                       "color :rgb(24, 182, 255);\n"
                                       "border: none;\n"
                                       "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                       "}\n"
                                       "")
        self.performance.setFlat(True)
        self.ranking = QPushButton(self.frame_2)
        self.ranking.setObjectName(u"ranking")
        self.ranking.setGeometry(QRect(570, 40, 81, 31))
        self.ranking.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                   "font: 700 9pt \"Yu Gothic UI\";")
        self.ranking.setFlat(True)
        self.attendancetop = QPushButton(self.frame_2)
        self.attendancetop.setObjectName(u"attendancetop")
        self.attendancetop.setGeometry(QRect(490, 40, 81, 31))
        self.attendancetop.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                         "font: 700 9pt \"Yu Gothic UI\";")
        self.attendancetop.setFlat(True)
        self.other = QPushButton(self.frame_2)
        self.other.setObjectName(u"other")
        self.other.setGeometry(QRect(650, 40, 81, 31))
        self.other.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                 "font: 700 9pt \"Yu Gothic UI\";")
        self.other.setFlat(True)
        self.Graph_frame_2 = HoverFrame(self.page, start=QRect(590, 140, 351, 321), end=QRect(555, 105, 421, 391),
                                        start2=QRect(200, 140, 351, 321), end2=QRect(235, 175, 281, 251))
        self.Graph_frame_2.setObjectName(u"scrollArea_2")
        self.Graph_frame_2.setGeometry(QRect(590, 140, 351, 321))
        self.Graph_frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "border: 2px solid black;")

        self.Graph_frame = HoverFrame(self.page, frame=self.Graph_frame_2, start=QRect(200, 140, 351, 321),
                                      end=QRect(165, 105, 421, 391), start2=QRect(590, 140, 351, 321),
                                      end2=QRect(625, 175, 281, 251))
        self.Graph_frame_2.frame = self.Graph_frame
        self.Graph_frame_2.anim2 = QPropertyAnimation(self.Graph_frame, b"geometry")
        self.Graph_frame.setObjectName(u"scrollArea_3")
        self.Graph_frame.setGeometry(QRect(200, 140, 351, 321))
        self.Graph_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 15px;\n"
                                       "border: 2px solid black;")

        self.Graph_frame_5 = QFrame(self.page)
        self.Graph_frame_5.setObjectName(u"Graph_frame_5")
        self.Graph_frame_5.setGeometry(QRect(200, 140, 351, 341))
        self.Graph_frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 40px;\n"
                                         "border: 1px solid rgb(25, 86, 179),")
        self.Graph_frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.Graph_frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.top1_name = QLabel(self.Graph_frame_5)
        self.top1_name.setObjectName(u"top1_name")
        self.top1_name.setGeometry(QRect(0, 40, 131, 61))
        self.top1_name.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                     "\n"
                                     "border-top-right-radius: 0px;\n"
                                     "border-bottom-left-radius: 0px;\n"
                                     "border-bottom-right-radius: 0px;\n"
                                     "font: 600 11pt \"Segoe UI\";\n"
                                     "border: none;\n"
                                     "border-left: 1px solid rgb(25, 86, 179)")
        self.top1_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top2_name = QLabel(self.Graph_frame_5)
        self.top2_name.setObjectName(u"top2_name")
        self.top2_name.setGeometry(QRect(0, 100, 131, 61))
        self.top2_name.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
                                     "background-color: #F8F8F8;\n"
                                     "border: none;\n"
                                     "border-left: 1px solid rgb(25, 86, 179)")
        self.top2_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top4_name = QLabel(self.Graph_frame_5)
        self.top4_name.setObjectName(u"top4_name")
        self.top4_name.setGeometry(QRect(0, 220, 131, 61))
        self.top4_name.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
                                     "background-color: #F0F0F0;\n"
                                     "border: none;\n"
                                     "border-left: 1px solid rgb(25, 86, 179)")
        self.top4_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top3_name = QLabel(self.Graph_frame_5)
        self.top3_name.setObjectName(u"top3_name")
        self.top3_name.setGeometry(QRect(0, 160, 131, 61))
        self.top3_name.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
                                     "background-color: #F5F5F5;\n"
                                     "border: none;\n"
                                     "border-left: 1px solid rgb(25, 86, 179)")
        self.top3_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top5_name = QLabel(self.Graph_frame_5)
        self.top5_name.setObjectName(u"top5_name")
        self.top5_name.setGeometry(QRect(0, 280, 131, 61))
        self.top5_name.setStyleSheet(u"border:none;\n"
                                     "border-left :1px solid rgb(25, 86, 179);\n"
                                     "border-bottom :1px solid rgb(25, 86, 179);\n"
                                     "border-top-left-radius: 0px;\n"
                                     "border-top-right-radius: 0px;\n"
                                     "border-bottom-left-radius: 40px;\n"
                                     "border-bottom-right-radius: 0px;\n"
                                     "font: 600 11pt \"Segoe UI\";\n"
                                     "background-color: #E8E8E8")
        self.top5_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top2_id = QLabel(self.Graph_frame_5)
        self.top2_id.setObjectName(u"top2_id")
        self.top2_id.setGeometry(QRect(130, 100, 111, 61))
        self.top2_id.setStyleSheet(u"color: #6B7280;\n"
                                   "font: 10pt \"Segoe UI\";\n"
                                   "background-color : #F8F8F8;\n"
                                   "border: none")
        self.top2_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top4_id = QLabel(self.Graph_frame_5)
        self.top4_id.setObjectName(u"top4_id")
        self.top4_id.setGeometry(QRect(130, 220, 111, 61))
        self.top4_id.setStyleSheet(u"color: #6B7280;\n"
                                   "font: 10pt \"Segoe UI\";\n"
                                   "background-color: #F0F0F0;\n"
                                   "border: none")
        self.top4_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top5_id = QLabel(self.Graph_frame_5)
        self.top5_id.setObjectName(u"top5_id")
        self.top5_id.setGeometry(QRect(130, 280, 111, 61))
        self.top5_id.setStyleSheet(u"color: #6B7280;\n"
                                   "font: 10pt \"Segoe UI\";\n"
                                   "background-color: #E8E8E8;\n"
                                   "border: none;\n"
                                   "border-bottom :1px solid rgb(25, 86, 179);\n"
                                   "")
        self.top5_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top3_id = QLabel(self.Graph_frame_5)
        self.top3_id.setObjectName(u"top3_id")
        self.top3_id.setGeometry(QRect(130, 160, 111, 61))
        self.top3_id.setStyleSheet(u"color: #6B7280;\n"
                                   "font: 10pt \"Segoe UI\";\n"
                                   "background-color: #F5F5F5;\n"
                                   "border: none")
        self.top3_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top1_id = QLabel(self.Graph_frame_5)
        self.top1_id.setObjectName(u"top1_id")
        self.top1_id.setGeometry(QRect(130, 40, 111, 61))
        self.top1_id.setStyleSheet(u"color: #6B7280;\n"
                                   "font: 10pt \"Segoe UI\";\n"
                                   "border: none")
        self.top1_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top1_grade = QLabel(self.Graph_frame_5)
        self.top1_grade.setObjectName(u"top1_grade")
        self.top1_grade.setGeometry(QRect(240, 40, 111, 61))
        self.top1_grade.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                      "color: rgb(33, 130, 12);\n"
                                      "font: 600 11pt \"Segoe UI\";\n"
                                      "border-top-right-radius: 0px;\n"
                                      "border-bottom-left-radius: 0px;\n"
                                      "border-bottom-right-radius: 0px;\n"
                                      "border: none;\n"
                                      "border-right: 1px solid rgb(25, 86, 179)\n"
                                      "")
        self.top1_grade.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top2_grade = QLabel(self.Graph_frame_5)
        self.top2_grade.setObjectName(u"top2_grade")
        self.top2_grade.setGeometry(QRect(240, 100, 111, 61))
        self.top2_grade.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                      "font: 600 11pt \"Segoe UI\";\n"
                                      "border-top-right-radius: 0px;\n"
                                      "border-bottom-left-radius: 0px;\n"
                                      "border-bottom-right-radius: 0px;\n"
                                      "color: rgb(33, 130, 12);\n"
                                      "background-color : #F8F8F8;\n"
                                      "border: none;\n"
                                      "border-right: 1px solid rgb(25, 86, 179)")
        self.top2_grade.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top5_grade = QLabel(self.Graph_frame_5)
        self.top5_grade.setObjectName(u"top5_grade")
        self.top5_grade.setGeometry(QRect(240, 280, 111, 61))
        self.top5_grade.setStyleSheet(u"border: none;\n"
                                      "border-right :1px solid rgb(25, 86, 179);\n"
                                      "border-bottom :1px solid rgb(25, 86, 179);\n"
                                      "border-top-left-radius: 0px;\n"
                                      "font: 600 11pt \"Segoe UI\";\n"
                                      "border-top-right-radius: 0px;\n"
                                      "border-bottom-left-radius: 0px;\n"
                                      "border-bottom-right-radius: 40px;\n"
                                      "color: rgb(33, 130, 12);\n"
                                      "background-color: #E8E8E8")
        self.top5_grade.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top4_grade = QLabel(self.Graph_frame_5)
        self.top4_grade.setObjectName(u"top4_grade")
        self.top4_grade.setGeometry(QRect(240, 220, 111, 61))
        self.top4_grade.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                      "font: 600 11pt \"Segoe UI\";\n"
                                      "border-top-right-radius: 0px;\n"
                                      "border-bottom-left-radius: 0px;\n"
                                      "border-bottom-right-radius: 0px;\n"
                                      "color: rgb(33, 130, 12);\n"
                                      "background-color: #F0F0F0;\n"
                                      "border:none;\n"
                                      "border-right: 1px solid rgb(25, 86, 179)")
        self.top4_grade.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top3_grade = QLabel(self.Graph_frame_5)
        self.top3_grade.setObjectName(u"top3_grade")
        self.top3_grade.setGeometry(QRect(240, 160, 111, 61))
        self.top3_grade.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                      "font: 600 11pt \"Segoe UI\";\n"
                                      "border-top-right-radius: 0px;\n"
                                      "border-bottom-left-radius: 0px;\n"
                                      "border-bottom-right-radius: 0px;\n"
                                      "color: rgb(33, 130, 12);\n"
                                      "background-color: #F5F5F5;\n"
                                      "border: none;\n"
                                      "border-right: 1px solid rgb(25, 86, 179)")
        self.top3_grade.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.full_name = QLabel(self.Graph_frame_5)
        self.full_name.setObjectName(u"full_name")
        self.full_name.setGeometry(QRect(0, 0, 131, 41))
        self.full_name.setStyleSheet(u"border-top-left-radius: 40px;\n"
                                     "font: 600 13pt \"Sitka\";\n"
                                     "color: #F9FAFB;\n"
                                     "border-top-right-radius: 0px;\n"
                                     "border-bottom-left-radius: 0px;\n"
                                     "border-bottom-right-radius: 0px;\n"
                                     "background-color: rgb(25, 86, 179)")
        self.full_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.grade_lbl = QLabel(self.Graph_frame_5)
        self.grade_lbl.setObjectName(u"grade_lbl")
        self.grade_lbl.setGeometry(QRect(240, 0, 111, 41))
        self.grade_lbl.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                     "font: 600 13pt \"Sitka\";\n"
                                     "color: #F9FAFB;\n"
                                     "border-top-right-radius: 40px;\n"
                                     "border-bottom-left-radius: 0px;\n"
                                     "border-bottom-right-radius: 0px;\n"
                                     "background-color: rgb(25, 86, 179)")
        self.grade_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.id_lbl = QLabel(self.Graph_frame_5)
        self.id_lbl.setObjectName(u"id_lbl")
        self.id_lbl.setGeometry(QRect(130, 0, 111, 41))
        self.id_lbl.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                  "font: 600 13pt \"Sitka\";\n"
                                  "color: #F9FAFB;\n"
                                  "border-top-right-radius: 0px;\n"
                                  "border-bottom-left-radius: 0px;\n"
                                  "border-bottom-right-radius: 0px;\n"
                                  "background-color: rgb(25, 86, 179)")
        self.id_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_16 = QLabel(self.page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(290, 100, 49, 16))
        self.comboBox2_1 = QComboBox(self.page)
        self.comboBox2_1.setObjectName(u"comboBox2_1")
        self.comboBox2_1.setGeometry(QRect(680, 500, 231, 41))
        self.comboBox2_1.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.class2_1 = QLabel(self.page)
        self.class2_1.setObjectName(u"class2")
        self.class2_1.setGeometry(QRect(620, 510, 41, 16))
        self.class2_1.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                    "font: 600 12pt \"Segoe UI\";")
        self.class2_2 = QLabel(self.page)
        self.class2_2.setObjectName(u"class2_2")
        self.class2_2.setGeometry(QRect(230, 510, 41, 16))
        self.class2_2.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                    "font: 600 12pt \"Segoe UI\";")
        self.comboBox2_2 = QComboBox(self.page)
        self.comboBox2_2.setObjectName(u"comboBox2_2")
        self.comboBox2_2.setGeometry(QRect(290, 500, 231, 41))
        self.comboBox2_2.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.average_class = QLabel(self.page)
        self.average_class.setObjectName(u"average_class")
        self.average_class.setGeometry(QRect(200, 100, 351, 31))
        self.average_class.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                         "color: rgb(34, 34, 34);")
        self.average_class.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Graph_frame.title = self.average_class
        self.Graph_frame.start3 = QPoint(200, 100)
        self.Graph_frame.end3 = QPoint(200, 65)
        self.Graph_frame_2.title2 = self.average_class
        self.Graph_frame_2.start4 = QPoint(200, 100)
        self.Graph_frame_2.end4 = QPoint(200, 135)
        self.top_students = QLabel(self.page)
        self.top_students.setObjectName(u"top_students")
        self.top_students.setGeometry(QRect(200, 100, 351, 31))
        self.top_students.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                        "color: rgb(34, 34, 34);")
        self.top_students.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subject_averages = QLabel(self.page)
        self.subject_averages.setObjectName(u"subject_avaeges")
        self.subject_averages.setGeometry(QRect(590, 100, 351, 31))
        self.subject_averages.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                            "color: rgb(34, 34, 34);")
        self.subject_averages.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Graph_frame.title2 = self.subject_averages
        self.Graph_frame.start4 = QPoint(590, 100)
        self.Graph_frame.end4 = QPoint(590, 135)
        self.Graph_frame_2.title = self.subject_averages
        self.Graph_frame_2.start3 = QPoint(590, 100)
        self.Graph_frame_2.end3 = QPoint(590, 65)
        self.top_students_3 = QLabel(self.page)
        self.top_students_3.setObjectName(u"top_students_3")
        self.top_students_3.setGeometry(QRect(590, 100, 351, 31))
        self.top_students_3.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                          "color: rgb(34, 34, 34);")
        self.top_students_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Graph_frame_6 = QFrame(self.page)
        self.Graph_frame_6.setObjectName(u"Graph_frame_6")
        self.Graph_frame_6.setGeometry(QRect(590, 140, 351, 341))
        self.Graph_frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 40px;\n"
                                         "border: 1px solid rgb(25, 86, 179),")
        self.Graph_frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.Graph_frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.top1_name_2 = QLabel(self.Graph_frame_6)
        self.top1_name_2.setObjectName(u"top1_name_2")
        self.top1_name_2.setGeometry(QRect(0, 40, 131, 61))
        self.top1_name_2.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                       "\n"
                                       "border-top-right-radius: 0px;\n"
                                       "border-bottom-left-radius: 0px;\n"
                                       "border-bottom-right-radius: 0px;\n"
                                       "font: 600 11pt \"Segoe UI\";\n"
                                       "border: none;\n"
                                       "border-left: 1px solid rgb(25, 86, 179)")
        self.top1_name_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top2_name_2 = QLabel(self.Graph_frame_6)
        self.top2_name_2.setObjectName(u"top2_name_2")
        self.top2_name_2.setGeometry(QRect(0, 100, 131, 61))
        self.top2_name_2.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
                                       "background-color: #F8F8F8;\n"
                                       "border: none;\n"
                                       "border-left: 1px solid rgb(25, 86, 179)")
        self.top2_name_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top4_name_2 = QLabel(self.Graph_frame_6)
        self.top4_name_2.setObjectName(u"top4_name_2")
        self.top4_name_2.setGeometry(QRect(0, 220, 131, 61))
        self.top4_name_2.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
                                       "background-color: #F0F0F0;\n"
                                       "border: none;\n"
                                       "border-left: 1px solid rgb(25, 86, 179)")
        self.top4_name_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top3_name_2 = QLabel(self.Graph_frame_6)
        self.top3_name_2.setObjectName(u"top3_name_2")
        self.top3_name_2.setGeometry(QRect(0, 160, 131, 61))
        self.top3_name_2.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
                                       "background-color: #F5F5F5;\n"
                                       "border: none;\n"
                                       "border-left: 1px solid rgb(25, 86, 179)")
        self.top3_name_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top5_name_2 = QLabel(self.Graph_frame_6)
        self.top5_name_2.setObjectName(u"top5_name_2")
        self.top5_name_2.setGeometry(QRect(0, 280, 131, 61))
        self.top5_name_2.setStyleSheet(u"border:none;\n"
                                       "border-left :1px solid rgb(25, 86, 179);\n"
                                       "border-bottom :1px solid rgb(25, 86, 179);\n"
                                       "border-top-left-radius: 0px;\n"
                                       "border-top-right-radius: 0px;\n"
                                       "border-bottom-left-radius: 40px;\n"
                                       "border-bottom-right-radius: 0px;\n"
                                       "font: 600 11pt \"Segoe UI\";\n"
                                       "background-color: #E8E8E8")
        self.top5_name_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top2_id_2 = QLabel(self.Graph_frame_6)
        self.top2_id_2.setObjectName(u"top2_id_2")
        self.top2_id_2.setGeometry(QRect(130, 100, 111, 61))
        self.top2_id_2.setStyleSheet(u"color: #6B7280;\n"
                                     "font: 10pt \"Segoe UI\";\n"
                                     "background-color : #F8F8F8;\n"
                                     "border: none")
        self.top2_id_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top4_id_2 = QLabel(self.Graph_frame_6)
        self.top4_id_2.setObjectName(u"top4_id_2")
        self.top4_id_2.setGeometry(QRect(130, 220, 111, 61))
        self.top4_id_2.setStyleSheet(u"color: #6B7280;\n"
                                     "font: 10pt \"Segoe UI\";\n"
                                     "background-color: #F0F0F0;\n"
                                     "border: none")
        self.top4_id_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top5_id_2 = QLabel(self.Graph_frame_6)
        self.top5_id_2.setObjectName(u"top5_id_2")
        self.top5_id_2.setGeometry(QRect(130, 280, 111, 61))
        self.top5_id_2.setStyleSheet(u"color: #6B7280;\n"
                                     "font: 10pt \"Segoe UI\";\n"
                                     "background-color: #E8E8E8;\n"
                                     "border: none;\n"
                                     "border-bottom :1px solid rgb(25, 86, 179);\n"
                                     "")
        self.top5_id_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top3_id_2 = QLabel(self.Graph_frame_6)
        self.top3_id_2.setObjectName(u"top3_id_2")
        self.top3_id_2.setGeometry(QRect(130, 160, 111, 61))
        self.top3_id_2.setStyleSheet(u"color: #6B7280;\n"
                                     "font: 10pt \"Segoe UI\";\n"
                                     "background-color: #F5F5F5;\n"
                                     "border: none")
        self.top3_id_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top1_id_2 = QLabel(self.Graph_frame_6)
        self.top1_id_2.setObjectName(u"top1_id_2")
        self.top1_id_2.setGeometry(QRect(130, 40, 111, 61))
        self.top1_id_2.setStyleSheet(u"color: #6B7280;\n"
                                     "font: 10pt \"Segoe UI\";\n"
                                     "border: none")
        self.top1_id_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top1_grade_2 = QLabel(self.Graph_frame_6)
        self.top1_grade_2.setObjectName(u"top1_grade_2")
        self.top1_grade_2.setGeometry(QRect(240, 40, 111, 61))
        self.top1_grade_2.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                        "color: rgb(33, 130, 12);\n"
                                        "font: 600 11pt \"Segoe UI\";\n"
                                        "border-top-right-radius: 0px;\n"
                                        "border-bottom-left-radius: 0px;\n"
                                        "border-bottom-right-radius: 0px;\n"
                                        "border: none;\n"
                                        "border-right: 1px solid rgb(25, 86, 179)\n"
                                        "")
        self.top1_grade_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top2_grade_2 = QLabel(self.Graph_frame_6)
        self.top2_grade_2.setObjectName(u"top2_grade_2")
        self.top2_grade_2.setGeometry(QRect(240, 100, 111, 61))
        self.top2_grade_2.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                        "font: 600 11pt \"Segoe UI\";\n"
                                        "border-top-right-radius: 0px;\n"
                                        "border-bottom-left-radius: 0px;\n"
                                        "border-bottom-right-radius: 0px;\n"
                                        "color: rgb(33, 130, 12);\n"
                                        "background-color : #F8F8F8;\n"
                                        "border: none;\n"
                                        "border-right: 1px solid rgb(25, 86, 179)")
        self.top2_grade_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top5_grade_2 = QLabel(self.Graph_frame_6)
        self.top5_grade_2.setObjectName(u"top5_grade_2")
        self.top5_grade_2.setGeometry(QRect(240, 280, 111, 61))
        self.top5_grade_2.setStyleSheet(u"border: none;\n"
                                        "border-right :1px solid rgb(25, 86, 179);\n"
                                        "border-bottom :1px solid rgb(25, 86, 179);\n"
                                        "border-top-left-radius: 0px;\n"
                                        "font: 600 11pt \"Segoe UI\";\n"
                                        "border-top-right-radius: 0px;\n"
                                        "border-bottom-left-radius: 0px;\n"
                                        "border-bottom-right-radius: 40px;\n"
                                        "color: rgb(33, 130, 12);\n"
                                        "background-color: #E8E8E8")
        self.top5_grade_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top4_grade_2 = QLabel(self.Graph_frame_6)
        self.top4_grade_2.setObjectName(u"top4_grade_2")
        self.top4_grade_2.setGeometry(QRect(240, 220, 111, 61))
        self.top4_grade_2.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                        "font: 600 11pt \"Segoe UI\";\n"
                                        "border-top-right-radius: 0px;\n"
                                        "border-bottom-left-radius: 0px;\n"
                                        "border-bottom-right-radius: 0px;\n"
                                        "color: rgb(33, 130, 12);\n"
                                        "background-color: #F0F0F0;\n"
                                        "border:none;\n"
                                        "border-right: 1px solid rgb(25, 86, 179)")
        self.top4_grade_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top3_grade_2 = QLabel(self.Graph_frame_6)
        self.top3_grade_2.setObjectName(u"top3_grade_2")
        self.top3_grade_2.setGeometry(QRect(240, 160, 111, 61))
        self.top3_grade_2.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                        "font: 600 11pt \"Segoe UI\";\n"
                                        "border-top-right-radius: 0px;\n"
                                        "border-bottom-left-radius: 0px;\n"
                                        "border-bottom-right-radius: 0px;\n"
                                        "color: rgb(33, 130, 12);\n"
                                        "background-color: #F5F5F5;\n"
                                        "border: none;\n"
                                        "border-right: 1px solid rgb(25, 86, 179)")
        self.top3_grade_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.full_name_2 = QLabel(self.Graph_frame_6)
        self.full_name_2.setObjectName(u"full_name_2")
        self.full_name_2.setGeometry(QRect(0, 0, 131, 41))
        self.full_name_2.setStyleSheet(u"border-top-left-radius: 40px;\n"
                                       "font: 600 13pt \"Sitka\";\n"
                                       "color: #F9FAFB;\n"
                                       "border-top-right-radius: 0px;\n"
                                       "border-bottom-left-radius: 0px;\n"
                                       "border-bottom-right-radius: 0px;\n"
                                       "background-color: rgb(25, 86, 179)")
        self.full_name_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.grade_lbl_2 = QLabel(self.Graph_frame_6)
        self.grade_lbl_2.setObjectName(u"grade_lbl_2")
        self.grade_lbl_2.setGeometry(QRect(240, 0, 111, 41))
        self.grade_lbl_2.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                       "font: 600 13pt \"Sitka\";\n"
                                       "color: #F9FAFB;\n"
                                       "border-top-right-radius: 40px;\n"
                                       "border-bottom-left-radius: 0px;\n"
                                       "border-bottom-right-radius: 0px;\n"
                                       "background-color: rgb(25, 86, 179)")
        self.grade_lbl_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.id_lbl_2 = QLabel(self.Graph_frame_6)
        self.id_lbl_2.setObjectName(u"id_lbl_2")
        self.id_lbl_2.setGeometry(QRect(130, 0, 111, 41))
        self.id_lbl_2.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                    "font: 600 13pt \"Sitka\";\n"
                                    "color: #F9FAFB;\n"
                                    "border-top-right-radius: 0px;\n"
                                    "border-bottom-left-radius: 0px;\n"
                                    "border-bottom-right-radius: 0px;\n"
                                    "background-color: rgb(25, 86, 179)")
        self.id_lbl_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Graph_frame_3 = HoverFrame(self.page, start=QRect(590, 140, 351, 321), end=QRect(555, 105, 421, 391),
                                        start2=QRect(200, 140, 351, 321), end2=QRect(235, 175, 281, 251))
        self.Graph_frame_3.setObjectName(u"scrollArea_2")
        self.Graph_frame_3.setGeometry(QRect(590, 140, 351, 321))
        self.Graph_frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "border: 2px solid black;")

        self.Graph_frame_4 = HoverFrame(self.page, frame=self.Graph_frame_3, start=QRect(200, 140, 351, 321),
                                        end=QRect(165, 105, 421, 391), start2=QRect(590, 140, 351, 321),
                                        end2=QRect(625, 175, 281, 251))
        self.Graph_frame_3.frame = self.Graph_frame_4
        self.Graph_frame_3.anim2 = QPropertyAnimation(self.Graph_frame_4, b"geometry")
        self.Graph_frame_4.setObjectName(u"scrollArea_3")
        self.Graph_frame_4.setGeometry(QRect(200, 140, 351, 321))
        self.Graph_frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "border: 2px solid black;")

        self.class2_3 = QLabel(self.page)
        self.class2_3.setObjectName(u"class2_2")
        self.class2_3.setGeometry(QRect(230, 480, 41, 16))
        self.class2_3.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                    "font: 600 12pt \"Segoe UI\";")
        self.comboBox2_3 = QComboBox(self.page)
        self.comboBox2_3.setObjectName(u"comboBox2_2")
        self.comboBox2_3.setGeometry(QRect(290, 470, 231, 41))
        self.comboBox2_3.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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

        self.Graph_frame_3.combo1 = self.comboBox2_3

        self.Graph_frame_3.lbl = self.class2_3

        self.Graph_frame_3.com1s = QPoint(290, 470)
        self.Graph_frame_3.com1e = QPoint(290, 435)

        self.Graph_frame_3.lbls = QPoint(230, 480)
        self.Graph_frame_3.lble = QPoint(230, 445)

        self.Graph_frame_4.combo1 = self.comboBox2_3

        self.Graph_frame_4.lbl = self.class2_3
        self.Graph_frame_4.com1s = QPoint(290, 470)
        self.Graph_frame_4.com1e = QPoint(290, 505)

        self.Graph_frame_4.lbls = QPoint(230, 480)
        self.Graph_frame_4.lble = QPoint(230, 515)

        self.malesfemales = QLabel(self.page)
        self.malesfemales.setObjectName(u"average_class")
        self.malesfemales.setGeometry(QRect(200, 100, 351, 31))
        self.malesfemales.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                        "color: rgb(34, 34, 34);")
        self.malesfemales.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.students_per_class = QLabel(self.page)
        self.students_per_class.setObjectName(u"subject_avaeges")
        self.students_per_class.setGeometry(QRect(590, 100, 351, 31))
        self.students_per_class.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                              "color: rgb(34, 34, 34);")
        self.students_per_class.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Graph_frame_4.title = self.malesfemales
        self.Graph_frame_4.start3 = QPoint(200, 100)
        self.Graph_frame_4.end3 = QPoint(200, 65)
        self.Graph_frame_3.title2 = self.malesfemales
        self.Graph_frame_3.start4 = QPoint(200, 100)
        self.Graph_frame_3.end4 = QPoint(200, 135)

        self.Graph_frame_4.title2 = self.students_per_class
        self.Graph_frame_4.start4 = QPoint(590, 100)
        self.Graph_frame_4.end4 = QPoint(590, 135)
        self.Graph_frame_3.title = self.students_per_class
        self.Graph_frame_3.start3 = QPoint(590, 100)
        self.Graph_frame_3.end3 = QPoint(590, 65)

        self.Graph_frame_7 = QFrame(self.page)
        self.Graph_frame_7.setObjectName(u"scrollArea_2")
        self.Graph_frame_7.setGeometry(QRect(170, 140, 511, 331))
        self.Graph_frame_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "border: 2px solid black;")

        self.Graph_frame_8 = QFrame(self.page)
        self.Graph_frame_8.setObjectName(u"scrollArea_2")
        self.Graph_frame_8.setGeometry(QRect(700, 140, 271, 221))
        self.Graph_frame_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "border: 2px solid black;")

        self.comboBox2_5 = QComboBox(self.page)
        self.comboBox2_5.setObjectName(u"comboBox2_2")
        self.comboBox2_5.setGeometry(QRect(740, 370, 191, 41))
        self.comboBox2_5.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.dateEdit5 = QDateEdit(self.page)
        self.dateEdit5.setObjectName(u"dateEdit")
        self.dateEdit5.setGeometry(QRect(740, 420, 191, 41))
        self.dateEdit5.setStyleSheet(u"QDateEdit {border-radius: 15px;\n"
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
        self.dateEdit5.setDate(QDate.currentDate())
        self.dateEdit5.setCalendarPopup(True)

        self.comboBox2_6 = QComboBox(self.page)
        self.comboBox2_6.setObjectName(u"comboBox2_2")
        self.comboBox2_6.setGeometry(QRect(240, 490, 181, 41))
        self.comboBox2_6.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.comboBox2_7 = QComboBox(self.page)
        self.comboBox2_7.setObjectName(u"comboBox2_2")
        self.comboBox2_7.setGeometry(QRect(500, 490, 181, 41))
        self.comboBox2_7.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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

        self.attendace_title = QLabel(self.page)
        self.attendace_title.setObjectName(u"average_class")
        self.attendace_title.setGeometry(QRect(170, 100, 511, 31))
        self.attendace_title.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                           "color: rgb(34, 34, 34);")
        self.attendace_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.attendace_title2 = QLabel(self.page)
        self.attendace_title2.setObjectName(u"average_class")
        self.attendace_title2.setGeometry(QRect(680, 100, 311, 31))
        self.attendace_title2.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                            "color: rgb(34, 34, 34);")
        self.attendace_title2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.classe = QLabel(self.page)
        self.classe.setObjectName(u"average_class")
        self.classe.setGeometry(QRect(160, 495, 100, 31))
        self.classe.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")
        self.classe.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.year = QLabel(self.page)
        self.year.setObjectName(u"average_class")
        self.year.setGeometry(QRect(420, 495, 100, 31))
        self.year.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                "font: 600 12pt \"Segoe UI\";")
        self.year.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def Statistics_retranslate(self, Dialog):
        self.top1_name.setText("")
        self.top2_name.setText("")
        self.top4_name.setText("")
        self.top3_name.setText("")
        self.top5_name.setText("")
        self.top2_id.setText("")
        self.top4_id.setText("")
        self.top5_id.setText("")
        self.top3_id.setText("")
        self.top1_id.setText("")
        self.top1_grade.setText("")
        self.top2_grade.setText("")
        self.top5_grade.setText("")
        self.top4_grade.setText("")
        self.top3_grade.setText("")
        self.full_name.setText(QCoreApplication.translate("Dialog", u"Full Name", None))
        self.grade_lbl.setText(QCoreApplication.translate("Dialog", u"Grade", None))
        self.id_lbl.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.label_16.setText("")
        self.class2_1.setText(QCoreApplication.translate("Dialog", u"Class     ", None))
        self.class2_2.setText(QCoreApplication.translate("Dialog", u"Class     ", None))
        self.average_class.setText(QCoreApplication.translate("Dialog", u"Class Average Scores", None))
        self.top_students.setText(QCoreApplication.translate("Dialog", u"Top 5 Students by Grade", None))
        self.malesfemales.setText(QCoreApplication.translate("Dialog", u"Gender Distribution", None))
        self.students_per_class.setText(QCoreApplication.translate("Dialog", u"Students per Class", None))
        self.subject_averages.setText(QCoreApplication.translate("Dialog", u"Subject Average Scores", None))
        self.top_students_3.setText(QCoreApplication.translate("Dialog", u"Top 5 Students by Attendance", None))
        self.top1_name_2.setText("")
        self.top2_name_2.setText("")
        self.top4_name_2.setText("")
        self.top3_name_2.setText("")
        self.top5_name_2.setText("")
        self.top2_id_2.setText("")
        self.top4_id_2.setText("")
        self.top5_id_2.setText("")
        self.top3_id_2.setText("")
        self.top1_id_2.setText("")
        self.top1_grade_2.setText("")
        self.top2_grade_2.setText("")
        self.top5_grade_2.setText("")
        self.top4_grade_2.setText("")
        self.top3_grade_2.setText("")
        self.full_name_2.setText(QCoreApplication.translate("Dialog", u"Full Name", None))
        self.grade_lbl_2.setText(QCoreApplication.translate("Dialog", u"Presence", None))
        self.id_lbl_2.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.performance.setText(QCoreApplication.translate("Dialog", u"Performance", None))
        self.ranking.setText(QCoreApplication.translate("Dialog", u"Ranking", None))
        self.attendancetop.setText(QCoreApplication.translate("Dialog", u"Attendance", None))
        self.other.setText(QCoreApplication.translate("Dialog", u"Other", None))
        self.attendace_title.setText(QCoreApplication.translate("Dialog", u"Monthly Attendance Rate (%) ", None))
        self.attendace_title2.setText(QCoreApplication.translate("Dialog", u"Attendance Status Distribution ", None))
        self.classe.setText(QCoreApplication.translate("Dialog", u"Class ", None))
        self.year.setText(QCoreApplication.translate("Dialog", u"Year ", None))
        self.class2_3.setText(QCoreApplication.translate("Dialog", u"Class     ", None))


