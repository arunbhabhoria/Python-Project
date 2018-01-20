# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:36:06 2017

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
df=pd.read_csv("C:/Users/HP/Desktop/MINI 5/Dataset_FIFA/FullData.csv")
x=df['Aggression'].tolist()
y=df['Age'].tolist()
z=df['Rating'].tolist()
plt.scatter(x,y,alpha=0.05)
plt.xlabel('Aggression')
plt.ylabel('Age')
plt.title('Aggression Vs. Age')
plt.show()
plt.scatter(z,x,alpha=0.04,color='red',edgecolors='black')
plt.xlabel('Rating')
plt.ylabel('Aggression')
plt.title('Rating Vs. Aggression')
plt.show()
arr=[]
print("\n\nPlayers with Best ON-Field Behaviour")
print('Name, Nationality, National_Position, National_Kit, Club') 
i=1
with io.open('C:/Users/HP/Desktop/MINI 5/Dataset_FIFA/FullData.csv','r',encoding='utf-8')as myfile:
    data1=myfile.read().splitlines()
    for i in range(1,len(data1)-1):
        data=data1[i].split(',')
        i=i+1
        if((int(data[24])>20) and (int(data[24])<50) and (int(data[9])>80) and (int(data[14])>22)):
           print(data[0:5])
        