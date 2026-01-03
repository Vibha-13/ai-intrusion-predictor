from datetime import datetime


class IDSLogger:
    def __init__(self, log_path="../logs/ids.log"):
        self.log_path = log_path

    def log(
        self,
        packet_count,
        avg_packet_size,
        alerts,
        ml_label,
        confidence,
        final_alert
    ):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        verdict = "SUSPICIOUS" if ml_label == 1 else "NORMAL"
        alert_text = ",".join(alerts) if alerts else "None"

        if final_alert:
            severity = "HIGH"
        elif alerts:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        line = (
            f"{timestamp} | "
            f"packets={packet_count} | "
            f"avg_size={avg_packet_size:.2f} | "
            f"alerts=[{alert_text}] | "
            f"ML={verdict}({confidence:.2f}) | "
            f"FINAL_ALERT={'YES' if final_alert else 'NO'} | "
            f"SEVERITY={severity}\n"
        )

        with open(self.log_path, "a") as f:
            f.write(line)
