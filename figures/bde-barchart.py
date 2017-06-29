# Bar chart for number of errors in composite chemistry methods
# from experiment
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
mpl.rcParams['hatch.linewidth'] = 2

N = 4
labels = ('W1BD $^a$', 'LDBS', 'ROCBS-QB3', 'G4 $^b$')
error_01 = (22, 23, 19, 25)
error_12 = (6, 11, 17, 10)
error_23 = (3, 8, 6, 2)
error_34 = (0, 0, 3, 3)
error_45 = (0, 3, 1, 2)
error_5p = (2, 4, 3, 2)
zeros = (0, 0, 0, 0)

ind = np.arange(0,N)# the x locations for the groups
width = 0.12      # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, error_01, width, color='none', ec='k', hatch='///', lw=2)
rects2 = ax.bar(ind + 1.3*width, error_12, width, color='none', ec = 'b', hatch='++', lw=2)
rects3 = ax.bar(ind + 2.6*width, error_23, width, color='none', ec='grey', hatch='\\\\\\', lw=2)
rects4 = ax.bar(ind + 3.9*width, error_34, width, color='none', ec='g', hatch='|||', lw=2)
rects5 = ax.bar(ind + 5.2*width, error_45, width, color='none', ec='orange', hatch='XX', lw=2)
rects6 = ax.bar(ind + 6.5*width, error_5p, width, color='none', ec='r', hatch='--', lw=2)
# rects7 = ax.bar(ind + 6*width + 0.02, zeros, width, color='black')


# add some text for labels, title and axes ticks
ax.set_ylabel('# of Deviations')
ax.set_title('Number of Absolute Deviations from Experiment')
ax.set_xticks(ind + width*3)
ax.set_xticklabels((labels[0],labels[1],labels[2],labels[3]), rotation=40)

ax.legend(('0-1', '1-2', '2-3', '3-4', '4-5', '>5'),title='Absolute Error Range',fancybox=False,fontsize='8',loc=0,ncol=3)

# add some additional labels
# ax.annotate('33/49',(0.3,15))
# ax.annotate('49/49',(1.3,15))
# ax.annotate('49/49',(2.3,15))
# ax.annotate('49/49',(3.3,15))
# ax.annotate('40/49',(4.3,15))
# ax.annotate('44/49',(5.3,15))
# ax.annotate('49/49',(6.3,15))

# plot and save fig
plt.ylim(0,35)
plt.xlim(-0.2,N)
plt.tight_layout()
plt.show()

fig.savefig("figures/bde-barchart.png", dpi = (400))
