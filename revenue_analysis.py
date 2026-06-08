import pandas as pd

df = pd.read_excel("data/Online Retail.xlsx")

# Data Cleaning
df = df.dropna(subset=['CustomerID'])
df = df[df['Quantity'] > 0]
df = df.drop_duplicates()

# Revenue
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

print("Total Customers:")
print(df['CustomerID'].nunique())

print("\nTotal Orders:")
print(df['InvoiceNo'].nunique())

print("\nTotal Revenue:")
print(round(df['TotalAmount'].sum(), 2))