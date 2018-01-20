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
#loading dataset 
full_data = pd.read_csv('FullData.csv')


#//////////////////////////////////////////////////////////////////////////////////
#Analysis on best attribute

Africa = {'Algeria','Guinea Bissau','São Tomé & Príncipe','Guinea Bissau ','DR Congo',
          'Central African Rep.','Angola','Benin','Botswana','Burkina Faso'
          ,'Burundi','Cameroon','Cape Verde','Central African Republic','Chad','Comoros',
          'Congo','Congo Democratic Republic of','Djibouti','Egypt','Equatorial Guinea','Eritrea',
          'Ethiopia','Gabon','Gambia','Ghana','Guinea','Guinea-Bissau','Ivory Coast','Kenya','Lesotho',
          'Liberia','Libya','Madagascar','Malawi','Mali','Mauritania','Mauritius','Morocco','Mozambique',
          'Namibia','Niger','Nigeria','Rwanda','Sao Tome and Principe','Senegal','Seychelles','Sierra Leone',
          'Somalia','South Africa','South Sudan','Sudan','Swaziland','Tanzania','Togo','Tunisia','Uganda','Zambia',
          'Zimbabwe','Burkina Faso'}



Asia = {'Afghanistan','China PR','Korea Republic','Palestine','Korea DPR','Timor-Leste','Chinese Taipei',
        'Bahrain','Armenia','Bangladesh','Azerbaijan','Bhutan','Brunei','Burma (Myanmar)','Cambodia','China',
        'East Timor','India','Indonesia','Iran','Iraq','Israel','Japan','Jordan','Georgia','Kazakhstan',
        'North Korea','South Korea','Kuwait','Kyrgyzstan','Laos','Lebanon','Malaysia','Maldives','Mongolia',
        'Nepal','Oman','Pakistan','Philippines','Qatar','Russian Federation','Saudi Arabia','Singapore','Sri Lanka',
        'Syria','Tajikistan','Thailand','Turkey','Turkmenistan','United Arab Emirates','Uzbekistan','Vietnam','Yemen'}


Europe = {'Albania','FYR Macedonia','Faroe Islands','Serbia','Gibraltar','Kosovo','Bosnia Herzegovina','Andorra',
          'Scotland','Austria','Belarus','Belgium','Bosnia and Herzegovina','Bulgaria','Croatia','Cyprus','Czech Republic',
          'Denmark','Estonia','Finland','France','Germany','Greece','Hungary','Iceland','Republic of Ireland','Italy','Latvia',
          'Liechtenstein','Northern Ireland','Lithuania','Luxembourg','Macedonia','Malta','Moldova','Monaco','Montenegro',
          'Netherlands','Norway','Poland','Portugal','Romania','Russia','San Marino','Serbi','Slovakia','Slovenia','Spain',
          'Sweden','Switzerland','Ukraine','England','Vatican City','Republic of Ireland','Wales'}


North_America = {'Antigua and Barbuda','Puerto Rico','St Lucia','Antigua & Barbuda','Montserrat','Bermuda',
                 'St Kitts Nevis','Bahamas','Barbados','Belize','Canada','Costa Rica','Cuba','Dominica',
                 'Dominican Republic','El Salvador','Grenada','Guatemala','Haiti','Honduras','Jamaica','Mexico',
                 'Nicaragua','Panama','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines',
                 'Trinidad and Tobago','United States'}


Australia = {'Australia','FIFA16_NationName_215','Guam','Fiji','Kiribati','Marshall Islands','Micronesia',
             'Nauru','New Zealand','Palau','Papua New Guinea','Samoa','Solomon Islands','Tonga','Tuvalu','Vanuatu'}


South_America ={'Argentina','Curacao','Trinidad & Tobago','Aruba','Bolivia','Brazil','Chile','Colombia',
                'Ecuador','Guyana','Paraguay','Peru','Suriname','Uruguay','Venezuela'}

f_d = full_data

for i in range(0,17588):
    if f_d.loc[i,"Nationality"] in Africa:
        f_d.loc[i,"Nationality"]='Africa'
        
    elif f_d.loc[i,"Nationality"] in North_America:
        f_d.loc[i,"Nationality"]='North_America'
        
    elif f_d.loc[i,"Nationality"] in Australia:
        f_d.loc[i,"Nationality"]='Australia'
        
    elif f_d.loc[i,"Nationality"] in South_America:
        f_d.loc[i,"Nationality"]='South_America'
        
    elif f_d.loc[i,"Nationality"] in Europe:
        f_d.loc[i,"Nationality"]='Europe'
    
    elif f_d.loc[i,"Nationality"] in Asia:
        f_d.loc[i,"Nationality"]='Asia'
    
        
