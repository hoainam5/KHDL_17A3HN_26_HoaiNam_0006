import math
def f(x, n):
    S=((x**2)+1)**n
    return math.pow(math.pow(x,2)+1,n)
x=float(input("nhập số x:"))
n=float(input("nhập số n:"))
print("s=",f(x, n))