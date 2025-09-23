import pandas as pd

# Load the CSV files
transactions = pd.read_csv('transactions_data.csv')
users = pd.read_csv('users_data.csv') 
cards = pd.read_csv('cards_data.csv')

print("Original sizes:")
print(f"Transactions: {len(transactions)}")
print(f"Users: {len(users)}")
print(f"Cards: {len(cards)}")

# Join transactions with users and cards
df = transactions.merge(users, left_on='client_id', right_on='id', how='left')
df = df.merge(cards, left_on='card_id', right_on='id', how='left')

print(f"\nAfter join: {len(df)} rows, {len(df.columns)} columns")
print("\nFirst few columns:", df.columns.tolist()[:10])

# Show sample data
print("\nSample data:")
print(df.head(2))
