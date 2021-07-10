import tkinter as tk
win = tk.Tk()

#標題
win.title("小豬秤重")

#大小
win.geometry("400x200")
#win.minsize(width=400, height=200)
#win.maxsize(width=500, height=300)
win.resizable(0,0)

#icon
#win.iconbitmap()

#顏色
win.config(bg="skyblue")

#透明度
#win.attributes("-alpha", 0.857)

#置頂
win.attributes("-topmost",1)


#function
def say_hi():
    print("Hi everyone!!")

#button
btn = tk.Button(text="開始")
#btn.config(width=10,height=5)
btn.config(command=say_hi)
btn.pack()


win.mainloop()
