dic = {"a": 1, "b": 2, "c": 3}
print(dic.keys())  #gives all keys in dictionary
print(dic.values())  #gives all values in dictionary
print(dic.items())  #gives all items in dictionary as (key,value) pairs
print(len(dic))  #gives length of dictionary
dic.update({"d": 4,"c":5})  #adds new key-value pair to dictionary
print(dic.get("a"))  #accessing value using key
print(dic.pop("b"))  #removes key-value pair and returns value of the key
print(dic)
dic.clear()  #clears the dictionary
print(dic)