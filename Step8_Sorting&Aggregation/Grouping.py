#we can split our data in small groups
import pandas as pd

data = {
    "Name":['Ram','Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age":[22,25,35,22,28,28,22,25],
    "Salary":[50000,40000,22000,45000,55000,35000,30000,60000],
    "Performance Score":[85,95,90,88,89,75,80,92]
}

df = pd.DataFrame(data)


#for 1 column 
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)

#for multiple column ( find salary based on name and age)
grouped_2 = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped_2)

# sum(), mean(), count(), min(), max(), std()