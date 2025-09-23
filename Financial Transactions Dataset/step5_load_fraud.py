import json
import pandas as pd

# Load the fraud labels
print("Loading fraud labels...")
with open('train_fraud_labels.json', 'r') as f:
    fraud_data = json.load(f)

print("Fraud data type:", type(fraud_data))
print("Fraud data keys:", list(fraud_data.keys()))

# Get the actual fraud labels
fraud_labels = fraud_data['target']
print(f"\nNumber of fraud labels: {len(fraud_labels)}")

# Convert to DataFrame
fraud_df = pd.DataFrame([
    {'transaction_id': int(tx_id), 'is_fraud': label == 'Yes'} 
    for tx_id, label in fraud_labels.items()
])

print(f"\nFraud DataFrame shape: {fraud_df.shape}")
print("Sample data:")
print(fraud_df.head(10))

# Check fraud rate
fraud_rate = fraud_df['is_fraud'].mean()
print(f"\nFraud rate: {fraud_rate:.4f} ({fraud_rate*100:.2f}%)")
print(f"Number of fraud cases: {fraud_df['is_fraud'].sum()}")
print(f"Number of non-fraud cases: {(~fraud_df['is_fraud']).sum()}")

# Check transaction ID range
print(f"\nTransaction ID range: {fraud_df['transaction_id'].min()} to {fraud_df['transaction_id'].max()}")

# Save for later use
fraud_df.to_csv('data/processed/fraud_labels.csv', index=False)
print("\nSaved fraud labels to data/processed/fraud_labels.csv")
