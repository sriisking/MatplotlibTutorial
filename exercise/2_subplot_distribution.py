#Sample exercise - 2. Trace and allied distribution subplot

#Imports
import pylab as plt
import numpy as np

#Data
trace = np.random.normal(0,1,100)

#Plotting
f, ax = plt.subplots(1, 2, sharey=True)
ax[1].plot(trace)
ax[0].set_ylabel('Value')
ax[1].set_xlabel('Samples')
ax[0].set_xlabel('Frequency distribution')
x_val = ax[0].hist(list(trace),bins=10, orientation="horizontal")

#Additional
plt.show()
