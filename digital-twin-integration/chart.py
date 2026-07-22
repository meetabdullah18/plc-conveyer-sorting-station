import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("default")

df = pd.read_csv("conveyor_log.csv", header=None,
                  names=["timestamp", "count_a", "count_b", "enabled"])
df["timestamp"] = pd.to_datetime(df["timestamp"])

plt.figure(figsize=(9, 5), facecolor="white")

plt.plot(df["timestamp"], df["count_a"],
         label="Type A", color="#007AFF", linewidth=2.5)
plt.plot(df["timestamp"], df["count_b"],
         label="Type B", color="#34C759", linewidth=2.5)

plt.xlabel("Time", fontsize=11)
plt.ylabel("Count", fontsize=11)
plt.title("Conveyor Sort Counts Over Time",
          fontsize=16, weight="bold", pad=15)

plt.grid(True, color="#E5E5EA", linewidth=0.8)
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["left"].set_color("#C7C7CC")
plt.gca().spines["bottom"].set_color("#C7C7CC")

plt.legend(frameon=False)

plt.tight_layout()
plt.savefig("sort_counts_chart.png", dpi=300)
print("Chart saved as sort_counts_chart.png")
