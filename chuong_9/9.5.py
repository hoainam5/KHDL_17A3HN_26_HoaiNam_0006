import math
def f(x, n):
    S=((((x**2)+x+1)**n)+(((x**2)-x+1)**n))
    return S
x=float(input("nhập số x:"))
n=float(input("nhập số n:"))
print("s=",f(x, n))
