# 1. Write a program to find the greatest of four numbers entered by the user
# num1=int(input("enter number 1: "))
# num2=int(input("enter number 2: "))
# num3=int(input("enter number 3: "))
# num4=int(input("enter number 4: "))

# if(num1>num2 and num1>num3 and num1>num4):
#     print("the greates number is num1 ",num1)
# elif(num2>num1 and num2>num3 and num2>num4):
#     print("the greates number is num2 ",num2)
# elif(num3>num2 and num3>num1 and num3>num4):
#     print("the greates number is num3",num3)
# elif(num4>num1 and num4>num2 and num4>num3):
#     print("the greates number is num 4",num4)
 
# 2. Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the user.

# a1=int(input("enter your subject 1 number :"))
# a2=int(input("enter your subject 2 number :"))
# a3=int(input("enter your subject 3 number :"))

# total_percentage=(100)*(a1+a2+a3)/300


# if(total_percentage>=40 and a1>33 and a2>33 and a3>33):
#     print(" you are pass")
# else:
#     print("your failed", total_percentage)
 
# 3. A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

# a="Make a lot of money"
# b="buy now" 
# c="subscribe this"
# d="click this" 

# e=input("enter the comment : ")
# if((a in e) or (b in e) or (c in e) or (d in e )):# in keyword use to add massage words
#     print("this is spam ")
# else:
#     print("this is not spam")


# 4. Write a program to find whether a given username contains less than 10 characters or not.

# username=input("enter your username :")
# if(len(username)<10 ):
#     print("username contains less than 10 characters \" rewrite the username \"  ")
# else:
#     print(" your username is right")

# 5. Write a program which finds out whether a given name is present in a list or not.

# list=["ajay","ram", "rishi","rahul"]


# name=input("enter the name ")
# if(name in list):
#     print("name is present in the list ")
# else:
#     print("name is not present in list")

# 6. Write a program to calculate the grade of a student from his marks from the following
# scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

# marks = int(input("Enter your mark: "))

# if (marks <= 100 and marks >= 90):
#     grade = "EX"

# elif (marks < 90 and marks >= 80):
#     grade = "A"

# elif (marks < 80 and marks >= 70):
#     grade = "B"

# elif(marks < 70 and marks >= 60):
#     grade = "C"

# elif (marks < 60 and marks >= 50):
#     grade = "D"

# elif (marks < 50 and marks >= 0):
#     grade = "F"
# print("Your grade is", grade)

# 7. Write a program to find out whether a given post is talking about “krish” or not.

# post=input("enter the post :" )

# if("Rishi".lower() in post.lower()):
#     print( "it is talking about the rishi")
# else:
#     print("it is not talking about the rishi")
