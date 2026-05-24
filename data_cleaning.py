import pandas as pd
df = pd.read_excel("Data Assignment projects.xlsx")
df.columns = df.columns.str.strip()

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].str.strip()

df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%b-%y')
df['Order Month'] = pd.to_datetime(df['Order Month'], format='%d-%b-%y')

num_cols = [
    'Quantity',
    'Return Qty',
    'Net Qty',
    'Net Sales',
    'Gross Sales'
]
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['Net Sales'] = df['Net Sales'].fillna(0)
df['Return Reason'] = df['Return Reason'].fillna('No Return')

df = df.drop_duplicates()

print(df.info())
print(df.isnull().sum())
print(df.head())
print(df.shape)

df.to_excel("cleaned Data Assignment projects.xlsx")
print("data cleaned successfully")