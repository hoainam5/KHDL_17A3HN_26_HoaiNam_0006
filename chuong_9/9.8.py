a=int(input("nhập số:"))
b=0
def kiem_tra_so_hoan_hao(a,b):
    for i in range(1, a):
        if a%i==0:
            b+=i
    return b
kiem_tra_so_hoan_hao(a,b)
if a==1:
    print("1 là số hoàn hảo")
elif b==a:
    print(a, "là số hoàn hảo")
else:
    print(a,"là số không hoàn hảo")