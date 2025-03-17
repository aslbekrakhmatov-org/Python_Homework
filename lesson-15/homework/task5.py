import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=30, label = "Dataset", alpha = 0.8, color='b', edgecolor ="#000000")
plt.title("Histogram")
plt.xlabel("Frequency")
plt.ylabel("Values")
plt.legend()
plt.show()