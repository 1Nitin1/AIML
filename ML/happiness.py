import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import plotly.express as px

df = pd.read_csv('ML/WHI_Inflation.csv')

d = df.groupby('GDP per Capita',as_index=False)['Score'].mean()
plt.scatter(d['GDP per Capita'],d['Score'],label='GDP vs Happiness',color='green')

plt.title('GDP per Capita vs Happiness Predictor')
plt.xlabel('GDP per Capita')
plt.ylabel('Happiness')
plt.xlim(0,1)
plt.show()
model = LinearRegression()
model.fit(d[['GDP per Capita']],d['Score'])
x_new = [[float(input('Enter GDP per capita :'))]]
print(f'Predicted Happiness = {round(model.predict(x_new)[0],3)}')