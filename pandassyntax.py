# pip install pandas
import pandas as pd
s=pd.Series([10,20,30,42])
print(s)

data={"name":["Rain","Floral"],"age":[10,20]}
df=pd.DataFrame(data)
print(df)

data={"name":["Wolf","Winter","Summer","Home","Serene"],
"Score":[80,78,90,96,84]}
df=pd.DataFrame(data)
print(df.head())
print(df.head(3))

print(df.tail())
print(df.tail(3))

data={"name":["Wolf","Winter","Summer","Home","Serene","Day"],
      "Age":[20,18,14,16,None,22],
      "Score":[80,78,90,96,84,56]}
df=pd.DataFrame(data)
df.info()
df.describe()
print(df.columns)
print(df.shape)

data={"city":["Mumbai","Goa","Chennai","Bangalore","Mysore",None],
    "name":["Wolf","Winter","Summer","Home","Serene","Day"]}
df=pd.DataFrame(data,index=[1,2,3,4,5,6])
print(df.loc[2])
print(df.loc[4,"name"])
print(df.loc[:,["name","city"]])

print(df.iloc[0])
print(df.iloc[1,1])
print(df.iloc[:,0:1])
print(df.isnull())
print(df.dropna())
print(df.fillna("Cochin"))

data={"name":["Wolf","Winter","Summer","Home","Serene","Day"],
      "Age":[20,18,14,16,None,22],
      "Score":[80,78,90,96,84,56]}
df=pd.DataFrame(data)

df["Age"].fillna(df["Age"].mean(),inplace=True)
print(df)