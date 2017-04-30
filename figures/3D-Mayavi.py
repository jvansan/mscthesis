!#/usr/bin/env python
# coding: utf-8
from mayavi import mlab
import numpy as np

x = np.arange(-2, 7, 0.1)
y = np.arange(-2, 7, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.sin(X)+np.cos(Y)
s = mlab.mesh(X,Y,Z)

mlab.figure(bgcolor=(1,1,1))

xx, zz = np.meshgrid(np.linspace(-1.9,7.1,2),np.linspace(-3,4,2))
yy = xx*0 +3

a = mlab.mesh(X,Y,Z)
a = mlab.mesh(xx,yy,zz, opacity=0.5)

mlab.show()
