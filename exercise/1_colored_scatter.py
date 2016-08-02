#Sample exercise - 1 Scatter plot with z axis shown as color

#Imports
import pylab as plt
import numpy as np

#Data
np.random.seed(137)
x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

#Plotting
sc = plt.scatter(x, y, c=z, vmin=0, vmax=1)
plt.colorbar(sc)

#Additional
plt.show()