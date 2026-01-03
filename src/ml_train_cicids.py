import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier

# Load aligned dataset
df = pd.read_csv("../data/datasets/cicids/cicids_aligned.csv")

# Clean dataset
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

X = df.drop("Label", axis=1)
y = df["Label"]

# Train final Random Forest
rf = RandomForestClassifier(
    n_estimators=150,
    max_depth=12,
    random_state=42,
    n_jobs=-1
)

rf.fit(X, y)

# Save model
joblib.dump(rf, "../models/ids_rf_cicids.pkl")

print("✅ Random Forest model trained and saved as ids_rf_cicids.pkl")
