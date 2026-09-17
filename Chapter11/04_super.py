class company:
    def __init__(self):
        print("constructor of employee")
    a=1
class programmer(company):
    def __init__(self):
        print("constructor of employee")
    b=2
class manager(programmer):
     def __init__(self):
        super().__init__()
        print("constructor of employee")

     c = 3

# o=company()
# print(o.a)

# o=programmer()
# print(o.a,o.b)

o=manager()
print(o.a,o.b,o.c)
