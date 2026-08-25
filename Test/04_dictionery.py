# Q7. Ek dictionary banao apni detail ki:
# python
# student = {
#     "name": "Rishi",
#     "age": 20,
#     "city": "Khandwa",
#     "marks": 85
# }
# Sirf city print karo
# Age update karo 21 kar do
# Ek naya key "college" add karo
# Saari keys print karo
# Saari values print karo

# student = {
#     "name": "Rishi",
#     "age": 20,
#     "city": "Khandwa",
#     "marks": 85
# }
# print(student["city"])
# student.update({"age": 21})
# print(student)
# student.update({"collage":"cdgi"})
# print(student)
# print(student.keys())
# print(student.values())

# Q8. User se 3 subject aur unke marks lo — dictionary mein store karo aur print karo
d={}
s=input("enter subject :")
m=int(input("enter marks :"))
d.update({s:m})
s=input("enter subject :")
m=input("enter marks :")
d.update({s:m})
s=input("enter subject :")
m=input("enter marks :")
d.update({s:m})
print(d)