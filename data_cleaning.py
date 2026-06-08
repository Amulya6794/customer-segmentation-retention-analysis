import pandas as pd

# Load dataset
df = pd.read_excel("data/Online Retail.xlsx")

print("Original Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove rows with missing CustomerID
df = df.dropna(subset=['CustomerID'])

# Remove cancelled/returned orders
df = df[df['Quantity'] > 0]

# Remove duplicates
df = df.drop_duplicates()

print("\nCleaned Shape:", df.shape)