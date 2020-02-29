import numpy as np

from mpl_toolkits import mplot3d

import matplotlib.pyplot as plt


fig = plt.figure()

ax = plt.axes(projection="3d")

x =np.arange(-4,4,0.001)
y =np.arange(-4,4,0.001)

X,Y =np.meshgrid(x,y)

Z =3* X**2-2*X*Y

z1 = (4 * X) -2 * Y -1

ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, z1)
plt.show()
