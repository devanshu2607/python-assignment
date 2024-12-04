##51.	Use Matplotlib to plot a simple line graph representing a mathematical function.

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,2*np.pi,100)
plt.plot(x,np.sin(x))
plt.show()