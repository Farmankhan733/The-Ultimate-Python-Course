class Employee:
    a = 1 

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3
    
o = Employee()
print(o.a) # Print the an attributes
# print(o.b) # Print an error as there is no b attributes in Employee class

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)