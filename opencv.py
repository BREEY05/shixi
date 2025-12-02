import numpy as np
import matplotlib.pyplot as plt
zeros = np.zeros((5,5)) 
zeros[2:,:2] = 1          
plt.imshow(zeros, cmap='gray_r') 
plt.show()