class number:
    def __init__(self,n):
        self.n=n
    def __sub__(self,num):
        return self.n-num.n   
e=number(2)
f=number(2)
print(e-f)

# p1+p2 # p1.__add__(p2)
# p1-p2 # p1.__sub__(p2)
# p1*p2 # p1.__mul__(p2)
# p1/p2 # p1.__truediv__(p2)
# p1//p2 # p1.__floordiv__(p2)