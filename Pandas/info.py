import pandas as pd
# r and c, col name, data type, non null cts, mem usage of data frame

df=pd.read_csv('Pandas/age_gender.csv')
print(df.info())