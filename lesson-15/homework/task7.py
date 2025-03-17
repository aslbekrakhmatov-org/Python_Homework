import numpy as np
import matplotlib.pyplot as plt

categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = [200, 150, 250, 175, 225]
colors = plt.get_cmap("tab10").colors[:len(categories)]
plt.bar(categories, values, color = colors, width=0.5)
plt.title("Bar Chart")
plt.xlabel("Catg")
plt.ylabel("Values")
plt.show()