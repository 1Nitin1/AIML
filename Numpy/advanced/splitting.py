"""
np.split() -> equal
np.hsplit()
np.vsplit()
"""
import numpy as np
arr=np.array([[1,2],[5,6],[3,4],[7,8]])
print(np.split(arr,4))
print(np.hsplit(arr,2))