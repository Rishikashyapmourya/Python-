
# Q11. User se number lo aur batao:

# Positive hai, Negative hai ya Zero hai

# num=int(input("enter the number"))
# if(num==0):
#     print("number is zero")
# elif(num<0):
#     print("number is negative")
# else:
#     print("number is pasitive")


# Q12. User se age lo aur batao:

# 18 se kam — "Minor ho aap"
# 18 se 60 ke beech — "Adult ho aap"
# 60 se zyada — "Senior citizen ho aap"

# age=int(input("enter your age :"))
# if age<18:
#     print("you are minor")
# elif age>=60:
#     print("you are senior")
# else:
#     print("you are adult")

# Q13. User se 3 subjects ke marks lo — average nikalo aur grade batao:

# 90+ → Grade A
# 75-89 → Grade B
# 60-74 → Grade C
# 60 se kam → Fail
mark1=int(input("enter your marks"))
mark2=int(input("enter your marks"))
mark3=int(input("enter your marks"))
avg_marks= (mark1 + mark2+ mark3)/3

if avg_marks>=90:
    print("your grade is A  and maarks are " ,avg_marks)
elif avg_marks<=75:
    print("your garade is B and maarks are",avg_marks)
elif avg_marks<=60:
    print("your grade is C and maarks are",avg_marks)
else:
    ("your fail nd maarks are", avg_marks)    
