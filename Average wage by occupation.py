# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 06:06:21 2020

@author: kathe
"""

import pandas as pd
from pandas import plotting
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
#%%
data = pd.read_csv('C:/Users/kathe/downloads/wages1998') 
print(data.set())
print(data.describe())

val = 20
n, num_bins, patches = plt.hist(data['wage'], val, facecolor='green', alpha = 0.5)
plt.title('wage')
plt.show()

data.set['wagelog']=np.log10(data.set('wage'))

n, bins, patches = plt.hist(data.set('wagelog'), num_bins, facecolor='blue', alpha=0.5)
plt.show()

x = data['grade']
y = data['wagelog']
# Plot
plt.scatter(x, y, alpha=0.5)
plt.title('Scatter plot of grade vs wage log')
plt.xlabel('grade')
plt.ylabel('wagelog')
plt.show()

x = data['ttl_exp']
y = data['wagelog']

plt.scatter(x, y, alpha=0.5)
plt.title('Scatter plot of total experience vs wage log')
plt.xlabel('total exp')
plt.ylabel('wagelog')
plt.show()

print("\n")
print('\033[4m' + '\033[1m' + 'Average Wages By Occupation\n' + '\033[0m')
print(data.groupby('occupation')['wage'].mean())
#those with 10-20 years of experience usually earned more.
#It also looks like Admin workers made the most compared to farmers
