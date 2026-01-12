class Programmer:
    def __init__(self, name, age, lang):
        self.name = name
        self.age = age
        self.lang = lang

    def getInfo(self):
        return f"Name: {self.name}, Age: {self.age}, Language: {self.lang}"
    
prog1 = Programmer("Nitin", 20, "Python")
prog2 = Programmer("Rohan", 22, "JavaScript")
print(prog1.getInfo())
print(prog2.getInfo())