a=[]
for i in range(4):
    a.append(int(input()))
max,min=a[1],a[1]
for i in a:
    if i>max:
        max=i
    if i<min:
        min=i
print('max = ',max,',','min = ',min)
