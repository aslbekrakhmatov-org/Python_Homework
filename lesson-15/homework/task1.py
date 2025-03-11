import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
def f(x):
    return x**2 -4*x +4
y = f(x)

plt.plot(x, y, label=("f(x)"), color = "b")
plt.title("Parabola")
plt.xlabel("X")
plt.ylabel("Y", rotation = 0)
plt.legend()
plt.grid()
plt.show()