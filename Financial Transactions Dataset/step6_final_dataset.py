import pandas as pd

# Load all our data
print("Loading data...")
transactions = pd.read_csv('transactions_data.csv')
users = pd.read_csv('users_data.csv')
cards = pd.read_csv('cards_data.csv')
fraud_labels = pd.read_csv('data/processed/fraud_labels.csv')

print("Data loaded:")
print(f"Transactions: {len(transactions)}")
print(f"Users: {len(users)}")
print(f"Cards: {len(cards)}")
print(f"Fraud labels: {len(fraud_labels)}")

# Join transactions with users and cards
print("\nJoining data...")
df = transactions.merge(users, left_on='client_id', right_on='id', how='left')
df = df.merge(cards, left_on='card_id', right_on='id', how='left')

# Join with fraud labels
df = df.merge(fraud_labels, left_on='id_x', right_on='transaction_id', how='left')

print(f"Final dataset: {len(df)} rows, {len(df.columns)} columns")

# Check how many transactions have fraud labels
labeled_count = df['is_fraud'].notna().sum()
print(f"Transactions with fraud labels: {labeled_count}")
print(f"Transactions without fraud labels: {len(df) - labeled_count}")

# Show fraud rate in our dataset
fraud_rate = df['is_fraud'].mean()
print(f"Overall fraud rate: {fraud_rate:.4f} ({fraud_rate*100:.2f}%)")

# Show sample of final data
print("\nSample of final dataset:")
print(df[['id_x', 'date', 'amount', 'client_id_x', 'is_fraud']].head(10))

# Save final dataset
df.to_csv('data/processed/final_dataset.csv', index=False)
print(f"\nSaved final dataset to data/processed/final_dataset.csv")

# Create a sample for faster development
sample_df = df.sample(n=min(100000, len(df)), random_state=42)
sample_df.to_csv('data/processed/sample_dataset.csv', index=False)
print(f"Saved sample dataset ({len(sample_df)} rows) to data/processed/sample_dataset.csv")
