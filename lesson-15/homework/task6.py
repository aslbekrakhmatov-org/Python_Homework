import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection ="3d")

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

xx, yy = np.meshgrid(x,y)

zz = np.cos(xx**2, yy**2)

obj = ax.plot_surface(xx, yy, zz, label = "$f(x)=\cos(x^2+y^2)$", cmap = "plasma")
fig.colorbar(obj, ax=ax, aspect = 10, shrink = 0.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
ax.set_title("3D plot of f(x)")
plt.show()