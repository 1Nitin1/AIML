import matplotlib.pyplot as plt
d1=['Mon','Tue','Wed','Thu','Fri']
d2=[1000,10000,3000,7000,2000]
plt.barh(d1,d2,label='chart',linewidth=2, color='green')
plt.xlabel('Days')
plt.ylabel('Sale')
plt.title('Chart')
plt.legend(loc='upper left')
plt.savefig('Matplotlib/bar.png',dpi=200,bbox_inches='tight',facecolor='blue',edgecolor='black')
plt.show()