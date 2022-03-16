# Constructors sample program
class Addition:
    first = 0
    second = 0
    answer = 0
     
    def __init__(self):
        print("No arguments are passed for addition")
    # parameterized constructor

    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))
 
    def calculate(self):
        self.answer = self.first + self.second

# creating object of the class
# this will invoke parameterized constructor
a=int(input("Enter First number for addition: "))
b=int(input("Enter Second number for addition: "))
obj = Addition(a,b)

# obj = Addition(1000, 2000)
 
# perform Addition
obj.calculate()
 
# display result
obj.display()
