"""
Heat Maps (Densest possible data representation)
- Correlations
- Clustering results
- Spatial relationship
"""

#Imports
import pylab as plt
import numpy as np

#Data
np.random.seed(137)
mat = np.random.rand(10, 10)
data = np.corrcoef(mat)

#Plotting
heatmap = plt.pcolor(data, vmin=0, vmax=1)
plt.colorbar(heatmap)

#Additional
plt.show()