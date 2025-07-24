from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox,
)
import sys
import os
from PyQt5.QtGui import QPixmap 

def add(username, password):
    if username and password:
        with open("passwords.txt", 'a') as f:
            f.write(f"{username}:{password}\n")
        return True, "Password added successfully!"
    else:
        return False, "Please enter both username and password."

def get(username):
    passwords = {}
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.strip().split(':')
                if len(i) == 2:
                    passwords[i[0]] = i[1]
    except Exception as e:
        return False, "Error, nothing matches."

    if passwords:
        if username in passwords:
            return True, f"Password for {username} is {passwords[username]}"
        else:
            return False, "No password found for that username."
    else:
        return False, "No passwords stored."

def getlist():
    passwords = {}
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.strip().split(':')
                if len(i) == 2:
                    passwords[i[0]] = i[1]
    except:
        return False, "Error, No passwords found."

    if passwords:
        mess = "List of passwords:\n"
        for name, password in passwords.items():
            mess += f"Password for {name} is {password}\n"
        return True, mess
    else:
        return False, "No passwords stored."

def delete(username):
    temp_pass = []
    found = False
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.strip().split(':')
                if len(i) == 2 and i[0] != username:
                    temp_pass.append(f"{i[0]}:{i[1]}")
                elif len(i) == 2 and i[0] == username:
                    found = True
        with open("passwords.txt", 'w') as f:
            for line in temp_pass:
                f.write(line + '\n')
        if found:
            return True, f"User {username} deleted successfully!"
        else:
            return False, "User not found."
    except:
        return False, "Could not delete user. Please check the username and try again."

class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyWord - Really unsafe password manager (PyQt5)")
        self.setGeometry(100, 100, 400, 300)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Username
        user_layout = QHBoxLayout()
        self.labelName = QLabel("Username:")
        self.entryName = QLineEdit()
        user_layout.addWidget(self.labelName)
        user_layout.addWidget(self.entryName)
        layout.addLayout(user_layout)

        # cute label
        img_label = QLabel()
        pixmap = QPixmap("Assets/phroog.png")
        img_label.setPixmap(pixmap)
        layout.addWidget(img_label)

        # Password
        pass_layout = QHBoxLayout()
        self.labelPassword = QLabel("Password:")
        self.entryPassword = QLineEdit()
        self.entryPassword.setEchoMode(QLineEdit.Password)
        # Set custom mask character (e.g., '*')
        self.entryPassword.setPasswordCharacter('*')
        pass_layout.addWidget(self.labelPassword)
        pass_layout.addWidget(self.entryPassword)
        layout.addLayout(pass_layout)

        # Buttons
        btn_layout = QHBoxLayout()
        self.addBtn = QPushButton("Add")
        self.getBtn = QPushButton("Get")
        self.listBtn = QPushButton("List All")
        self.delBtn = QPushButton("Delete")
        btn_layout.addWidget(self.addBtn)
        btn_layout.addWidget(self.getBtn)
        btn_layout.addWidget(self.listBtn)
        btn_layout.addWidget(self.delBtn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        # Connect buttons
        self.addBtn.clicked.connect(self.add_password)
        self.getBtn.clicked.connect(self.get_password)
        self.listBtn.clicked.connect(self.list_passwords)
        self.delBtn.clicked.connect(self.delete_password)

    def add_password(self):
        username = self.entryName.text()
        password = self.entryPassword.text()
        success, msg = add(username, password)
        if success:
            QMessageBox.information(self, "Success", msg)
        else:
            QMessageBox.warning(self, "Input Error", msg)

    def get_password(self):
        username = self.entryName.text()
        success, msg = get(username)
        if success:
            QMessageBox.information(self, "Password", msg)
        else:
            QMessageBox.warning(self, "Error", msg)

    def list_passwords(self):
        success, msg = getlist()
        if success:
            QMessageBox.information(self, "Passwords", msg)
        else:
            QMessageBox.warning(self, "Error", msg)

    def delete_password(self):
        username = self.entryName.text()
        success, msg = delete(username)
        if success:
            QMessageBox.information(self, "Success", msg)
        else:
            QMessageBox.warning(self, "Error", msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordManager()
    window.show()
    sys.exit(app.exec_())
