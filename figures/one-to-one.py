# One:one plots of BDEs
# Modify according to desired methods
# BDEs are in data/bde_methodx_methody.tsv

from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from pylab import *

# load data
mat0 = genfromtxt("figures/data/bde_w1bd_g4mp2.tsv")


# initialize figure
fig = plt.figure()
ax = fig.add_subplot(111)

## generate lines of best fit and plot data
A = np.arange(120)
ax.plot(A,A,'-k')
slope, intercept, r_value, p_value, std_err = stats.linregress(mat0[:,1],mat0[:,2])
x = np.arange(120)
y = slope*x+intercept
plt.plot(x,y,'--r')
plt.scatter(mat0[:,1], mat0[:,2], color='black')
ax.annotate("y=%1.3f x+ %1.3f\n$R^2$=%1.4f\nN=33"%(slope,intercept,r_value**2),(90,80))

# properties and show plot
#plt.legend(fancybox=True,prop={'size':8},scatterpoints=1)
plt.xlim(70,110)
plt.ylim(70,110)
plt.xlabel('W1BD BDE (kcal mol$^{-1}$)')
plt.ylabel('G4(MP2) BDE (kcal mol$^{-1}$)')
plt.show()

# Save Figure to fig.png with 4x default dpi
fig.savefig("figures/w1bd-g4mp2.png", dpi = (400))
