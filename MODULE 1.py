# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 23:06:05 2017

@author: HP
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io

df=pd.read_csv("C:/Users/HP/Desktop/MINI 5/Dataset_FIFA/FullData.csv")

drop_cols = ['National_Position','National_Kit','Club_Kit','Club_Joining','Contract_Expiry']
df['Club_Joining'] = pd.to_datetime(df['Club_Joining'])
#Sorting players by date to keep only the leatest attributes in a  descending order,as some players
#are registered in different clubs due to transfers.
df = df[~df.Club_Position.isnull()].sort_values('Club_Joining', ascending=False)
#keeping the first as it will be the leatest attributes and club for the player.
df = df.drop_duplicates(subset='Name', keep='first')
#Delete the unwanted columes
df= df.drop(drop_cols, axis=1)
#Resort Players by making top players first
df= df.sort_values('Rating', ascending=False)
df = df.reset_index(drop=True)
df.head()
Signed_Player = df[df.Club != 'Free Agents']
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(223)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(221)
ax4 = fig.add_subplot(224)
ax1.set_title('KDE PLOT OF ATTACKING POSITION-RATING')
sns.kdeplot(Signed_Player.Finishing,Signed_Player.Attacking_Position, shade=True,cmap="Greens",ax=ax1)
ax2.set_title('KDE PLOT OF FINISHING-AGE')
sns.kdeplot(Signed_Player.Finishing,Signed_Player.Age, shade=True,cmap="Blues",ax=ax2)
ax3.set_title('KDE PLOT OF COMPOSURE-AGE')
sns.kdeplot(Signed_Player.Composure,Signed_Player.Age, shade=True,cmap="Reds",ax=ax3)
ax4.set_title('KDE PLOT OF SKILL MOVES-FINISHING')
sns.kdeplot(Signed_Player.Skill_Moves,Signed_Player.Finishing, shade=True,cmap="rainbow",ax=ax4)
arr=[]
print("                      ::BEST GOAL SCORERS::")
print('Name, Nationality, National_Position, National_Kit, Club')
with io.open('C:/Users/HP/Desktop/MINI 5/Dataset_FIFA/FullData.csv','r',encoding='utf-8')as myfile:
    data1=myfile.read().splitlines()
    data=data1[0].split(',')
    for i in range(1,len(data)-1):
        if((data[i]=="Attacking_Position")or(data[i]=="Finishing")or(data[i]=="Shot_Power")or(data[i]=="Long_Shots")or(data[i]=="Volleys")or(data[i]=="Freekick_Accuracy")or(data[i]=="Penalties")or(data[i]=="Composure")):
            arr.append(i)   
i=1
with io.open('C:/Users/HP/Desktop/MINI 5/Dataset_FIFA/FullData.csv','r',encoding='utf-8')as myfile:
    data1=myfile.read().splitlines()
    for i in range(1,len(data1)-1):
        data=data1[i].split(',')
        sum=0
        k=0
        i=i+1
        for j in arr:
            s=arr[k]
            m=float(data[s])
            sum=sum+m
            k=k+1
        sum1=float(sum/8)
        if(sum1>82):
           print(data[0:5])    