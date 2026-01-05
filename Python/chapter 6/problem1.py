a= int(input("Enter a number: "))
b= int(input("Enter another number: "))
c= int(input("Enter another number: "))
d= int(input("Enter another number: "))
if(a>b and a>c and a>d):
    print("a is greatest")
elif(b>a and b>c and b>d):
    print("b is greatest")
elif(c>a and c>b and c>d):
    print("c is greatest")
else:
    print("d is greatest")
    