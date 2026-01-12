class nitin:
    name="nitin"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    @staticmethod
    def morning():
        print("Good Morning!")
    
person1 = nitin("Nitin", 20)
person1.gender="Male"
person2 = nitin("Rohan", 22)
print(person1.greet())
print(person2.greet())
nitin.morning()