eno=int(input("Enter Employee No:")) 
ename=input("Enter Employee Name:")
esal=float(input("Enter Employee Salary:"))
eaddr=input("Enter Employee Address:")
married=input("Employee Married ?[True|False]:")
print("Please Confirm Information") 
print("Employee No :",eno)
print("Employee Name :",ename) 
print("Employee Salary :",esal) 
print("Employee Address :",eaddr)
if married == 'True':
    print("Employee Married ")
else:
     print("Not Married ")
