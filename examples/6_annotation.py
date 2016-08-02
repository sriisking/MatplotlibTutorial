#Basic annotation example

#Imports
import pylab as plt
import numpy as np
import scipy.special as sps

#Data
np.random.seed(137)
shape, scale = 2., 2. # mean and dispersion
s = np.random.gamma(shape, scale, 500)

#Plotting
count, bins, _ = plt.hist(s, 50, normed=True, orientation="vertical", color="green", alpha=0.8, edgecolor = "none", label = "Histogram")
y = bins ** (shape - 1) * (np.exp(-bins / scale) / (sps.gamma(shape) * scale ** shape))
plt.plot(bins, y, linewidth=3, color='r', label = "Fitted distribution")
plt.annotate('Long tail', xy=(12, .02), xytext=(13, 0.05), fontsize=16,arrowprops=dict(facecolor='black', shrink=0.05))

#Additional
plt.legend()
plt.show()