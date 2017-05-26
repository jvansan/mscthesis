%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from pylab import *

# load data
mat0 = genfromtxt("figures/data/luo_alkyl.tsv")
mat1 = genfromtxt("figures/data/luo_allylic.tsv")
mat2 = genfromtxt("figures/data/luo_nonfit.tsv")

# initialize figure
fig = plt.figure()
ax = fig.add_subplot(111)

# ROCBS-QB3 Data
## generate lines of best fit and plot data
slope, intercept, r_value, p_value, std_err = stats.linregress(mat0[:,3],mat0[:,2])
x = np.arange(120)
y = slope*x+intercept
A = mat0[:,3]
B = mat0[:,2]
labels = mat0[:,0]
#for i, txt in enumerate(labels):
#    ax.annotate(int(txt),(A[i],B[i]))
plt.plot(x,y,'-k')
plt.scatter(mat0[:,3], mat0[:,2], s=30, label = "Alkyl", color='black', marker='s')
ax.annotate("y = %1.4f x + %1.4f \n$R^2$ = %1.3f"%(slope,intercept,r_value**2), (96,7), color='black',bbox=dict(boxstyle="square", fc="w", ec="k"))
print("Alkyl slope %1.3f"%slope)
print(len(mat0))

slope, intercept, r_value, p_value, std_err = stats.linregress(mat1[:,3],mat1[:,2])
x = np.arange(120)
y = y=slope*x+intercept
# A = mat1[:,3]
# B = mat1[:,2]
# labels = mat1[:,0]
# #for i, txt in enumerate(labels):
# #    ax.annotate(int(txt),(A[i],B[i]))
plt.plot(x,y,'-g')
plt.scatter(mat1[:,3], mat1[:,2], s=30, label = "Allylic/Benzylic", color='green')
ax.annotate("y = %1.4f x + %1.4f \n$R^2$ = %1.3f"%(slope,intercept,r_value**2), (72,4), color='green', bbox=dict(boxstyle="square", fc="w", ec="g"))
print("Allylic slope %1.3f"%slope)
print(len(mat1))

A = mat2[:,3]
B = mat2[:,2]
labels = mat2[:,0]
#for i, txt in enumerate(labels):
#    ax.annotate(int(txt),(A[i],B[i]))
plt.scatter(mat2[:,3], mat2[:,2], s=60, facecolors='none', edgecolors='r',label = 'Non-fit')

# add labels to each data point
ax.annotate('1',  xy=( 98.5  , 4.68) )  ##2,2-dimethylbutane
ax.annotate('2',  xy=( 95.7, 5.6) )  ##2,3-dimethylbutane
ax.annotate('3',  xy=( 87.2, 7.08) )  ##Benzaldehyde
ax.annotate('4',  xy=( 91  , 5.90) )  ##DABCO
ax.annotate('5',  xy=( 91  , 5.65) )  ##DiethylEther
ax.annotate('6',  xy=( 97.3  , 5.01) )  ##Dioxane
ax.annotate('7',  xy=(102.3, 3.78) )  ##DMSO
ax.annotate('8',  xy=( 94.4, 6.13) )  ##HMPA
ax.annotate('9',  xy=( 89.5, 7.65) )  ##Pyrrolidine
ax.annotate('10', xy=(90.3, 6.16) )   ##THF
ax.annotate('11', xy=(90.7, 7.7) )   ##Triethylamine
ax.annotate('12', xy=(79.5, 6.17) )   ##BenzylAlcohol
ax.annotate('13', xy=(82, 5.75) )   ##Cumene
ax.annotate('14', xy=(76  , 7.4) )   ##Cyclohexadiene
ax.annotate('15', xy=(86, 6.15) )   ##DibenzylEther
ax.annotate('16', xy=(77, 7.10) )   ##Dihydroanthracene
ax.annotate('17', xy=(84, 5.3) )   ##Diphenylmethane
ax.annotate('18', xy=(86, 5.60) )   ##Ethylbenzene
ax.annotate('19', xy=(89.7, 4.5) )   ##Toluene
ax.annotate('20', xy=(101, 5.76) )   ##Adamantane2
ax.annotate('21', xy=(97, 6.24) )   ##Adamantane3
ax.annotate('22', xy=(  92, 5.20) )   ##Cycloheptane
ax.annotate('23', xy=(100.2, 4.96) )   ##Cyclohexane
ax.annotate('24', xy=(96.5, 5.27) )   ##Cyclooctane
ax.annotate('25', xy=(95, 4.65) )   ##Cyclopentane


# properties and show plot
plt.legend(fancybox=True,prop={'size':8},scatterpoints=1)
plt.xlim(70,113)
plt.ylim(3,9)
plt.xlabel('Bond Dissociation Enthalpy (kcal mol$^{-1}$)')
plt.ylabel('$\log_{10}(k_H)$')
plt.tight_layout()
#plt.show()

# Save Figure to fig.png with 2x default dpi
fig.savefig("figures/bep-expt.png", dpi = (400))
