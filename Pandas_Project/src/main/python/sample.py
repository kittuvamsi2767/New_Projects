'''
from sys import argv
x = input("Enter any number :")
argv = input("Enter your name: ")
for x in argv:
print(type(x))
print(x)

print(type(name))
print(name)
'''

'''
import sys
print(sys.version_info)
'''

'''
a = "Enter age: "
b = "Enter name: "
num = input("Enter any number: ")
if asking_for_age:
    age = input(a)
elif asking_for_name:
    name = raw_input(b)
print(int(name))
print(type(name))
print(name)
'''

# python 2.0 - Here every input will be seggregated based on input, if we want to consider the input as string then use raw_input


# python 3.0 - Here everything is by default string


side1 = float(input('Enter length of a side: '))
side2 = float(input('Enter another length: '))
hyp = ((side1 * side1) + (side2 * side2)) ** 0.5
print('Length of hypotenuse is:', hyp)
