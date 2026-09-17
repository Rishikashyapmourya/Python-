# class company:
#     name="rs.info"
#     er="aman"
#     def show(self):
#         print(f"campony name is {self.name}")
# class coder(company):
#     language="Java"
#     def printlan(self):
#         print(f"the language is {self.language}")
# class programmer(coder):
#     def showlanguage(self):
#         print(f" programmer {self.er} is {self.language} developer")

# a=company()
# b=programmer()
# b.show()
# b.printlan()
# b.showlanguage()



class company:
    a=1
class programmer(company):
    b=2
class manager(programmer):
    c=3

o=company()
# print(o.a) #  print the a attribute
# print(o.b) # Show an error as there is no b attribute in employee class
o=programmer()
# print(o.a)
# print(o.b)
# print(o.c) # Show an error as there is no c attribute in programmer class
o=manager()
print(o.a)
print(o.b)
print(o.c)