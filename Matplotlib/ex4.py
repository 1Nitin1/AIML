import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Matplotlib/cancer.csv')
print(df['Concave points (se)'].describe())
x=df['Concave points (se)'] 
y=df['Area (se)']
plt.scatter(x,y,color='green',marker='^', label='concave pts vs area')
plt.title('cancer analysis')
plt.xlabel('Concave points')
plt.ylabel('Area')
plt.xlim(0,0.07)
plt.show()