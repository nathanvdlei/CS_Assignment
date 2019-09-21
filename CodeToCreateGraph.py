import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('istherecorrelation.csv', ';')

years = data.iloc[:,0]
data1 = data.iloc[:,1]
data2 = data.iloc[:,2]

data1_float = [float(data1[i].replace(',', '.')) for i in range(0,len(data1))]
np.array(data1_float[1:])-np.array(data1_float[:-1])
data1_float

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Years')
ax1.set_ylabel('WO', color=color)
ax1.plot(years, data1_float, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  

color = 'tab:blue'
ax2.set_ylabel('Beer', color=color)
ax2.plot(years, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()

