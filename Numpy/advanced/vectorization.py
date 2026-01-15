import numpy as np
l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
res=[x+y+z for x,y,z in zip(l1,l2,l3)]
#list compression
print(res)
ar1=np.array(l1)
ar2=np.array(l2)
result=ar1+ar2
print(result)