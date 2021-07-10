# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 23:16:29 2020

@author: ASUS
"""


from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100')

var = tk.StringVar()
l = tk.Label(window,textvariable=var, bg='green', font=('Arial', 12), width=15, height=2 ).pack()  

on_hit1 = False  

def hit_me():
    global on_hit1
    if on_hit1 == False:  
        on_hit1 = True
        var.set('press the button')   
    else:      
        on_hit1 = False
        var.set(' cancel the button') 

b = tk.Button(window,text='hit me', width=15, height=2,command=hit_me).pack()   

window.mainloop()