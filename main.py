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

def get():
    username = entryName.get()
    passwords = {}
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                #create key-value pair for username and password
                passwords[i[0]] = i[i]
    except:
        print("Uh oh, shit's fucked bro")

    if passwords:
        mess = "Your password:\n"
        for i in passwords:
            if i == username:
                mess += f"Password for {username} is {passwords[i]}\n"
                break
        
        else:
            mess += "Dave's not here man"
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "M/t as fuck my guy")