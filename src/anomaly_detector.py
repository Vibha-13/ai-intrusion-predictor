class AnomalyDetector:
    """
    Explainable rule-based anomaly detector for live network traffic.
    """

    def __init__(self):
        self.prev_packet_count = None
        self.prev_avg_size = None

    def detect(self, packet_count, avg_packet_size, protocol_count):
        alerts = []

        # 1. Traffic spike detection
        if self.prev_packet_count is not None:
            if packet_count > self.prev_packet_count * 2:
                alerts.append(
                    f"🚨 Traffic Spike: packets jumped "
                    f"{self.prev_packet_count} → {packet_count}"
                )

        # 2. Large packet size anomaly
        if self.prev_avg_size is not None:
            if avg_packet_size > 800 and avg_packet_size > self.prev_avg_size * 1.5:
                alerts.append(
                    f"⚠️ Large Packets: avg size increased "
                    f"{self.prev_avg_size:.1f} → {avg_packet_size:.1f} bytes"
                )

        # 3. Protocol dominance (ignore Ether, require significant volume)
        if packet_count >= 50:
            for proto, count in protocol_count.items():
                if proto == "Ether":
                    continue

                if count > packet_count * 0.85:
                    alerts.append(
                        f"⚠️ Protocol Dominance: {proto} = "
                        f"{count}/{packet_count} packets"
                    )

        # Store previous window stats
        self.prev_packet_count = packet_count
        self.prev_avg_size = avg_packet_size

        return alerts
