import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data/Online Retail.xlsx")

# Cleaning
df = df.dropna(subset=['CustomerID'])
df = df[df['Quantity'] > 0]
df = df.drop_duplicates()

# Revenue
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# Monthly Revenue
df['Month'] = df['InvoiceDate'].dt.to_period('M')

monthly_revenue = df.groupby('Month')['TotalAmount'].sum()

plt.figure(figsize=(12,6))
monthly_revenue.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)

plt.savefig("outputs/monthly_revenue.png")
plt.close()

print("Chart saved successfully!")