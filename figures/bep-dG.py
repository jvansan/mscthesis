%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from pylab import *

# load data
mat0 = genfromtxt("figures/data/bep-dG-cyclicalkanes.tsv")
mat1 = genfromtxt("figures/data/bep-dG-otheralkanes.tsv")
mat2 = (11,	'Diethylamine',91.9,	-9.120851575)
mat3 = genfromtxt("figures/data/bep-dG-hetneighbours.tsv")
mat4 = genfromtxt("figures/data/bep-dG-allylic.tsv")
mat5 = genfromtxt("figures/data/bep-dG-nonfit.tsv")

# initialize figure
fig = plt.figure()
ax = fig.add_subplot(111)

# ROCBS-QB3 Data
## generate lines of best fit and plot data

slope, intercept, r_value, p_value, std_err = stats.linregress(mat0[:,2],mat0[:,3])
x = np.arange(120)
y = slope*x+intercept
plt.plot(x,y,'--r')
plt.scatter(mat0[:,2], mat0[:,3], s=30, label = "Cyclic Alkanes $R^2$ = %.3f"%r_value**2, color='red', marker='s')
# print(slope, intercept)

slope, intercept, r_value, p_value, std_err = stats.linregress(mat1[:,2],mat1[:,3])
# x = np.arange(120)
# y = slope*x+intercept
# plt.plot(x,y,'-k')
plt.scatter(mat1[:,2], mat1[:,3], s=30, label = "Other Alkanes $R^2$ = %.3f"%r_value**2, color='blue', marker='^')

plt.scatter(mat2[2], mat2[3], s=30, label = "H-Bond Donor", color='black', marker='v')

slope, intercept, r_value, p_value, std_err = stats.linregress(mat3[:,2],mat3[:,3])
x = np.arange(120)
y = slope*x+intercept
plt.plot(x,y,'-.',color='orange')
plt.scatter(mat3[:,2], mat3[:,3], s=30, label = "Het. Neighbours $R^2$ = %.3f"%r_value**2, color='orange', marker='D')

slope, intercept, r_value, p_value, std_err = stats.linregress(mat4[:,2],mat4[:,3])
x = np.arange(120)
y = slope*x+intercept
plt.plot(x,y,':g')
plt.scatter(mat4[:,2], mat4[:,3], s=30, label = "Allylic $R^2$ = %.3f"%r_value**2, color='green', marker='o')
# print(slope, intercept)

plt.scatter(mat5[:,2], mat5[:,3], label = "Excluded", s=60, facecolors='none', edgecolors='r')

# add labels to each data point

ax.annotate('1', xy=(97.5, 0.0 ))  #Acetone
ax.annotate('2', xy=(97.5, 2.4 )) #Acetonitrile

ax.annotate('3', xy=(97.0, -2.1 ))#Cyclopentane
ax.annotate('4', xy=(99.7, -0.7 ))#Cyclohexane
ax.annotate('6', xy=(92.8, -2.2 )) #Cyclooctane

ax.annotate('7', xy=(99.0, -1.9 ))#Neohexane
ax.annotate('8', xy=(98.2, -3.3 )) #Diisopropyl
ax.annotate('9', xy=(100.8, -2.1 )) #Adamantane2
ax.annotate('10', xy=(100.3, -3.9 ))  #Adamantane3

ax.annotate('11', xy=(92.2,  -9.1 ))  #DEA

ax.annotate('18', xy=(99.2, -5.3 )) #DABCO
ax.annotate('20', xy=(95.9, -4.6 ))  #DiethylEther
ax.annotate('21', xy=(98.0, -4.0 ))  #Dioxane
ax.annotate('22', xy=(94.3, -7.3 ))  #HMPA
ax.annotate('23', xy=(102.7, -1.0 ))  #Dimethylsulfoxide
ax.annotate('24', xy=(92.0, -5.6 ))  #Benzaldehyde

ax.annotate('25', xy=(75.4, -6.8 )) #14Cyclohexadiene
ax.annotate('26', xy=(90.1,	-3.7 ))  #Toluene
ax.annotate('29', xy=(87.3,	-5.8 ))  #Cumene
ax.annotate('30', xy=(83.2,	-5.6 ))  #diphenylmethane
ax.annotate('32', xy=(78.5,	-8.5 ))  #DHanthracene

# properties and show plot
plt.legend(fancybox=True,prop={'size':8},scatterpoints=1)
plt.xlim(70,113)
plt.ylim(-10,3)
plt.xlabel('Bond Dissociation Enthalpy (kcal mol$^{-1}$)')
plt.ylabel('$\Delta H^\ddag$ (kcal mol$^{-1}$)')
plt.tight_layout()
#plt.show()

# Save Figure to fig.png with 2x default dpi
fig.savefig("figures/bep-dG.png", dpi = (400))
