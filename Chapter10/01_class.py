class employee :
    language = "Py" #class attribute
    salary = 1700000
Rishi = employee()
Rishi.name="rishi" #class attribute
print(Rishi.name,Rishi.salary,Rishi.language,)

Raj = employee()
Raj.name="raj" #insatance attribute
print(Raj.name,Raj.language,Raj.salary)

# here name is instance attribute (object attribute) and salary and language are 
# class attributes. they are direactly belong to the class 