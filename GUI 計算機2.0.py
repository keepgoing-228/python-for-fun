# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:06:54 2020

@author: ASUS
"""

import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog as sd

def mymethod(*args):# Button executes me
    var=tk.var.get # Gets var from Entry textvariable
    var=var*10
    var2.set(var) # Set for StringVar for our Label below

    

win = tk.Tk()
win.title("my calculator")
win.geometry("300x500+200+200")


 
#example for a label from a button press event
var=tk.StringVar()
var2=tk.StringVar() # Is set by the method when invoked.
 
l1=tk.Label(text="I will Change Soon !", textvariable=var2).pack()# shows the methods .set var2
e1=tk.Entry(textvariable=var).pack()# will show whats typed as var
b1=tk.Button(text="Times By Ten !",command=mymethod).pack()# executes the mymethod




win.mainloop()