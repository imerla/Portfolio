# Credit Card Fraud Detection Dashboard

A comprehensive data analytics project that builds an AI-powered fraud detection system with interactive Power BI visualisations.

## 🎯 Project Overview

This project demonstrates end-to-end data analytics skills by:
- Processing and cleaning financial transaction data
- Performing exploratory data analysis (EDA)
- Creating interactive dashboards and visualisations
- Generating business intelligence reports
- Providing actionable insights for fraud prevention

## 📊 Dashboard Features

### Key Performance Indicators (KPIs)
- **Total Fraud Cases**: 89 detected fraud instances
- **Average Fraud Score**: 0.60 (ML model confidence)
- **High-Risk Alerts**: 480 transactions flagged
- **Total Transactions**: 100K+ processed

### Visualizations
- **Fraud Rate Trends**: Line chart showing fraud patterns over time
- **Hourly Risk Patterns**: Bar chart revealing peak fraud hours
- **Transaction Analysis**: Scatter plot correlating transaction counts with fraud scores
- **Detailed Table**: Comprehensive transaction breakdowns

## 🛠️ Technical Stack

- **Data Processing**: Python, Pandas, NumPy
- **Machine Learning**: Scikit-learn (Random Forest)
- **Visualization**: PowerBI Desktop
- **Data Sources**: CSV files (transactions, users, cards)

## 📁 Project Structure

```
Financial Transactions Dataset/
├── bi/                          # PowerBI data files
│   ├── daily_summary.csv        # Daily aggregated metrics
│   ├── hourly_patterns.csv      # Hourly fraud patterns
│   ├── high_risk_transactions.csv # Flagged transactions
│   ├── merchant_risk_analysis.csv # Merchant risk profiles
│   ├── user_risk_profiles.csv   # User risk assessments
│   └── Fraud_Dashboard.pbix     # PowerBI dashboard file
├── data/processed/              # Intermediate processing files
├── transactions_data.csv        # Raw transaction data
├── users_data.csv              # User demographic data
├── cards_data.csv              # Credit card information
└── mcc_codes.json              # Merchant category codes
```

## 📥 Data Download

Download the raw dataset via Kaggle:
- Direct link: `https://www.kaggle.com/api/v1/datasets/download/computingvictor/transactions-fraud-datasets`

## 🚀 Quick Start

### Prerequisites
- PowerBI Desktop (free)
- Python 3.8+ (optional, for data processing)

### Setup Instructions

1. **Download PowerBI Desktop** from [Microsoft](https://powerbi.microsoft.com/desktop/)

2. **Open the Dashboard**
   - Launch Power BI Desktop
   - Open `bi/Fraud_Dashboard.pbix`
   - Refresh data if needed

3. **Explore the Dashboard**
   - Navigate through different pages
   - Interact with filters and slicers
   - Analyse fraud patterns and trends

## 📈 Key Insights

### Fraud Patterns Discovered
- **Peak Risk Hours**: 10 AM and 6 PM show the highest fraud rates
- **Weekend Vulnerability**: Higher fraud rates on weekends
- **Amount Thresholds**: Large transactions (>$200) have elevated risk
- **User Behavior**: Users with unusual spending patterns flagged

### Business Impact
- **Risk Mitigation**: Identified 480 high-risk transactions
- **Cost Savings**: Prevented potential fraud losses
- **Pattern Recognition**: Automated detection of suspicious activities

## 🔧 Data Processing Pipeline

The project includes a complete data analytics pipeline:

1. **Data Integration** (`step3_join.py`): Combines transaction, user, and card data
2. **Data Cleaning** (`step4_simple.py`): Handles missing values and outliers
3. **Feature Engineering** (`step7_features.py`): Creates risk indicators and metrics
4. **Analytics Preparation** (`step9_bi_data.py`): Aggregates data for visualization

## 📊 Analytics Methodology

- **Data Sources**: Transaction, user, and card data integration
- **Key Metrics**: 20+ calculated indicators including:
  - Transaction patterns (amount, time, location)
  - User behavior (spending habits, card usage)
  - Risk indicators (unusual amounts, high-risk hours)
- **Output**: Risk scores and flagged transactions for business action

## 🎨 Dashboard Pages

1. **KPI Overview**: Executive summary with key metrics
2. **Fraud Trends**: Temporal analysis of fraud patterns
3. **High-Risk Transactions**: Detailed view of flagged transactions
4. **Hourly Patterns**: Time-based risk analysis
5. **User Risk Profiles**: Individual user risk assessments

## 📝 Usage Notes

- Dashboard updates automatically when data refreshes
- All visualisations are interactive and filterable
- Export capabilities available for reports
- Mobile-responsive design for on-the-go access

## 🔒 Data Privacy

- All personal identifiers are anonymised
- Sample dataset for demonstration purposes
- No real financial data included

## 📞 Support

For questions or issues:
- Check Power BI documentation for visualisation help
- Ensure all CSV files are properly formatted

## 🏆 Portfolio Value

This project demonstrates:
- **Data Analytics**: End-to-end data processing and visualization
- **Business Intelligence**: Interactive dashboards and KPIs
- **Domain Knowledge**: Financial fraud detection and risk analysis
- **Technical Skills**: Python, Power BI, data visualisation, SQL
- **Problem Solving**: Real-world business challenges and insights


