'''
class check:
    def __init__(self):
        print("Address of self = ",id(self))
    def add(a,b):
        print("Sum of values is ",(a+b))
obj=check()
print("Address of class object = ",id(obj))
'''

class car():

    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model,end=' --> ')
        print("color is", self.color )

# both objects have different self which
# contain their attributes
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")

audi.show()     # same output as car.show(audi)
ferrari.show()
