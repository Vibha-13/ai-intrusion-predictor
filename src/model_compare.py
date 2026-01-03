import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load aligned dataset
df = pd.read_csv("../data/datasets/cicids/cicids_aligned.csv")

# 🔹 Clean dataset (important for CICIDS)
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

print("✅ Cleaned dataset shape:", df.shape)

X = df.drop("Label", axis=1)
y = df["Label"]

# Replace infinite values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Drop rows with NaN values
df.dropna(inplace=True)

print("✅ Cleaned dataset shape:", df.shape)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Scale features (important for Logistic Regression)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("===================================")
print("🔹 Logistic Regression")
print("===================================")

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train_scaled, y_train)
lr_preds = lr.predict(X_test_scaled)

print("Confusion Matrix:")
print(confusion_matrix(y_test, lr_preds))

print("\nClassification Report:")
print(classification_report(y_test, lr_preds, digits=4))

print("\n===================================")
print("🌳 Random Forest")
print("===================================")

rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)
rf_preds = rf.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, rf_preds))

print("\nClassification Report:")
print(classification_report(y_test, rf_preds, digits=4))

