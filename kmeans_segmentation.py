import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_excel("data/Online Retail.xlsx")

# Data Cleaning
df = df.dropna(subset=['CustomerID'])
df = df[df['Quantity'] > 0]
df = df.drop_duplicates()

# Revenue
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# Snapshot Date
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

# RFM Table
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalAmount': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

# Scale Data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(
    rfm[['Recency', 'Frequency', 'Monetary']]
)

# K-Means
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

# Cluster Summary
print(
    rfm.groupby('Cluster')[
        ['Recency', 'Frequency', 'Monetary']
    ].mean()
)

print("\nCustomers per Cluster:")
print(rfm['Cluster'].value_counts())