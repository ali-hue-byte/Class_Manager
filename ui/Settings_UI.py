from Logic.Utils import HoverButton

from PySide6.QtCore import QCoreApplication, QRect

from PySide6.QtWidgets import QLabel, QLineEdit, QComboBox

class SettingsUI(object):
    def Settings_setup(self, Dialog):
        self.transfer_btn = HoverButton(self.page)
        self.transfer_btn.setObjectName(u"transfer_btn")
        self.transfer_btn.setGeometry(QRect(520, 510, 91, 31))
        self.transfer_btn.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                        "color : rgb(255,255,255);\n"
                                        "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                        "border-radius: 15px}\n"
                                        "\n"
                                        "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                        "color: rgb(255,255,255)\n"
                                        "}")
        self.score_settings_lbl = QLabel(self.page)
        self.score_settings_lbl.setObjectName(u"score_settings_lbl")
        self.score_settings_lbl.setGeometry(QRect(180, 105, 241, 41))
        self.score_settings_lbl.setStyleSheet(u"font: 700 20pt \"Segoe UI Variable\";\n"
                                              "color: rgb(51, 51, 51);")
        self.info2 = QLabel(self.page)
        self.info2.setObjectName(u"requirederrfirst_22")
        self.info2.setGeometry(QRect(340, 220, 180, 16))
        self.info2.setStyleSheet(u"color: #6B7280;\n"
                                 u"font-size: 11px;")

        self.score_line = QLineEdit(self.page)
        self.score_line.setObjectName(u"score_line")
        self.score_line.setGeometry(QRect(340, 170, 221, 41))
        self.score_line.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
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
        self.transfe_lbl = QLabel(self.page)
        self.transfe_lbl.setObjectName(u"transfe_lbl")
        self.transfe_lbl.setGeometry(QRect(180, 320, 251, 31))
        self.transfe_lbl.setStyleSheet(u"font: 700 20pt \"Segoe UI Variable\";\n"
                                       "color: rgb(51, 51, 51);")
        self.to_combobox = QComboBox(self.page)
        self.to_combobox.setObjectName(u"to_combobox")
        self.to_combobox.setGeometry(QRect(680, 440, 221, 41))
        self.to_combobox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.errscore_lbl = QLabel(self.page)
        self.errscore_lbl.setObjectName(u"errscore_lbl")
        self.errscore_lbl.setGeometry(QRect(340, 220, 300, 16))
        self.errscore_lbl.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.max_score_lbl = QLabel(self.page)
        self.max_score_lbl.setObjectName(u"max_score_lbl")
        self.max_score_lbl.setGeometry(QRect(170, 180, 161, 16))
        self.max_score_lbl.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                         "font: 600 12pt \"Segoe UI\";")
        self.to_lbl = QLabel(self.page)
        self.to_lbl.setObjectName(u"to_lbl")
        self.to_lbl.setGeometry(QRect(630, 450, 21, 16))
        self.to_lbl.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")
        self.from_combobox = QComboBox(self.page)
        self.from_combobox.setObjectName(u"from_combobox")
        self.from_combobox.setGeometry(QRect(300, 440, 221, 41))
        self.from_combobox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.set_btn = HoverButton(self.page)
        self.set_btn.setObjectName(u"set_btn")
        self.set_btn.setGeometry(QRect(520, 260, 91, 31))
        self.set_btn.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                   "color : rgb(255,255,255);\n"
                                   "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                   "border-radius: 15px}\n"
                                   "\n"
                                   "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                   "color: rgb(255,255,255)\n"
                                   "}")
        self.id_combobox = QComboBox(self.page)
        self.id_combobox.setObjectName(u"id_combobox")
        self.id_combobox.setGeometry(QRect(490, 370, 241, 41))
        self.id_combobox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.from_lbl = QLabel(self.page)
        self.from_lbl.setObjectName(u"from_lbl")
        self.from_lbl.setGeometry(QRect(230, 450, 51, 16))
        self.from_lbl.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                    "font: 600 12pt \"Segoe UI\";")
        self.id_lbl2 = QLabel(self.page)
        self.id_lbl2.setObjectName(u"id_lbl")
        self.id_lbl2.setGeometry(QRect(390, 380, 100, 16))
        self.id_lbl2.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                   "font: 600 12pt \"Segoe UI\";")

    def Settings_retranslate(self, Dialog):
        self.transfer_btn.setText(QCoreApplication.translate("Dialog", u"Transfer", None))
        self.score_settings_lbl.setText(QCoreApplication.translate("Dialog", u"Score Settings", None))
        self.score_line.setPlaceholderText("20")
        self.transfe_lbl.setText(QCoreApplication.translate("Dialog", u"Transfer Student", None))
        self.errscore_lbl.setText(QCoreApplication.translate("Dialog", u"", None))
        self.max_score_lbl.setText(QCoreApplication.translate("Dialog", u"Set Maximum Score", None))
        self.to_lbl.setText(QCoreApplication.translate("Dialog", u"To", None))
        self.set_btn.setText(QCoreApplication.translate("Dialog", u"Set", None))
        self.from_lbl.setText(QCoreApplication.translate("Dialog", u"From", None))
        self.id_lbl2.setText(QCoreApplication.translate("Dialog", u"Student ID", None))
        self.info2.setText(QCoreApplication.translate("Dialog", u"Default value: 20", None))