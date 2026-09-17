class employee:
    company="js_pvt_ltd"
    name="rajesh"
    def show(self):
        print(f"company name is {self.company}. and employee is {self.name}")
class coder:
    language ="python"
    def printlanguage(self):
        print(f" this is the language of coder is {self.language}")
class programmer (employee,coder):
    company="js_infotech"
    def showlanguage(self):
        print(f"campony is {self.company}  and employee is {self.name}")
a=employee()
b=programmer()
b.show()
b.printlanguage()
b.showlanguage()