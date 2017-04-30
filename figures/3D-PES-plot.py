import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, proj3d, art3d
from matplotlib.patches import Rectangle

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.arange(-2, 7, 0.1)
y = np.arange(-2, 7, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.sin(X)+np.cos(Y)

xx, zz = np.meshgrid(np.linspace(-1.9,7.1,2),np.linspace(-3,4,2))
yy = xx*0 +3



ax.plot_surface(xx,yy,zz, color='blue',alpha=0.2,linewidth=0,antialiased=False)

ax.plot_surface(X,Y,Z,cmap='Oranges',linewidth=0, antialiased=False,alpha=1)

ax.view_init(elev=60,azim=-130)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

plt.show()
#plt.savefig('foo.png',dpi=450)
