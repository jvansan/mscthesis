%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from pylab import *

# load data
mat0 = genfromtxt("figures/data/bep-dG-cyclicalkanes.tsv")
mat1 = genfromtxt("figures/data/bep-dG-otheralkanes.tsv")
mat2 = genfromtxt("figures/data/bep-dG-hetother.tsv")
mat3 = genfromtxt("figures/data/bep-dG-hetneighbours.tsv")
mat4 = genfromtxt("figures/data/bep-dG-allylic.tsv")
mat5 = genfromtxt("figures/data/bep-dG-nonfit.tsv")

# initialize figure
fig = plt.figure()
ax = fig.add_subplot(111)

# ROCBS-QB3 Data
## generate lines of best fit and plot data

slope, intercept, r_value, p_value, std_err = stats.linregress(mat0[:,2],mat0[:,3])
# x = np.arange(120)
# y = slope*x+intercept
# plt.plot(x,y,'-k')
plt.scatter(mat0[:,2], mat0[:,3], s=30, label = "Cyclic Alkanes $R^2$ = %.3f"%r_value**2, color='red', marker='s')


slope, intercept, r_value, p_value, std_err = stats.linregress(mat1[:,2],mat1[:,3])
# x = np.arange(120)
# y = slope*x+intercept
# plt.plot(x,y,'-k')
plt.scatter(mat1[:,2], mat1[:,3], s=30, label = "Other Alkanes $R^2$ = %.3f"%r_value**2, color='blue', marker='^')

plt.scatter(mat2[:,2], mat2[:,3], s=30, label = "Tert. Amine and H-Bond Donor", color='black', marker='v')

slope, intercept, r_value, p_value, std_err = stats.linregress(mat3[:,2],mat3[:,3])
# x = np.arange(120)
# y = slope*x+intercept
# plt.plot(x,y,'-k')
plt.scatter(mat3[:,2], mat3[:,3], s=30, label = "Het. Neighbours $R^2$ = %.3f"%r_value**2, color='orange', marker='D')

slope, intercept, r_value, p_value, std_err = stats.linregress(mat4[:,2],mat4[:,3])
# x = np.arange(120)
# y = slope*x+intercept
# plt.plot(x,y,'-k')
plt.scatter(mat4[:,2], mat4[:,3], s=30, label = "Allylic $R^2$ = %.3f"%r_value**2, color='green', marker='o')
print(slope, intercept)

plt.scatter(mat5[:,2], mat5[:,3], label = "Non-fit", s=60, facecolors='none', edgecolors='r')

# add labels to each data point
# ax.annotate('1',  xy=( 97.1,3.30))   #Acetone
# ax.annotate('2',  xy=( 97.0,3.48))   #Acetonitrile
ax.annotate('1', xy=(97.1,3.58))  #Acetone
ax.annotate('2', xy=(97.0,6.84)) #Acetonitrile

ax.annotate('3', xy=(96.7, 0.470975748 ))#Cyclopentane
ax.annotate('4', xy=(99.7, 1.183118022 ))#Cyclohexane
ax.annotate('6', xy=(92.8, -0.530547782)) #Cyclooctane

ax.annotate('7', xy=(99.0, 0.164908943 ) )#Neohexane
ax.annotate('8', xy=(97.8, -1.420574119) ) #Diisopropyl
ax.annotate('9', xy=(100.8, 0.591030961) ) #Adamantane2
ax.annotate('10', xy=(100.3, -0.958321977))  #Adamantane3

ax.annotate('11', xy=(99.0,  -0.535348234))  #DABCO
ax.annotate('18', xy=(92.3, -3.037895137 )) #Diethylamine

ax.annotate('20', xy=(95.9, -3.831983314))  #DiethylEther
ax.annotate('21', xy=(95.6, -0.523751228))  #Dioxane
ax.annotate('22', xy=(94.3, -2.303181956))  #HMPA
ax.annotate('23', xy=(102.7, 3.751443033))  #Dimethylsulfoxide
ax.annotate('24', xy=(91.4, -0.143252363))  #Benzaldehyde

ax.annotate('25', xy=(75.4, -1.007242656)  )#14Cyclohexadiene
ax.annotate('26', xy=(90.1,	 0.933622556))  #Toluene
ax.annotate('29', xy=(87.3,	-1.911363457))  #Cumene
ax.annotate('30', xy=(83.2,	-0.979302774))  #diphenylmethane
ax.annotate('32', xy=(78.5,	-3.237288322))  #DHanthracene

# properties and show plot
plt.legend(fancybox=True,prop={'size':8},scatterpoints=1)
plt.xlim(70,113)
plt.ylim(-5,10)
plt.xlabel('Bond Dissociation Enthalpy (kcal mol$^{-1}$)')
plt.ylabel('$\Delta H^\ddag$ (kcal mol$^{-1}$)')
plt.tight_layout()
#plt.show()

# Save Figure to fig.png with 2x default dpi
fig.savefig("figures/bep-dG.png", dpi = (400))
