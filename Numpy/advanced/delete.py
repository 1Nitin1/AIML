"""
np.delete(array,index,axis)
if axis=none -> flatten and delete
"""
import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(np.delete(arr,2,axis=1))