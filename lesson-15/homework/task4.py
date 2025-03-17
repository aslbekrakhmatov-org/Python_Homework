import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
marker_choices = ['.', 's', '*', ',', 'o', 'D', 'H', 'x', 'v', '^']
markers = np.random.choice(marker_choices, size=100)
for i in range(len(x)):
    plt.scatter(x[i], y[i], color=np.random.rand(3,), marker=markers[i])

plt.title("Scatter plot")
plt.xlabel("X")
plt.ylabel("Y", rotation = 0)
plt.grid(True)
plt.show()