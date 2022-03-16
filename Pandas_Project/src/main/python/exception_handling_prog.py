
# scenario 1:
# simple exception handling
'''
a = [1, 2, 3]
try:
    print ("Second element = %d" %(a[1]))
 
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))
 
except:
    print ("An error occurred")
'''


# scenario 2:
# Program to handle multiple errors with one except statement
# try:
    # Some Code.... 

# except:
    # optional block
    # Handling of exception (if required)

# else:
    # execute if no exception

# finally:
    # Some code .....(always executed)

'''
def fun(a):
    
    if a == 2:
        b = a

    elif a > 2 and a < 4:
        # throws ZeroDivisionError for a = 3
        b = a/(a-3)
    
    else:
        # throws NameError if a >= 4
        print("Value of b = ", b)

try:
    fun(2)
#    fun(3)
#    fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")
else:
    print("No errors/exceptions")
finally:
    print("In Finally block")
'''

# scenario 3:
# Program to depict Raising Exception

try:
	raise NameError("Hi there") # Raise Error
except NameError:
	print ("An exception")
	raise # To determine whether the exception was raised or not

