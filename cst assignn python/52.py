##52.	Create a program that plots a scatter plot for random data points.

import matplotlib.pyplot as plt
import numpy as np

x,y,z= np.random.rand(3,50,17)
plt.scatter(x,y,z)
plt.show()