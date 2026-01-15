'''
1- how big is dataset
2- names of columns

shape and columns
'''
import pandas as pd
data = {
    "name":['abc','sdf','hdjahf','gdhjad','hghda','dhj','bda','dhj'],
    'age':[23,34,45,45,54,65,65,73],
    'salary':[1000,2000,4000,3000,6000,70000,7000,4000],
    "performance":[85,90,92,97,87,85,89,99]
}
df = pd.DataFrame(data)
print(df.shape)
print(df.columns)