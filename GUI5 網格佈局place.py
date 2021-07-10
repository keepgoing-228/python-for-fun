# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:51:23 2020

@author: ASUS
"""
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("")
win.geometry("200x200+600+200")

#btn = tk.Button(text="button")
#btn.pack()
#btn = tk.Button(text="button")
#btn.pack()
#btn = tk.Button(text="button")
#btn.pack()
#btn = tk.Button(text="button")
#btn.pack()

#place佈局
btn = ttk.Button(text="buttton")
btn.place(anchor=tk.CENTER ,x=100,y=100)


win.mainloop()