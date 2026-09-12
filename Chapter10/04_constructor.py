class employee:
    language="python"#class attribute
    salary = 1200000

    def __init__(self,name,salary,language):#  dunder method which is automatically called
         self.name=name
         self.salary=salary
         self.language=language
         print("i am creating object")

    def getInfo(self):
        print(f" the language is: {self.language}. and my salary is {self.salary}")
    @staticmethod
    def greet():
        print("good morrning")
rishi=employee("Rishi",1900000,"JavaScript")
# rishi.name="Rishi" #instance attribute
print(rishi.name,rishi.salary,rishi.language)
# rishi.greet()
# rishi.getInfo()

