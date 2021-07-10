# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:42:41 2020

@author: ASUS
"""


import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

def open_file():
    openfilename=fd.askopenfilename(initialdir="/",title="Select file",\
                 filetypes = (("text files","*.txt"),("all files","*.*")))
    print (openfilename)
    try:
        with open(openfilename,'r') as file:
            print(file.read())
    except:
        print("檔案不存在!") 
def save_file():
    f=fd.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    f.write("Hello World!")
    f.close() 

root=tk.Tk()
root.title("檔案開啟 & 儲存檔案")
ttk.Button(root, text="開啟檔案", command=open_file).pack()
ttk.Button(root, text="儲存檔案", command=save_file).pack()
root.mainloop()