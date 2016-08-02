#Basic line plotting example

#Imports
import pylab as plt
#import matplotlib.pyplot as plt
import numpy as np

#Data
y = np.cos(np.linspace(0,4*np.pi,100))
x = np.linspace(0,4*np.pi,100)

#Plotting function
plt.plot(x,y)

#Additional
plt.show()