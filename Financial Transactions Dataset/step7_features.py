import pandas as pd
import numpy as np
from datetime import datetime

print("Loading sample dataset...")
df = pd.read_csv('data/processed/sample_dataset.csv')

print(f"Working with {len(df)} transactions")

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Clean amount column (remove $ and convert to float)
df['amount'] = df['amount'].str.replace('$', '').str.replace(',', '').astype(float)

print("Creating fraud detection features...")

# 1. TIME-BASED FEATURES
df['hour'] = df['date'].dt.hour
df['day_of_week'] = df['date'].dt.dayofweek
df['is_weekend'] = df['day_of_week'].isin([5, 6])
df['is_night'] = df['hour'].isin([22, 23, 0, 1, 2, 3, 4, 5])

# 2. AMOUNT FEATURES
df['amount_abs'] = df['amount'].abs()
df['is_negative'] = df['amount'] < 0
df['is_large_amount'] = df['amount_abs'] > df['amount_abs'].quantile(0.95)

# 3. USER BEHAVIOR FEATURES (per user)
user_stats = df.groupby('client_id_x').agg({
    'amount_abs': ['mean', 'std', 'max'],
    'date': ['min', 'max', 'count'],
    'merchant_id': 'nunique'
}).round(2)

user_stats.columns = ['user_avg_amount', 'user_std_amount', 'user_max_amount', 
                     'user_first_tx', 'user_last_tx', 'user_tx_count', 'user_unique_merchants']

# 4. CARD FEATURES
card_stats = df.groupby('card_id').agg({
    'amount_abs': ['mean', 'std'],
    'date': 'count',
    'merchant_id': 'nunique'
}).round(2)

card_stats.columns = ['card_avg_amount', 'card_std_amount', 'card_tx_count', 'card_unique_merchants']

# 5. MERCHANT FEATURES
merchant_stats = df.groupby('merchant_id').agg({
    'amount_abs': ['mean', 'std'],
    'date': 'count',
    'client_id_x': 'nunique'
}).round(2)

merchant_stats.columns = ['merchant_avg_amount', 'merchant_std_amount', 'merchant_tx_count', 'merchant_unique_users']

# Join features back to main dataset
df = df.merge(user_stats, left_on='client_id_x', right_index=True, how='left')
df = df.merge(card_stats, left_on='card_id', right_index=True, how='left')
df = df.merge(merchant_stats, left_on='merchant_id', right_index=True, how='left')

# 6. DEVIATION FEATURES
df['amount_vs_user_avg'] = df['amount_abs'] / (df['user_avg_amount'] + 1)
df['amount_vs_card_avg'] = df['amount_abs'] / (df['card_avg_amount'] + 1)

# 7. RISK FLAGS
df['high_risk_hour'] = df['hour'].isin([0, 1, 2, 3, 4, 5, 22, 23])
df['high_risk_day'] = df['day_of_week'].isin([5, 6])  # Weekend
df['unusual_amount'] = (df['amount_vs_user_avg'] > 3) | (df['amount_vs_card_avg'] > 3)

print(f"Created {len(df.columns)} total features")
print("Sample features:")
print(df[['amount', 'hour', 'is_weekend', 'is_night', 'amount_vs_user_avg', 'is_fraud']].head())

# Save features
df.to_csv('data/processed/features_dataset.csv', index=False)
print("Saved features to data/processed/features_dataset.csv")

# Show fraud rate by some features
print("\nFraud rates by feature:")
print("Weekend vs Weekday:")
print(df.groupby('is_weekend')['is_fraud'].mean())
print("\nNight vs Day:")
print(df.groupby('is_night')['is_fraud'].mean())
print("\nLarge amounts:")
print(df.groupby('is_large_amount')['is_fraud'].mean())
