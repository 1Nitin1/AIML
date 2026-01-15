import pandas as pd
data = {
    "name":['abc','sdf','hdjahf','gdhjad','hghda','dhj','bda','dhj'],
    'age':[23,34,45,45,54,65,65,73],
    'salary':[1000,2000,4000,3000,60000,70000,7000,4000],
    "performance":[85,90,92,97,87,85,89,99]
}
df = pd.DataFrame(data)
#.loc[]
#df.loc[rowidx,'col name']=new value
df.loc[0,'salary']=10000
print(df)

#increasing salary by 5%

df['salary']=df['salary']*1.05
print(df)