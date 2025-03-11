import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2/np.pi, 10)
def sin(x):
    return np.sin(x)
y_sin = sin(x)
plt.plot(x, y_sin, label="f(x)=sin", color='b', linestyle="--", marker = "D")
plt.legend()

def cos(x):
    return np.cos(x)
y_cos = cos(x)
plt.plot(x, y_cos, label="f(x)=cos", color='r', linestyle="-", marker ="o")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y", rotation = 0)
plt.title("Sine and Cosine functions")
plt.show()