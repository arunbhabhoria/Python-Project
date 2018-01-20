#5.
import pandas as pd                                    
import numpy as np                                       
import matplotlib.pyplot as plt  
import seaborn as sns                                                                                  
df=pd.read_csv("C:/Users/HP/Desktop/MINI 5/Dataset_FIFA/FullData.csv")

a=(df.loc[:,'Contract_Expiry']==2023).sum()
b=(df.loc[:,'Contract_Expiry']==2022).sum()
c=(df.loc[:,'Contract_Expiry']==2021).sum()
d=(df.loc[:,'Contract_Expiry']==2020).sum()
e=(df.loc[:,'Contract_Expiry']==2019).sum()
f=(df.loc[:,'Contract_Expiry']==2018).sum()
print("No. of players having Contract Expiry in 2023:")
print(a)                 
print("No. of players having Contract Expiry in 2022:")
print(b)   
print("No. of players having Contract Expiry in 2021:")
print(c)   
print("No. of players having Contract Expiry in 2020:")
print(d) 
print("No. of players having Contract Expiry in 2019:")
print(e)   
print("No. of players having Contract Expiry in 2018:")
print(f)  
y=[a,b,c,d,e,f]
x=[2023,2022,2021,2020,2019,2018]
z=df['Contract_Expiry'].tolist()
plt.figure(figsize=(9,8))
sns.barplot(x,y)    
plt.xlabel("YEAR OF CONTRACT EXPIRY",fontsize=12)
plt.ylabel("NUMBER OF PLAYERS",fontsize=12)
plt.title("CONTRACT EXPIRY ANALYSIS",fontsize=16) 
plt.show()
print("No. of players having rating >=89 and Contract Expiring in next 4 years:")
print((df.loc[:,'Rating'] > 89).sum())
print("Their Names: ")
bestRated_players = df[df.loc[:,'Rating']>89] #[['Name','Club','Rating']]
print(bestRated_players)