Goal_Keeping = []

for i in range(0,17588):
    sum=full_data.loc[i,"GK_Positioning"]+full_data.loc[i,"GK_Diving"]+full_data.loc[i,"GK_Kicking"]+full_data.loc[i,"GK_Handling"]+full_data.loc[i,"GK_Reflexes"]
    Goal_Keeping.append(sum/5)
    
#print Goal_Keeping
        
#Taking two dimensional matrix
a = [[0 for x in range(25)] for y in range(6)]
        
#List of continents    
Continent = ["Africa","Asia","Australia","Europe","North_America","South_America"]

#grouping each continent and finding mean of the attributes w.t.r to them
x1 = f_d.groupby('Nationality')["Ball_Control"].mean()

#copying to 2d matrix
for i in range(0,6):
    a[i][0]=x1[i]
    
    
x2 = f_d.groupby('Nationality')["Dribbling"].mean()

#copying to 2d matrix
for i in range(0,6):
    a[i][1]=x2[i]
x3 = f_d.groupby('Nationality')["Penalties"].mean()

#copying to 2d matrix
for i in range(0,6):
    a[i][2]=x3[i]

x4 = f_d.groupby('Nationality')["Freekick_Accuracy"].mean()

#copying to 2d matrix
for i in range(0,6):
    a[i][3]=x4[i]
x5 = f_d.groupby('Nationality')["Volleys"].mean()

#copying to 2d matrix
for i in range(0,6):
    a[i][4]=x5[i]
    
x6 = f_d.groupby('Nationality')["Vision"].mean()

#copying to 2d matrix
for i in range(0,6):
    a[i][5]=x6[i]
    
x7 = f_d.groupby('Nationality')["Long_Shots"].mean()

#copying to 2d matrix
for i in range(0,6):
    a[i][6]=x7[i]
    
x8 = f_d.groupby('Nationality')["Long_Pass"].mean()

#copying to 2d matrix
for i in range(0,6):
    a[i][7]=x8[i]
    
x9 = f_d.groupby('Nationality')["Speed"].mean()

#copying to 2d matrix
for i in range(0,6):
    a[i][8]=x9[i]
    
x10 = f_d.groupby('Nationality')["Stamina"].mean()
#print x10

for i in range(0,6):
    a[i][9]=x10[i]
    
'''
plt.figure(figsize=(9,8))
Stamina = pd.DataFrame({"Continent" : Continent,
                             "Stamina" : x10})
sns.barplot(x = "Continent",y = "Stamina",data = ball_control)
plt.title("Stamina According to Continent")

'''


x11 = f_d.groupby('Nationality')["Balance"].mean()
#print x11

for i in range(0,6):
    a[i][10]=x11[i]
    
'''
plt.figure(figsize=(9,8))
Balance = pd.DataFrame({"Continent" : Continent,
                             "Balance" : x11})
sns.barplot(x = "Continent",y = "Balance",data = ball_control)
plt.title("Balance According to Continent")
'''

x12 = f_d.groupby('Nationality')["Crossing"].mean()
#print x12

for i in range(0,6):
    a[i][11]=x12[i]
    
'''
plt.figure(figsize=(9,8))
Crossing = pd.DataFrame({"Continent" : Continent,
                             "Crossing" : x12})
sns.barplot(x = "Continent",y = "Crossing",data = ball_control)
plt.title("Crossing According to Continent")
'''

x13 = f_d.groupby('Nationality')["Curve"].mean()
#print x13

for i in range(0,6):
    a[i][12]=x13[i]
    
'''
plt.figure(figsize=(9,8))
Curve = pd.DataFrame({"Continent" : Continent,
                             "Curve" : x13})
sns.barplot(x = "Continent",y = "Curve",data = ball_control)
plt.title("Curve According to Continent")
'''


x14 = f_d.groupby('Nationality')["Finishing"].mean()
#print x14
for i in range(0,6):
    a[i][13]=x14[i]
    
'''

plt.figure(figsize=(9,8))
Finishing = pd.DataFrame({"Continent" : Continent,
                             "Finishing" : x14})
sns.barplot(x = "Continent",y = "Finishing",data = ball_control)
plt.title("Finishing According to Continent")
'''

x15 = f_d.groupby('Nationality')["Strength"].mean()
#print x15

for i in range(0,6):
    a[i][14]=x15[i]
    
