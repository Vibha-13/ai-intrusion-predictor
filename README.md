📌 AI-Based Hybrid Intrusion Detection System

This project implements a real-time hybrid intrusion detection system (IDS) that combines rule-based anomaly detection with machine learning to identify suspicious network traffic.
The system is designed to reduce false positives while maintaining strong detection capability under high traffic conditions.

🔍 Key Features
Live packet capture using Scapy
Window-based traffic analysis (2-second intervals)
Rule-based anomaly detection (traffic spikes, large packets)
Machine Learning detection using Random Forest
Model trained on CICIDS 2017 dataset
Decision fusion to avoid false alarms
Severity-based logging
Live traffic visualization

🧠 Machine Learning Approach
Dataset used: CICIDS 2017
Features aligned with live traffic:
Flow Packets/s
Average Packet Size
Flow Bytes/s
Models evaluated:
Logistic Regression (baseline)
Random Forest (selected)
Final model achieved high accuracy and low false-negative rates.

⚙️ How It Works (High Level)
1. Capture live network packets
2. Extract traffic features in fixed windows
3. Run rule-based and ML-based detection in parallel
4. Fuse decisions to raise only high-confidence alerts
5. Log all outcomes with severity levels

▶️ How to Run
pip install -r requirements.txt
sudo python3 src/packet_capture.py

Logs are written to:
 logs/ids.log
📘 What I Learned
Handling real-world network datasets
Feature alignment between offline ML and live systems
Model comparison and evaluation
Reducing false positives using decision fusion
Designing explainable and modular security systems

🧾 Status
✔ Core system complete
✔ Machine learning integrated
✔ Tested under idle, normal, and heavy traffic
✔ Project finalized

🌱 Note
This project was built for learning and understanding intrusion detection systems, not for production deployment.
