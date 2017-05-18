# Bar chart for number of errors in composite chemistry methods
# from experiment

import numpy as np
import matplotlib.pyplot as plt

N = 7
labels = ('W1BD', 'LDBS', 'CBS-QB3', 'ROCBS-QB3', 'CBS-APNO', 'G4', 'G4(MP2)')
error_01 = (22, 23, 16, 19, 13, 25, 24)
error_12 = (6, 11, 15, 17, 15, 10, 9)
error_23 = (3, 8, 10, 6, 6, 2, 8)
error_34 = (0, 0, 2, 3, 2, 3, 2)
error_45 = (0, 3, 2, 1, 2, 2, 2)
error_5p = (2, 4, 4, 3, 2, 2, 3)
zeros = (0, 0, 0, 0, 0, 0, 0)

ind = np.arange(N)# the x locations for the groups
width = 0.14       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, error_01, width, color='green')
rects2 = ax.bar(ind + width, error_12, width, color='blue')
rects3 = ax.bar(ind + 2*width, error_23, width, color='grey')
rects4 = ax.bar(ind + 3*width, error_34, width, color='yellow')
rects5 = ax.bar(ind + 4*width, error_45, width, color='orange')
rects6 = ax.bar(ind + 5*width, error_5p, width, color='red')
rects7 = ax.bar(ind + 6*width, zeros, width, color='black')


# add some text for labels, title and axes ticks
ax.set_ylabel('# of Deviations')
ax.set_title('Number of Absolute Deviations from Experiment')
ax.set_xticks(ind + width*4)
ax.set_xticklabels((labels[0],labels[1],labels[2],labels[3],
                    labels[4],labels[5],labels[6]), rotation=40)

ax.legend(('0-1', '1-2', '2-3', '3-4', '4-5', '>5'),title='Absolute Error Range',fancybox=True,fontsize='8',loc=0,ncol=2)

# add some additional labels
ax.annotate('33/49',(0.3,15))
ax.annotate('49/49',(1.3,15))
ax.annotate('49/49',(2.3,15))
ax.annotate('49/49',(3.3,15))
ax.annotate('40/49',(4.3,15))
ax.annotate('44/49',(5.3,15))
ax.annotate('49/49',(6.3,15))

# plot and save fig
plt.ylim(0,35)
plt.xlim(-0.14,N)
plt.tight_layout()
plt.show()

#\fig.savefig("bde-barchart.png", dpi = (400))
