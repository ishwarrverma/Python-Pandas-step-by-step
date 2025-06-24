import pandas as pd

data = {
    "Name":['Ram','Shyam', 'Ghanshyam',None,None, 'Jagdish', 'Raj', 'Simran'],
    "Age":[26,25,35,None,36,27,22,41],
    "Salary":[50000,40000,22000,None,55000,35000,30000,None],
    "Performance_Score":[85,95,90,None,89,75,None,92]
}

df = pd.DataFrame(data)
print(df)


df.dropna(inplace=True)
print(df)

#removing rows only
df.dropna(axis=0, inplace=True)

#removing column only
df.dropna(axis=1, inplace=True)