#Aggregation--> It invlove calculated summry statistics

import pandas as pd

data = {
    "Name":['Ram','Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age":[26,25,35,40,36,27,22,41],
    "Salary":[50000,40000,22000,45000,55000,35000,30000,60000],
    "Performance Score":[85,95,90,88,89,75,80,92]
}

df = pd.DataFrame(data)
print(df)

df_mean = df['Salary'].mean() #average
print(df_mean)

df_sum = df['Salary'].sum() #total
print(df_sum)

# min(), max()

