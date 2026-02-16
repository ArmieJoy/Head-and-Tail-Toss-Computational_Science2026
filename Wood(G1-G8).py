import matplotlib.pyplot as plt
import numpy as np

# Data
classes = ["1A", "1B", "2", "5A", "5B", "10A", "10B", "20"]
heads = [111, 197, 46, 158, 306, 102, 155, 48]
tails = [89, 203, 54, 142, 294, 98, 145, 52]
totals = [200, 400, 100, 300, 600, 200, 300, 100]

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
