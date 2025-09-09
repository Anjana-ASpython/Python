import pandas as pd
data = pd.read_csv("C:panda1.py", encoding='latin1')
print(data.isnull().sum())


data=data.drop(columns=["ADDRESSLINE2"])
print(data.isnull().sum())


data=data.dropna(subset=["ORDINATE", "PRODUCTLINE"])
print(data.isnull().sum())


data["MSRP"] =data["MSRP"].fillna(data["MSRP"].median())
data["YEAR_ID"]=data["YEAR_ID"].fillna(data["YEAR_ID"].mode()[0])
print(data.isnull().sum())

data["STATUS"].fillna(data["STATUS"].mode()[0],inplace=True)
print(data.isnull().sum())

data["PHONE"].fillna("unknown",inplace=True)
print(data.isnull().sum())

