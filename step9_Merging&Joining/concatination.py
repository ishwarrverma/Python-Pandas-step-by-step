import pandas as pd 

df_region1 = pd.DataFrame({
    'Customer_ID': [1,2],
    'Name': ['Gopal', 'Raju']
})

df_region2 = pd.DataFrame({
    'Customer_ID': [3,4],
    'Name': ['Shyam', 'Baburao']
})

df_concate = pd.concat([df_region1,df_region2], axis = 0, ignore_index=True)
print(df_concate)

# ignore index --> it reset indexing number
# axis=0 ( for vertically row wise )
# axis=1 ( for horizontally column wise)