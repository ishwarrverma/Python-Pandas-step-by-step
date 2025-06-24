import pandas as pd

data = {
    "Name":['Ram','Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age":[26,25,35,40,36,27,22,41],
    "Salary":[50000,40000,22000,45000,55000,35000,30000,60000],
    "Performance_Score":[85,95,90,88,89,75,80,92]
}

df = pd.DataFrame(data)
print(df)

#update ram salary by 55000-->

df.loc[0,'Salary'] = 55000
print(df)

#update everyone's salary by 5%

df['Salary'] = df['Salary'] * 1.05
print(df)