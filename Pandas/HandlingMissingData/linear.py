import pandas as pd
data = {
    
    'age':[23,34,45,None,54,65,65,73],
    'salary':[1000,2000,4000,3000,None,70000,7000,4000],
    "performance":[85,None,92,97,87,85,89,99]
}
df = pd.DataFrame(data)
df['age']=df['age'].interpolate(method="cubicspline")
print(df)