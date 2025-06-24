import pandas as pd

#data farme 1
df_customers = pd.DataFrame({
    'Customer_ID':[1,2,3],
    'Name':['Ramesh', 'Sursh', 'Kalpesh']
})

#data frame 2

df_orders = pd.DataFrame({
    'Customer_ID':[1,2,4],
    'Order_Amount':[250, 450,350]
})

#merge

df_merged = pd.merge(df_customers,df_orders, on='Customer_ID', how="inner")
print('inner join')
print(df_merged)

df_merged = pd.merge(df_customers,df_orders, on='Customer_ID', how="outer")
print('outer join')
print(df_merged)

# inner join, outer join, left join, right join, cross join