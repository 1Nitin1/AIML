l=['a',1,True,4.5]
t=('b',2,False,5.5)
for item in l:
    print(item)

for item in t:
    print(item)

for i in range(len(l)):
    print(l[i])    
else:
    print("Loop is over")
s="Nitin Baranwal"
for char in s:
    print(char,end='')

#break and continue and pass
for i in range(10):
    if i==5:
        break
    print(i)
for i in range(10):
    if i==5:
        continue
    print(i)

for i in range(10):
    pass