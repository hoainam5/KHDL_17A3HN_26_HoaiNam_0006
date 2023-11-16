def ucln(a,b):
    if b==0:
        return a
    return ucln(b,a%b)
def bcnn(a,b):
    return int((a*b)/ucln(a,b))
a,b=map(int,input("nhập 2 số nguyên : ").split())
print("Bội chung nhỏ nhất là :n",bcnn(a,b))