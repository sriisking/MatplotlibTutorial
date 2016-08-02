#Advanced scatter plotting example

#Imports
import pylab as plt
import numpy as np

#Data
x = range(30)
y1 = np.random.random(30)
y2 = np.random.random(30)
volume = 50*np.random.random(30)

#Plotting functions
plt.scatter(x, y1, s = volume, label="Random1", marker="o", c="g")
plt.scatter(x, y2, s = volume, label="Random2", marker="o", c="r")

#Additional
plt.title("Random scatter plots", fontsize=16)
plt.legend(ncol=2, loc=2)
plt.tight_layout()
plt.show()