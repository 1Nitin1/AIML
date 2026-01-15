import pandas as pd
data = {
    "name":['abc','sdf','hdjahf','gdhjad','hghda','dhj','bda','dhj'],
    'age':[23,34,45,45,54,65,65,73],
    'salary':[1000,2000,4000,3000,60000,70000,7000,4000],
    "performance":[85,90,92,97,87,85,89,99]
}
df = pd.DataFrame(data)
#df.drop(columns=['col name'],inplace=True)
df.drop(columns=['performance','age'],inplace=True)
print(df)
