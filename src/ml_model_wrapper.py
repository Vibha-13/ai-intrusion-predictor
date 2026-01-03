import joblib
import pandas as pd

WINDOW_SECONDS = 2  # must match FeatureExtractor window


class MLModel:
    def __init__(self):
        self.model = joblib.load("../models/ids_rf_cicids.pkl")

    def predict(self, packet_count, avg_packet_size):
        # Map live features → CICIDS-aligned features
        flow_packets_per_sec = packet_count / WINDOW_SECONDS
        flow_bytes_per_sec = (packet_count * avg_packet_size) / WINDOW_SECONDS

        # Use DataFrame with feature names (removes warning)
        X = pd.DataFrame(
            [[flow_packets_per_sec, avg_packet_size, flow_bytes_per_sec]],
            columns=[
                "Flow Packets/s",
                "Average Packet Size",
                "Flow Bytes/s"
            ]
        )

        label = int(self.model.predict(X)[0])
        confidence = float(self.model.predict_proba(X)[0][1])

        return label, confidence
