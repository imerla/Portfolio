import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

print("Loading features dataset...")
df = pd.read_csv('data/processed/features_dataset.csv')

# Remove rows without fraud labels for training
train_df = df.dropna(subset=['is_fraud'])
print(f"Training data: {len(train_df)} transactions")
print(f"Fraud rate: {train_df['is_fraud'].mean():.4f}")

# Select features for the model
feature_cols = [
    'amount', 'hour', 'day_of_week', 'is_weekend', 'is_night',
    'amount_abs', 'is_negative', 'is_large_amount',
    'user_avg_amount', 'user_std_amount', 'user_tx_count', 'user_unique_merchants',
    'card_avg_amount', 'card_std_amount', 'card_tx_count', 'card_unique_merchants',
    'merchant_avg_amount', 'merchant_std_amount', 'merchant_tx_count', 'merchant_unique_users',
    'amount_vs_user_avg', 'amount_vs_card_avg',
    'high_risk_hour', 'high_risk_day', 'unusual_amount'
]

# Handle missing values
X = train_df[feature_cols].fillna(0)
y = train_df['is_fraud'].astype(int)

print(f"Features: {len(feature_cols)}")
print(f"Training samples: {len(X)}")

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"Train set: {len(X_train)}, Test set: {len(X_test)}")

# Train Random Forest model
print("\nTraining Random Forest model...")
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=50,
    min_samples_leaf=20,
    random_state=42,
    class_weight='balanced'  # Handle imbalanced data
)

model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Evaluate model
print("\n=== MODEL PERFORMANCE ===")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print(f"\nROC AUC Score: {roc_auc_score(y_test, y_pred_proba):.4f}")

# Feature importance
feature_importance = pd.DataFrame({
    'feature': feature_cols,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nTop 10 Most Important Features:")
print(feature_importance.head(10))

# Predict on unlabeled data
print("\nPredicting on unlabeled transactions...")
unlabeled_df = df[df['is_fraud'].isna()]
if len(unlabeled_df) > 0:
    X_unlabeled = unlabeled_df[feature_cols].fillna(0)
    unlabeled_pred = model.predict(X_unlabeled)
    unlabeled_proba = model.predict_proba(X_unlabeled)[:, 1]
    
    print(f"Unlabeled transactions: {len(unlabeled_df)}")
    print(f"Predicted fraud cases: {unlabeled_pred.sum()}")
    print(f"Average fraud probability: {unlabeled_proba.mean():.4f}")

# Save model predictions
df['fraud_score'] = 0.0
df.loc[train_df.index, 'fraud_score'] = model.predict_proba(X)[:, 1]
if len(unlabeled_df) > 0:
    df.loc[unlabeled_df.index, 'fraud_score'] = unlabeled_proba

df.to_csv('data/processed/model_predictions.csv', index=False)
print("\nSaved model predictions to data/processed/model_predictions.csv")

print("\n=== SUMMARY ===")
print(f"✅ Model trained on {len(train_df)} transactions")
print(f"✅ ROC AUC: {roc_auc_score(y_test, y_pred_proba):.4f}")
print(f"✅ Top feature: {feature_importance.iloc[0]['feature']}")
print(f"✅ Predictions saved for all {len(df)} transactions")
