import pandas as pd

# Load dataset
df = pd.read_excel("data/Online Retail.xlsx")

print("Dataset Loaded Successfully!")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())