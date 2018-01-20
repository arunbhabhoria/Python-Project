# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 01:35:55 2017

@author: HP
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
arr=[]
print('BEST MIDFIELDERS')
with io.open('C:/Users/HP/Desktop/MINI 5/Dataset_FIFA/FullData.csv','r',encoding='utf-8')as myfile:
    data1=myfile.read().splitlines()
    data=data1[0].split(',')
    for i in range(1,len(data)-1):
        if((data[i]=="Ball_Control")or(data[i]=="Dribbling")or(data[i]=="Reactions")or(data[i]=="Interceptions")or(data[i]=="Vision")or(data[i]=="Crossing")or(data[i]=="Agility")or(data[i]=="Acceleration")or(data[i]=="Balance")or(data[i]=="Speed")or(data[i]=="Curve")):
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
        sum1=float(sum/11)
        if(sum1>80):
           print(data[0:5])

             