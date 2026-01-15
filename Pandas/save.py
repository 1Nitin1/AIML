import pandas as pd
data = {
    "name":['nitin','nidhi','mummy'],
    "age":[1,2,3],
    "city":['a','b','c']
}
df=pd.DataFrame(data)
print(df)
df.to_csv('Pandas/output.csv',index=False)