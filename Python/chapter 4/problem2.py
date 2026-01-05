list = []
for i in range(6):
    n = int(input("Enter the marks: "))
    list.append(n)
list.sort()
print(list)
print(tuple(list))