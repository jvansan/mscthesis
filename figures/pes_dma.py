%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from pylab import *

x = [2, 3, 4, 5]
Li = [0, -0.004, -0.0173, -0.022]
Na = [0, -0.0246, -0.0856, -0.1419]
Mg = [0, -0.022, -0.0817, -0.1474]
K = [0, -0.1061, -0.158, -0.2089]
Ca = [0, -0.101, -0.1585, -0.2176]


# Li
plt.plot(x, Li, color='ko')

# Na
plt.plot(x, Na, color='ko')

# Mg
plt.plot(x, Mg, color='ko')

# K
plt.plot(x, K, color='ko')

# Ca
plt.plot(x, Ca, color='ko')

# MeCN
# plt.plot(mat0[:,0],mat0[:,2], color='grey')
# plt.plot(mat0[:,0],mat0[:,2], 'grey', marker='s', ms='4' )
#
# # Water'
# plt.plot(mat0[:,0],mat0[:,3], '--',lw=1, color='k' )
# plt.plot(mat0[:,0],mat0[:,3], "o", ms='4', markerfacecolor='white', markeredgecolor='black', )

# plt.xlim(1,6)
# plt.ylim(-150,15)
plt.xlabel('Basis Cardinal Number')
plt.ylabel('Relative Energy (AU)')
plt.tight_layout()
plt.show()
# plt.savefig("figures/pes_dma_mg.png", dpi = (400))
