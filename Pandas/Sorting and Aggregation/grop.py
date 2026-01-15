import pandas as pd
data = {
    "name":['abc','hjsdh','hdjahf','gdhjad','hghda','dhj','bda','dhj'],
    'age':[23,34,45,23,54,65,65,73],
    'salary':[1000,2000,4000,3000,60000,70000,7000,4000],
    "performance":[85,90,92,97,87,85,89,99]
}
df = pd.DataFrame(data)
grpd=df.groupby('age')['salary'].sum()
print(grpd)