'''
plt.figure(figsize=(9,8))
Strength = pd.DataFrame({"Continent" : Continent,
                             "Strength" : x15})
sns.barplot(x = "Continent",y = "Strength",data = ball_control)
plt.title("Strength According to Continent")

'''
x16 = f_d.groupby('Nationality')["Marking"].mean()
#print x16

for i in range(0,6):
    a[i][15]=x16[i]
    
    
x17 = f_d.groupby('Nationality')["Sliding_Tackle"].mean()

for i in range(0,6):
    a[i][16]=x17[i]

'''
plt.figure(figsize=(9,8))
Marking = pd.DataFrame({"Continent" : Continent,
                             "Marking" : x16})
sns.barplot(x = "Continent",y = "Marking",data = ball_control)
plt.title("Marking According to Continent")
'''
x18 = f_d.groupby('Nationality')["Standing_Tackle"].mean()

for i in range(0,6):
    a[i][17]=x18[i]
    
    
x19 = f_d.groupby('Nationality')["Jumping"].mean()

for i in range(0,6):
    a[i][18]=x19[i]
    
x20 = f_d.groupby('Nationality')["Short_Pass"].mean()

for i in range(0,6):
    a[i][19]=x20[i]
    
    
x21 = f_d.groupby('Nationality')["Shot_Power"].mean()

for i in range(0,6):
    a[i][20]=x21[i]
    
x22 = f_d.groupby('Nationality')["Attacking_Position"].mean()

for i in range(0,6):
    a[i][21]=x22[i]
    
x23 = f_d.groupby('Nationality')["Heading"].mean()

for i in range(0,6):
    a[i][22]=x23[i]


x24 = f_d.groupby('Nationality')["Agility"].mean()

for i in range(0,6):
    a[i][23]=x24[i]
    
f_dt = pd.DataFrame({"Nationality" :f_d['Nationality'],
                     "Goal_Keeping" : Goal_Keeping})


x25 = f_dt.groupby('Nationality')['Goal_Keeping'].mean()

for i in range(0,6):
    a[i][24]=x25[i]



Attributes = ['Ball_Control','Dribbling','Penalties','Freekick_Accuracy','Volleys','Vission','Long_Shots','Long_Pass','Speed','Stamina','Balance',
              'Crossing','Curve','Finishing','Strength','Marking','Sliding_Tackle','Standing_Tackle','Jumping',
              'Shot_Pass','Shot_Power','Attacking_Position','Heading','Agility','Goal_Keeping']
list = []
for i in range(0,25):
    list.append(a[5][i])
    
south = pd.DataFrame({
        "Attributes" : Attributes,
        "Values" : list})
    
plt.figure(figsize=(10,10))
plt.xlabel("Values",fontsize=12)
plt.ylabel("Attributes",fontsize=12)
sns.barplot(x = "Values",y = "Attributes",data = south)    
plt.title("Graph Showing Best Attributes of Players of South_America Continent",fontsize=14)
plt.show()

list=[]
for i in range(0,25):
    list.append(a[4][i])
    
north = pd.DataFrame({
        "Attributes" : Attributes,
        "Values" : list})
    
plt.figure(figsize=(10,10))
plt.xlabel("Values",fontsize=12)
plt.ylabel("Attributes",fontsize=12)
sns.barplot(x = "Values",y = "Attributes",data = north)    
plt.title("Graph Showing Best Attributes of Players of North_America Continent",fontsize=14)
plt.show()    
       
list=[]
for i in range(0,25):
    list.append(a[3][i])
    
europe = pd.DataFrame({
        "Attributes" : Attributes,
        "Values" : list})
    
plt.figure(figsize=(10,10))
plt.xlabel("Values",fontsize=12)
plt.ylabel("Attributes",fontsize=12)
sns.barplot(x = "Values",y = "Attributes",data = europe)    
plt.title("Graph Showing Best Attributes of Players of Europe Continent",fontsize=14)
plt.show() 

list=[]
for i in range(0,25):
    list.append(a[0][i])   
africa = pd.DataFrame({
        "Attributes" : Attributes,
        "Values" : list})   
plt.figure(figsize=(10,10))
plt.xlabel("Values",fontsize=12)
plt.ylabel("Attributes",fontsize=12)
sns.barplot(x = "Values",y = "Attributes",data = africa)    
plt.title("Graph Showing Best Attributes of Players of Africa Continent",fontsize=14)
plt.show()   
#print summary

#summary.plot()
#print max(x)
            

