# 1. Write a program to print multiplication table of a given number using for loop.
# num=int(input("enter the number :"))
# for i in range(11):
#     print(f"{num} X {i} = {num*i}")

# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"hello {name}")
    

# 3. Attempt problem 1 using while loop.

# num=int(input("enter the number :"))
# i=1
# while i<11:
#     print(num*i)
#     i=i+1

# 4. Write a program to find whether a given number is prime or not.

# n=int(input("enter the number :"))

# for i in range(2,n):
#     if (n%1)==0:
#         print("number is not prime ")
#         break
# else:
#     print("number is prime")


# 5. Write a program to find the sum of first n natural numbers using while loop
n=int(input("enter the number :"))
i=1
sum=0
while i<=n:
    sum += i
    i=i+1
print(sum)
