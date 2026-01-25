import matplotlib.pyplot as plt
d1 = [1,2,3,4,5]
d2 = [10,30,50,30,100]
plt.plot(d1,d2,color='red',linewidth=1,linestyle='--',marker='o',label='This is my data')
plt.title('hello world')
plt.xlabel('hello')
plt.ylabel('world')
plt.show()