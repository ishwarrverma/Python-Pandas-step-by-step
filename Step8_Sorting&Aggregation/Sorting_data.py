import pandas as pd

data = {
    "Name":['Ram','Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age":[26,25,35,40,36,27,22,41],
    "Salary":[50000,40000,22000,45000,55000,35000,30000,60000],
    "Performance Score":[85,95,90,88,89,75,80,92]
}

df = pd.DataFrame(data)
print(df)

#sorting data in 1 column
df.sort_values(by="Name", ascending=True, inplace=True)
print(df)

#sorting data in multiple column

df.sort_values(by=['Age', 'Salary'], ascending=True, inplace=True)
print(df)