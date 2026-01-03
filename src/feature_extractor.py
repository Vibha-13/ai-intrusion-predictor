import time
from anomaly_detector import AnomalyDetector
from visualizer import TrafficVisualizer
from ml_model_wrapper import MLModel
from logger import IDSLogger

FUSION_THRESHOLD = 0.70


class FeatureExtractor:
    def __init__(self):
        # Traffic statistics
        self.packet_count = 0
        self.total_size = 0
        self.protocol_count = {}

        self.last_report_time = time.time()

        # Components
        self.anomaly_detector = AnomalyDetector()
        self.visualizer = TrafficVisualizer()
        self.ml_model = MLModel()
        self.logger = IDSLogger()

    def add_packet(self, packet_size, protocol):
        self.packet_count += 1
        self.total_size += packet_size

        if protocol not in self.protocol_count:
            self.protocol_count[protocol] = 0
        self.protocol_count[protocol] += 1

        current_time = time.time()
        if current_time - self.last_report_time >= 2:
            self.print_stats()
            self.reset_stats()

    def print_stats(self):
        # Calculate average packet size
        avg_packet_size = (
            self.total_size / self.packet_count
            if self.packet_count > 0 else 0
        )

        print("\n🔍 Traffic Summary (Last 2 seconds)")
        print(f"📌 Packets: {self.packet_count}")
        print(f"📌 Avg Packet Size: {avg_packet_size:.2f} bytes")
        print("📌 Protocol Count:", self.protocol_count)

        # Rule-based anomaly detection
        alerts = self.anomaly_detector.detect(
            self.packet_count,
            avg_packet_size,
            self.protocol_count
        )

        for alert in alerts:
            print(alert)

        # ML-based classification
        label, confidence = self.ml_model.predict(
            self.packet_count,
            avg_packet_size
        )

        if label == 1:
            print(
                f"🧠 ML Verdict: SUSPICIOUS "
                f"(confidence = {confidence:.2f})"
            )
        else:
            print(
                f"🧠 ML Verdict: NORMAL "
                f"(confidence = {confidence:.2f})"
            )

        # 🔹 Decision Fusion (FINAL INTELLIGENCE)
        final_alert = bool(alerts) and confidence >= FUSION_THRESHOLD

        if final_alert:
            print("🚨🚨 FINAL ALERT: HIGH CONFIDENCE INTRUSION 🚨🚨")
        else:
            print("✅ Final Decision: No high-confidence intrusion")

        # Persist log (audit trail)
        self.logger.log(
            packet_count=self.packet_count,
            avg_packet_size=avg_packet_size,
            alerts=alerts,
            ml_label=label,
            confidence=confidence,
            final_alert=final_alert
        )

        # Update live graphs
        self.visualizer.update(self.packet_count, avg_packet_size)

    def reset_stats(self):
        self.packet_count = 0
        self.total_size = 0
        self.protocol_count = {}
        self.last_report_time = time.time()
