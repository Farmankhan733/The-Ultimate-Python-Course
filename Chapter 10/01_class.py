class Employee:
    language = "py" # This is a class attribute
    salary = 1200000
    
harry = Employee()
harry.name = "Harry" # This is an instance attributes 
print(harry.name, harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.language, rohan.salary)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class 