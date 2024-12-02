import tkinter as tk
from tkinter import messagebox
from in_memory_db import InMemoryDB


db = InMemoryDB()


def begin_transaction():
    try:
        message = db.begin_transaction()
        messagebox.showinfo("Success", message)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def commit():
    try:
        # Call the backend commit() method and capture its message
        message = db.commit()
        messagebox.showinfo("Success", message)  # Display the backend message in the GUI
    except Exception as e:
        messagebox.showerror("Error", str(e))


def rollback():
    try:
        # Call backend and display its return message
        message = db.rollback()
        messagebox.showinfo("Success", message)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def put():
    key = key_entry.get()
    value = value_entry.get()
    try:
        message = db.put(key, int(value))
        messagebox.showinfo("Success", message)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def get():
    key = key_entry.get()
    try:
        message = db.get(key)
        messagebox.showinfo("Result", message)
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("In-Memory Database GUI")

# Key Entry
tk.Label(root, text="Key:").grid(row=0, column=0)
key_entry = tk.Entry(root)
key_entry.grid(row=0, column=1)

# Value Entry
tk.Label(root, text="Value:").grid(row=1, column=0)
value_entry = tk.Entry(root)
value_entry.grid(row=1, column=1)

# Buttons
tk.Button(root, text="Begin Transaction", command=begin_transaction).grid(row=2, column=0)
tk.Button(root, text="Commit", command=commit).grid(row=2, column=1)
tk.Button(root, text="Rollback", command=rollback).grid(row=2, column=2)
tk.Button(root, text="Put", command=put).grid(row=3, column=0)
tk.Button(root, text="Get", command=get).grid(row=3, column=1)

root.mainloop()
