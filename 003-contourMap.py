import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10, 0.5)
y = np.arange(-10, 10, 0.5)
X, Y = np.meshgrid(x, y)
Z = (X**2 + Y**2)
# plt.contourf(X, Y, Z, hatches=['+', '*', '//', '!'], cmap='hot', alpha=0.65)
plt.contourf(X, Y, Z, hatches=['+', '*', '//', '!'], colors=['#abcd00', '#ff3456', '#456798'], alpha=0.95)
plt.show()
