class employee:
    language="py"
    salary = 1200000

    def getinfo(self):
        print(f"the language is {self.language}. and salary is {self.salary}")
    def greet(self):
        print("good morrning")


rishi = employee()
# print(rishi.language,rishi.salary)
rishi.greet()
rishi.getinfo()
# employee.getinfo(rishi)
