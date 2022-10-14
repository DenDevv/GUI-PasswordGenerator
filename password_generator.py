import os
import sys
import threading
import secrets

from PyQt5 import QtWidgets, QtGui


class GUI(QtWidgets.QMainWindow):
    statuses = {
        "c_lower": True,
        "c_upper": True,
        "c_numbers": True,
        "c_symbols": True,
        "length": 12
    }

    clipboard = []

    def __init__(self, parent = None):
        from themes.dark_theme import Ui_MainWindow
        
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.c_lower.setChecked(True)
        self.ui.c_upper.setChecked(True)
        self.ui.c_numbers.setChecked(True)
        self.ui.c_symbols.setChecked(True)

        threading.Thread(target=self.init_UI).start()

    def init_UI(self):
        self.ui.c_lower.clicked.connect(self._lower)
        self.ui.c_upper.clicked.connect(self._upper)
        self.ui.c_numbers.clicked.connect(self._numbers)
        self.ui.c_symbols.clicked.connect(self._symbols)
        self.ui.generate_button.clicked.connect(self._generate)
        self.ui.copy.clicked.connect(self._clipboard)
        
        self.ui.length.valueChanged[int].connect(self._length)
    
    def _lower(self, status):
        self.statuses["c_lower"] = status

    def _upper(self, status):
        self.statuses["c_upper"] = status

    def _numbers(self, status):
        self.statuses["c_numbers"] = status

    def _symbols(self, status):
        self.statuses["c_symbols"] = status

    def _length(self, num):
        self.ui.length_label_2.setText(str(num))
        self.statuses["length"] = num

    def _generate(self):
        try:
            lower = 'abcdefghigklmnopqrstuvyxwz'
            upper = lower.upper()
            digits = '0123456789'
            symbols = '~!@#$%&*_-=+,.?\/|";'

            password = ""
            create_password = ""

            if self.statuses.get("c_lower") == True:
                create_password += lower
            
            if self.statuses.get("c_upper") == True:
                create_password += upper
            
            if self.statuses.get("c_numbers") == True:
                create_password += digits
            
            if self.statuses.get("c_symbols") == True:
                create_password += symbols

            for _ in range(self.statuses.get("length")):
                password += secrets.choice(create_password)

            if any(i in digits for i in password):
                pass
            else:
                password = password.replace(secrets.choice(password[secrets.randbelow(len(password))]), secrets.choice("0123456789"))

            self.ui.copy.setText("Copy")
            self.ui.lineEdit.setText(password)
            self.clipboard.clear()
            self.clipboard.append(self.ui.lineEdit.text())
        except:
            pass
        
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