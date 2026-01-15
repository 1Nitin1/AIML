import pandas as pd
data = {
    "name":['abc','sdf','hdjahf','gdhjad','hghda','dhj','bda','dhj'],
    'age':[23,34,45,45,54,65,65,73],
    'salary':[1000,2000,4000,3000,6000,70000,7000,4000],
    "performance":[85,90,92,97,87,85,89,99]
}
df = pd.DataFrame(data)
highsalary = df[df['salary']>=4000]
print(highsalary)
#using and
highppl = df[(df['salary']>=4000) & (df['age']<65)]
print(highppl)
#using or
highppls = df[(df['salary']>=4000) | (df['age']<65)]
print(highppls)