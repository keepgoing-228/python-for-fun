# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:40:16 2020

@author: ASUS
"""


import tkinter as tk
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
#btn = tk.Button(text="buttton")
#btn.pack()


frm = tk.Frame(win)
frm.pack()


frm_r = tk.Frame(frm)
frm_l = tk.Frame(frm)
frm_r.pack(side='right')
frm_l.pack(side='left')

lb1 = tk.Label(frm_l,text="嗨嗨嗨",bg="skyblue").pack()
lb2 = tk.Label(frm_l,text="你最近好嘛").pack()
lb3 = tk.Label(frm_r,text="嗨~").pack()

win.mainloop()