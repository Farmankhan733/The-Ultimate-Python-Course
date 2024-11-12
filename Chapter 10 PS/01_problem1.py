class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.pincode = pincode
        self.salary = salary
        
p = programmer("Harry", 1200000, 333001)
print(p.name, p.salary, p.pincode, p.company)
r = programmer("Rohan", 1200000, 333001)
print(r.name, r.salary, r.pincode, r.company)