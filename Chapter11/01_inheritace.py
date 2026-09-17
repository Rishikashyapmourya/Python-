class company:
    name="jupitr_pvt.ltd"
    pr="raju"
    def getshow(self):
        print(f"this is  the company name {self.name}")
class employee(company):
    # name="jai ho "
    def gettd(self):
        print(f"this the company: {self.name} and the employe is {self.pr}")

a = company()
b=employee()
print(a.name,b.name)
b.gettd()