%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from pylab import *

x = [2, 3, 4]
Li = [0, -0.00777, -0.00777]
Na = [0, -0.086432, -0.09317]
Mg = [0, -0.08815, -0.09931]
K = [0, -0.40806, -0.4403]
Ca = [0, -0.5693, -0.60193]


# # Li
plt.plot(x, Li, 'o', color="grey", label="Li$^+$")
plt.plot(x, Li, '-', color="grey")
# Na
plt.plot(x, Na, 'd', markerfacecolor="white", markeredgecolor="r", label="Na$^+$")
plt.plot(x, Na, 'r--')
# Mg
plt.plot(x, Mg, 'b*', label="Mg$^{2+}$")
plt.plot(x, Mg, 'b-')
# # Ca
plt.plot(x, K, 'o', markerfacecolor="white", markeredgecolor="g", label="K$^{+}$")
plt.plot(x, K, 'g--')
# # K
plt.plot(x, Ca, 'ks', label="Ca$^{2+}$")
plt.plot(x, Ca, 'k-')


# plt.xlim(1,6)
# plt.ylim(-150,15)
plt.legend(fancybox=True,prop={'size':8},scatterpoints=1)
plt.xlabel('Basis Cardinal Number')
plt.xticks(x, x)
plt.ylabel('Relative Energy (AU)')
plt.tight_layout()
# plt.show()
plt.savefig("figures/ap_metals_explicit.png", dpi = (400))
