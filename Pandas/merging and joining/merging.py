import pandas as pd
data1 = {
    'id':[1,2,3],
    'name':['abs','hfja','hdkaj']
}
df1 = pd.DataFrame(data1)

data2 = {
    'id':[1,2,4],
    'cost':[200,450,1000]
}
df2 = pd.DataFrame(data2)
df = pd.merge(df1,df2,on='id',how="outer")
print(df)
