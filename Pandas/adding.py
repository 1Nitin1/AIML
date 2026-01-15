import pandas as pd
data = {
    "name":['abc','sdf','hdjahf','gdhjad','hghda','dhj','bda','dhj'],
    'age':[23,34,45,45,54,65,65,73],
    'salary':[1000,2000,4000,3000,60000,70000,7000,4000],
    "performance":[85,90,92,97,87,85,89,99]
}
df = pd.DataFrame(data)
# df['col name']=some data
df['bonus']=df['salary']*0.1
print(df)

# using insert()
# df.insert(loc,'col name',data)
df.insert(0,'id',[10,20,30,40,50,60,70,80])
print(df)
