import pandas as pd

data = {
    "Name":['Ram','Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age":[26,25,35,40,36,27,22,41],
    "Salary":[50000,40000,22000,45000,55000,35000,30000,60000],
    "Performance_Score":[85,95,90,88,89,75,80,92]
}

df = pd.DataFrame(data)
print(df)

#remove Performance_Score column-->
#df.drop(columns=['Performance_Score'], inplace = True)
#print('After Modification')
#print(df)

#remove Performance_Score and age column ( for two or more columns )-->

df.drop(columns=['Performance_Score','Age'], inplace = True)
print('After Modification')
print(df)


