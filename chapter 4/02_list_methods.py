random = [1,2,4.5,"Nitin",True]
random.append("Hello")  #adds at last
print(random)
random.insert(1,"World")  #adds at specific index
print(random)
random.remove("World")  #removes specific element
print(random)
a=random.pop(0)  #removes last element or the specified element and returns it
print(a)
random.reverse()  #reverses the list
print(random)
l=[5,3,4,1,2]
l.sort()  #sorts the list
print(l)  #gives error if different data types are present
