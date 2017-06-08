%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from pylab import *

# mat0 = genfromtxt("figures/data/pes_dma_na.txt")
mat0 = genfromtxt("figures/data/pes_dma_nacl.txt")
# mat0 = genfromtxt("figures/data/pes_dma_mg.txt")

# line at x=0
x = [0,1,2,3,4,5,6,7,8]
y = [0,0,0,0,0,0,0,0,0]
plt.plot(x , y,'k-',lw=1)

# gas-phase
plt.plot(mat0[:,0],mat0[:,1], color='k')
plt.plot(mat0[:,0],mat0[:,1], 'ko', ms='4' )

# MeCN
plt.plot(mat0[:,0],mat0[:,2], color='grey')
plt.plot(mat0[:,0],mat0[:,2], 'grey', marker='s', ms='4' )

# Water'
plt.plot(mat0[:,0],mat0[:,3], '--',lw=1, color='k' )
plt.plot(mat0[:,0],mat0[:,3], "o", ms='4', markerfacecolor='white', markeredgecolor='black', )

plt.xlim(1,6)
plt.ylim(-25,15)
plt.xlabel('O-Na Interatomic Distance ($\mathrm{\AA}$)')
plt.ylabel('BE (kcal mol$^{-1}$)')
plt.tight_layout()
plt.savefig("figures/pes_dma_nacl.png", dpi = (400))
