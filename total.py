# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:42:53 2020

@author: ASUS
"""


score = []
total = inscore = 0

while(inscore >= 0):
    inscore = int(input("please input number: "))
    score.append(inscore)

print("共有%d位學生" %(len(score)-1))


for i in range (len(score)-1):
    total += score[i]
    print("hi")

average = total / (len(score)-1)

print("總成績:%d，平均:%d分" %(total,average))