import pandas as pd
import numpy as np

print("Loading model predictions...")
df = pd.read_csv('data/processed/model_predictions.csv')

# Convert date for better analysis
df['date'] = pd.to_datetime(df['date'])

print(f"Working with {len(df)} transactions")
print(f"Fraud rate: {df['is_fraud'].mean():.4f}")

# Create BI-ready datasets
print("\nCreating BI datasets...")

# 1. Transaction Summary (for main dashboard)
transaction_summary = df.groupby(df['date'].dt.date).agg({
    'amount': ['count', 'sum', 'mean'],
    'is_fraud': ['sum', 'mean'],
    'fraud_score': ['mean', 'max']
}).round(4)

transaction_summary.columns = ['total_transactions', 'total_amount', 'avg_amount', 
                              'fraud_count', 'fraud_rate', 'avg_fraud_score', 'max_fraud_score']
transaction_summary = transaction_summary.reset_index()
transaction_summary.columns = ['date', 'total_transactions', 'total_amount', 'avg_amount', 
                              'fraud_count', 'fraud_rate', 'avg_fraud_score', 'max_fraud_score']

# 2. High Risk Transactions (for fraud operations)
high_risk = df[df['fraud_score'] > 0.5].copy()
high_risk = high_risk.sort_values('fraud_score', ascending=False)

# 3. User Risk Profiles
user_risk = df.groupby('client_id_x').agg({
    'amount': ['count', 'sum', 'mean'],
    'is_fraud': ['sum', 'mean'],
    'fraud_score': ['mean', 'max'],
    'merchant_id': 'nunique'
}).round(4)

user_risk.columns = ['tx_count', 'total_spent', 'avg_amount', 'fraud_count', 'fraud_rate', 
                    'avg_fraud_score', 'max_fraud_score', 'unique_merchants']
user_risk = user_risk.reset_index()

# 4. Merchant Risk Analysis
merchant_risk = df.groupby('merchant_id').agg({
    'amount': ['count', 'sum', 'mean'],
    'is_fraud': ['sum', 'mean'],
    'fraud_score': ['mean', 'max'],
    'client_id_x': 'nunique'
}).round(4)

merchant_risk.columns = ['tx_count', 'total_volume', 'avg_amount', 'fraud_count', 'fraud_rate',
                        'avg_fraud_score', 'max_fraud_score', 'unique_users']
merchant_risk = merchant_risk.reset_index()

# 5. Hourly Patterns
hourly_patterns = df.groupby('hour').agg({
    'amount': ['count', 'sum'],
    'is_fraud': ['sum', 'mean'],
    'fraud_score': 'mean'
}).round(4)

hourly_patterns.columns = ['tx_count', 'total_amount', 'fraud_count', 'fraud_rate', 'avg_fraud_score']
hourly_patterns = hourly_patterns.reset_index()

# Save all datasets
transaction_summary.to_csv('bi/daily_summary.csv', index=False)
high_risk.to_csv('bi/high_risk_transactions.csv', index=False)
user_risk.to_csv('bi/user_risk_profiles.csv', index=False)
merchant_risk.to_csv('bi/merchant_risk_analysis.csv', index=False)
hourly_patterns.to_csv('bi/hourly_patterns.csv', index=False)

print("✅ Saved BI datasets:")
print(f"  - daily_summary.csv: {len(transaction_summary)} days")
print(f"  - high_risk_transactions.csv: {len(high_risk)} high-risk transactions")
print(f"  - user_risk_profiles.csv: {len(user_risk)} users")
print(f"  - merchant_risk_analysis.csv: {len(merchant_risk)} merchants")
print(f"  - hourly_patterns.csv: {len(hourly_patterns)} hours")

# Create a simple summary report
print("\n=== FRAUD DETECTION SUMMARY ===")
print(f"Total transactions analyzed: {len(df):,}")
print(f"Known fraud cases: {df['is_fraud'].sum():,}")
print(f"High-risk predictions: {len(high_risk):,}")
print(f"Average fraud score: {df['fraud_score'].mean():.4f}")
print(f"Highest fraud score: {df['fraud_score'].max():.4f}")

print("\nTop 5 highest risk transactions:")
print(high_risk[['id_x', 'date', 'amount', 'fraud_score', 'is_fraud']].head())

print("\n=== NEXT STEPS ===")
print("1. Open Power BI Desktop")
print("2. Import the CSV files from the 'bi' folder")
print("3. Create dashboards with:")
print("   - Daily fraud trends")
print("   - High-risk transaction alerts")
print("   - User risk profiles")
print("   - Merchant risk analysis")
print("   - Hourly fraud patterns")
