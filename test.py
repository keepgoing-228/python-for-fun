# import tkinter as tk


# def click1():
#     str = "我已經被按過了！"


# win = tk.Tk()
# str = "hello"
# label1 = tk.Label(win, text=str)
# label1.pack()
# button1 = tk.Button(win, text='hihi', command=click1)
# button1.pack()
# win.mainloop()

def checkPW():
    if(pw.get() == "1234"):
        msg.set("密碼正確，歡迎登入！")
    else:
        msg.set("密碼錯誤，請修正密碼！")

import tkinter as tk

win = tk.Tk()
pw = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(win, text="請輸入密碼：")
label.pack()
entry = tk.Entry(win, textvariable=pw)
entry.pack()
button = tk.Button(win, text="登入", command=checkPW)
button.pack()
lblmsg = tk.Label(win, fg="red", textvariable=msg)
lblmsg.pack()
win.mainloop()