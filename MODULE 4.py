# -*- coding: utf-8 -*-
"""


@author: 
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import itertools as it
import seaborn as sns


#reload(sys)  
#sys.setdefaultencoding('utf8')


#loading dataset 
full_data = pd.read_csv('FullData.csv')

#initalising the matrix
a = [[0 for x in range(16)] for y in range(16)]

#list of clubs
Club = ['Arsenal','Bor. Dortmund','Chelsea','FC Barcelona','FC Bayern',
        'Juventus','Liverpool','Manchester City','Manchester Utd', 'PSG', 'Real Madrid']

 
#filtering the data
f_d = full_data[full_data["Rating"]>85]


#Taking mean of rach attribute according to club
x1 = f_d.groupby('Club')["Ball_Control"].mean()
print (x1)

#copying data into 2d matrix
for i in range(0,6):
    a[i][0]=x1[i]


x2 = f_d.groupby('Club')["Dribbling"].mean()

#copying data into 2d matrix
for i in range(0,6):
    a[i][1]=x2[i]

x3 = f_d.groupby('Club')["Penalties"].mean()

#copying data into 2d matrix
for i in range(0,6):
    a[i][2]=x3[i]



x4 = f_d.groupby('Club')["Freekick_Accuracy"].mean()
#print x4

for i in range(0,6):
    a[i][3]=x4[i]
'''
plt.figure(figsize=(9,8))
Freekick_Accuracy = pd.DataFrame({"Club" : Club,
                             "Dribbling" : x4})
sns.barplot(x = "Club",y = "Freekick_Accuracy",data = ball_control)
plt.title("Freekick_Accuracy Accordin to Club")

'''

x5 = f_d.groupby('Club')["Volleys"].mean()
#print x5
for i in range(0,6):
    a[i][4]=x5[i]
    
'''
plt.figure(figsize=(9,8))
Volleys = pd.DataFrame({"Club" : Club,
                             "Volleys" : x5})
sns.barplot(x = "Club",y = "Volleys",data = ball_control)
plt.title("Volleys According to Club")
'''



x6 = f_d.groupby('Club')["Vision"].mean()
#print x6

for i in range(0,6):
    a[i][5]=x6[i]
    
'''
plt.figure(figsize=(9,8))
Vision = pd.DataFrame({"Club" : Club,
                             "Vision" : x6})
sns.barplot(x = "Club",y = "Vision",data = ball_control)
plt.title("Vision According to Club")
'''


x7 = f_d.groupby('Club')["Long_Shots"].mean()
#print x7

for i in range(0,6):
    a[i][6]=x7[i]
    
'''
plt.figure(figsize=(9,8))
Long_Shots = pd.DataFrame({"Club" : Club,
                             "Dribbling" : x7})
sns.barplot(x = "Club",y = "Long_Shots",data = ball_control)
plt.title("Long_Shots According to Club")
'''


x8 = f_d.groupby('Club')["Long_Pass"].mean()
#print x8

for i in range(0,6):
    a[i][7]=x8[i]
    
'''
plt.figure(figsize=(9,8))
Long_Pass = pd.DataFrame({"Club" : Club,
                             "Long_Pass" : x8})
sns.barplot(x = "Club",y = "Long_Pass",data = ball_control)
plt.title("Long_Pass According to Club")
'''



x9 = f_d.groupby('Club')["Speed"].mean()
#print x9

for i in range(0,6):
    a[i][8]=x9[i]
    
'''
plt.figure(figsize=(9,8))
Speed = pd.DataFrame({"Club" : Club,
                             "Speed" : x9})
sns.barplot(x = "Club",y = "Speed",data = ball_control)
plt.title("Speed According to Club")
'''


x10 = f_d.groupby('Club')["Stamina"].mean()
#print x10

for i in range(0,6):
    a[i][9]=x10[i]
    
'''
plt.figure(figsize=(9,8))
Stamina = pd.DataFrame({"Club" : Club,
                             "Stamina" : x10})
sns.barplot(x = "Club",y = "Stamina",data = ball_control)
plt.title("Stamina According to Club")

'''


x11 = f_d.groupby('Club')["Balance"].mean()
#print x11

for i in range(0,6):
    a[i][10]=x11[i]
    
'''
plt.figure(figsize=(9,8))
Balance = pd.DataFrame({"Club" : Club,
                             "Balance" : x11})
sns.barplot(x = "Club",y = "Balance",data = ball_control)
plt.title("Balance According to Club")
'''

x12 = f_d.groupby('Club')["Crossing"].mean()
#print x12

for i in range(0,6):
    a[i][11]=x12[i]
    
'''
plt.figure(figsize=(9,8))
Crossing = pd.DataFrame({"Club" : Club,
                             "Crossing" : x12})
sns.barplot(x = "Club",y = "Crossing",data = ball_control)
plt.title("Crossing According to Club")
'''

x13 = f_d.groupby('Club')["Curve"].mean()
#print x13

for i in range(0,6):
    a[i][12]=x13[i]
    
'''
plt.figure(figsize=(9,8))
Curve = pd.DataFrame({"Club" : Club,
                             "Curve" : x13})
sns.barplot(x = "Club",y = "Curve",data = ball_control)
plt.title("Curve According to Club")
'''


x14 = f_d.groupby('Club')["Finishing"].mean()
#print x14
for i in range(0,6):
    a[i][13]=x14[i]
    
'''

plt.figure(figsize=(9,8))
Finishing = pd.DataFrame({"Club" : Club,
                             "Finishing" : x14})
sns.barplot(x = "Club",y = "Finishing",data = ball_control)
plt.title("Finishing According to Club")
'''

x15 = f_d.groupby('Club')["Strength"].mean()
#print x15

for i in range(0,6):
    a[i][14]=x15[i]
'''
plt.figure(figsize=(9,8))
Strength = pd.DataFrame({"Club" : Club,
                             "Strength" : x15})
sns.barplot(x = "Club",y = "Strength",data = ball_control)
plt.title("Strength According to Club")

'''
x16 = f_d.groupby('Club')["Marking"].mean()
#print x16

for i in range(0,6):
    a[i][15]=x16[i]
    
'''
plt.figure(figsize=(9,8))
Marking = pd.DataFrame({"Club" : Club,
                             "Marking" : x16})
sns.barplot(x = "Club",y = "Marking",data = ball_control)
plt.title("Marking According to Club")
'''


Attributes = ['Ball_Control','Dribbling','Penalties','Freekick_Accuracy','Volleys',
              'Vision','Long_Shots','Long_Pass','Speed','Stamina','Balance','Crossing',
              'Curve','Finishing','Strength','Marking']
list = []
for i in range(0,16):
    list.append(a[0][i]) 
    
#making nwe datframe
Arsenal = pd.DataFrame({
        "Attributes" : Attributes,
        "Value" : list})
plt.figure(figsize=(9,8))
sns.barplot(x = "Value",y = "Attributes",data = Arsenal)    
plt.xlabel("Values",fontsize=12)
plt.ylabel("Attributes",fontsize=12)
plt.title("Showing best attributes that Club Arsenal Prefers",fontsize=16)

list = []
for i in range(0,16):
    list.append(a[3][i])
#making nwe datframe
Dortmund = pd.DataFrame({
        "Attributes" : Attributes,
        "Value" : list})
plt.figure(figsize=(9,8))
sns.barplot(x = "Value",y = "Attributes",data = Dortmund)    
plt.xlabel("Values",fontsize=12)
plt.ylabel("Attributes",fontsize=12)
plt.title("Showing best attributes that Club Dortmund Prefers",fontsize=16)  
      

list = []
for i in range(0,16):
    list.append(a[4][i])
#making nwe datframe
Chelsea = pd.DataFrame({
        "Attributes" : Attributes,
        "Value" : list})
plt.figure(figsize=(9,8))
sns.barplot(x = "Value",y = "Attributes",data = Chelsea)    
plt.xlabel("Values",fontsize=12)
plt.ylabel("Attributes",fontsize=12)
plt.title("Showing best attributes that Club Chelsea Prefers",fontsize=16)  


list = []
for i in range(0,16):
    list.append(a[5][i])
#making nwe datframe
Barcelona  = pd.DataFrame({
        "Attributes" : Attributes,
        "Value" : list})
plt.figure(figsize=(9,8))
sns.barplot(x = "Value",y = "Attributes",data = Barcelona )    
plt.xlabel("Values",fontsize=12)
plt.ylabel("Attributes",fontsize=12)
plt.title("Showing best attributes that Club FC Barcelona Prefers",fontsize=16) 

#print f_d
