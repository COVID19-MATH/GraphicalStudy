# -*- coding: utf-8 -*-

"""
Created on Wed Apr  8 18:02:20 2020
DETECTING NEW CASES USING MACHINE LEARNING-INDIA
@author: Divyanshu kumar
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


def gradient_dec(x1,y):
    lr=0.0000001
    lr1=0.3
    i=1000
    m_curr=0
    b_curr=0
    n=len(x1)
    print("|Iteration|slope|Constant|Cost|")
    for l in range(0,i):
        y_pred=m_curr*x1+b_curr
        md=-(2/n)*sum(x1*(y-y_pred))
        bd=-(2/n)*sum(y-y_pred)
        m_curr-=(lr*md)
        b_curr-=(lr1*bd)
        cost=(1/n)*sum([val**2 for val in (y-y_pred)])
        print(l,"    ",m_curr, "     ",b_curr,"  ",cost)
        if l==i-1:
            m_learnt=m_curr
            b_learnt=b_curr
    what_learnt=[m_learnt,b_learnt]
    return what_learnt


data1=pd.read_csv("https://covid.ourworldindata.org/data/ecdc/total_cases.csv")
x=data1['India']

for e in range(0,len(x)):
    if math.isnan(x[e]):
        x[e]=(x[e+1]+x[e-1])/2

y=np.array([])
x1=np.array([])

for i in range(0,len(x)-1):
    x1=np.append(x1,[float(x[i])])        
    y=np.append(y,[float(x[i+1])-float(x[i])])

plt.figure()
plt.title("India - new cases vs previous cases- linear regression")
plt.plot(x1,y,'ro')



what_learnt=gradient_dec(x1,y)

y_for_plot=[]
for t in range(len(x1)):
    y_for_plot.append(what_learnt[0]*x1[t]+what_learnt[1])
plt.plot(x1,y_for_plot)
plt.xlabel("All cases detected to date")
plt.ylabel("New cases (daily)")
ren=len(x)-1
print("New Cases predicted=", x[ren]*what_learnt[0]+what_learnt[1], "Total predicted=",x[ren]*what_learnt[0]+what_learnt[1]+x[ren])
plt.show()
