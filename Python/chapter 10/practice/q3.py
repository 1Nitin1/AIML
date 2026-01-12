class Check:
    a=10
    def func(self):
        print("This is a function inside class")

obj=Check()
obj.a=20
print(obj.a)
print(Check.a)
