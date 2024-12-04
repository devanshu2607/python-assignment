##55.	Create a function that plots the trajectory of a projectile motion.

import matplotlib.pyplot as plt
import numpy as np

def projectile_motion(v,angle):
    t = np.linspace(0,2*v*np.sin(np.radians(angle))/9.8,100)
    x = v*np.cos(np.radians(angle))*t
    y = v*np.sin(np.radians(angle))*t-0.5*9.8*t**2
    plt.plot(x,y)
    plt.show()

projectile_motion(15,55)