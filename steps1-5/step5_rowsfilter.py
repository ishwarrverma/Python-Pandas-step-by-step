import pandas as pd

data = {
    "Name":['Ram','Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age":[26,25,35,40,36,27,22,41],
    "Salary":[50000,40000,22000,45000,55000,35000,30000,60000],
    "Performance_Score":[85,95,90,88,89,75,80,92]
}

df = pd.DataFrame(data)

high_salary = df[df['Salary']>50000]
print('Emplyoees with Salary > 50000')
print(high_salary)

#filtering rows salary > 50k & age >30
filtered = df[(df['Age'] > 30) & (df['Salary'] > 50000 )]
print('Employees list Age>30 + Salary>50000')
print(filtered)

#using OR condition

filtered_or = df[(df['Age']>35) | (df['Performance_Score']>90)]
print(filtered_or)