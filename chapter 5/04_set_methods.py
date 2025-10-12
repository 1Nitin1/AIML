s={1,2,3,4,5,"nitin",True,False}
s.add(6) #adds element to set
print(len(s)) #gives length of set
s.remove(3) #removes element from set, throws error if element not found
s.discard(10) #removes element from set, doesn't throw error if element not found
s.pop() #removes and returns an arbitrary element from set
