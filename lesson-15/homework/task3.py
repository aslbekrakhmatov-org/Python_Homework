import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(8,8))

x = np.linspace(-10, 10, 100)
y1 = x**3
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.log(np.log1p(x))

#top-left
axes[0, 0].plot(x,y1, label = "$f(x)=x^3$", color = 'b')
axes[0,0].set_title("Cubic Function")
axes[0,0].set_xlabel("X")
axes[0,0].set_ylabel("Y", rotation = 0)
axes[0,0].legend()

#top-right
axes[0, 1].plot(x,y2, label = "$f(x)=\sin(x)$", color = 'r')
axes[0,1].set_title("Sine Function")
axes[0,1].set_xlabel("X")
axes[0,1].set_ylabel("Y", rotation = 0)
axes[0,1].legend()

#bottom-left
axes[1, 0].plot(x,y3, label = "$f(x)=e^x$", color = 'g')
axes[1,0].set_title("Exponetial Function")
axes[1,0].set_xlabel("X")
axes[1,0].set_ylabel("Y", rotation = 0)
axes[1,0].legend()

#bottom-right
axes[1, 1].plot(x,y4, label = "$f(x)=\log(x+1)$", color = 'y')
axes[1,1].set_title("Logarithmic Function")
axes[1,1].set_xlabel("X")
axes[1,1].set_ylabel("Y", rotation = 0)
axes[1,1].legend()

plt.tight_layout()
plt.show()

