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
plt.plot(x,y,'-k')
plt.scatter(mat0[:,3], mat0[:,2], s=30, label = "Alkyl", color='black', marker='s')
ax.annotate("y = %1.4f x + %1.4f \n$R^2$ = %1.3f"%(slope,intercept,r_value**2), (96,7), color='black',bbox=dict(boxstyle="square", fc="w", ec="k"))
print("Alkyl slope %1.3f"%slope)
print(len(mat0))

slope, intercept, r_value, p_value, std_err = stats.linregress(mat1[:,3],mat1[:,2])
x = np.arange(120)
y = y=slope*x+intercept
plt.plot(x,y,'-g')
plt.scatter(mat1[:,3], mat1[:,2], s=30, label = "Allylic/Benzylic", color='green')
ax.annotate("y = %1.4f x + %1.4f \n$R^2$ = %1.3f"%(slope,intercept,r_value**2), (72,4), color='green', bbox=dict(boxstyle="square", fc="w", ec="g"))
print("Allylic slope %1.3f"%slope)
print(len(mat1))


plt.scatter(mat2[:,3], mat2[:,2], s=60, facecolors='none', edgecolors='r',label = 'Excluded')

# add labels to each data point
ax.annotate('1',     xy=(92.8 , 6.00)) ##14diazabicyclo222octane
ax.annotate('2',     xy=(96.5 , 4.60)) ##22dimethylbutane
ax.annotate('3',     xy=(95.8 , 5.45)) ##23dimethylbutane
ax.annotate('4',     xy=(87.5 , 7.00)) ##Benzaldehyde
ax.annotate('5',     xy=(91.5 , 5.75)) ##DiethylEther
ax.annotate('6',     xy=(102.5, 3.78)) ##DimethylSulfoxide
ax.annotate('7',     xy=(95.2 , 4.90)) ##Dioxane
ax.annotate('8',     xy=(94.4 , 6.20)) ##Hexamethylphorsphoramide
ax.annotate('9',     xy=(92.4 , 7.10)) ##Morpholine
ax.annotate('10',	 xy=(93.3 , 7.46)) ##Piperazine
ax.annotate('11',	 xy=(89.0 , 7.60)) ##Piperidine
ax.annotate('12',	 xy=(87.0 , 7.40)) ##Pyrrolidine
ax.annotate('13',	 xy=(90.5 , 6.10)) ##Tetrahydrofuran
ax.annotate('14',	 xy=(91.0 , 7.54)) ##Triethylamine
ax.annotate('15',	 xy=(76.0 , 7.40)) ##14cyclohexadiene
ax.annotate('16',	 xy=(76.7 , 7.10)) ##910dihydroanthracene
ax.annotate('17',	 xy=(83.2 , 5.90)) ##Cumene
ax.annotate('18',	 xy=(84.0 , 5.30)) ##Diphenylmethane
ax.annotate('19',	 xy=(85.8 , 5.60)) ##Ethylbenzene
ax.annotate('20',	 xy=(89.7 , 4.79)) ##Toluene
ax.annotate('21',	 xy=(98.8 , 5.76)) ##Adamantane2
ax.annotate('22',	 xy=(96.6 , 6.24)) ##Adamantane3
ax.annotate('23',	 xy=(93.5 , 5.40)) ##Cycloheptane
ax.annotate('24',	 xy=(99.9 , 4.96)) ##Cyclohexane
ax.annotate('25',	 xy=(92.0 , 5.20)) ##Cyclooctane
ax.annotate('26',	 xy=(96.0 , 5.90)) ##Cyclopentane
ax.annotate('27',	 xy=(94.0 , 3.30)) ##Acetone
ax.annotate('28',	 xy=(97.4 , 3.48)) ##Acetonitrile
ax.annotate('29',	 xy=(79.4 , 6.17)) ##BenzylAlcohol
ax.annotate('30',	 xy=(86.2 , 6.15)) ##DibenzylEther
# ax.annotate('31',	 xy=(81.4 , 5.48)) ##Triphenylmethane

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
