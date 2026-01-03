import pandas as pd

# Load dataset
df = pd.read_csv("../data/datasets/cicids/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Select aligned features
features = [
    "Flow Packets/s",
    "Average Packet Size",
    "Flow Bytes/s"
]

target = "Label"

df = df[features + [target]]

# Convert labels to binary
df["Label"] = df["Label"].apply(lambda x: 1 if x != "BENIGN" else 0)

print("✅ Selected features:")
print(features)

print("\n📊 Label distribution:")
print(df["Label"].value_counts())

print("\n🔍 Sample rows:")
print(df.head())

# Save clean dataset
df.to_csv("../data/datasets/cicids/cicids_aligned.csv", index=False)

print("\n💾 Saved cleaned dataset: cicids_aligned.csv")
