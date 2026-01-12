list = [" Helloa", " Nitin Baranwa", " Python Programming " , "a"]

def func(list, word):
    list.remove(word)
    for i in range(len(list)):
        list[i] = list[i].strip(word)
    
    return list
result = func(list, "a")
print(result)