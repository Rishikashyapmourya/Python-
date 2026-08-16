#.01 Write a python program to display a user entered name followed by Good Afternoon using
# input() function.
# a=input("enter your name :")
# print("good afternoon:",a)
# print (f"good afternoon, {a}")

# 2. Write a program to fill in a letter template given below with name and date.

#  1 solution
# letter = '''Dear <|Name|>,
# You are selected!
# <|Date|>'''
# print( letter.replace("<|Name|>","rishi").replace("<|Date|>","16/08/2026"))

#  2nd solution

# name=input("what is your name")
# date="16/08/2026"
# print( "dear:",name)
# print("You are selected!\n DATE=",date )

# 03.Write a program to detect double space in a string.

# a="hii  rishi"
# print(a.find("  "))

# 04. Replace the double space from problem 3 with single spaces. 

# a="hii  rishi"
# print(a.replace("  "," "))

# 05. Write a program to format the following letter using escape sequence characters.

letter = "\'Dear rishi\',\n \t this python course is nice. \n \" Thanks! \" "
print(letter)


