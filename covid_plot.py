# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:11:47 2020

@author: Divyanshu kumar
"""
import matplotlib.pyplot as plt
import pandas as pd

#READING DATA FROM ourworldindata.org----------------------------
total_c=pd.read_csv("https://covid.ourworldindata.org/data/ecdc/total_cases.csv")
#total_d=pd.read_csv("https://covid.ourworldindata.org/data/ecdc/total_deaths.csv")
#new_c=pd.read_csv("https://covid.ourworldindata.org/data/ecdc/new_cases.csv")
#new_d=pd.read_csv("https://covid.ourworldindata.org/data/ecdc/new_deaths.csv")
#full_data=pd.read_csv("https://covid.ourworldindata.org/data/ecdc/full_data.csv")
#------------------------------------------------------------------


x=total_c['date']


print("------The worst affected country plot-USA------")
plt.figure()
plt.plot(x,total_c['United States'])
plt.title("USA Total detected vs Time")


y=[]
for i in range(0,len(total_c['United States'])-1):
    y.append(total_c['United States'][i+1]-total_c['United States'][i])
y.append(0)

plt.figure()
plt.title("USA new cases vs previous cases")
plt.plot(total_c['United States'],y,'ro')


#USA_ratio=0.0
#for i in range(0,len(total_c['United States'])):
 #   if USA_ratio+=


print("-------Origin country plot- CHINA-------")
plt.figure()
plt.title("CHINA total detected vs time")
plt.plot(x,total_c['China'])

y1=[]
for i in range(0,len(total_c['China'])-1):
    y1.append(total_c['China'][i+1]-total_c['China'][i])
y1.append(0)
plt.figure()
plt.title("CHINA new case vs previous case")
plt.plot(total_c['China'],y1,'ro')


print("-----Next Most populous country- INDIA ------")
plt.figure()
plt.title("India Total detected vs time")
plt.plot(x,total_c['India'])

plt.figure()
plt.title("India new cases vs previous cases")

y2=[]
for i in range(0,len(total_c['India'])-1):
    y2.append(total_c['India'][i+1]-total_c['India'][i])
y2.append(0)
plt.plot(total_c['India'],y2,'ro')

print(len(y2))
print(len(total_c['India']))

