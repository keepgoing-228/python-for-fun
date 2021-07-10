import tkinter as tk
win = tk.Tk()

win.title("小豬秤重")
win.geometry("500x450")

def ok():
    text = en.get()
    lb.config(text=text)
    


lb = tk.Label(text="this is label",bg="blue")
lb.pack()

en = tk.Entry()
en.pack()

btn = tk.Button(text="OK",command=ok)
btn.pack()


win.mainloop()