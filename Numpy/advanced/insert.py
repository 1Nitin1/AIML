"""
np.insert(array, index, value, axis=None)
axis=0 -> row wise insert
axis=1 -> column wise insert
"""

import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(np.insert(arr,2,[0,0],axis=1))
print(np.insert(arr,2,[0,0]))