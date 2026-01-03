import pandas as pd

# Load dataset
df = pd.read_csv("../data/datasets/cicids/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

print("✅ Dataset loaded successfully")
print("Shape (rows, columns):", df.shape)

print("\n🧾 Column names:")
print(df.columns.tolist())

print("\n🔍 First 5 rows:")
print(df.head())

print("\n🏷️ Label distribution:")
print(df[" Label"].value_counts())

