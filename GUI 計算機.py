# -*- coding: utf-8 -*-
"""
Created on Wed May 20 13:35:15 2020

"""

import tkinter as tk

class Calculator(tk.Frame):
    def _init_(self):
        tk.Frame._init_(self)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.lblNum=tk.Label(self ,text="0")
        self.btnNum1= tk.Button(self ,text="1",command = self.clickBtnNum1)
        self.lblNum.grid(row = 0,column = 0)
        self.btnNum1.grid(row = 1, column = 0)
    def clickBtnNum1(self):
        self.lblNum.configure(text =self.lblNum.cget("text") +"1"
        



cal = Calculator()
cal.master.title("My calculator")
cal.mainloop()