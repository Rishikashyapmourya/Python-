#1. Create a class “Programmer” for storing information of few programmers working at
# Microsoft.

class programmer :
    campony = "Microsoft"

    def __init__(self,name,language,salary):
        self.name=name
        self.language=language
        self.salary=salary
    
raj=programmer("raj","pyhton",120000)
print(raj.name,raj.salary,raj.campony)

ajay=programmer("ajay","java",230000,)
print(ajay.name,ajay.salary,ajay.campony)

om=programmer("om","c++",200000,)
print(om.name,om.salary,om.campony)


