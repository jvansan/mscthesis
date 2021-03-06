%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from pylab import *

# load data
mat0 = genfromtxt("figures/data/rocbsqb3_alkyl_all.tsv")
mat1 = genfromtxt("figures/data/rocbsqb3_allylic_all.tsv")
mat2 = genfromtxt("figures/data/rocbsqb3_nonfit_all.tsv")

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


plt.scatter(mat2[:,3], mat2[:,2], s=60, facecolors='none', edgecolors='r',label = 'Excluded')

# add labels to each data point
ax.annotate('1',  xy=( 97.1,3.30))   #Acetone
ax.annotate('2',  xy=( 97.0,3.48))   #Acetonitrile

ax.annotate('3',  xy=( 94.9,4.90))   #Cyclopentane
ax.annotate('4',  xy=( 99.9,4.96))   #Cyclohexane
ax.annotate('5',  xy=( 94.2,5.20))   #Cycloheptane
ax.annotate('6',  xy=( 91.0,5.27))   #Cyclooctane
ax.annotate('7',  xy=( 99.7,4.55)) #22dimethylbutane
ax.annotate('8',  xy=( 98.2,5.45)) #23dimethylbutane
ax.annotate('9',  xy=(100.8,5.30))    #Adamantane-sec
ax.annotate('10', xy=( 100.3,6.05))     #Adamantane-ter

ax.annotate('11', xy=(91.9,7.44), xytext=( 92.2,7.84), arrowprops=dict(facecolor='black', width=0.5, headwidth=0))    #Diethylamine
ax.annotate('12', xy=( 93.9,7.46))    #Piperazine
ax.annotate('13', xy=( 92.2,7.55))    #Piperidine
ax.annotate('14', xy=( 88.7,7.55))    #Pyrrolidine
ax.annotate('15', xy=( 93.7,7.00))    #Morpholine
ax.annotate('16', xy=( 89.5,6.73))    #Propylamine

ax.annotate('17', xy=( 90.5,7.72))    #Triethylamine
ax.annotate('18', xy=( 99.2,5.70))    #DABCO

ax.annotate('19', xy=( 91.8,6.16))    #Tetrahydrofuran
ax.annotate('20', xy=( 97.6,5.10))    #Dioxane
ax.annotate('21', xy=(102.9,4.20))    #Dimethylsulfoxide
ax.annotate('22', xy=( 89.5,7.00))    #Benzaldehyde
ax.annotate('23', xy=( 94.3,5.92))    #HMPA
ax.annotate('24', xy=( 94.0,5.65))     #DiethylEther

ax.annotate('25', xy=( 75.4,7.22))     #Cyclohexadiene
ax.annotate('26', xy=( 90.0,4.65))     #Toluene
ax.annotate('27', xy=( 83.6,6.17))     #BenzylAlcohol
ax.annotate('28', xy=( 87.9,5.50))     #Ethylbenzene
ax.annotate('29', xy=( 87.1,5.80))     #Cumene
ax.annotate('30', xy=( 83.2,5.54))     #Diphenylmethane
ax.annotate('31', xy=( 81.0,6.00))     #DibenzylEther
ax.annotate('32', xy=( 78.5,7.10))     #Dihydroanthracene


# properties and show plot
plt.legend(fancybox=True,prop={'size':8},scatterpoints=1)
plt.xlim(70,113)
plt.ylim(3,9)
plt.xlabel('Bond Dissociation Enthalpy (kcal mol$^{-1}$)')
plt.ylabel('$\log(k_H/n)$')
plt.tight_layout()
#plt.show()

# Save Figure to fig.png with 2x default dpi
fig.savefig("figures/bde-bep.png", dpi = (400))
