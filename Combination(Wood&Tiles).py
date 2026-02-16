import matplotlib.pyplot as plt
import numpy as np

# Data for Wood
classes = ["1A", "1B", "2", "5A", "5B", "10A", "10B", "20"]
wood_heads = [111, 197, 46, 158, 306, 102, 155, 48]
wood_tails = [89, 203, 54, 142, 294, 98, 145, 52]

# Data for Tiles
tiles_heads = [134, 100, 0, 54, 207, 48, 99, 94]
tiles_tails = [166, 100, 0, 46, 193, 52, 101, 106]

x = np.arange(len(classes))  # positions
width = 0.2  # narrower bar width since we have 4 bars per group

plt.figure(figsize=(14,7))

# Plot Wood data
plt.bar(x - width*1.5, wood_heads, width, label="Wood Heads", color="#00b4d8")
plt.bar(x - width/2, wood_tails, width, label="Wood Tails", color="#ff4d6d")

# Plot Tiles data
plt.bar(x + width/2, tiles_heads, width, label="Tiles Heads", color="#007f5f")
plt.bar(x + width*1.5, tiles_tails, width, label="Tiles Tails", color="#d4a373")

# Labels and styling
plt.title("Heads vs Tails Comparison (Wood vs Tiles)", fontsize=16, fontweight="bold")
plt.xlabel("Coin Class")
plt.ylabel("Count")
plt.xticks(x, classes)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()
