# One:one plots of log kHs
# Modify according to desired methods
# kHs are in data/bde_methodx_methody.tsv

from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from pylab import *

# load data
mat0 = genfromtxt("figures/data/kH-expt-mecn.tsv")

# initialize figure
fig = plt.figure()
ax = fig.add_subplot(111)

## generate lines of best fit and plot data
A = np.arange(12)
ax.plot(A,A,'-k')
slope, intercept, r_value, p_value, std_err = stats.linregress(mat0[:,1],mat0[:,2])
x = np.arange(120)
y = slope*x+intercept
plt.plot(x,y,'--r')
plt.scatter(mat0[:,1], mat0[:,2], color='black')
ax.annotate("y=%1.3f x+ %1.3f\n$R^2$=%1.4f"%(slope,intercept,r_value**2),(8,6))
ax.text(3.5, 9, 'B', fontsize=24, fontweight='bold')

# properties and show plot
#plt.legend(fancybox=True,prop={'size':8},scatterpoints=1)
plt.xlim(3,10)
plt.ylim(3,10)
plt.xlabel('log $k_H (expt)$ (log M$^{-1}$s$^{-1}$)')
plt.ylabel('log $k_H (calc)$ (log M$^{-1}$s$^{-1}$)')
plt.show()

# Save Figure to fig.png with 4x default dpi
fig.savefig("figures/kH-expt-mecn.png", dpi = (400))
