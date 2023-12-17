a=[]
while True:
    a.append(int(input('Nhập giá trị:\n')))
    i=input('Tiếp tục nhập giá trị? 1: có, 0: không ')
    while i!='1' and i!='0':
        i=input(f'Giá trị {i} không hợp lệ! \nnhập lại giá trị (1: có, 0: không )')
    if i=='0':
        break     

i=int(input('nhập giá trị cần tìm x: '))
print(f'List: {a}')
print(f'Tổng các gía trị trong list: {sum(a)}')
if i in a:
    print(f'{i} xuất hiện {a.count(i)} trong list')
if i > max(a):
    print(f'{i} lớn hơn tất cả')
else:
    b=[]    
    for j in a:
        if i>j:
            b.append(j)
    if b==[]:
        print(f'{i} không lớn hơn số nào trong list')
        a=[j for j in a if j!=i]
        print(f'Các số lớn hơn {i} trong list {a}')
    elif b!=[]:
        b=[j for j in b if j!=i]
        print(f'{i} lớn hơn các số trong list: {b}')