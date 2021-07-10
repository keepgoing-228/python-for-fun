# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:32:26 2020

@author: ASUS
"""
import serial
ser = serial.Serial('COM3',9600,timeout=1)


try:
    while True:
        while ser.in_waiting:
            data_raw = ser.readline()
            data = data_raw.decode()
            #print('接收到的原始資料:',data_raw)
            print('接收到的資料:',data)
            

except KeyboardInterrupt:
    ser.close()
    print('再見~')
