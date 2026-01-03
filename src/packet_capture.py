from scapy.all import sniff
import time
from feature_extractor import FeatureExtractor

extractor = FeatureExtractor()

def packet_callback(packet):
    timestamp = time.strftime("%H:%M:%S", time.localtime())
    size = len(packet)
    proto = packet.summary().split()[0]

    # Send data to the extractor
    extractor.add_packet(size, proto)

    print(f"[{timestamp}] Size: {size} bytes | Protocol: {proto}")

def start_capture():
    print("🟣 Starting live packet capture… (Press CTRL + C to stop)")
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    start_capture()
