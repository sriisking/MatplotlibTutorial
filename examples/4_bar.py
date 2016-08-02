#Bar plotting example

#Imports
import pylab as plt
import numpy as np

#Data
x = range(10)
y = 20+40*np.random.random(10)

#Plotting functions
#plt.bar(x,y, color= 'g', alpha = 0.7, yerr=10*np.random.random(10), ecolor='r')
plt.barh(x,y, color= 'g', alpha = 0.7, xerr=10*np.random.random(10), ecolor='r')

#Additional
plt.grid()
plt.legend(ncol=2, loc=2)
plt.tight_layout()
plt.show()