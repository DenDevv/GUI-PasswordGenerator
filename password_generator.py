import os
import sys
import threading
import secrets

from functools import partial
from string import (
    ascii_lowercase as lower, 
    ascii_uppercase as upper,
    digits
)

from PyQt5 import QtWidgets, QtGui


class GUI(QtWidgets.QMainWindow):
    statuses = {
        "c_lower": True,
        "c_upper": True,
        "c_digits": True,
        "c_symbols": True,
    }
    length = 12
    clipboard = []

    def __init__(self, parent = None):
        from themes.dark_theme import Ui_MainWindow
        
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.c_lower.setChecked(True)
        self.ui.c_upper.setChecked(True)
        self.ui.c_digits.setChecked(True)
        self.ui.c_symbols.setChecked(True)

        threading.Thread(target=self.init_UI).start()

    def init_UI(self):
        self.ui.c_lower.stateChanged.connect(partial(
            self.update_status, args=["lower", self.ui.c_lower]
        ))

        self.ui.c_upper.stateChanged.connect(partial(
            self.update_status, args=["upper", self.ui.c_upper]
        ))

        self.ui.c_digits.stateChanged.connect(partial(
            self.update_status, args=["digits", self.ui.c_digits]
        ))

        self.ui.c_symbols.stateChanged.connect(partial(
            self.update_status, args=["symbols", self.ui.c_symbols]
        ))
        
        self.ui.generate_button.clicked.connect(self._generate)
        self.ui.copy.clicked.connect(self._clipboard)

        self.ui.length.valueChanged[int].connect(self._length)

    def update_status(self, args):
        self.statuses["c_" + args[0]] = bool(args[1].checkState())
    
    def _length(self, num):
        self.ui.length_label_2.setText(str(num))
        self.length = num

    def _generate(self):
        symbols = '~!@#$%&*_-=+,.?\/|";'

        if any(self.statuses):
            password = ""

            for _ in range(self.length):
                password += secrets.choice(
                    self.update_strength(
                        {
                            "lower": lower, 
                            "upper": upper,
                            "digits": digits,
                            "symbols": symbols
                        }
                    )
                )

            if not any(i in digits for i in password) and self.statuses['c_digits']:
                password = password.replace(
                    secrets.choice(
                        password[secrets.randbelow(len(password))]
                    ), 
                    secrets.choice(digits)
                )

            self.ui.copy.setText("Copy")
            self.ui.lineEdit.setText(password)
            self.clipboard.clear()
            self.clipboard.append(self.ui.lineEdit.text())

    def update_strength(self, _dict: dict):
        create_password = ""

        for k, v in _dict.items():
            if self.statuses["c_" + k]:
                create_password += v
        return create_password

    def _clipboard(self):
        try:
            cb = QtWidgets.QApplication.clipboard()
            cb.clear(mode=cb.Clipboard)
            cb.setText(self.clipboard[0], mode=cb.Clipboard)
            self.ui.copy.setText("Copied!")
        except:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    if not os.path.isdir("./images") and not os.path.isdir("./themes"):
        error = QtWidgets.QMessageBox()
        error.setWindowTitle("Missing files error")
        error.setText('Some important files are missing!')
        error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        error.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Close)
        error.exec_()
    else:
        win = GUI()
        win.setWindowTitle("PasswordGenerator - v1.0")
        win.setWindowIcon(QtGui.QIcon("images/icon.jpg"))
        win.show()
        sys.exit(app.exec_())