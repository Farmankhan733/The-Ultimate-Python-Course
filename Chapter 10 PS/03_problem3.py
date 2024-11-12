class Demo:
    a = 4
    
o = Demo()
print(o.a) # Print the class attributes because instance attribute is not present
o.a = 0 # Instance attributes is set
print(o.a) # Present the instance attributes because instance attributes is present
print(Demo.a)