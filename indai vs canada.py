# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:08:40 2020

@author: Divyanshu kumar
"""

import matplotlib.pyplot as plt
import pandas as pd

data1=pd.read_csv("https://covid.ourworldindata.org/data/ecdc/total_cases.csv")
y1=data1['Canada']
y2=data1['India']
y_c=[]
y_i=[]
commonn=0
for l in range(len(y1)):
    if y1[l]!=0:
        commonn+=1
commonn-=4
print (commonn)
for i in range(len(y1)):
    if y1[i]!=0 and len(y_c)<commonn+1:
        y_c.append(y1[i])
    if y2[i]!=0 and len(y_i)<commonn+1:
        y_i.append(y2[i])

x=range(1,len(y_c)+1)
plt.figure()
plt.title("INDIA - red || CANADA - blue || Total vs time")
plt.xlabel("DAYS(time)")
plt.ylabel("TOTAL cases predicted to date")
plt.plot(x,y_c)
x=range(1,len(y_i)+1)
plt.plot(x,y_i)

plt.show()