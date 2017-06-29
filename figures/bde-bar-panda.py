import matplotlib.pyplot as plt
import pandas as pd
import seaborn
seaborn.set()

labels = ('W1BD $^a$', 'LDBS', 'ROCBS-QB3', 'CBS-APNO $^b$', 'G4 $^c$')

errors = [[22,6,3,0,0,2],
          [23,11,8,0,3,4],
          [19,17,6,3,1,3],
          [13,15,6,2,2,2],
          [25,10,2,3,2,2]]

df = pd.DataFrame(errors, index = labels)
ax = df.plot(kind='bar', legend=False, width=0.8, figsize=(10,8))

ax.set(ylabel='# of Deviations', title='Number of Absolute Devations from Experiment')
plt.show()
