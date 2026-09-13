#1. Create a class “Programmer” for storing information of few programmers working at
# Microsoft.

# class programmer :
#     campony = "Microsoft"

#     def __init__(self,name,language,salary):
#         self.name=name
#         self.language=language
#         self.salary=salary
    
# raj=programmer("raj","pyhton",120000)
# print(raj.name,raj.salary,raj.campony)

# ajay=programmer("ajay","java",230000,)
# print(ajay.name,ajay.salary,ajay.campony)

# om=programmer("om","c++",200000,)
# print(om.name,om.salary,om.campony)


# 2. Write a class “Calculator” capable of finding square, cube and square root of a number

# class Calculator:

#     def __init__(self,n):
#         self.n = n
#     def square(self):
#         print(f"the square is {self.n*self.n}")
#     def cube(self):
#         print(f"the cube is {self.n*self.n *self.n}")
#     def square_root(self):
#         print(f"the square root is {self.n**1/2}")

# a=Calculator(4)
# a.square()
# a.cube()
# a.square_root()


# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using
# ‘object.a = 0’. Does this change the class attribute?

# class name:
#     a =4
    
# b = name()
# print(b.a)

# b.a=0
# print(b.a)


# 4. Add a static method in problem 2, to greet the user with hello.

# class calculator :

#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         print(f"this is the square {self.n*self.n}")
#     def cube(self):
#          print(f"this is the square {self.n*self.n*self.n}")
#     def square_root(self):
#         print(f"this is the square {self.n**1/2}")
#     @staticmethod
#     def greet():
#         print("hello friends")


# a =calculator(4)
# a.greet()
# a.square()
# a.cube()
# a.square_root()

# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get
# fare information of train running under Indian Railways.

# from random import randint

# class train:

#     def __init__(self,trainNo):
#         self.trainNo = trainNo
#     def getbook(self,fro,to):
#         print(f" ticket is booked trainNo : {self.trainNo} from {fro} to {to}")
#     def getstatus(self):
#         print(f" train no is :{self.trainNo} running on time ")
#     def getfare(self,fro,to):
#          print(f" ticket fare in trainNo{self.trainNo}, from {fro} to {to} is {randint(222,5555)}")

# t=train(22389)
# t.getbook("bhopal","delhi")
# t.getstatus()
# t.getfare("bhopal","khandwa")


# 6. Can you change the self-parameter inside a class to something else (say “ramesh”)? Try
# changing self to “slf” or “ramesh” and see the effects.


# class emp:
    
#     def getpr(slf,name):#changing self to “slf”
#         print(f" employee name is : {name}")
# e=emp()
# e.getpr("ritesh")
