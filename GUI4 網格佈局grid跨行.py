# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:32:30 2020

@author: ASUS
"""


import tkinter as tk

win = tk.Tk()

win.title("")
win.geometry("+500+200")

#網格布局
user = tk.Label(text="user:")
user.grid(row=0,column=0)

password = tk.Label(text="password: ")
password.grid(row=1,column=0)

user_entry = tk.Entry(font="微軟正黑體 20")
user_entry.grid(row=0,column=1,rowspan=2)


win.mainloop()