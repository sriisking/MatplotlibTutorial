#Basic subplots example

#Imports
import pylab as plt
import numpy as np
from statsmodels import api as sm

#Data
x = np.linspace(0,20*np.pi,1000)
y1 = np.sin(x)
y2 = sm.tsa.acf(y1, nlags=len(y1))
labels = ["Sine function", "Autocorrelation"]

#Plotting
f, ax = plt.subplots(2, 1, sharex=True)
l1, = ax[0].plot(x,y1, c='red', linewidth=2)
l2, = ax[1].plot(x,y2, c='green', linewidth=2)


#Additional
f.legend([l1, l2], labels, bbox_to_anchor=[0.5, 0.5], loc='center', ncol=2)
plt.show()