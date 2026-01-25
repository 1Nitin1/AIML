import matplotlib.pyplot as plt
d1=['Mon','Tue','Wed','Thu','Fri']
d2=[1000,10000,3000,7000,2000]
plt.pie(d2,labels=d1,autopct='%1.1f%%',shadow=True)
plt.show()