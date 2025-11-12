"""
Data preprocessing module.
Handles cleaning, feature engineering, and splitting.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(path: str) -> pd.DataFrame:
    """Load dataset from a CSV file."""
    return pd.read_csv(path)

def preprocess_data(df: pd.DataFrame):
    """Basic preprocessing example: handle NaNs and scale numeric features."""
    df = df.dropna(subset=['readmit_30'])  # drop rows missing target
    X = df.drop(columns=['readmit_30'])
    y = df['readmit_30']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X.select_dtypes(include='number'))
    X[X.select_dtypes(include='number').columns] = X_scaled

    return train_test_split(X, y, test_size=0.15, stratify=y, random_state=42)
