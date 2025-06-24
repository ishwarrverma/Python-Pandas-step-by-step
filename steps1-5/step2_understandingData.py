import pandas as pd

df = pd.read_json(r"E:\vscode\Data Analysis\__pycache__\sample_Data.json")
print("Displaying the info of data set")
print(df.info())