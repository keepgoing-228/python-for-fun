# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 22:59:57 2020

@author: ASUS
"""



import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog as sd
from tkinter import filedialog as fd
import serial



def connecting():
    ser = serial.Serial('COM3',9600,timeout=1)
    try:
        while True:
            while ser.in_waiting:
                data_raw = ser.readline()
                data = data_raw.decode()
                var.set(data)
                
                
    
    except KeyboardInterrupt:
        ser.close()
        print('再見~')

    
def do_setting1():
    str_input = sd.askinteger("設定儲存鎖定值", "請輸入儲存鎖定值")  
    print("{}".format(str_input, type(str_input)))

def do_setting2():
    str_input = sd.askinteger("設定總重鎖定值", "請輸入總重鎖定值")  
    print("{}".format(str_input, type(str_input)))

def do_setting3():
    str_input = sd.askinteger("設定母豬身分資料", "請輸入母豬身分資料")  
    print("{}".format(str_input, type(str_input)))

def do_setting4():
    str_input = sd.askinteger("設定仔豬身分資料", "請輸入仔豬身分資料")  
    print("{}".format(str_input, type(str_input)))

def frame1():
    frm_1 = tk.Frame(win)
    frm_1.place(x=0,y=10)
    btn_set1 = tk.Button(frm_1,text="設定儲存鎖定值",command=do_setting1)
    btn_set1.grid(row=0,column=0)
    btn_set2 = tk.Button(frm_1,text="設定總重鎖定值",command=do_setting2)
    btn_set2.grid(row=0,column=1)
    btn_set3 = tk.Button(frm_1,text="設定母豬身分資料",command=do_setting3)
    btn_set3.grid(row=1,column=0)
    btn_set4 = tk.Button(frm_1,text="設定仔豬身分資料",command=do_setting4)
    btn_set4.grid(row=1,column=1)
    btn_connect = tk.Button(frm_1,command=connecting,text="連線")
    btn_connect.grid(row=0,column=2)
    btn_disconnect = tk.Button(frm_1,text="中斷連線")
    btn_disconnect.grid(row=0,column=3)
    cbb_com = ttk.Combobox(frm_1,values=["comport7","comport8","comport9"])
    cbb_com.grid(row=2,column=0)
    cbb_staff = ttk.Combobox(frm_1,values=["小明","阿嬌"])
    cbb_staff.grid(row=2,column=1)
    
def frame2():
    frm_2 = tk.Frame(win)
    frm_2.place(x=0,y=200)
    frm_2_up = tk.Frame(frm_2)
    frm_2_down = tk.Frame(frm_2)
    frm_2_up.pack(side='top')
    frm_2_down.pack(side='bottom')
    lb_sow =  tk.Label(frm_2_up,text="母豬資料")
    lb_sow.grid(row=0,column=0)
    lb_smallpig = tk.Label(frm_2_up,text="仔豬資料")
    lb_smallpig.grid(row=0,column=1)
    en_sow = tk.Entry(frm_2_up)
    en_sow.grid(row=1,column=0)
    en_smallpig = tk.Entry(frm_2_up)
    en_smallpig.grid(row=1,column=1)
    btn_zero = tk.Button(frm_2_down,text="歸零")
    btn_zero.grid(row=0,column=0)
    btn_clean = tk.Button(frm_2_down,text="清除上筆")
    btn_clean.grid(row=0,column=1)

def frame3():
    frm_3 = tk.Frame(win)
    frm_3.place(x=500,y=10)
    lb_nowshow = tk.Label(frm_3,text="目前秤值")
    lb_nowshow.grid(row=0,column=0)
    label_weighing_nowshow = tk.Label(frm_3,textvariable=var,height=1,width=20)
    label_weighing_nowshow.grid(row=1,column=0)
    lb_lastshow = tk.Label(frm_3,text="上筆記錄")
    lb_lastshow.grid(row=2,column=0)
    lb_savenum = tk.Label(frm_3,text="已存豬數")
    lb_savenum.grid(row=2,column=1)
    text_weighing_lastshow = tk.Text(frm_3,height=1,width=20)
    text_weighing_lastshow.grid(row=3,column=0)
    text_weighing_savenum = tk.Text(frm_3,height=1,width=20)
    text_weighing_savenum.grid(row=3,column=1)

def frame4():
    frm_4 = tk.Frame(win)
    frm_4.place(x=500,y=200)
    setting = tk.Label(frm_4,text="設定內容")
    setting.grid(row=0,column=1)
    history = tk.Label(frm_4,text="歷史紀錄")
    history.grid(row=0,column=2)
    text_setting = tk.Text(frm_4,height=10,width=20)
    text_setting.grid(row=1,column=1)
    
    text_history = tk.Text(frm_4,height=10,width=20)
    text_history.grid(row=1,column=2)
    
    
    temp = tk.StringVar()
    setting_context = tk.LabelFrame(frm_4,padx=5, pady=5)
    setting_context.grid(column=0,row=1)
    r1 = tk.Label(setting_context, text="狀態:"+temp.get()).pack(anchor="w")
    r2 = tk.Label(setting_context, text="儲存鎖定值:"+temp.get()).pack(anchor="w")
    r3 = tk.Label(setting_context, text="總重鎖定值:"+temp.get()).pack(anchor="w")
    r4 = tk.Label(setting_context, text="運算速度:"+temp.get()).pack(anchor="w")
    r5 = tk.Label(setting_context, text="紀錄路徑:"+temp.get()).pack(anchor="w")
    r6 = tk.Label(setting_context, text="秤電量:"+temp.get()).pack(anchor="w")



win = tk.Tk()
win.title("仔豬磅秤")
win.geometry("900x500+200+200")

var = tk.StringVar()

frame1()
frame2()
frame3()
frame4()


win.mainloop()
