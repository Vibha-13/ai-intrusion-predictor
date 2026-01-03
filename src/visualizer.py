import matplotlib.pyplot as plt
from collections import deque

class TrafficVisualizer:
    def __init__(self, window_size=20):
        self.packet_history = deque(maxlen=window_size)
        self.size_history = deque(maxlen=window_size)

        plt.ion()
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(8, 6))

    def update(self, packet_count, avg_packet_size):
        self.packet_history.append(packet_count)
        self.size_history.append(avg_packet_size)

        self.ax1.clear()
        self.ax2.clear()

        self.ax1.plot(self.packet_history, marker='o')
        self.ax1.set_title("Packets per Time Window")
        self.ax1.set_ylabel("Packets")

        self.ax2.plot(self.size_history, marker='o', color='orange')
        self.ax2.set_title("Average Packet Size per Window")
        self.ax2.set_ylabel("Bytes")
        self.ax2.set_xlabel("Time Window")

        plt.tight_layout()
        plt.pause(0.01)
