import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
data = pd.read_csv("../data/training_data.csv")

X = data[["packet_count", "avg_packet_size"]]
y = data["label"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "../models/ids_model.pkl")

print("✅ ML model trained and saved.")
