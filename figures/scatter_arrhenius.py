%matplotlib inline
%config Inline.Backend.figure_format='svg'
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


#Data
labels = [2,3,4,8,9,10]
x = [-14.79,-10.12,-10.04,-5.5,-5.67,-7.99]
y = [3.8,5.1,5.5,7.2,6.4,6.0]

outliers = [1,5,6,7]
xo = [-10.82,-6.75,-14.84,-8.56]
yo = [3.7,4.2,7.0,8.3]
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)


#plot
plt.scatter(x, y, color = 'k')
plt.scatter(xo,yo,color='r')
a = np.arange(-20,0)
b = slope*a+intercept
plt.plot(a,b, 'k')
plt.axis([-17,-4,3,8.6])

# add annotations
for i in range(len(labels)):
    plt.annotate("%s" %labels[i],xy=(x[i]-0.5,y[i]+0.1))
for i in range(len(outliers)):
    plt.annotate("%s" %outliers[i],xy=(xo[i]-0.5,yo[i]))

plt.annotate("R$^2$ = %.3f\n  y = %.4f x + %.4f" %(r_value**2,slope,intercept),xy=(-16,7.5))

plt.xlabel('Binding Energy (kcal mol$^{-1}$)',fontsize=14, fontweight='bold')
plt.ylabel('log$_{10}$ A',fontsize=14, fontweight='bold')

#plt.show()
plt.savefig('arrhenius-scatter.pdf',dpi=450,frameon=False,bbox_inches='tight')
