class Calculator:
    @staticmethod
    def square(number):
        return number * number
    @staticmethod
    def cube(number):
        return number * number * number
    @staticmethod
    def sqrt(number):
        return number ** 0.5
    
    @staticmethod
    def greet():
        print("Welcome to the Calculator class!")
    
print(Calculator.square(4))
print(Calculator.cube(3))