%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from pylab import *

# load data
mat1 = genfromtxt("figures/data/rocbsqb3_alkyl_all.tsv")
mat2 = genfromtxt("figures/data/rocbsqb3_alkyl_cyclicalkanes.tsv")
mat3 = genfromtxt("figures/data/rocbsqb3_alkyl_otheralkanes.tsv")
#mat4 = genfromtxt("figures/data/rocbsqb3_alkyl_satamines.tsv")
mat5 = genfromtxt("figures/data/rocbsqb3_alkyl_hbdonors.tsv")
mat6 = genfromtxt("figures/data/rocbsqb3_alkyl_hetneighbours.tsv")

# initialize figure
fig = plt.figure()
ax = fig.add_subplot(111)

# ROCBS-QB3 Data
## generate lines of best fit and plot data
slope, intercept, r_value, p_value, std_err = stats.linregress(mat1[:,3],mat1[:,2])
x = np.arange(120)
y = slope*x+intercept

ax.plot(x,y,':k',label="All Alkyl $R^2$ = %.3f" %r_value**2)

slope, intercept, r_value, p_value, std_err = stats.linregress(mat2[:,3],mat2[:,2])
ax.scatter(mat2[:,3], mat2[:,2], s=30, label = "Cyclic Alkanes $R^2$ = %.3f" %r_value**2, color='red', marker='s')
x = np.arange(120)
y = slope*x+intercept
ax.plot(x,y,'--r')


slope, intercept, r_value, p_value, std_err = stats.linregress(mat3[:,3],mat3[:,2])
ax.scatter(mat3[:,3], mat3[:,2], s=30, label = "Other Alkanes", color='blue', marker='^')

# ax.scatter(mat4[:,3], mat4[:,2], s=30, label = "Tert. Amines" %r_value**2, color='black', marker='v')

slope, intercept, r_value, p_value, std_err = stats.linregress(mat5[:,3],mat5[:,2])
ax.scatter(mat5[:,3], mat5[:,2], s=30, label = "H-Bond Donors $R^2$ = %.3f" %r_value**2, color='orange', marker='o')


slope, intercept, r_value, p_value, std_err = stats.linregress(mat6[:,3],mat6[:,2])
ax.scatter(mat6[:,3], mat6[:,2], s=30, label = "Het. Neighbours $R^2$ = %.3f" %r_value**2, color='green', marker='D')
x = np.arange(120)
y = slope*x+intercept
ax.plot(x,y,'-g')

# add labels to each data point
ax.annotate('3',  xy=( 95.5,4.90))   #Cyclopentane
ax.annotate('4',  xy=( 99.9,4.96))   #Cyclohexane
ax.annotate('5',  xy=( 94.7,5.20))   #Cycloheptane
ax.annotate('6',  xy=( 91.5,5.37))   #Cyclooctane

ax.annotate('7',  xy=( 99.7,4.55)) #22dimethylbutane
ax.annotate('8',  xy=( 98.2,5.45)) #23dimethylbutane

ax.annotate('9',  xy=(100.8,5.30))    #Adamantane-sec
ax.annotate('10', xy=( 100.3,5.85))     #Adamantane-ter

ax.annotate('11', xy=(91.9,7.44), xytext=( 92.2,7.84), arrowprops=dict(facecolor='black', width=0.5, headwidth=0))    #Diethylamine
ax.annotate('12', xy=( 93.9,7.46))    #Piperazine
ax.annotate('13', xy=( 92.2,7.55))    #Piperidine
ax.annotate('14', xy=( 89.3,7.55))    #Pyrrolidine
ax.annotate('15', xy=( 93.7,7.00))    #Morpholine
ax.annotate('16', xy=( 89.8,6.73))    #Propylamine

ax.annotate('17', xy=( 90.5,7.72))    #Triethylamine
ax.annotate('18', xy=( 99.2,5.70))    #DABCO

ax.annotate('19', xy=( 92.7,6.16))    #Tetrahydrofuran
ax.annotate('20', xy=( 97.6,5.10))    #Dioxane
ax.annotate('21', xy=(101.2,4.25))    #Dimethylsulfoxide
ax.annotate('22', xy=( 89.9,7.00))    #Benzaldehyde
ax.annotate('23', xy=( 94.3,5.92))    #HMPA
ax.annotate('24', xy=( 94.8,5.65))     #DiethylEther


# properties and show plot
plt.legend(fancybox=True,prop={'size':8},scatterpoints=1)
plt.xlim(85,105)
plt.ylim(4,8)
plt.xlabel('Bond Dissociation Enthalpy (kcal mol$^{-1}$)')
plt.ylabel('$\log(k_H/n)$')
plt.tight_layout()
#plt.show()

# Save Figure to fig.png with 2x default dpi
fig.savefig("figures/bep-breakdown.png", dpi = (400))
