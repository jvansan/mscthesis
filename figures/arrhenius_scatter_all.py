%matplotlib inline
%config Inline.Backend.figure_format='svg'
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


#Data
labels = [2,3,4,8,9,10]
x = [-14.79,-10.12,-10.04,-5.5,-5.67,-7.99]
y = [3.8,5.1,5.5,7.2,6.4,6.0]

outliersLow = [1,5]
xo = [-10.82,-6.46]
yo = [3.7,4.2]

outliersHigh = [6,7]
x1 = [-13.64,-8.56]
y1 = [7.0,8.3]
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)


#plot
plt.scatter(x, y, color = 'k')
plt.scatter(xo,yo, color='r')
plt.scatter(x1,y1, color='r')
# a = np.arange(-20,0)
# b = slope*a+intercept
# plt.plot(a,b, 'k')
plt.axis([-17,-4,3,8.6])

# add annotations
for i in range(len(labels)):
    plt.annotate("%s" %labels[i],xy=(x[i]-0.5,y[i]+0.1))
for i in range(len(outliersLow)):
    plt.annotate("%s" %outliersLow[i],xy=(xo[i]-0.5,yo[i]))
for i in range(len(outliersHigh)):
    plt.annotate("%s" %outliersHigh[i],xy=(x1[i]-0.5,y1[i]))

plt.annotate("$R^2$ = 0.33",xy=(-16,7.75), fontsize=14, fontweight='bold')

plt.xlabel('Binding Energy (kcal mol$^{-1}$)',fontsize=14, fontweight='bold')
plt.ylabel('log$_{10}$ A',fontsize=14, fontweight='bold')

#plt.show()
plt.savefig('arrhenius-scatter-all.pdf',dpi=450,frameon=False,bbox_inches='tight')
