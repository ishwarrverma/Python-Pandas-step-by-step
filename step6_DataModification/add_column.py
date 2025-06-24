import pandas as pd

data = {
    "Name":['Ram','Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age":[26,25,35,40,36,27,22,41],
    "Salary":[50000,40000,22000,45000,55000,35000,30000,60000],
    "Performance_Score":[85,95,90,88,89,75,80,92]
}

df = pd.DataFrame(data)
print(df)

#add using directly value assign

df["Bonus"] = df['Salary'] * 0.1
print(df)

#add using insert() for specific location

df.insert(0,'Emplyoee_ID',[10,20,30,40,50,60,70,80])
print(df)