import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

plt.style.use('fivethirtyeight')

# Example simulated data (replace with your own if needed)
flips = 100
heads = np.cumsum(np.random.randint(0, 2, flips))   # random cumulative heads
tails = np.arange(1, flips+1) - heads               # cumulative tails

fig, ax = plt.subplots(figsize=(10,6))
ax.set_xlim(0, flips)
ax.set_ylim(0, max(heads.max(), tails.max()) + 5)

line_heads, = ax.plot([], [], label="Cumulative Heads", color="#00b4d8", linewidth=2)
line_tails, = ax.plot([], [], label="Cumulative Tails", color="#ff4d6d", linewidth=2)

ax.set_title("Running Line Graph: Heads vs Tails", fontsize=16, fontweight="bold")
ax.set_xlabel("Flip Number")
ax.set_ylabel("Cumulative Count")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.6)

def update(frame):
    x_data = np.arange(1, frame+1)
    line_heads.set_data(x_data, heads[:frame])
    line_tails.set_data(x_data, tails[:frame])
    return line_heads, line_tails

ani = animation.FuncAnimation(
    fig, update,
    frames=flips,
    interval=100,   # speed of animation (ms)
    blit=True,
    repeat=False
)

plt.show()
