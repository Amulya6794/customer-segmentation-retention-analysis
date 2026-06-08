import pandas as pd

df = pd.read_excel("data/Online Retail.xlsx")

# Cleaning
df = df.dropna(subset=['CustomerID'])
df = df[df['Quantity'] > 0]
df = df.drop_duplicates()

# Revenue
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# Snapshot Date
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

# RFM
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalAmount': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

# Churn Definition
rfm['Churn'] = rfm['Recency'].apply(
    lambda x: 1 if x > 90 else 0
)

print("Active Customers:")
print((rfm['Churn'] == 0).sum())

print("\nChurned Customers:")
print((rfm['Churn'] == 1).sum())

print("\nChurn Rate:")
print(
    round(
        (rfm['Churn'].sum() / len(rfm)) * 100,
        2
    ),
    "%"
)