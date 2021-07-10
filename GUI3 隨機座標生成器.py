import tkinter as tk 
import random
win=tk.Tk()

win.title("Random X,Y Generater")
win.geometry("500x450")



title_text=tk.Label(text="Random X,Y Generater",font="微軟正黑體 20")
title_text.pack()

min_range = tk.Label(text="min range")
min_range.pack()
min_entry = tk.Entry()
min_entry.pack()

max_range = tk.Label(text="max range")
max_range.pack()
max_entry = tk.Entry()
max_entry.pack()

x_show = tk.Label()
x_show.pack()
y_show = tk.Label()
y_show.pack()

def gen_xy():
    min_val = int(min_entry.get())
    max_val = int(max_entry.get())
    x = str(random.randint(min_val, max_val))
    y = str(random.randint(min_val, max_val))
    x_show.config(text=x)
    y_show.config(text=y)
    
    
generate_btn = tk.Button(text="generate",command = gen_xy)
generate_btn.pack()


win.mainloop()