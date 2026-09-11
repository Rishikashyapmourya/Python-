f=open("file.txt","r")
print(f.read())
f.close()

# the same can written using a with statement
with open("file.txt") as f:
    print(f.read())