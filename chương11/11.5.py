a=[]
while True:
    a.append(int(input('Nhập giá trị:\n')))
    i=input('Tiếp tục nhập giá trị? 1: có, 0: không ')
    while i!='1' and i!='0':
        i=input(f'Giá trị {i} không hợp lệ! \nnhập lại giá trị (1: có, 0: không )')
    if i=='0':
        break
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
print('List: ',a)
b=[i for i in a if is_prime(i)]
if b==[]:
    print('không có số nguyên tố trong list')
else:print('Các số nguyên tố trong list: ',b)
b=[i for i in a if i<0]
print('Các phần tử âm trong list: ',b)
print('Trung bình cộng các phần tử âm: ',sum(b)/len(b))
b=[i for i in a if i>0]
print('Các phần tử dương trong list: ',b)
print('Trung bình cộng các phần tử dương: ',sum(b)/len(b))
print('giá trị max trong list ',max(a))
print('Giá trị min trong list ',min(a))