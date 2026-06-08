import pandas as pd

# Load dataset
df = pd.read_excel("data/Online Retail.xlsx")

# Cleaning
df = df.dropna(subset=['CustomerID'])
df = df[df['Quantity'] > 0]
df = df.drop_duplicates()

# Revenue
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# Snapshot date
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

# RFM
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalAmount': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

# Scores
rfm['R_Score'] = pd.qcut(
    rfm['Recency'],
    5,
    labels=[5,4,3,2,1]
)

rfm['F_Score'] = pd.qcut(
    rfm['Frequency'].rank(method='first'),
    5,
    labels=[1,2,3,4,5]
)

rfm['M_Score'] = pd.qcut(
    rfm['Monetary'],
    5,
    labels=[1,2,3,4,5]
)

# Combined score
rfm['RFM_Score'] = (
    rfm['R_Score'].astype(str) +
    rfm['F_Score'].astype(str) +
    rfm['M_Score'].astype(str)
)

print(rfm.head())

print("\nTop 10 Customers:")
print(
    rfm.sort_values(
        by='Monetary',
        ascending=False
    ).head(10)
)