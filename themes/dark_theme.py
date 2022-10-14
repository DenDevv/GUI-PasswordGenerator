from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(574, 475)
        MainWindow.setStyleSheet("background-color: #2C3E50;")
        MainWindow.setFixedWidth(580)
        MainWindow.setFixedHeight(475)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(160, 30, 261, 21))
        self.logo_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.logo_label.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 25px;\n")
        self.logo_label.setObjectName("logo_label")

        pixmap = QtGui.QPixmap("images/logo.png")
        self.labelImage = QtWidgets.QLabel(self.centralwidget)
        self.labelImage.setGeometry(QtCore.QRect(240, 80, 100, 95))
        self.labelImage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelImage.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "font-size: 20px;\n"
        "color: white;")
        self.labelImage.setObjectName("labelImage")
        self.labelImage.setPixmap(pixmap)
        self.labelImage.setScaledContents(True)

        self.c_lower = QtWidgets.QCheckBox(self.centralwidget)
        self.c_lower.setGeometry(QtCore.QRect(80, 270, 91, 20))
        self.c_lower.setObjectName("c_lower")
        self.c_lower.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_lower.setStyleSheet("""
            QCheckBox {
                color: white;
                font-size: 13px;
            }

            QCheckBox::indicator {
                border: 3px solid rgb(74,84,103);
                width: 15px;
                height: 15px;
                border-radius: 5px;
                background: rgb(61,69,84);
            }

            QCheckBox::indicator:hover {
                border: 3px solid rgb(81,92,112);
            }

            QCheckBox::indicator:checked {
                background: 3px solid rgb(61,69,84);
                border: 3px solid rgb(74,84,103);	
                background-image: url(images/cil-check-alt.png);
            }
            """
            )

        self.c_upper = QtWidgets.QCheckBox(self.centralwidget)
        self.c_upper.setGeometry(QtCore.QRect(195, 270, 91, 20))
        self.c_upper.setObjectName("c_upper")
        self.c_upper.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_upper.setStyleSheet("""
            QCheckBox {
                color: white;
                font-size: 13px;
            }

            QCheckBox::indicator {
                border: 3px solid rgb(74,84,103);
                width: 15px;
                height: 15px;
                border-radius: 5px;
                background: rgb(61,69,84);
            }

            QCheckBox::indicator:hover {
                border: 3px solid rgb(81,92,112);
            }

            QCheckBox::indicator:checked {
                background: 3px solid rgb(61,69,84);
                border: 3px solid rgb(74,84,103);	
                background-image: url(images/cil-check-alt.png);
            }
            """
            )

        self.c_numbers = QtWidgets.QCheckBox(self.centralwidget)
        self.c_numbers.setGeometry(QtCore.QRect(310, 270, 81, 20))
        self.c_numbers.setObjectName("c_numbers")
        self.c_numbers.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_numbers.setStyleSheet("""
            QCheckBox {
                color: white;
                font-size: 13px;
            }

            QCheckBox::indicator {
                border: 3px solid rgb(74,84,103);
                width: 15px;
                height: 15px;
                border-radius: 5px;
                background: rgb(61,69,84);
            }

            QCheckBox::indicator:hover {
                border: 3px solid rgb(81,92,112);
            }

            QCheckBox::indicator:checked {
                background: 3px solid rgb(61,69,84);
                border: 3px solid rgb(74,84,103);	
                background-image: url(images/cil-check-alt.png);
            }
            """
            )

        self.c_symbols = QtWidgets.QCheckBox(self.centralwidget)
        self.c_symbols.setGeometry(QtCore.QRect(420, 270, 81, 20))
        self.c_symbols.setObjectName("c_symbols")
        self.c_symbols.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_symbols.setStyleSheet("""
            QCheckBox {
                color: white;
                font-size: 13px;
            }

            QCheckBox::indicator {
                border: 3px solid rgb(74,84,103);
                width: 15px;
                height: 15px;
                border-radius: 5px;
                background: rgb(61,69,84);
            }

            QCheckBox::indicator:hover {
                border: 3px solid rgb(81,92,112);
            }

            QCheckBox::indicator:checked {
                background: 3px solid rgb(61,69,84);
                border: 3px solid rgb(74,84,103);	
                background-image: url(images/cil-check-alt.png);
            }
            """
            )

        self.length = QtWidgets.QSlider(self.centralwidget)
        self.length.setMinimum(12)
        self.length.setMaximum(256)
        self.length.setGeometry(QtCore.QRect(80, 360, 411, 22))
        self.length.setOrientation(QtCore.Qt.Horizontal)
        self.length.setObjectName("length")
        self.length.setStyleSheet("""
            QSlider::groove:horizontal {
                border-radius: 5px;
                height: 15px;
                margin: 0px;
                background-color: rgb(63,89,115);
            }

            QSlider::groove:horizontal:hover {
                background-color: rgb(73,103,133);
            }

            QSlider::handle:horizontal {
                background-color: rgb(61,179,158);
                height: 20px;
                width: 20px;
                margin: 0px;
                border-radius: 5px;
            }

            QSlider::handle:horizontal:hover {
                background-color: rgb(63,161,185);
            }

            QSlider::handle:horizontal:pressed {
                background-color: rgb(73,215,173);
            }
        """)

        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setGeometry(QtCore.QRect(220, 407, 131, 41))
        self.generate_button.setObjectName("generate_button")
        self.generate_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generate_button.setStyleSheet("QPushButton {\n"
        "    font-family: \"Eras Bold ITC\";\n"
        "    border-radius: 10px;\n"
        "    background-color: #3db39e;\n"
        "    color: white;\n"
        "    font-size: 20px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3ca492;\n"
        "    color: white;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3d9888;\n"
        "    color: white;\n"
        "}")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 200, 421, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setStyleSheet(
            "color: white;\n"
            "font-family: \"Eras Bold ITC\";\n"
            "outline: none;\n"
            "background-color: #3C556E;\n"
            "border: 2px solid #5B81A6;\n"
            "border-radius: 5px;")

        self.length_label = QtWidgets.QLabel(self.centralwidget)
        self.length_label.setGeometry(QtCore.QRect(225, 300, 261, 61))
        self.length_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.length_label.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "font-size: 20px;\n"
        "color: white;")
        self.length_label.setObjectName("length_label")

        self.length_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.length_label_2.setGeometry(QtCore.QRect(315, 300, 261, 61))
        self.length_label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.length_label_2.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 20px;")
        self.length_label_2.setText("12")
        self.length_label_2.setObjectName("length_label_2")

        self.copy = QtWidgets.QPushButton(self.centralwidget)
        self.copy.setGeometry(QtCore.QRect(490, 200, 71, 31))
        self.copy.setObjectName("copy")
        self.copy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copy.setStyleSheet("QPushButton {\n"
        "    font-family: \"Eras Bold ITC\";\n"
        "    border-radius: 6px;\n"
        "    background-color: #3db39e;\n"
        "    color: white;\n"
        "    font-size: 14px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: #3ca492;\n"
        "    color: white;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color: #3d9888;\n"
        "    color: white;\n"
        "}")

        MainWindow.setCentralWidget(self.centralwidget)        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.logo_label.setText(_translate("MainWindow", "Password Generator"))
        self.c_lower.setText(_translate("MainWindow", "Lowercase"))
        self.c_upper.setText(_translate("MainWindow", "Uppercase"))
        self.c_numbers.setText(_translate("MainWindow", "Numbers"))
        self.c_symbols.setText(_translate("MainWindow", "Symbols"))
        self.generate_button.setText(_translate("MainWindow", "Generate"))
        self.length_label.setText(_translate("MainWindow", "Length: "))
        self.copy.setText(_translate("MainWindow", "Copy"))