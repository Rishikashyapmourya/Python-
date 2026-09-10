import random
#snak=1
#water=-1
#gun=0
computer= random.choice([-1,0,1])
youstr = input("enter your choice:")
youDict={ "s":1,"w":-1,"g":0}
reverseDict={ 1:"snak",-1:"water",0:"gun"}

you = youDict[youstr]

print(f"you chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")

if(computer==you):
    print("its drow")

elif you==1 and computer==-1:
    print("you win!")
elif you==0 and computer==-1:
    print("you loos!")
elif you==-1 and computer==1:
    print("you loos!")
elif you==0 and computer==1:
    print("you win!")
elif you==-1 and computer==0:
    print("you win!")
elif you==1 and computer==0:
    print("you loos!")
else:
    print("Something went wrong")