import matplotlib.pyplot as plt

# Data from your table
cumulative_heads = [0,0,1,2,2,3,3,4,5,5,5,6,7,8,8,8,8,9,10,11,11,12,12,
                    12,13,14,14,14,14, 15,16,17,17,18,19,19,19,19,20,21
                    ,22,23,23,23,24,25,25,25,25,26,27,27, 28,29,29,30,31,
                    32,33,33,33,33,34,35,36,37,37,37,37,38,38,38,38,39,40, 
                    40,40,41,42,42,42,42,42,43,44,45,45,45,46,46,47,48,48,48,49,49,49,50, 51,51]
cumulative_tails = [1,2,2,2,3,3,4,4,4,5,6,6,6,6,7,8,9,9,9,9,10,10,11,12,12,12,
                    13,14,15,15, 15,15,16,16,16,17,18,19,19,19,19,19,20,21,21,
                    21,22,23,24,24,24,25,25, 25,26,26,26,26,26,27,28,29,29,29,
                    29,29,30,31,32,32,33,34,35,35,35,36, 37,37,37,38,39,40,41,
                    41,41,41,42,43,43,44,44,44,45,46,46,47,48,48,48,49]

# Ensure both lists are the same length
min_len = min(len(cumulative_heads), len(cumulative_tails))
cumulative_heads = cumulative_heads[:min_len]
cumulative_tails = cumulative_tails[:min_len]

# Number of flips
flips = list(range(1, min_len+1))

# Plotting
plt.figure(figsize=(10,6))
plt.plot(flips, cumulative_heads, label="Cumulative Heads", color="blue")
plt.plot(flips, cumulative_tails, label="Cumulative Tails", color="red")

# Optional: add difference line (Heads - Tails)
difference = [h - t for h, t in zip(cumulative_heads, cumulative_tails)]
plt.plot(flips, difference, label="Heads - Tails Difference", color="green", linestyle="--")

plt.title("Coin Flip Simulation: Cumulative Heads vs Tails")
plt.xlabel("Flip Number")
plt.ylabel("Cumulative Count")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
