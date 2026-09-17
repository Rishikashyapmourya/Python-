# 1. Create a class (2-D vector) and use it to create 
# another class representing a 3-D vector

# class TwoDvector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j

#     def show(self):
#         print(f"the vactor is {self.i}i + {self.j}j")

# class ThreeDvector(TwoDvector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k

#     def show(self):
#         print(f" the vctor is {self.i}i + {self.j}j + {self.k}k")

# a = TwoDvector(1,2)
# a.show()

# b = ThreeDvector(1,2,3)
# b.show()
 


#2. Create a class ‘Pets’ from a class ‘Animals’ and further create a 
# class ‘Dog’ from ‘Pets’.Add a method ‘bark’ to class ‘Dog’.

# class Animals:
#     pass
# class pets(Animals):
#     pass
# class dog(pets):

#     @staticmethod
#     def bark():
#         print("Bow Bow!")
# a=dog()
# a.bark()


# 3. Create a class ‘Employee’ and add salary and increment properties to it. 
# Write a method‘salaryAfterIncrement’ method with a @property decorator with
#  a setter which changes the value of increment based on the salary.

# class employee:
#     salary = 350
#     increment = 20

#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + self.salary * (self.increment/100))
   
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,salary):
#         self.increment = ((salary/self.salary)-1)*100

# a=employee()
# # print(a.salaryAfterIncrement)
# a.salaryAfterIncrement=420
# print(a.increment)



# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators
# ‘+’ and ‘*’ which adds and multiplies them.

# class complex:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i
#     def __add__(self,c2):
#         return complex(self.r + c2.r, self.i+c2.i)
#     def __mul__(self,c2):
#         real_part=self.r * c2.r - self.i *c2.i
#         imag_part=self.r * c2.i - self.i *c2.r
#         return complex(real_part,imag_part) b

#     def __str__(self):
#         return f"{self.r}+{self.i}i"
    
# c1=complex(1,2)
# c2=complex(3,4)
# print(c1+c2)
# print(c1*c2)

