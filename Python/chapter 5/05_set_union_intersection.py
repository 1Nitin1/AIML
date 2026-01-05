s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1 | s2)  #union of two sets
print(s1 & s2)  #intersection of two sets
print(s1 - s2)  #elements in s1 but not in s2
print(s2 - s1)  #elements in s2 but not in s1
print(s1 ^ s2)  #elements in s1 or s2 but not in both
print(s1.isdisjoint(s2))  #checks if two sets have no elements in common
print(s1.issubset(s2))  #checks if s1 is subset of s2
print(s1.issuperset(s2))  #checks if s1 is superset
print(s1.union(s2))  #union of two sets
print(s1.intersection(s2))  #intersection of two sets
print(s1.difference(s2))  #elements in s1 but not in s2
print(s1.symmetric_difference(s2))  #elements in s1 or s2 but not in both
s1.update(s2)  #updates s1 with elements from s2 (union)