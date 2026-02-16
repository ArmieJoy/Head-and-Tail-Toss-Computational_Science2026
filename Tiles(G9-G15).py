import matplotlib.pyplot as plt
import numpy as np

# Data
classes = ["1A", "1B", "2", "5A", "5B", "10A", "10B", "20"]
heads = [134, 100, 0, 54, 207, 48, 99, 94]
tails = [166, 100, 0, 46, 193, 52, 101, 106]
totals = [300, 200, 0, 100, 400, 100, 200, 200]

x = np.arange(len(classes))  # positions
width = 0.35  # bar width

# Plot
plt.figure(figsize=(12,6))
plt.bar(x - width/2, heads, width, label="Heads", color="#00b4d8")
plt.bar(x + width/2, tails, width, label="Tails", color="#ff4d6d")

# Labels and styling
plt.title("Total Heads vs Tails per Coin Class", fontsize=16, fontweight="bold")
plt.xlabel("Coin Class")
plt.ylabel("Count")
plt.xticks(x, classes)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Annotate totals above bars
for i, total in enumerate(totals):
    plt.text(x[i], max(heads[i], tails[i]) + 5, f"Total={total}", 
             ha='center', fontsize=9, color='black')

plt.tight_layout()
plt.show()
