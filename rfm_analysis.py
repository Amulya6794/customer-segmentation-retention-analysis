import pandas as pd

# Load dataset
df = pd.read_excel("data/Online Retail.xlsx")

# Data Cleaning
df = df.dropna(subset=['CustomerID'])
df = df[df['Quantity'] > 0]
df = df.drop_duplicates()

# Revenue column
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# Reference date
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

# Create RFM table
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalAmount': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

print(rfm.head())

print("\nRFM Table Shape:")
print(rfm.shape)