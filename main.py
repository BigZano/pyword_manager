import tkinter as tk
from tkinter import messagebox

def add():
    username = entryName.get()
    password = entryPassword.get()
    if username and password:
        with open("passwords.txt", 'a') as f:
            f.write(f"{username}:{password}\n")
        messagebox.showinfo("Success", "Password added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please enter both username and password.")