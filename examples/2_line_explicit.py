#Advanced line plotting example

#Imports
import pylab as plt
import numpy as np

#Data
x = np.linspace(0,4*np.pi,100)
y1 = np.cos(x)
y2 = np.sin(x)

#Plotting functions
plt.plot(x,y1, label="Cosine", linewidth=3)
plt.plot(x,y2, label="Sine", linewidth=3)

#Axis labels
plt.xlabel("Angle in radians", fontsize=16)
plt.ylabel("Function value", fontsize=16)

#Axis ticks
plt.xticks(np.linspace(0,4*np.pi,9),["0","$\pi/2$","$\pi$","$3\pi/2$","$2\pi$","$5\pi/2$","$3\pi$","$7\pi/2$","$4\pi$"], fontsize=16)
plt.yticks(fontsize=16)

#Axis limits
plt.xlim([0,4*np.pi])
plt.ylim([-1.5,+1.5])

#Additional
plt.legend()
plt.tight_layout()
plt.show()