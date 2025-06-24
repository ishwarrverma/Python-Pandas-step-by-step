import pandas as pd

data = {
    "Name": ['Ram', 'Shayam', 'Ghanshyam'],
    "Age": [10,20,30],
    "City": ['Nagpur', 'Mumbai', 'Delhi']
   }
df = pd.DataFrame(data)
print(df)

#create csv ->

#df.to_csv("Output.CSV", index=False)
#df.to_excel("Output.xlsx", index=False)
df.to_json("Output.json", index=False)