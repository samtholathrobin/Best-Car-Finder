from cmath import nan
import pandas as pd 
import numpy as np 
import sklearn
import regex as re
from sklearn.impute import SimpleImputer
DF=pd.read_csv("C:/Users/samth/Documents/Python Scripts/carsprojidk/new-used-cars-dataset.csv")#to read csv file
DF.fillna(0)
DF.drop(['price drop','Reviews'],axis=1,inplace=True)#to drop certain columns basically means cleaning data
# print(DF.tail())#show last 4 rows
DF.rename(columns={'used/certified':'Used/Certified'},inplace=True)#to rename column names
# print(DF.head())#show first 4 rows
print(DF.describe())#it describes the elements of the data frame
# print(DF.info())#it gives the info of the table and its attributes(columns)
# df2=DF.groupby("Ratings")[["Ratings","Used/Certified","Mileages"]].sum().reset_index()
# print(df2.head())

for i in DF["Price"]:
    if (re.match('[$][1-9][0-9]{2}[,][0-9]{3}$',i)):
        p=int(i[1]+i[2]+i[3]+i[5]+i[6]+i[7])
    elif (re.match('[$][1-9][0-9][,][0-9]{3}$',i)):
        p=int(i[1]+i[2]+i[4]+i[5]+i[6])
    elif (re.match('[$][1-9][0-9]{3}[,][0-9]{3}$',i)):
        p=int(i[1]+i[2]+i[4]+i[5]+i[6])
    DF["Price"]=DF["Price"].replace([i],p)

for i in DF["Mileages"]:
    if (re.match('[1-9][0-9][,][0-9]{3}[\s][a-z]{2}[.]$',i)):
        p=int(i[0]+i[1]+i[3]+i[4]+i[5])
    else:
        p=nan
    DF["Mileages"]=DF["Mileages"].replace([i],p)

for i in DF["Car Names"]:
    if (re.match('^[1,2][0-9]{3}',i)):
        p=int(i[0]+i[1]+i[2]+i[3])
    else:
        p=nan

print(DF[(DF["Price"]<30000) & (DF["Used/Certified"]!="Used") & (DF["Ratings"]>4.5) & (DF["Mileages"]<20000)])
