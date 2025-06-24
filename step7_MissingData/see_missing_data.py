import pandas as pd

data = {
    "Name":['Ram','Shyam', 'Ghanshyam',None,None, 'Jagdish', 'Raj', 'Simran'],
    "Age":[26,25,35,None,36,27,22,41],
    "Salary":[50000,40000,22000,None,55000,35000,30000,None],
    "Performance_Score":[85,95,90,None,89,75,None,92]
}

df = pd.DataFrame(data)
print(df)

print('After Finding Missing Data')
print(df.isnull())

#In this
#True--> NaN is Missing (Not a value is missing)
#False--> Value is present