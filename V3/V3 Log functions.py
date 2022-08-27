"""
Plotting functions
@author: GK
"""

import numpy as np
from matplotlib import pyplot as plt 


x = np.linspace(0.0001, 10, 1000)
y = np.log(x)
plt.title("The ln function") 
plt.xlabel("x") 
plt.ylabel("ln(x)") 
plt.plot(x,y) 
plt.savefig('Ln.png', dpi=360)
plt.show()