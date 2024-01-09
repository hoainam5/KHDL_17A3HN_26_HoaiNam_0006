QD_đi=eval(input('nhập quoãng đường đi(km)'))
xe=eval(input('nhập loại xe '))
tgc=eval(input('nhập thời gian chờ(phút)'))
t=0
if tgc>5:
    t=tgc*800

s=0
if xe==4:
    if QD_đi<0.8:
        s=11000
    elif QD_đi <= 20:
        s=12100
    else:
        s=10000

if xe==7:
    if QD_đi<0.8:
        s=13000
    elif QD_đi <= 20:
        s=14100
    else:
        s=12000    
print('số tiền cần phải thành toán',s*QD_đi+t)