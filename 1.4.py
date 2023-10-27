a,b,c=map(int,input('nhập 3 cạnh của tam giác: ').split())
p=(a+b+c)/2
s=(p*(p-a)*(p-b)*(p-c))**(1/2)
print('diện tích của tam giác là :',s)